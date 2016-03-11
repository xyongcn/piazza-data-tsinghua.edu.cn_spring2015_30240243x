#!/bin/bash

local_time=$(date '+%Y-%m-%d_%H:%M:%S')
tt=Update:
commit_message=${tt}${local_time}
cd /mnt/piazza_update/piazza-data-tsinghua.edu.cn_spring2015_30240243x
git pull -u origin master
git add .
git commit -m ${commit_message}
git push -u origin master

