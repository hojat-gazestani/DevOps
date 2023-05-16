
```bash
user@backend:~$ cat Postgres01/Dockerfile 
FROM postgres:13.2

ENV POSTGRES_USER myuser
ENV POSTGRES_PASSWORD mypassword
ENV POSTGRES_DB mydb

COPY init.sql /docker-entrypoint-initdb.d/

EXPOSE 5432
```

```bash
user@backend:~$ cat Postgres01/init.sql 
SELECT 1 FROM pg_roles WHERE rolname = 'myuser' LIMIT 1;
DO $$BEGIN
  IF NOT FOUND THEN
    CREATE ROLE myuser WITH LOGIN PASSWORD 'mypassword';
  ELSE
    ALTER ROLE myuser WITH PASSWORD 'mypassword';
  END IF;
END$$;

CREATE DATABASE mydb;
GRANT ALL PRIVILEGES ON DATABASE mydb TO myuser;
```

```bash
docker build -t my-postgres .

docker run --name my-postgres-container -e POSTGRES_PASSWORD=mysecretpassword -d -p 5432:5432 postgres:13.2
```
