# Cloning

git clone source destination_dir

## Local clone

```sh
Documents/ww/git
❯ cd math

math on  another_fix_branch 
❯ gsw main     
Switched to branch 'main'

math on  main 
❯ cd .. 

Documents/ww/git
❯ ls
buildtools            
math              
empty                           
ff                  


Documents/ww/git 
❯ git clone math math.clone1                       
Cloning into 'math.clone1'...
done.

Documents/ww/git
❯ ls
buildtools            
math              
empty                           
ff                  
math.clone1
```

## Get simplified list of branches
```sh
math.clone2 on  main 
❯ gig log --simplify-by-decoration --decorate --all --oneline 
cba7cad (HEAD -> main, origin/main) A small upate to readme.
0a202df (origin/new_feature) Starting a second new file
1b0908d (origin/another_fix_branch) Renamed c and d
24dc910 (tag: add_readme_file) Add readme file
dc173ff This is the first commit.
```

## Remote branches

```sh
# To see all branched on cloned repository
❯ gba # git branch --all
* main
  remotes/origin/HEAD -> origin/main
  remotes/origin/another_fix_branch
  remotes/origin/main
  remotes/origin/new_feature

# re-create any branch that exist in the original repository
math.clone1 on  main 
❯ gsw another_fix_branch # git switch another_fix_branch 
# git checkout -b another_fix_branch  remotes/origin/another_fix_branch
branch 'another_fix_branch' set up to track 'origin/another_fix_branch'.
Switched to a new branch 'another_fix_branch'

math.clone1 on  another_fix_branch 
❯ ls
another_rename math.sh        readme.txt     renamed_file
```

## Bare clone - only the repository file

- You can’t perform any Git operations within the math.git directory, because there’s no working directory. But you can clone this math.git directory and push commits to it.

```sh
Documents/ww/git 
❯ ls
buildtools          ff                  make_merge_ff.sh    math                math.clone2         my_project
empty               libgit2             make_merge_repos.sh math.clone1         mergesample         twoatonce

Documents/ww/git 
❯ git clone --bare math math.git
Found existing alias for "git". You should use: "g"
Cloning into bare repository 'math.git'...
done.

Documents/ww/git 
❯ 

Documents/ww/git 
❯ ls
buildtools          libgit2             math                math.git            twoatonce
empty               make_merge_ff.sh    math.clone1         mergesample
ff                  make_merge_repos.sh math.clone2         my_project
```

## cloning from a bare directory

- Bare directory has no refrence to the original repository
- Unlike a clone, which has a reference to its origination repository, the bare directory is a completely standalone repository.

```sh
Documents/ww/git 
❯ git clone math.git math.clone3
Found existing alias for "git". You should use: "g"
Cloning into 'math.clone3'...
done.

Documents/ww/git 
❯ cd math.clone3

math.clone3 on  main 
❯ git log --oneline --all                   
Found existing alias for "git". You should use: "g"
cba7cad (HEAD -> main, origin/main, origin/HEAD) A small upate to readme.
0a202df (origin/new_feature) Starting a second new file
1450a38 Adding a new file to a new branch
1884180 Adding printf.
e210da6 change math
c88fd30 try dash p
2c6d92c Add calculation
411fb74 Add Testing lines
810f6f6 First comment
f891966 Retry Adding parts of change
c017e9e Adding new doc dir and file
1b0908d (origin/another_fix_branch) Renamed c and d
5884d8b Removed a and b
24dc910 (tag: add_readme_file) Add readme file
c1db8be This is the second commit.
dc173ff This is the first commit.

math.clone3 on  main 
❯ 
```

## Listing files in the repo by using git ls-tree

```sh
math.clone3 on  main 
❯ g ls-tree --name-only -r  HEAD
another_rename
doc/doc.txt
math.sh
readme.txt
renamed_file

```

- show tag

```sh
math.clone3 on  main 
❯ gloga                         
* cba7cad (HEAD -> main, origin/main, origin/HEAD) A small upate to readme.
| * 0a202df (origin/new_feature) Starting a second new file
| * 1450a38 Adding a new file to a new branch
|/  
* 1884180 Adding printf.
* e210da6 change math
* c88fd30 try dash p
* 2c6d92c Add calculation
* 411fb74 Add Testing lines
* 810f6f6 First comment
* f891966 Retry Adding parts of change
* c017e9e Adding new doc dir and file
* 1b0908d (origin/another_fix_branch) Renamed c and d
* 5884d8b Removed a and b
* 24dc910 (tag: add_readme_file) Add readme file
* c1db8be This is the second commit.
* dc173ff This is the first commit.

math.clone3 on  main 
❯ g ls-tree add_readme_file     
100644 blob e69de29bb2d1d6434b8b29ae775ad8c2e48c5391    a
100644 blob e69de29bb2d1d6434b8b29ae775ad8c2e48c5391    b
100644 blob e69de29bb2d1d6434b8b29ae775ad8c2e48c5391    c
100644 blob e69de29bb2d1d6434b8b29ae775ad8c2e48c5391    d
100644 blob 0bbfff72133899fe3aa250e2e53d7febf6975f7e    math.sh
100644 blob e69de29bb2d1d6434b8b29ae775ad8c2e48c5391    readme.txt

```








