#!/bin/bash
#restart scrape news process if the process exited accidentally

log_file="restart_scrape.log"
TIMESTAMP=`date "+%Y-%m-%d %H:%M:%S"`

scrape_dir="/home/xiongyu/scrape_yy/scrape_yy"
#scrape_dir="/home/xiongyu/search_start_sh/"
scrape_py_file="scrape_yy_news_main.py"
#scrape_py_file="nohup_restart_test_py.py"
scrape_py_process="[p]ython.*$scrape_py_file"

search_dir="/home/xiongyu/scrape_search_yy/scrape_search_yy"
search_py_file="check_yy_news_warn.py"
search_py_process="[p]ython.*$search_py_file"

#when execute this shell script, if the process is running, kill it firstly
scrape_process_run=$(ps -ef|grep $scrape_py_process | wc -l)

echo $(ps -ef|grep $scrape_py_process)

if [ $scrape_process_run -gt 0 ];
then
	echo "$TIMESTAMP scrape_yy_news_main is running, I'm going to kill it"
	kill -9 $(ps -ef|grep "[p]ython.*$scrape_py_file" | awk '{print $2}')
	if [ $? -eq 0 ];
	then
		echo "kill $scrape_py_file successfully!!!!"
	fi
fi

search_process_run=$(ps -ef|grep $search_py_process)

if [ $search_process_run -gt 0 ];
then
	echo "$TIMESTAMP $search_py_file is running, I'm going to kill it"
	kill -9 $(ps -ef|grep "[p]ython.*$search_py_file" | awk '{print $2}')
	if [ $? -eq 0 ];
	then
		echo "kill $search_py_file successfully!!!!"
	fi
fi


while :
do
	if [ $(ps -ef | grep $scrape_py_process | wc -l) -eq 0 ];
	then
		echo "$TIMESTAMP $scrape_py_file got down, now I will restart it" | tee -a $log_file 
		#echo $PWD
		cd $scrape_dir
		echo "Now I am in $PWD"
		nohup python $scrape_py_file & 2>&1
        if [ $? -eq 0 ];
		then
			echo "$TIMESTAMP $(ps -ef | grep $scrape_py_process) restart scussfully!!!!" | tee -a $log_file
        fi
		cd -
	else
		echo "$scrape_py_process is running no need to restart"
	fi
    

	if [ $(ps -ef | grep $search_py_process | wc -l) -eq 0 ];
	then
		echo "$TIMESTAMP $search_py_file got down, now I will restart it" | tee -a $log_file 
		#echo $PWD
		cd $search_dir
		echo "Now I am in $PWD"
		nohup python $search_py_file & 2>&1
        if [ $? -eq 0 ];
		then
			echo "$TIMESTAMP $(ps -ef | grep $search_py_process) restart scussfully!!!!" | tee -a $log_file
        fi
		cd -
	else
		echo "$search_py_process is running no need to restart"
	fi

	echo "$TIMESTAMP I will sleep 30s"
	sleep 30
done
