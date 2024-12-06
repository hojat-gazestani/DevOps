## The time machine that is git

```sh
git log		# commit timeline

		--oneline	# more concise listing
		--stat		# which files were changed and how many lines were added or removed
		--patch		# Show patch information
		--patch-with-stat	# Patch info, changed file, removed and added lines

g log --oneline math.sh 	# Commits that pertain to just math.sh
72a8ae3 (HEAD -> main) Testign checkout
659617d test
2a809d1 Adding b variable
f8a9ffa This is the first commit message.

git commit --amend	# Commited but need to give it more text

g rev-parse @    # Translate branch names to their SHA1 IDs        
6857281670498e2fe38807e8edc8dc01df527d8f
```

## Going back in time with git checkout

```sh
ls
another_rename doc            math.sh        renamed_file

git log --oneline           
Found existing alias for "git". You should use: "g"
6857281 (HEAD -> main) This is the second test
6fc6afe Adding printf
c3f6215 This is a test commit 
72a8ae3 Testign checkout
659617d test
41d7f2e Adding new doc dir and file
8e9c36e Renaming c and d
6b00af9 Removed a and b
e2a828d dding four empty files
2a809d1 Adding b variable
f8a9ffa This is the first commit message.

git checkout e2a828d
ls
a       b       c       d       math.sh

gswc try-from-adding-four-files
ls
a       b       c       d       math.sh

gsw main
```

## Breadcrumbs to previous versions

```sh
git tag testing_checkout_one 72a8ae3 -m "This is testing checkout one"

gloga                                                                 
* 6857281 (HEAD -> main, tag: testing_checkout) This is the second test
* 6fc6afe Adding printf
* c3f6215 This is a test commit These are extra explaination And it is another line description This is the third line
* 72a8ae3 (tag: testing_checkout_one) Testign checkout
* 659617d test
* 41d7f2e Adding new doc dir and file
* 8e9c36e Renaming c and d
* 6b00af9 Removed a and b
* e2a828d (tag: four_files_galore, try-from-adding-four-files) dding four empty files
* 2a809d1 Adding b variable
* f8a9ffa This is the first commit message.

math on  main 
❯ git checkout four_files_galore

ls
a       b       c       d       math.sh

```







































