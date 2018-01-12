# _*_ coding:utf-8 _*_

import requests
appId = "wxe02491f98cc727ad"
sessionKey = "0818gUwY0Nou822fbiuY0maKwY08gUwh"
url = 'https://api.weixin.qq.com/sns/oauth2/access_token?appid=%s&secret=ddf03c948cfe2610dd8d1ae125b212ea&' \
      'code=%s&grant_type=authorization_code' % (appId, sessionKey)
res = requests.get(url)
print res.content