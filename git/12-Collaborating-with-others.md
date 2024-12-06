# Collaborating with others

```sh
gr -v 		# git remote -v
gb --all	# git branch --all

```

## Renaming a remote

```sh
gr rename origin begining 	# git remote origin begining
gr -v                    
begining        /Users/hojat/Documents/ww/git/math.git (fetch)
begining        /Users/hojat/Documents/ww/git/math.git (push)
```

## Adding a remote

```sh
Documents/ww/git 
❯ ls -d math.git math.bob math.carol
math.bob   math.carol math.git

Documents/ww/git 
❯ cd math.carol

math.carol on  main 
❯ gr -v   
origin  /Users/hojat/Documents/ww/git/math.git (fetch)
origin  /Users/hojat/Documents/ww/git/math.git (push)

math.carol on  main 
❯ gr add bob ../math.bob

math.carol on  main 
❯ gr -v                 
bob     ../math.bob (fetch)
bob     ../math.bob (push)
origin  /Users/hojat/Documents/ww/git/math.git (fetch)
origin  /Users/hojat/Documents/ww/git/math.git (push)
```

## interrogating a remote

`git ls-remote <BRANCH-NAME>` return a list of the SHA1 IDs of each branch and tag

```sh
math.carol on  main 
❯ git ls-remote             
Found existing alias for "git". You should use: "g"
From /Users/hojat/Documents/ww/git/math.git
cba7cadef153a58790399e6420e2a1c0459584f1        HEAD
1b0908d9351c78d5358cde9cd49d34817efd79ce        refs/heads/another_fix_branch
cba7cadef153a58790399e6420e2a1c0459584f1        refs/heads/main
0a202dfc2e1e32a06aff9ef78f7610c2636f21bc        refs/heads/new_feature
95187fa566638f57355ce1215193a6a0befcd913        refs/tags/add_readme_file
24dc91069cfbdb797d7e8a997aa105c85559e078        refs/tags/add_readme_file^{}

math.carol on  main 
❯ git ls-remote origin
Found existing alias for "git". You should use: "g"
cba7cadef153a58790399e6420e2a1c0459584f1        HEAD
1b0908d9351c78d5358cde9cd49d34817efd79ce        refs/heads/another_fix_branch
cba7cadef153a58790399e6420e2a1c0459584f1        refs/heads/main
0a202dfc2e1e32a06aff9ef78f7610c2636f21bc        refs/heads/new_feature
95187fa566638f57355ce1215193a6a0befcd913        refs/tags/add_readme_file
24dc91069cfbdb797d7e8a997aa105c85559e078        refs/tags/add_readme_file^{}

math.carol on  main 
❯ git ls-remote bob   
Found existing alias for "git". You should use: "g"
cba7cadef153a58790399e6420e2a1c0459584f1        HEAD
cba7cadef153a58790399e6420e2a1c0459584f1        refs/heads/main
cba7cadef153a58790399e6420e2a1c0459584f1        refs/remotes/origin/HEAD
1b0908d9351c78d5358cde9cd49d34817efd79ce        refs/remotes/origin/another_fix_branch
cba7cadef153a58790399e6420e2a1c0459584f1        refs/remotes/origin/main
0a202dfc2e1e32a06aff9ef78f7610c2636f21bc        refs/remotes/origin/new_feature
95187fa566638f57355ce1215193a6a0befcd913        refs/tags/add_readme_file
24dc91069cfbdb797d7e8a997aa105c85559e078        refs/tags/add_readme_file^{}
```

```sh
math.carol on  main 
❯ cd ../math.bob  

math.bob on  main [⇡] 
❯ ls                                
another_rename doc            math.sh        readme.txt     renamed_file

math.bob on  main [⇡] 
❯ gswc another_branch            
Switched to a new branch 'another_branch'

math.bob on  another_branch 
❯ echo "Small change to file" >> another_rename_a

math.bob on  another_branch [?] 
❯ gaa                                      

math.bob on  another_branch [+] 
❯ gc -am "Updating this file on new branch"
[another_branch ab2245b] Updating this file on new branch
 1 file changed, 1 insertion(+)
 create mode 100644 another_rename_a

math.bob on  another_branch 
❯ cd ../math.carol

math.carol on  main 
❯ 

math.carol on  main 
❯ g ls-remote .                            
cba7cadef153a58790399e6420e2a1c0459584f1        HEAD
cba7cadef153a58790399e6420e2a1c0459584f1        refs/heads/main
cba7cadef153a58790399e6420e2a1c0459584f1        refs/remotes/origin/HEAD
1b0908d9351c78d5358cde9cd49d34817efd79ce        refs/remotes/origin/another_fix_branch
cba7cadef153a58790399e6420e2a1c0459584f1        refs/remotes/origin/main
0a202dfc2e1e32a06aff9ef78f7610c2636f21bc        refs/remotes/origin/new_feature
95187fa566638f57355ce1215193a6a0befcd913        refs/tags/add_readme_file
24dc91069cfbdb797d7e8a997aa105c85559e078        refs/tags/add_readme_file^{}

math.carol on  main 
❯ g ls-remote bob
ab2245b1e0d6ff34de9c63c97e643dabec37f44f        HEAD
ab2245b1e0d6ff34de9c63c97e643dabec37f44f        refs/heads/another_branch
5c140f97ee962b231b7aff36e0d1a848c1eef4d3        refs/heads/main
cba7cadef153a58790399e6420e2a1c0459584f1        refs/remotes/origin/HEAD
1b0908d9351c78d5358cde9cd49d34817efd79ce        refs/remotes/origin/another_fix_branch
cba7cadef153a58790399e6420e2a1c0459584f1        refs/remotes/origin/main
0a202dfc2e1e32a06aff9ef78f7610c2636f21bc        refs/remotes/origin/new_feature
95187fa566638f57355ce1215193a6a0befcd913        refs/tags/add_readme_file
24dc91069cfbdb797d7e8a997aa105c85559e078        refs/tags/add_readme_file^{}

math.carol on  main 
❯ 

```

```sh
math.carol on  main 
❯ g log --oneline -1   # show only one commit                                    
cba7cad (HEAD -> main, origin/main, origin/HEAD) A small upate to readme.

❯ g log --oneline -2 	# show two last commit                 
cba7cad (HEAD -> main, origin/main, origin/HEAD) A small upate to readme.
1884180 Adding printf.
```

## push reject

```sh
git push bob main
To ../math.bob
 ! [rejected]        main -> main (fetch first)

git pull         
Already up to date.

git fetch bob
From ../math.bob
 * [new branch]      another_branch -> bob/another_branch
 * [new branch]      main           -> bob/main

git log --oneline main..bob/main

git merge bob/main
Updating cba7cad..5c140f9
Fast-forward
 another_rename | 1 +
 1 file changed, 1 insertion(+)

git push bob main
Everything up-to-date
```


```sh
git pull origin
fatal: Not possible to fast-forward, aborting.

git fetch origin
git merge origin/main
git mergetool
gc -am "Conflict resolved"
```








