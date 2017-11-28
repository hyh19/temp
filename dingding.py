#!/usr/bin/env python 
#coding: utf-8
import time
import urllib,urllib2
import json
import sys
import time

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
        f = open("/usr/lib/zabbix/alertscripts/weixin/"+host+"_"+touser+"_time.log")
        time_mo = float(f.read())
        time_diff = int(now - time_mo)
        f.close()
    except:
        time_diff = 30
    return time_diff

if __name__ == '__main__':
    if len(sys.argv) == 4:
        touser,subject,content = sys.argv[1:]        
        info = content.strip().split('\n')
        host = info[5].split(':')[1]
        nseverity = int(info[3].split(':')[1])
        time_diff = mo_time(host)
        time_wait = wait - time_diff
        content_with_subject = str(subject+"\n\n"+content)

    else:
        print 'error segments, now exit'
        sys.exit()

    if nseverity >1 or time_diff >wait:
        posturl = "https://oapi.dingtalk.com/robot/send?access_token=479181ecee938dde9df46a0569c61a3524294c4a96254712eb2866081777b578"
        data = { "msgtype": "text", "text": { "content": content_with_subject } }
        result = sendDingDingMessage(posturl, data)
        
        f = open("/usr/lib/zabbix/alertscripts/weixin/"+host+"_"+touser+"_exception","w")
        f.write(str(result))
        f.close()

        f = open("/usr/lib/zabbix/alertscripts/weixin/"+host+"_"+touser+"_time.log","w")
        f.write(str(now))
        f.close()
    else:
        print "Sending too fast! Waiting for more than",time_wait,"seconds."
