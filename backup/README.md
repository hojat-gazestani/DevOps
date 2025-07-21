# Backup databses

Using this you can backup your databases and copy them to a remote host

+ put it in `crontab -e`
```sh
0 1 * * * /usr/bin/python3 /home/hojat/rigan/backup/backup_daily_cityname.py >> /var/project_backups/cron.log 2>&1
```

+ Copy backups to remote host using rsync
```sh
rsync -az --inplace --partial --append-verify -e "ssh -T -c aes128-ctr -o Compression=no -x" src/ user@192.168.1.X:/path/
```
