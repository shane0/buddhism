---
tags:
  - mkdocs
  - todo 
---
# todo cli integration

- my workflow template deployments always include [todo cli](https://github.com/todotxt/todo.txt-cli)
- except I use aliases so it runs from inside any folder
- tasks are rendered on mkdocs
- tasks sometimes become a [project](projects.md)

## screencast

## layout

```sh
todocli/
├── done.txt
├── report.txt
├── todo.cfg
├── todo.sh
├── todo.txt
<projects>/ template or whatever
```

## todo.txt

```text
-8<- "todocli/todo.txt"
```

## done.txt

```text
-8<- "todocli/done.txt"
```

## alias

```sh
-8<- "utils/bash_aliases:27:38"
```

## usage
  
```text
  Usage: todo.sh [-fhpantvV] [-d todo_config] action [task_number] [task_description]

  Actions:
    add|a "THING I NEED TO DO +project @context"
    addm "THINGS I NEED TO DO
          MORE THINGS I NEED TO DO"
    addto DEST "TEXT TO ADD"
    append|app ITEM# "TEXT TO APPEND"
    archive
    command [ACTIONS]
    deduplicate
    del|rm ITEM# [TERM]
    depri|dp ITEM#[, ITEM#, ITEM#, ...]
    do ITEM#[, ITEM#, ITEM#, ...]
    help [ACTION...]
    list|ls [TERM...]
    listall|lsa [TERM...]
    listaddons
    listcon|lsc [TERM...]
    listfile|lf [SRC [TERM...]]
    listpri|lsp [PRIORITIES] [TERM...]
    listproj|lsprj [TERM...]
    move|mv ITEM# DEST [SRC]
    prepend|prep ITEM# "TEXT TO PREPEND"
    pri|p ITEM# PRIORITY
    replace ITEM# "UPDATED TODO"
    report
    shorthelp

  Actions can be added and overridden using scripts in the actions
  directory.

  See "help" for more details.
```
