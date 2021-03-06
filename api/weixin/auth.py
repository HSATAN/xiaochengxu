# _*_ coding:utf-8 _*_
from __future__ import print_function
from baseresource.greenresource import BaseResource
from lxml import etree
import random
import logging
from config.default import appId
from WXBizDataCrypt import WXBizDataCrypt
import json
import requests
from common.function import timestamp_to_date, get_day
from database.mysql import MysqlDB
import ujson


class AuthWeiXin(BaseResource):

    back_data = ["我是智能", "你好", "你是"]
    data_length = 0
    def __init__(self, back_data):
        BaseResource.__init__(self)
        self.back_data = back_data
        self.data_length = len(self.back_data)
    def real_POST(self, request):
        receiveData = request.content.read() #获取微信发送过来的body
        print(receiveData)
        data = etree.fromstring(receiveData)
        ToUserName = data.find('ToUserName').text
        FromUserName = data.find('FromUserName').text
        CreateTime = data.find('CreateTime').text
        Content = data.find('Content').text
        print(Content)
        Content = self.back_data[random.randint(0,self.data_length-1)]
        Content = Content.strip('\n')
        # print(receiveData)
        message = '<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType><![CDATA[text]]></MsgType><Content><![CDATA[%s]]></Content></xml>'%(FromUserName, ToUserName, CreateTime, Content)
        print(message)
        return message
    def real_GET(self, request):
        try:
            echostr = request.args.get('echostr')[0]
            return echostr
        except Exception as e:
            logging.info("访问错误")
            print("微信验证失败")
        return "非法访问"

class WXRunData(BaseResource):

    def real_POST(self, request):
        nickName = request.args.get('nickName')[0]
        rundata = request.args.get('rundata')[0]
        code = request.args.get('code')[0]
        avatarUrl = request.args.get('avatarUrl')[0]
        logging.info(avatarUrl)
        iv = request.args.get('iv')[0]
        logging.info('iv=%s' % iv)
        url = 'https://api.weixin.qq.com/sns/jscode2session?appid=%s&secret=ddf03c948cfe2610dd8d1ae125b212ea&' \
              'js_code=%s&grant_type=authorization_code' % (appId, code)
        res = requests.get(url)
        logging.info(res.content)
        content = json.loads(res.content)
        sessionKey = content['session_key']
        openid = content['openid']
        logging.info(sessionKey)
        pc = WXBizDataCrypt(appId, sessionKey)
        logging.info("rundata = %s" % rundata)
        data = pc.decrypt(rundata, iv)
        for item in data:
            timestamp = timestamp_to_date(item['timestamp'])
            step = item['step']
            logging.info("%s   %s " % (timestamp, step))
            run_day = get_day(item['timestamp'])
            logging.info("insert into rundata(openid,step,runday,nickname) value"
                " ('%s',%s,'%s','%s') on DUPLICATE key update step=%s  , avatarUrl='%s'" % (openid, step,run_day, nickName, step, avatarUrl))
            MysqlDB.insert(
                "insert into rundata(openid,step,runday,nickname) value"
                " ('%s',%s,'%s','%s') on DUPLICATE key update step=%s  , avatarUrl='%s'" % (openid, step,run_day, nickName, step, avatarUrl))

        logging.info("nickname = %s" % nickName)
        resp = {'openid': openid, 'code': 0}
        return  resp
    def real_GET(self, request):
        nickName = request.args.get('nickName')[0]
        rundata = request.args.get('rundata')[0]
        code = request.args.get('sessionKey')[0]

        iv = request.args.get('iv')[0]
        logging.info('iv=%s' % iv)
        url = 'https://api.weixin.qq.com/sns/jscode2session?appid=%s&secret=ddf03c948cfe2610dd8d1ae125b212ea&' \
              'js_code=%s&grant_type=authorization_code' % (appId, code)
        res = requests.get(url)
        content = json.loads(res.content)
        sessionKey = content['session_key']
        pc = WXBizDataCrypt(appId, sessionKey)
        data = pc.decrypt(rundata, iv)
        for item in data:
            timestamp = timestamp_to_date(item['timestamp'])
            step = item['step']
            logging.info("%s   %s " %(timestamp, step))
        logging.info("nickname %s" % nickName)
        logging.info(nickName)
        return "success"