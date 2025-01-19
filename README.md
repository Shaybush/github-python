# Git Basics Cheat Sheet + Python

## Initial Setup

### How to run python file

```bash
python {file_name}.py
```

### Configure Git

```bash
# Set your name
$ git config --global user.name "Your Name"

# Set your email
$ git config --global user.email "your.email@example.com"

# Check configuration
$ git config --list
```

---

## Creating and Cloning Repositories

```bash
# Initialize a new repository
$ git init

# Clone an existing repository
$ git clone <repository_url>
```

---

## Staging and Committing Changes

```bash
# Check the status of your repository
$ git status

# Add a file to the staging area
$ git add <file>

# Add all files to the staging area
$ git add .

# Commit changes with a message
$ git commit -m "Commit message"

# View commit history
$ git log
```

---

## Branching and Merging

```bash
# Create a new branch
$ git branch <branch_name>

# Switch to a branch
$ git checkout <branch_name>

# Create and switch to a new branch
$ git checkout -b <branch_name>

# Merge a branch into the current branch
$ git merge <branch_name>

# Delete a branch locally
$ git branch -d <branch_name>
```

---

## Stashing Changes

```bash
# Save changes without committing
$ git stash

# View stashed changes
$ git stash list

# Apply the latest stashed changes
$ git stash apply

# Apply and remove the latest stashed changes
$ git stash pop

# Drop a specific stash
$ git stash drop <stash_id>
```

---

## Rebasing

```bash
# Rebase the current branch onto another branch
$ git rebase <branch_name>

# Interactive rebase to edit commits
$ git rebase -i <commit_hash>

# Abort an ongoing rebase
$ git rebase --abort

# Continue rebase after resolving conflicts
$ git rebase --continue
```

---

## Viewing Changes

```bash
# Show changes in the working directory
$ git diff

# Show changes between the working directory and staging area
$ git diff --staged

# Show changes for a specific file
$ git diff <file>
```

---

## Undoing Changes

```bash
# Unstage a file
$ git reset <file>

# Undo the last commit (keep changes in working directory)
$ git reset --soft HEAD~1

# Undo the last commit (discard changes)
$ git reset --hard HEAD~1

# Revert a commit by creating a new commit
$ git revert <commit_hash>
```

---

## Working with Remotes

```bash
# Add a remote repository
$ git remote add origin <repository_url>

# List remotes
$ git remote -v

# Fetch changes from the remote
$ git fetch

# Pull changes from the remote and merge
$ git pull origin <branch_name>

# Push changes to the remote
$ git push origin <branch_name>
```

---

## Tagging

```bash
# Create a lightweight tag
$ git tag <tag_name>

# Create an annotated tag
$ git tag -a <tag_name> -m "Tag message"

# Push a tag to the remote
$ git push origin <tag_name>

# List tags
$ git tag
```

---

## Useful Shortcuts

```bash
# Check the short summary of repository status
$ git status -s

# Show a one-line log
$ git log --oneline

# Show a graphical representation of branches
$ git log --oneline --graph --all
```

---

## Resolving Conflicts

```bash
# Show conflicts in files
$ git diff

# After resolving conflicts, add the files and continue
$ git add <file>
$ git rebase --continue  # If in a rebase
$ git merge --continue  # If in a merge
```

---

This cheat sheet summarizes the basic and commonly used Git commands to help you navigate through version control tasks efficiently.
