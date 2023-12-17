#!/usr/bin/env bash
git pull
mike deploy 2024 latest --push
mike set-default latest 
mike list
# checkout first
# mike deploy 2023 latest --push
# checkout first
# mike deploy 2022 latest --push