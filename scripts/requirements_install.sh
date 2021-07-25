#/bin/bash


SOURCE=$1
# root project dir name
PROJECT_DIR=$(dirname $(cd $(dirname "${BASH_SOURCE[0]}") && pwd))
cd ${PROJECT_DIR}

# pipenv path
PIPENV='/usr/local/bin/pipenv'

# activate pipenv environment
PIPENV_PATH=`${PIPENV} --venv`
#echo ${PIPENV_PATH}/bin/pip

# install requirements.txt packages
echo "installing python package ..."
${PIPENV_PATH}/bin/pip install --upgrade pip
while read PKG
do
  if [ "${SOURCE}" = "pypi" ]; then
    ${PIPENV_PATH}/bin/pip install ${PKG} -i https://pypi.org/simple
  elif [ "${SOURCE}" = "aliyun" ]; then
    ${PIPENV_PATH}/bin/pip install ${PKG} -i https://mirrors.aliyun.com/pypi/simple
  else
    ${PIPENV_PATH}/bin/pip install ${PKG} -i https://pypi.org/simple
  fi
done  < ${PROJECT_DIR}/requirements.txt
