#!/usr/bin/env bash
git pull
mike deploy 2024 latest --push
mike set-default latest 
mike list
# to publish on gh pages
# git checkout gh-pages
# git pull
# make sure you have 2023/ etc. mike folders
# add commit push
# pipeline publishes
# mike serve
# checkout first
# mike deploy 2023 --push
# checkout first
# mike deploy 2022 --push