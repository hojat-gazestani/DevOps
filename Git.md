[TOC]





# Git

## ADD, STATUS, COMMIT

cd ww/project
git init
ls -la .git

git status
on brach master
Initial commit



```html
vim index.html
<html>
<body>
	hi
</body>
</html>
```



git status
```shell
Untracked files:
	index.html
```

​	

git add index.html
git status
new file:  index.html

git commit -m "this is message"

vim index.html
```html
<html>
<body>
	hi here
</body>
</html>
```



git status 
modified : index.html

git add -A
git status
git commit -m "commited all"


## JOB HISTORY: GIT LOG

git log

vim page1.html
	this is page1
vim page2.html
	this is page2
vim page3.html
	this is page3

```shell
git status
Untracked file:
	page1.html	
	page2.html
	page3.html
```


```html
vim index.html
<html>
<body>
	wait for commit
</body>
</html>
```



```shell
git status
Changes not staged for commit:
	modified: index.html
Untracked file:
	page1.html	
	page2.html
	page3.html
```

​	
git add "page*"

git commit -m "3 pages"

git status
Changes not staged for commit:
	modified: index.html
	
git add index.html

git commit -m "commit on index.html"

git log




## HISTORY OF CHANGES


git status

git diff HEAD

git diff --staged

git add -A

git reset page3.html
unstaged changes after reset:
	page3.html
	
git checkout -- page3.html

git commit


## BRANCHES


git branch
*master

git branch fixpages

git branch
*master
fixpages

git checkout fixpages

git branch
master
*fixpages



```shell
# MADE SOME CHAGE ON PAGE FILE
vim footer.html
	<hr >
	fun site for fun
```



git status
On branch fixpages

Changes not stagged for commit:
	PAGE FILE
	
Untracked files:
	footer.html
	
git add commit -m "adding PAGE FILE"

git add -A

git commit -m "footer added"

git branch
master
*fixpages

git checkout master

git merge fixpages

git log




## COUNTINIOU BRANCHES

git branch linkingpages

git checkout linkingpages

git status

git rm footer.html

```html
vim index.html
<html>
<body>
	hi there baby
	<br /><a href="page1.html">1</a>
	<br /><a href="page1.html">1</a>
	<br /><a href="page1.html">1</a>
</body>
</html>
```



git commit -m "removed footer"

git add -A

git commit -m "added page to index"

git checkout master

git merge linkingpages

git branch -d linkingpages




## COUNTINIOU BRANCHES - REMOTE


git push origin maser
gazestani
password

git pull origin master




## CONFLICT


cd ww/project

git status

git remote  add origin https://peygir.net/project/...

git remote

git remote -v

git push -u origin master

cd ../titabmistory

```shell
# MADE SOME CHANGES
```



git commit -M "added a newline text only for show conflict"

```shell
# MADE SOME ANOTHER CHANGES FROM ANOTHER COMPUTER
```

git commit -m "second edited"

git push origin master
[rejected]

git pull

git status

vim FILE
   MADE YOUR CHANGE

git add -A

git commit -m "fix the conflict on new line"

git push 




## SIGN AND TAG


pgp
gpg

gpg --list-keys

gpg --gen-key
name:
emage:
password:

gpg --list-keys

git config

git config --global user.name

git config --global user.signingkey

gpg --list-secret-keys --keyid-format LONG

git conifg --global user.signinkey PUBKEY

git tag -a v2.1 -m "this is version 2.1"

git tag -s v2.1 -m "this is version 2.1"

git log

git tag

git show v2.1

git tag -v v2.1

git commit -S  -m "this is sign commit"




## DEBUG


git help blame

less somefile.sh

git blame somefile -L8,10

git bisect start
git bisect bad
git bisect good SOME-SIGNE-STADE 

## GITLAB



##  store the github https token using pass

```shell
git config --global --replace-all credential.helper cache
git push
```

