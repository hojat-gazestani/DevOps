# Tracking and updating files in Git

## Creating a new repository 
```sh
take math
git init

echo "# Comment" > math.sh
ga math.sh
gc -m "This is the first commit message."
glo                                      
f8a9ffa (HEAD -> main) This is the first commit message.
```

## Telling Git about changes

```sh
echo "a=1" >> math.sh

cat math.sh              
# Comment
a=1

gst
Changes not staged for commit:
	modified:   math.sh

git checkout -- math.sh	# any uncommitted changes in `math.sh`` will be lost

cat math.sh
# Comment
```

## seeing what's different

```sh
echo "a=1" >> math.sh

gd		# (git diff) current files vs last committed.
gds		# (git diff --staged) committed vs remove.
gd commit1 commit2 # differences between two commits
dg branch1 branch3 # differences between two branches
gd math.sh	# compared to the last commit,
```

## Updating the staging area

```sh
echo "echo \$a" >> math.sh
echo "b=2" >> math.sh
ga math.sh
gst
	modified:   math.sh

vim math.sh		# remove the echo line
cat math.sh        
# Comment
a=1
b=2

gst		# It has already staged and isn't staged yet changes.
Changes to be committed:
	modified:   math.sh
Changes not staged for commit:
	modified:   math.sh

gd 		# file in working directory vs stagin area
 
Δ math.sh
 
─────┐
• 1: │
─────┘
│  1 ││  1 │# Comment
│  2 ││  2 │a=1
│  3 ││    │echo $a
│  4 ││  3 │b=2


gds       # Commited file  vs staged
 
Δ math.sh
 
─────┐
• 1: │
─────┘
│  1 ││  1 │# Comment
│    ││  2 │a=1
│    ││  3 │echo $a
│    ││  4 │b=2

ga math.sh
gc -m "Adding b variable"
```

## Adding multiple files

```sh
ls
a       b       c       d       math.sh

gst             
Untracked files:
        a
        b
        c
        d

git add --dry-run .	# show you what it would have done.
add 'a'
add 'b'
add 'c'
add 'd'

gst      
Changes to be committed:
        new file:   a
        new file:   b
        new file:   c
        new file:   d

gc -m "dding four empty files"           
 create mode 100644 a
 create mode 100644 b
 create mode 100644 c
 create mode 100644 d

glo                           
e2a828d (HEAD -> main) dding four empty files
2a809d1 Adding b variable
f8a9ffa This is the first commit message.
```


















