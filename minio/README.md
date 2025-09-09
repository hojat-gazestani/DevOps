
```bash
mc alias set localminio http://localhost:9000 MINIO_ROOT_USER MINIO_ROOT_PASSWORD

mc admin user list localminio
mc admin group list localminio
mc admin policy list localminio

mc admin user add localminio test TestPass123
mc admin policy attach localminio readwrite --user test
mc admin user info localminio test
```
