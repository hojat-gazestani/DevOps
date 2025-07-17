#!/usr/bin/env python3

import glob
import time
import os
import subprocess
from datetime import datetime

# --- Configuration ---
container_name = "mssql_cityname"
db_user = os.environ.get("DB_USER", "sa")
db_pass = os.environ.get("DB_PASS", "mssql_password")
db_name = os.environ.get("DB_NAME", "database_name")
sqlcmd_path = "/opt/mssql-tools18/bin/sqlcmd"

# --- Path ---
container_backup_dir = "/backup"
host_backup_dir = "/var/project_backups/"

# --- Timestamp and file paths ---
now = datetime.now()
timestamp = now.strftime("%d_%m_%Y_%H_%M_%S")
backup_filename = f"{db_name}_{timestamp}.bak"

container_backup_path = os.path.join(container_backup_dir, backup_filename)
host_backup_path = os.path.join(host_backup_dir, backup_filename)

log_file = os.path.join(host_backup_dir, f"project_backup.log")

def log(msg):
    with open(log_file, "a") as f:
        f.write(f"{msg}\n")
        f.flush()

def change_ownership(path: str, user: str = "hojat", group: str = "hojat"):
    try:
        subprocess.run(["sudo", "chown", f"{user}:{group}", path], check=True)
        log(f"✅ Changed ownership: {path} -> {user}:{group}")
    except subprocess.CalledProcessError as e:
        log(f"❌ Failed to change ownership of {path}")
        log(e.stderr)
    except Exception as e:
        log(f"❌ Unexpected error while changing ownership: {str(e)}")


#docker exec -it mssql_stage $sqlcmd_path -U sa -P $PASS -C \
#  -Q "BACKUP DATABASE [dababase_name] TO DISK = N'/backup/city_name.bak' WITH INIT, FORMAT;"

def backup():
    log(f"Backup started at {now.strftime('%d-%m-%Y %H:%M:%S')}")
    query = (
        f"BACKUP DATABASE [{db_name}]"
        f"TO DISK = N'{container_backup_path}' "
        f"WITH INIT, FORMAT;"
    )

    cmd = [
        "docker",
        "exec",
        container_name,
        sqlcmd_path,
        "-S", "localhost",
        "-U", db_user,
        "-P", db_pass,
        "-C",
        "-Q", query
    ]

    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        log("✅ Backup completed successfully.")
        log(result.stdout)

        wait_for_file(host_backup_path)
        change_ownership(host_backup_path)
    except subprocess.CalledProcessError as e:
        log("❌ Backup failed.")
        log(e.stderr)
        exit(1)
    except Exception as e:
        log(f"❌ Unexpected error: {str(e)}")
        exit(1)

def transfer_backup():
    remote_user = "hojat"
    remote_host = "192.168.1.1"
    remote_port = "2221"
    remote_dir = "/var/project_backups/"

    scp_cmd = [
        "scp",
        "-P",
        remote_port,
        "-i", "/home/hojat/.ssh/id_ed25519",
        host_backup_path,
        f"{remote_user}@{remote_host}:{remote_dir}"
    ]

    try:
        result = subprocess.run(scp_cmd, check=True, capture_output=True, text=True)
        log("✅ Backup transferred successfully.")
        log(result.stdout)
    except subprocess.CalledProcessError as e:
        log("❌ Failed to transfer backup to remote server.")
        log(e.stderr)
        exit(1)

def cleanup_old_backups(retention_days=3):
    now = time.time()
    cutoff = now - (retention_days * 86400)

    try:
        for file in glob.glob(os.path.join(host_backup_dir, f"{db_name}_*.bak")):
            if os.path.isfile(file) and os.path.getmtime(file) < cutoff:
                os.remove(file)
                log(f"🗑️ Removed old backup: {file}")
        log(f"🚮 Removed all backup file more than {retention_days} days.")
    except Exception as e:
        log(f"❌ Cleaning old backup fialed: {str(e)}")

def wait_for_file(path, timeout=10):
    start = time.time()
    while not os.path.exists(path):
        if time.time() - start > timeout:
            raise FileNotFoundError(f"Timeout waiting for file: {path}")
        time.sleep(0.5)


if __name__ == "__main__":
    try:
        backup()
        transfer_backup()
        cleanup_old_backups()
    except Exception as e:
        log(f"❌ Fatal error during back pipeline: {str(e)}")

