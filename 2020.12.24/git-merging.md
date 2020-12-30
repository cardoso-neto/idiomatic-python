`git pull origin master`
i.e.,: `git fetch ; git merge origin/master`
Merging changes you made when someone else renamed/moved the files you were
working on.

If you made minor changes to the files, the easiest way to merge will be by
applying those minor changes to the new files.
Step by step:
- Locate the files
- diff them to highlight your changes
    - CLI: `git diff $their_file $your_file`
    - VSCode: right click on their file > Select for Compare, right click on
    yours > Compare with Selected.
- find your changes and copypaste them (editing whenever necessary) to their
file
- aftwerwards, you should remove your files and git add the modifications you
made on theirs.
- git commit and the merge is done.
