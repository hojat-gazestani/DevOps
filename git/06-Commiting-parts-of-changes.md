# Commiting parts of changes

## Deleting files from Git

```sh
ls
a       b       c       d       math.sh

gst  # You have updated working directory
Changes not staged for commit:
        deleted:    a

grm a  # (git rm) Adding update to staging area      	
rm 'a'


grm b 	# (git rm) Deleting file from working dir and staging area

gc -m "Removed a and b"
```


## Renaming file in Git

```sh
ls
c       d       math.sh

mv c renamed_file

gst                    
Changes not staged for commit:
        deleted:    c
 
Untracked files:
        renamed_file

grm c
rm 'c'

ga renamed_file

gst            
Changes to be committed:
        renamed:    c -> renamed_file

git mv d another_rename

gst                    
Changes to be committed:
        renamed:    c -> another_rename
        renamed:    d -> renamed_file

gc -m "Renaming c and d"
```

## Adding directories into your repository

```sh
mkdir doc
touch doc/doc.txt

ga doc/
gc -m "Adding new doc dir and file"
```

## Adding parts of changes

```sh
cat math.sh
# Add a and b
a=1
b=2
#
# These are for testing
#
echo $a
echo $b
let c=$a+$b
echo $c

ga -p math.sh	# Edit file to commit
```

## Removing changes form the staging area

git add
git reset

```sh
cat math.sh
# Add a and b
a=1
b=2
#
# These are for testing
#
echo $a
echo $b
let c=$a+$b
echo $c

 gd        
 
Δ math.sh
 
─────┐
• 1: │
─────┘
│  1 ││  1 │# Add a and b
│  2 ││  2 │a=1
│  3 ││  3 │b=2
│    ││  4 │#
│    ││  5 │# These are for testing
│    ││  6 │#
│  4 ││  7 │echo $a
│  5 ││  8 │echo $b
│  6 ││  9 │let c=$a+$b


ga math.sh

gd
# Nothing

grh		# (git reset) to Undo a staging area changee.

git reset math.sh
Unstaged changes after reset:
M       math.sh

gd 
 
Δ math.sh
 
─────┐
• 1: │
─────┘
│  1 ││  1 │# Add a and b
│  2 ││  2 │a=1
│  3 ││  3 │b=2
│    ││  4 │#
│    ││  5 │# These are for testing
│    ││  6 │#
│  4 ││  7 │echo $a
│  5 ││  8 │echo $b
│  6 ││  9 │let c=$a+$b
```

## Reseting a file to the last commited version

```sh
cat math.sh
# Add a and b
a=1
b=2
echo $a
echo $b
let c=$a+$b
echo $c

g show @:math.sh       
# Add a and b
a=1
b=2
#
# These are for testing
#
echo $a
echo $b
let c=$a+$b
echo $c

git checkout -- math.sh

cat math.sh
# Add a and b
a=1
b=2
#
# These are for testing
#
echo $a
echo $b
let c=$a+$b
echo $c
```



























