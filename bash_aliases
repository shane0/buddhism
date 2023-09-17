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
