---
tags:
  - workflow 
---
# workflow

- these are my notes on maintaining this site
- this site uses mkdocs + mike + commitizen
- I am using the main branch named 2024 alias latest
- or checkout other versions to update previous years
- each has their own workflow page
- deploy changes to 2024 using this script:

```sh
./push.sh
# for manual one offs
# ./utils/mike.sh
```

- to preview changes use the local mike server
- <http://localhost:8000>

```sh
mike list
mike deploy 2024 latest
# optional add push
mike deploy 2024 latest --push
mike serve
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
