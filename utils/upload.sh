#!/usr/bin/env bash
# echo "# buddhism" >> README.md
git init
git add . 
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:shane0/buddhism.git
git push -u origin main
