# _*_ coding:utf-8 _*_
from baseresource.greenresource import BaseResource
from lxml import etree
import random

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
            print("微信验证失败")
        return "非法访问"