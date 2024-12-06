# An overview of Git and version controll

```sh
git ls-files	# Get the list of files
gbl README.txt	# (git blame) To see a detailed view of the file

git log --oneline	# To get a listing f the repository's history of commits
gloga='git log --oneline --decorate --graph --all'
glols='git log --graph --pretty="%Cred%h%Creset -%C(auto)%d%Creset %s %Cgreen(%ar) %C(bold blue)<%an>%Creset" --stat'

```