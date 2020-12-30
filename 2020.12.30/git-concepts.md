# git

Version Control System.
Content-addressed file system.
Directed Acyclic Graph of "commits".

## Glossary

### remote

References a url which has a git daemon running or a directory with a git repo.
Created with `git remote add $name $url`. Listed with `git remote -v`.

### branch

A named pointer to a commit. Created with `git switch -c $new_branch_name`.

### merge
branch atual = função_nova
git pull origin master
git fetch origin
git merge master

A commit that joins two or more divergent histories.
https://marc.info/?l=linux-kernel&m=139033182525831

### fast-forward

One of several strategies for "merging" branches.
A fast-forward means that the "current branch" pointer only moved ahead.
It usually happens when someone receives new commits from a remote on a branch
in which no new local commits were created.

### Working tree

The files and folders currently checked-out (i.e., on the file system).

### checkout

The `git checkout` brings stuff to the working tree.

### index

Also known as staging area. Files are added here via `git add $path`.
Files here are going to be "saved" with the next `git commit`.

### diff

Show lines that have been removed and added from a "tree" (file, folder,
branch, etc.).
Used to compare two versions of the same thing.
Running `git diff` with no arguments shows what has changed in the
"working tree" in comparison to the "index" or the last commit if the index is
empty.
`git diff $branch_name` compares $branch_name to the currently checked out
branch.

### HEAD pointer

HEAD is a pointer to the currently checked out commit.

### "detached HEAD state"

When you checkout a commit that is not referenced by any branch or tag, it is
said that the HEAD is detached.

### rebase

`git rebase --help` has a neat little diagram.

## Useful things

### Visualize the commit graph

`git log --oneline --graph --all` is a standard way of seeing the graph.
`code --install-extension mhutchie.git-graph` enables you to see the graph
directly on VS code.
Seeing the graph allows you to know where you are.

### Undoing a commit

`git reset HEAD~1` keeps the changes of the undone commit in the working tree.
While `git reset --hard HEAD~1` discards them.
The `~1` represents how many commits "back in time" you're going.
