#!/bin/bash
#set -x
elastic_pid=`ps -ef | grep elast | grep java | awk '{print $2}'`
elastic_headpid=` ps -ef | grep [g]runt | awk '{print $2}'`
kibana_pid=`ps -ef | grep [k]ibana/bin | awk '{print $2}'`
logstash_pid=`ps -ef | grep logstash | grep java | awk '{print $2}'`
filebeat_pid=`ps -ef | grep [.]/filebeat | awk '{print $2}' | tr '\n' ' '`

efk_start(){
case $2 in
  elastic)
    [ -n "$elastic_pid" ] && echo "进程存在" && exit || echo "开始进程" && cd /usr/local/efk/alone/ && su lin && /usr/local/efk/alone/es/bin/elasticsearch -d &>>/var/log/elasticsearch/elasticsearch.log &;;
  elastic_head)
    [ -n "$elastic_headpid" ] && echo "进程存在" && exit || echo "开始进程" && cd /usr/local/efk/alone/plugin/es/elasticsearch-head/ && nohup ./node_modules/grunt/bin/grunt server &>>/var/log/elasticsearch/elasticsearch.log &;;
  kibana)
    [ -n "$kibana_pid" ] && echo "进程存在" && exit || echo "开始进程" && cd /usr/local/efk/alone/ && nohup /usr/local/efk/alone/kibana/bin/kibana  &>>/var/log/kibana/kibana.log &;;
  logstash)
    [ -n "$logstash_pid" ] && echo "进程已存在" && exit || echo "开始进程" && cd /usr/local/efk/alone/logstash/conf.d/ && nohup /usr/local/efk/alone/logstash/bin/logstash -f $3 --config.reload.automatic &>>/var/log/logstash/logstash.log &;;
  filebeat)
    cd /usr/local/efk/alone/filebeat/
    rm -f data/registry
    nohup ./filebeat -e -c filebeat.d/$3 -d "publish" &>> /var/log/filebeat/filebeat &;;
  *)
    echo "实例名称为elastic/elastic_head/kibana/logstash/filebeat";;  
esac
}
#这里的参数是由主函数传递过来的，主函数传递过来几个，位置参数会重新排列
efk_stop(){
case $1 in
  elastic)
    pid=${elastic_pid};;
  elastic_head)
    pid=${elastic_headpid};;
  kibana)
    pid=${kibana_pid};;
  logstash)
    pid=${logstash_pid};;
  filebeat)
    pid=${filebeat_pid};;
  *)
    echo "实例名称为elastic/elastic_head/kibana/logstash/filebeat";;
esac
kill $pid || echo "该实例pid为$pid,未启动"
}

efk_status(){
echo "进程pid:" && echo "    elastic:${elastic_pid:=-1} head:${elastic_headpid:=-1} kibana${kibana_pid:=-1} logstash:${logstash_pid:=-1} filebeat:${filebeat_pid:=-1}" 
echo "logstash配置文件:" && echo -n "    " && ls /usr/local/efk/alone/logstash/conf.d/ 
echo "filebeat配置文件:" && echo -n "    " && ls /usr/local/efk/alone/filebeat/filebeat.d/
}
#这里是主函数，有最多三个参数
case $1 in
  start)
    [ $# == 3 ] && efk_start $1 $2 $3 && exit || echo "参数不够" && /usr/bin/echo '第一个参数是启动/停止。第二个参数是实例，第三个参数是配置文件';;
  stop)
    efk_stop $2;;
  status)
    efk_status;;
  *)
    /usr/bin/echo '第一个参数是启动/停止。第二个参数是实例，第三个参数是配置文件';;
esac	
