#/bin/bash


# root project dir name
PROJECT_DIR=$(dirname $(cd $(dirname "${BASH_SOURCE[0]}") && pwd))
cd ${PROJECT_DIR}

# set pipenv environment install dir
#export WORKON_HOME=${PROJECT_DIR}  # install into project dir

# install pipenv environment
pipenv install --skip-lock --pypi-mirror https://pypi.org/simple
#pipenv install --skip-lock --pypi-mirror http://mirrors.aliyun.com/pypi/simple/



