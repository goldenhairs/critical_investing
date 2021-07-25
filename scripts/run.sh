#/bin/bash


PYTHON_SCRIPTS=$1
# root project dir name
PROJECT_DIR=$(dirname $(cd $(dirname "${BASH_SOURCE[0]}") && pwd))
cd ${PROJECT_DIR}


# pipenv path
PIPENV='/usr/local/bin/pipenv'

${PIPENV} run python ${PROJECT_DIR}/${PYTHON_SCRIPTS}



