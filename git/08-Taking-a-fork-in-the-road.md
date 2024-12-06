# Taking a fork in the road

## Creating refrences

```sh
take empty
g init
touch foo
ga foo
gc -m "commiting the file foo"

gb                            
* main

git branch dev		# Create new branch
gb            
  dev
* main

gsw dev
gb     
* dev
  main

gb -d main
gb        
* dev
```

## introdocing new code with branches

```sh
cd ../math
gb new_feature
gb            
* main
  new_feature
  try-from-adding-four-files

gsw new_feature
echo "new file" > newfile.txt
ga newfile.txt 
gc -m "Adding a new file to a new branch"
echo "another new file" > file3.c
ga file3.c
gc -m "Starting a second new file"
```

## Switching between branches

```sh
gb                             
  main
* new_feature
  try-from-adding-four-files

gb -v
  main                       6857281 This is the second test
* new_feature                18be3bf Starting a second new file
  try-from-adding-four-files e2a828d dding four empty files

gsw main

echo "A small upate." >> readme.txt
ga readme.txt 
gc -m "A small upate to readme." 
```

## Introducing fixes with branches

```sh
gb 
* main
  new_feature
  try-from-adding-four-files

glo  
b1ca9c3 (HEAD -> main) A small upate to readme.
6857281 (tag: testing_checkout) This is the second test
6fc6afe Adding printf
c3f6215 This is a test commit These are extra explaination And it is another line description This is the third line
72a8ae3 (tag: testing_checkout_one) Testign checkout
659617d test
41d7f2e Adding new doc dir and file
8e9c36e Renaming c and d
6b00af9 Removed a and b
e2a828d (tag: four_files_galore, try-from-adding-four-files) dding four empty files
2a809d1 Adding b variable
f8a9ffa This is the first commit message.

g branch fixing_readme 8e9c36e
gb                            
  fixing_readme
* main
  new_feature
  try-from-adding-four-files

g checkout -b another_fix_branch fixing_readme
gb                                            
* another_fix_branch
  fixing_readme
  main
  new_feature
  try-from-adding-four-files
```

## Deleting branches

```sh
gsw main
gb      
  another_fix_branch
  fixing_readme
* main
  new_feature
  try-from-adding-four-files

gb -d fixing_readme
gb                 
  another_fix_branch
* main
  new_feature
  try-from-adding-four-files

gb -d another_fix_branch
Deleted branch another_fix_branch (was 8e9c36e).
gb                      
* main
  new_feature
  try-from-adding-four-files

# If you realize that this delete was the wrong thing to do,
# you can re-create the branch by immidiately type the following
g checkout -b recover_delete_branch 8e9c36e
gb                                         
  main
  new_feature
* recover_delete_branch
  try-from-adding-four-files


# Shows a record of all the times that you have changed branchs.
git reflog       
Found existing alias for "git reflog". You should use: "grf"
8e9c36e (HEAD -> recover_delete_branch) HEAD@{0}: checkout: moving from main to recover_delete_branch
b1ca9c3 (main) HEAD@{1}: checkout: moving from another_fix_branch to main
8e9c36e (HEAD -> recover_delete_branch) HEAD@{2}: checkout: moving from main to another_fix_branch
b1ca9c3 (main) HEAD@{3}: commit: A small upate to readme.
6857281 (tag: testing_checkout) HEAD@{4}: checkout: moving from new_feature to main
18be3bf (new_feature) HEAD@{5}: commit: Starting a second new file
3bd204a HEAD@{6}: commit: Adding a new file to a new branch
6857281 (tag: testing_checkout) HEAD@{7}: checkout: moving from main to new_feature
6857281 (tag: testing_checkout) HEAD@{8}: checkout: moving from e2a828d508b737e4b720a3bacf0e7b5ef3b0b422 to main
e2a828d (tag: four_files_galore, try-from-adding-four-files) HEAD@{9}: checkout: moving from main to four_files_galore
6857281 (tag: testing_checkout) HEAD@{10}: checkout: moving from e2a828d508b737e4b720a3bacf0e7b5ef3b0b422 to main
e2a828d (tag: four_files_galore, try-from-adding-four-files) HEAD@{11}: checkout: moving from main to e2a828d
6857281 (tag: testing_checkout) HEAD@{12}: checkout: moving from try-from-adding-four-files to main
e2a828d (tag: four_files_galore, try-from-adding-four-files) HEAD@{13}: checkout: moving from e2a828d508b737e4b720a3bacf0e7b5ef3b0b422 to try-from-adding-four-files
e2a828d (tag: four_files_galore, try-from-adding-four-files) HEAD@{14}: checkout: moving from main to e2a828d
6857281 (tag: testing_checkout) HEAD@{15}: checkout: moving from e2a828d508b737e4b720a3bacf0e7b5ef3b0b422 to main
e2a828d (tag: four_files_galore, try-from-adding-four-files) HEAD@{16}: checkout: moving from main to e2a828d
6857281 (tag: testing_checkout) HEAD@{17}: checkout: moving from 659617d8408106cb6da691c0a690fb18f6914026 to main
659617d HEAD@{18}: checkout: moving from main to 659617d
6857281 (tag: testing_checkout) HEAD@{19}: checkout: moving from 659617d8408106cb6da691c0a690fb18f6914026 to main
659617d HEAD@{20}: checkout: moving from main to 659617d
6857281 (tag: testing_checkout) HEAD@{21}: rebase (finish): returning to refs/heads/main
6857281 (tag: testing_checkout) HEAD@{22}: rebase (start): checkout @~9
6857281 (tag: testing_checkout) HEAD@{23}: rebase (finish): returning to refs/heads/main
6857281 (tag: testing_checkout) HEAD@{24}: rebase (start): checkout @~9
```

## Switching branches safely

# stashing away your work

- Putting aside your work temporary

```sh
gsw another_fix_branch
echo "c=3" >> math.sh

gst                   
Changes not staged for commit:
        modified:   math.sh

gsw main              
error: Your local changes to the following files would be overwritten by checkout:
        math.sh
Please commit your changes or stash them before you switch branches.
Aborting

g stash                                       
Saved working directory and index state WIP on another_fix_branch: 8e9c36e Renaming c and d

gst     
On branch another_fix_branch
nothing to commit, working tree clean

gsw main
Switched to branch 'main'

gsw another_fix_branch
g stash list          
stash@{0}: WIP on another_fix_branch: 8e9c36e Renaming c and d
g stash pop

```


















