# todocli app

todo cli was scaffolded using <https://gitlab.com/shane0/cookiecutter-todocli>

```sh
alias t='clear && ./todocli/todo.sh'
alias d='clear && t listpri a'
alias tedit='vim ./todocli/todo.txt'
alias tall='clear && find . -name "todo.txt" | xargs grep "+"'
alias tpri='clear && find . -name "todo.txt" | xargs grep "(A"'
alias tprib='clear && find . -name "todo.txt" | xargs grep "(B"'
alias tpric='clear && find . -name "todo.txt" | xargs grep "(C"'
alias thelp='clear && ./todocli/todo.sh shorthelp'
```

```sh
# bullet journaling aka bujo 
#set -o vi
alias ea='vim ~/.bash_aliases'
alias sa='source ~/.bashrc'
alias c='clear'
alias r='ranger'
alias rd="vim ./readme.md"
alias cl="vim ./changelog.md"
alias jf='mkdir "$(date +%F)" && cd "$(date +%F)"'
alias ft='vim ./future.md'
alias in='vim ./index.md'
alias fj='vim ./"$(date +%F)".md'
alias bj='cd ./bujo && fj || echo "there is no bujo folder"'
alias bujo='cd ./bujo && fj || mkdir bujo && cd ./bujo && vim ./"$(date +%F)".md'
```
