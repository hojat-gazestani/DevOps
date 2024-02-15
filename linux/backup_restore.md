# Backup and Restore Ubuntu Using Tar in Terminal

### backup
```shell
sudo tar -cvpzf backup.`date +%d-%m-%y`.tar.gz --exclude=/home/server/backup.`date +%d-%m-%y`.tar.gz --one-file-system / 
	-c	create new tar file
	-v	verbos
	-p	preserve permissions
	-z	gzip compresion is smaller
	-f	file name and location
	--one-file-system	exclude certian system directorys (proc, sys, mount, media, run, dev	()
```
-
### restore
```shell
sudo tar -xvpzf /home/server/backup.tar.gz -C / --numeric-owner 
	-x extract 
```
