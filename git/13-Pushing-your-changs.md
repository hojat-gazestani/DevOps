# Pushing your changs

```sh
math.carol on  main [?] 
echo "Added a line here." >> renamed_file
gc -am "Updated renamed_file"

gst                          
Your branch is ahead of 'origin/main' by 1 commit.

gp origin main 
Enumerating objects: 5, done.

g log -2

# Verifying a successful git push, same SHA1
g ls-remote origin
dd1eea8608317b1c5a97beff2fe031c2db2c6313        HEAD
dd1eea8608317b1c5a97beff2fe031c2db2c6313        refs/heads/main


g remote show origin                                                 
* remote origin
  Fetch URL: /Users/hojat/Documents/ww/git/math.git
  Push  URL: /Users/hojat/Documents/ww/git/math.git
  HEAD branch: main
  Remote branches:
    another_fix_branch tracked
    main               tracked
    new_feature        tracked
  Local branch configured for 'git pull':
    main merges with remote main
  Local ref configured for 'git push':
    main pushes to main (up to date)

## From Bob's view
g remote -v show origin                                              
* remote origin
  Fetch URL: /Users/hojat/Documents/ww/git/math.git
  Push  URL: /Users/hojat/Documents/ww/git/math.git
  HEAD branch: main
  Remote branches:
    another_fix_branch tracked
    main               tracked
    new_feature        tracked
  Local branch configured for 'git pull':
    main merges with remote main
  Local ref configured for 'git push':
    main pushes to main (local out of date) 	# Not sync
```

## Understanding push conflicts

```sh
math.bob on  main 
echo "Small change to file" >> another_rename

gc -am "Updating this file"
gp origin main             
To /Users/hojat/Documents/ww/git/math.git
 ! [rejected]        main -> main (fetch first)
```

## Pushing branches

```sh
g checkout another_fix_branch
echo "Carol Small change to file" >> another_rename
gc -am "Carol small changes to another_rename"
gp

g checkout -b new_branch main
gp
fatal: The current branch new_branch has no upstream branch
git push --set-upstream origin new_branch 
```

## Deleting branch on remote

```sh
math.carol on  new_branch 
❯ gsw main

gb      
  another_fix_branch
* main
  new_branch

gb -d new_branch

gb              
  another_fix_branch
* main

git ls-remote origin   # It's still on remote                  
...
04ddba627a73bc4191d58c92ee31676e8f32e782        refs/heads/new_branch
...


git push origin :new_branch
To /Users/hojat/Documents/ww/git/math.git
 - [deleted]         new_branch
```

## Pushing and deleting tags

```sh
g tag 
add_readme_file

g tag -a two_back -m "Two behind the HEAD" @^^
glo                                           
04ddba6 (HEAD -> main, origin/main, origin/HEAD) Carol Updated renamed_file
ce7e120 Carol resovle confilict
6745a89 Bob update to another readme
697651e (tag: two_back) Carol line to another_renam

g ls-remote origin                            
ada32fcc81a0ddecba1a3262fb8dbb4c8ae965f5        HEAD
7798927154d976f697da3649e031cb5d28bc9804        refs/heads/another_fix_branch
ada32fcc81a0ddecba1a3262fb8dbb4c8ae965f5        refs/heads/main
0a202dfc2e1e32a06aff9ef78f7610c2636f21bc        refs/heads/new_feature
95187fa566638f57355ce1215193a6a0befcd913        refs/tags/add_readme_file
24dc91069cfbdb797d7e8a997aa105c85559e078        refs/tags/add_readme_file^{}

gp origin two_back

g ls-remote origin
...
15e831ae8fa6cf68f86211890d2b80eebc6806ff        refs/tags/two_back
697651e3213719b5d3bea23d9b5d1565af4853f5        refs/tags/two_back^{}

gp --tags	# Send over all the local tags

# Deleting tags

g ls-remote origin
...
15e831ae8fa6cf68f86211890d2b80eebc6806ff        refs/tags/two_back
697651e3213719b5d3bea23d9b5d1565af4853f5        refs/tags/two_back^{}

gp origin :two_back
 - [deleted]         two_back

g ls-remote origin 
ada32fcc81a0ddecba1a3262fb8dbb4c8ae965f5        HEAD
7798927154d976f697da3649e031cb5d28bc9804        refs/heads/another_fix_branch
ada32fcc81a0ddecba1a3262fb8dbb4c8ae965f5        refs/heads/main
0a202dfc2e1e32a06aff9ef78f7610c2636f21bc        refs/heads/new_feature
95187fa566638f57355ce1215193a6a0befcd913        refs/tags/add_readme_file
24dc91069cfbdb797d7e8a997aa105c85559e078        refs/tags/add_readme_file^{}


```