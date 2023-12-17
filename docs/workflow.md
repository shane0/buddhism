---
tags:
  - workflow 
---
# workflow

- these are my notes on maintaining this site
- this site uses mkdocs + mike + commitizen

## updating versioned docs

- check branch 2024 (latest) 2023 2022
- example deploy updates to 2024

```sh
git checkout 2024
mike serve
# update markdown files
mike deploy --push 2024
# deploy online
mkdocs gh-deploy
git add .
cz c
```

## 2023-12-17 added versioned docs

- added versioned docs for: 2024 2023 2022
- examples: <https://github.com/squidfunk/mkdocs-material-example-versioning>

### adding new versions

- create a new branch for example 2022
- push to the remote
- in this case I created `.placeholder`
- then run `git add . && cz c && git push origin 2022`
- no need to merge the branch and do not delete it
- you will checkout this branch to update it later
