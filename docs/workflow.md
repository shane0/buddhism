---
tags:
  - workflow 
---
# workflow

- these are my notes on maintaining this site
- this site uses mkdocs + mike + commitizen

## updating versioned docs

- checkout branch 2022
- update docs/ markdown pages
- view your changes locally

```sh
git checkout 2022
mike deploy 2022
mike serve
```

- deploy

```sh
mike deploy 2022 --push
./push.sh
```
