#!/bin/bash

message=$1

cd /var/www/zyni/answer

git add . 
git commit -m ${message}
git push origin master

