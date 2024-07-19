#!/bin/bash
set -e

# https://github.com/romanr/rebase-script
# Rebase script version 1.0
# Usage:
# Rebase current branch:
# rebase
# Rebase specific branch:
# rebase [branch name]

branch=`git rev-parse --abbrev-ref HEAD`
echo "Current branch: $branch"

if [ -z "$1" ] && [ "$branch" == "main" ]
  then
    echo "Branch name parameter is missing."
    echo "Usage:"
    echo "$0 [branch name]"
    exit 1
fi

# rebase specified branch
if [ "$1" ] 
  then
branch=$1
fi

if ! [[ -z "$(git status --porcelain)" ]]; then
  echo "Working directory is not clean. Stash your changes first."
  exit 1
fi

echo "Preparing to rebase branch $branch on to main..."
git fetch
git checkout main
git pull
git show-branch $branch &>/dev/null && git checkout $branch || git checkout --track origin/$branch

# Check if the branch has an upstream set, if not, set it
if ! git rev-parse --abbrev-ref --symbolic-full-name @{u} &>/dev/null; then
  echo "Setting upstream for branch $branch to origin/$branch"
  git branch --set-upstream-to=origin/$branch $branch
fi
git pull

echo 
echo "🔝 Rebase..."
git rebase main
git push --force-with-lease