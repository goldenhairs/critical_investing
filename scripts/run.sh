#!/bin/sh


TO_EXECUTE_FILENAME=$(echo $(basename $1) | cut -d . -f1)   # 要执行的脚本名

# root project dir name
PROJECT_DIR=$(dirname $(cd $(dirname "${BASH_SOURCE[0]}") && pwd))
cd ${PROJECT_DIR}
# pipenv path
PIPENV='/usr/local/bin/pipenv'

# export environments
export PYTHONIOENCODING=utf-8
export LANG=zh_CN.UTF-8
export PYTHONPATH=${PROJECT_DIR}
export LC_CTYPE=zh_CN.UTF-8


ABSFILE=${BASH_SOURCE[0]}   # 当前执行脚本的绝对路径
PWDIR=$(dirname $ABSFILE)   # 当前执行脚本所在的绝对路径
FULL_FILENAME=$(basename $ABSFILE)   # 当前脚本的全名
FILENAME=$(echo $FULL_FILENAME | cut -d . -f1)     # 当前脚本的名
SUFFIX=$(echo $FULL_FILENAME | cut -d . -f2)    # 当前脚本的后缀
#echo $FILENAME, $PWDIR

# log dirs
LOGS_DIR="$PROJECT_DIR/datasets/logs"
LOG_NORMS_DIR="$LOGS_DIR/norms"
LOG_ERRORS_DIR="$LOGS_DIR/errors"
# if log dirs not exists, then auto create ...
if [ ! -d $LOG_NORMS_DIR ] & [ ! -d $LOGS_ERRORS_DIR ]; then
    mkdir -p $LOGS_ERRORS_DIR $LOG_NORMS_DIR
fi



DATETIME=`date +%Y-%m-%d:%H:%M:%S`
DATE=`date +%Y-%m-%d`


##################################################
#                                         Functions
##################################################
# 将秒转换为时分秒
swap_seconds () {
        SEC=$1
        FILENAME="${TO_EXECUTE_FILENAME}.py"
        (( SEC < 60 )) && echo "[01;34m Execute ${FILENAME} elapsed time: ${SEC} seconds[0m"

        (( SEC >= 60 && SEC < 3600 )) && echo "[01;34m Execute ${FILENAME} elapsed time: $(( SEC / 60 )) min $(( SEC % 60 )) sec[0m"

        (( SEC > 3600 )) && echo "[01;34m Execute ${FILENAME} elapsed time: $(( SEC / 3600 )) hr $(( (SEC % 3600) / 60 )) min $(( (SEC % 3600) % 60 )) sec[0m"
}

##########################################################
#          Tasks     末尾加上&，让命令在后台运行，不阻塞当前任务
##########################################################
start=$(date +%s)

echo "开始执行${TO_EXECUTE_FILENAME}.py ..."
echo "###################"$DATETIME"###################" >> ${LOG_NORMS_DIR}/${TO_EXECUTE_FILENAME}.${DATE}.log
echo "###################"$DATETIME"###################" > ${LOG_ERRORS_DIR}/${TO_EXECUTE_FILENAME}.${DATE}.log
${PIPENV} run python ${PROJECT_DIR}/$1 >> ${LOG_NORMS_DIR}/${TO_EXECUTE_FILENAME}.${DATE}.log 2>>${LOG_ERRORS_DIR}/${TO_EXECUTE_FILENAME}.${DATE}.log &#2>&1

wait   # 和&配合使用，等待前面的命令执行完成，再执行后面的命令

while read str; do
    echo $str     # 读取错误日志到终端显示
done <${LOG_ERRORS_DIR}/${TO_EXECUTE_FILENAME}.${DATE}.log

end=$(date +%s)
swap_seconds $(( end - start ))

#清除前几天的日志数据。
find ${LOG_ERRORS_DIR} -mtime +1 -name "*.log" -exec rm -rf {} \;
find ${LOG_NORMS_DIR} -mtime +1 -name "*.log" -exec rm -rf {} \;
