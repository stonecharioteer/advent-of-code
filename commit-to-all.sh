#!/bin/bash

git commit $1 -m "$2"
last_commit=`git log --format="%H" -n 1 | cat`

current_branch=`git rev-parse --abbrev-ref HEAD -- | head -n 1`

git checkout master
git cherry-pick $last_commit

git checkout dev
git cherry-pick $last_commit

git checkout python
git cherry-pick $last_commit

git checkout rust
git cherry-pick $last_commit

git checkout nodejs
git cherry-pick $last_commit


git checkout $current_branch

