# Keeping in sync

##

```sh
git clone --bare math math.git

g clone math.git math.carol
g clone math.git math.bob
g clone math.git math.bill
```

```sh
cd math.bill
echo "Small change Bill" >> another_rename
gc -am "Small change bill" 
gp
```

```sh
cd math.carol
gr -v show origin         
...
    main pushes to main (local out of date

gp  
 ! [rejected]

gl 
...
Fast-forward
 another_rename | 1 +
 1 file changed, 1 insertion(+)
```

## Fetching files from a remote repository (git fetch)

```sh
math.bill on  main 
❯ echo "Tiny change bill" >> another_rename 
gc -am "Another tiny change of bill"
gp
```

```sh
math.carol on  main 
❯ g log --decorate --oneline --all
1f20693 (HEAD -> main, origin/main, origin/HEAD) Small change bill
1a760c4 (origin/new_feature) A small update to readme.
6c557e0 Starting a second new file
1d3cdf7 Adding a new file to a new branch
c71e0e8 Adding printf.
e611968 Adding two numbers.
311abc7 (origin/another_fix_branch) Renaming c and d.
181bd03 Removed a and b.
6fed1fa Adding readme.txt
0d4a213 (tag: four_files_galore) Adding four empty files.
a068bc2 Adding b variable.
1f6e344 This is the second commit.
2393699 This is the first commit.


math.carol on  main took 21s 
❯ git fetch 
git log --decorate --oneline --all
fd9044e (origin/main, origin/HEAD) Another tiny change of bill
1f20693 (HEAD -> main) Small change bill
1a760c4 (origin/new_feature) A small update to readme.
6c557e0 Starting a second new file
1d3cdf7 Adding a new file to a new branch
c71e0e8 Adding printf.
e611968 Adding two numbers.
311abc7 (origin/another_fix_branch) Renaming c and d.
181bd03 Removed a and b.
6fed1fa Adding readme.txt
0d4a213 (tag: four_files_galore) Adding four empty files.
a068bc2 Adding b variable.
1f6e344 This is the second commit.
2393699 This is the first commit.
```

# Merging two branches (git merge)

```sh
math.carol on  main [⇣] took 34s 
❯ g rev-parse FETCH_HEAD            
fd9044e21438dfe4c81cc335e50d3ad1b9796eed

math.carol on  main [⇣] 
❯ g rev-parse origin/main
fd9044e21438dfe4c81cc335e50d3ad1b9796eed

g diff HEAD..FETCH_HEAD
 
another_rename
 
───┐
1: │
───┘
│  1 ││  1 │Small change Bill
│    ││  2 │Tiny change bill


g merge FETCH_HEAD
```

## Clean merge

```sh
math.carol on  main 
❯ echo "Small change 2" >> another_rename
gc -am "Small change 2 form carol"
```

```sh
math.bill on  main 
❯ echo "Small change 2 Carol" >> another_rename
gc -am "Small change 2 bill" 
gp

gl                     
fatal: Not possible to fast-forward, aborting.

git merge origin/main
Merge made by the 'ort' strategy.
```

## Clean merge with automatic commit

```sh
g log -1
Merge: bd789de 78dad35
```

## Conflicted merges

```sh
math.carol on  main [⇡] took 4s 
❯ gp


math.bill on  main 
❯ gl
Fast-forward
```

```sh
math.bill on  main 
❯ echo "JKL MNO PQR" >> another_rename 
gc -am "JKL part of alphabet"
gp
```

```sh
math.carol on  main 
❯ echo "ABC DEF GHI" >> another_rename 
gc -am "ABC part of alphabet"
gl 
fatal: Not possible to fast-forward, aborting.

❯ gst
Your branch and 'origin/main' have diverged,

g merge origin/main
Auto-merging another_rename
CONFLICT (content): Merge conflict in another_rename

cat another_rename 
Small change Bill
Tiny change bill
Small change 2 Carol
<<<<<<< HEAD
ABC DEF GHI
||||||| b917359
=======
JKL MNO PQR
>>>>>>> origin/main

math.carol on  main (MERGING) [=⇕] 
❯ 

math.carol on  main (MERGING) [=⇕] 
❯ vim another_rename   

math.carol on  main (MERGING) [=⇕] took 8s 
❯ cat another_rename
Small change Bill
Tiny change bill
Small change 2 Carol
ABC DEF GHI
JKL MNO PQR

gc -am "Correct alphabet"

math.carol on  main [⇡] 
❯ gp

math.bill on  main 
❯ gl
```

## Restricting pulls to fast-forwards only

```sh
math.bill on  main 
❯ echo "ABC" >> another_rename  
gc -am "Alphabet (on bill)"
gp
```

```sh
math.carol on  main 
❯ echo "ABC" >> another_rename
gc -am "Alphabet (on caral)"
gl --ff-only
fatal: Not possible to fast-forward, aborting.

g merge origin/main     
Merge made by the 'ort' strategy.

gl
```














