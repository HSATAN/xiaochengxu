# _*_ coding:utf-8 _*_

import time
timestamp = 1513094400
localtime = time.localtime(timestamp)
date = time.strftime("%Y-%m-%d %H:%M:%S", localtime)
print(date)

import re

data = '[I,[{"timestamp":1513094400,"step":0},{"timestamp":1513180800,"step":0},{"timestamp":1513267200,"step":0},{"timestamp":1513353600,"step":0},{"timestamp":1513440000,"step":0},{"timestamp":1513526400,"step":0},{"timestamp":1513612800,"step":0},{"timestamp":1513699200,"step":0},{"timestamp":1513785600,"step":0},{"timestamp":1513872000,"step":10762},{"timestamp":1513958400,"step":9321},{"timestamp":1514044800,"step":7257},{"timestamp":1514131200,"step":0},{"timestamp":1514217600,"step":0},{"timestamp":1514304000,"step":0},{"timestamp":1514390400,"step":0},{"timestamp":1514476800,"step":0},{"timestamp":1514563200,"step":0},{"timestamp":1514649600,"step":0},{"timestamp":1514736000,"step":0},{"timestamp":1514822400,"step":0},{"timestamp":1514908800,"step":0},{"timestamp":1514995200,"step":0},{"timestamp":1515081600,"step":0},{"timestamp":1515168000,"step":0},{"timestamp":1515254400,"step":0},{"timestamp":1515340800,"step":0},{"timestamp":1515427200,"step":0},{"timestamp":1515513600,"step":0},{"timestamp":1515600000,"step":6898},{"timestamp":1515686400,"step":941}],"watermark":{"timestamp":1515736018,"appid":"wxe02491f98cc727ad"}}'

data = '{"rundata":[{' + re.findall('"timestamp.+', data)[0]
print data
import json
print json.loads(data)['rundata']