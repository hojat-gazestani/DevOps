# Making and using a git repository

## Creating a new repository with git init

```sh
take buildtools
git init
ls -a 
.    ..   .git

gst			# (git status) Tell the state of your workin directory

echo -n contents > filefixup.bat
gst
Untracked files:
	filefixup.bat

ga filefixup.bat	# (git add) Telling git keep track of this file
gst
Changes to be committed:
	new file:   filefixup.bat

gc	# (git commit) Create the timeline
gc -m "This is the first commit message."


glog	# (git log --stat) To see the files that are a part of the commit
```