#!/usr/bin/env python 
#coding: utf-8
import time
import urllib,urllib2
import json
import sys
import time
import MySQLdb
import os.path
import string
import re

now = time.time()
wait = 30

# 发送钉钉消息
def sendDingDingMessage(url, data):
    req = urllib2.Request(url)
    req.add_header("Content-Type", "application/json; charset=utf-8")
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
    response = opener.open(req, json.dumps(data))
    return response.read()

def mo_time(host):
    try:
        f = open("/usr/lib/zabbix/alertscripts/app/"+host+"_"+touser+"_time.log")
        time_mo = float(f.read())
        time_diff = int(now - time_mo)
        f.close()
    except:
        time_diff = 30
    return time_diff


def get_info(mm):
		sql_item="SELECT id,from_unixtime(clock),clock from history_text where itemid in (25469,25470) and from_unixtime(clock)= %s limit 1"
		conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='tcbj',db='zabbix',port=3306,charset='utf8')
		cur=conn.cursor()
		cur.execute(sql_item,[mm])
		data = cur.fetchone()
		cur.close()
		conn.close()
#		url = "http://112.74.39.143:10065/app/kibana#/discover?_g="+str(data[0])+"?"+str(data[2])
		url = "http://wx-test1.by-health.com/jiankong/Default.aspx?id="+str(data[0])+"&clock="+str(data[2])
		return url 

if __name__ == '__main__':
    if len(sys.argv) == 4:
		touser,subject,content = sys.argv[1:]
		info = content.strip().split('\n')
		host = info[5].split(':')[1]
		nseverity = int(info[3].split(':')[1])
		trigger_time1=str(info[4].split(':')[1])+":"+str(info[4].split(':')[2])+":"+str(info[4].split(':')[3])
#		trigger_time1.replace(".","-")
		strinfo = re.compile('\.')
		trigger_time =  strinfo.sub('-',trigger_time1)
		f = open("/usr/lib/zabbix/alertscripts/app/"+host+"_"+touser+"_test","w")
		f.write(str(subject)+"\n"+str(trigger_time))
		f.close()
#		trigger_time = "2016-11-23 15:13:13"
		time_diff = mo_time(host)
		time_wait = wait - time_diff
		url = get_info(trigger_time)
		content1 = content.split('THE log content is:')[0]
		content_with_subject = str(subject+"\n\n"+content1+"\n\n日志链接如下:\n\n"+url)
#		content_with_subject = url
#		f = open("/usr/lib/zabbix/alertscripts/app/"+host+"_"+touser+"_data","w")
#		f.write(str(subject)+"\n"+str(trigger_time1))
#		f.close()

    else:
		print 'error segments, now exit'
		sys.exit()

    if nseverity >1 and time_diff >wait:
        posturl = "https://oapi.dingtalk.com/robot/send?access_token=479181ecee938dde9df46a0569c61a3524294c4a96254712eb2866081777b578"
        data = { "msgtype": "text", "text": { "content": content_with_subject } }
        result = sendDingDingMessage(posturl, data)

        f = open("/usr/lib/zabbix/alertscripts/app/"+host+"_"+touser+"_exception","w")
        f.write(str(result))
        f.close()

        f = open("/usr/lib/zabbix/alertscripts/app/"+host+"_"+touser+"_time.log","w")
        f.write(str(now))
        f.close()
    else:
        print "Sending too fast! Waiting for more than",time_wait,"seconds."
