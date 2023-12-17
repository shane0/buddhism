# push.sh 'comment'
#!/usr/bin/env bash
# ./push.sh commit_message

function addcommitpush () {
  message=(\'"$@"\')
  current=$(git branch | grep "*" | cut -b 3-)
  # read -r -i "$current" -e branch
  remote=$(git remote -v | head -1 | cut -d ' ' -f 1 )
  echo push local branch "$current" to "$remote" y n ?
  read -r yn
  if [ "$yn" = y ]; then
    git pull
    # echo "$current" "$remote"
    git add -A 
    # git commit -a -m "$message"
    cz c
    git pull
    mike deploy 2024 latest --push
    mike set-default latest 
    mike list
    git push origin "$current"
  else
    echo "nope"
  fi
}

addcommitpush "$1"
# do not run this it will erase mike versioning
#  see workflow.md to deploy push gh-pages branch
# mkdocs gh-deploy
open https://github.com/shane0/buddhism/actions 