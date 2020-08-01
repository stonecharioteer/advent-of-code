#!/bin/bash

git commit $1 -m "$2"
last_commit=`git log --format="%H" -n 1 | cat`

current_branch=`git rev-parse --abbrev-ref HEAD -- | head -n 1`

for branch in $(git for-each-ref --format='%(refname)' refs/heads/); do
	git checkout $branch
	git cherry-pick $last_commit
done

git checkout $current_branch

