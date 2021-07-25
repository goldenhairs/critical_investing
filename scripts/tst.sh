#!/bin/bash

XX=$1
TO_EXECUTE_FILENAME=$(echo $(basename ${XX}) | cut -d . -f1)   # 要执行的脚本名
echo $TO_EXECUTE_FILENAME
# root project dir name
PROJECT_DIR=$(dirname $(cd $(dirname "${BASH_SOURCE[0]}") && pwd))
cd ${PROJECT_DIR}
#export PYTHONPATH=${PROJECT_DIR}
PROJECT_DIR1=`python -c "from settings import files;from os.path import basename;print(basename(files.LOGS_ERRORS))"`
PROJECT_DIR1=`python -c "from settings import files;print(files.LOGS_ERRORS)"`
echo $PROJECT_DIR1
XX=$(basename "${PROJECT_DIR1}")
echo ${XX}
