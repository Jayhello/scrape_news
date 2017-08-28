#!/bin/bash
#restart scrape news process if the process exited accidentally

log_file="restart_sh.log"

# return the current date time
TIMESTAMP(){
    echo $(date "+%Y-%m-%d %H:%M:%S")
}

stop_process_if_running(){
	# $1->process_name to grep
	echo $(ps -ef | grep $1)
	be_running=$(ps -ef | grep $1 | wc -l)
	if [ $be_running -gt 0 ]
	then
		echo "$(TIMESTAMP) $1 is running, T'm going to kill it"
		ps -ef | grep "$1" | awk '{print $2}' | xargs kill -9
		if [ $? -eq 0 ];
		then
			echo "kill $1 successfully!!!"
		fi
	else
		echo "$(TIMESTAMP) $1 is not running"
	fi
}

restart_process_if_die(){
	# $1->process_name by grep, $2->python directory
	# $3->process python file name
	echo "paras is: $@"
	be_running=$(ps -ef | grep $1 | wc -l)
	if [ $be_running -eq 0 ];
	then
		echo "$(TIMESTAMP) $3 got down, now I will restart it" | tee -a $log_file
		cd $2
		echo "Now I am in $PWD"
		nohup python $3 & 2>&1
		if [ $? -eq 0 ];
		then
			echo "$(TIMESTAMP) $3 restart successfully" | tee -a $log_file
		fi
		cd -
	else
		echo "$(TIMESTAMP) $3 is running, no need to restart"
	fi
}

test_process="[p]ython.*nohup_restart_test_py"
file_dir=/home/xiongyu/search_start_sh/
py_file=nohup_restart_test_py.py
#when execute this shell script, if the process is running,kill it firstly
stop_process_if_running $test_process

# poll if the process is died, if got died then restart it.
while :
do
	restart_process_if_die $test_process $file_dir $py_file
	echo "$(TIMESTAMP) now I will sleep 10S"
	sleep 10
done