---
tags:
  - workflow 
---
# workflow

- these are my notes on maintaining this site
- this site uses mkdocs + mike + commitizen
- checkout a branch and deploy changes using this script

```sh
./push.sh
# for manual one offs
# ./utils/mike.sh
```

## adding new versions

- create a new branch `2025`
- `touch .placeholder`
- `mike deploy 2025 latest --push`
- `mike set-defaul 2025`
- to have a file to push to the remote
- run `git add . && cz c && git push origin 2022`
- no need to merge the branch but you could
- do not delete it
- you will checkout this branch to update it later

## 2023-12-17 added versioned docs

- added versioned docs for: 2024 2023 2022
- examples: <https://github.com/squidfunk/mkdocs-material-example-versioning>
