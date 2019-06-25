# Git

#### Basic usage
```bash
git init
git init --bare

git checkout {branch/commit}

git add {file}
git commit -m {comment}

git status # Check current file change status
```

#### Remote
```bash
git remote add {remote} {url}
git remote get-url {remote}
git remote set-url {remote} {new url}

git push {remote} {branch}
git pull {remote} {branch}
```

#### Branching
```bash
# Create branch
git branch {new branch}

# Create and checkout
git checkout -b {new branch}

# Remove branch 
git branch -d {branch}
```


#### Logging
```bash
# Basic log
git log 

# One-line log
git log --oneline

# Detailed log 
git log --name-only
git log --name-status
git log --stat

# Pretty 
git log --stat --pretty=short --graph

# Log file
git log -- {filename}   # Show file history
git log -p {filename}   # Show history with patch 
```

#### Select commit
```bash
# Head
HEAD

# Range of commit
{from commit}..{to commit}

# Select {count}-th last commit (if multiple branches merge into one)
HEAD^{count}

# Last {count} commit
HEAD~{count}      # HEAD^^^^ 
```

#### Resetting
```bash
git reset --soft  # Soft reset  : Keep index and changes, move HEAD position
git reset         # Mixed reset : Reset index but keep all changes (Unstage)
git reset --hard  # Hard reset  : Remove all changes

git reset --merge # Abort failed merge

git clean -df     # Remove all untracked files

git revert {commit} # Revert will create a new commit to reset the commit
```

#### Merge
```bash
git merge {branch}
git merge {branch1} {branch2} {branch3} # ...

git merge -s {ours/theirs} {branch} # Strategy to resolve conflicts, use mine or theirs

git merge --{continue | abort}
```

#### Cherrypick
Select several commits and apply to current branch
```bash
git cherry-pick {commit}
git cherry-pick {from commit}..{to commit}

# If sth happened blocking cherrypick progress
git cherry-pick --{coutinue | quit | abort}
```

#### Diff & Patch
```bash
# Diff file
git diff {commit 1} {commit 2}  # Diff commits

# Create patch
git format-patch {commit} -{n}  # Create patch since (commit - n)th patch
git format-patch {from commit}..{to commit}
git diff {commit 1} {commit 2} > {path}  # Another way to create patch 

# Apply patch
git apply --check {path of patch/diff}  # Dry run
git apply {path of patch/diff} 

# Resolve conflicts 
git add .
git am --{ resolved | continue | abort | skip}
```

#### Squash
Group multiple commits (discrete/small commits) into one big commit
```bash
# Merge squash
git merge --squash {branch}


# Rebase squash (Interactive Mode)
git rebase -i {commit}
## p : use commit
## s : squash commit into previous commit
```

#### Stash
Temporary store and hide unstaged modified files,  
```bash
# Stash all unstaged modified files
git stash 

# List stashed files
git stash list

# Apply latest stash
git stash pop

# Remove latest stash
git stash drop

# Clear all stash
git stash clear
```