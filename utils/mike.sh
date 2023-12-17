#!/usr/bin/env bash
git pull
git checkout 2022
mike deploy 2022 --push
mike list
# checkout first
# mike deploy 2024 latest --push
# checkout first
# mike deploy 2022 --push