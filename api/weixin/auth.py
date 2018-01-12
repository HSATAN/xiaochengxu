# _*_ coding:utf-8 _*_
from __future__ import print_function
from baseresource.greenresource import BaseResource
from lxml import etree
import random
import logging
from config.default import appId
from WXBizDataCrypt import WXBizDataCrypt


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

class WXRunData(BaseResource):

    def real_POST(self, request):
        nickName = request.args.get('nickName')[0]
        rundata = request.args.get('rundata')[0]
        sessionKey = request.args.get('sessionKey')[0]
        iv = request.args.get('iv')[0]
        pc = WXBizDataCrypt(appId, sessionKey)
        print(pc.decrypt(rundata, iv))
        print("rundata = %s" % rundata)
        logging.info("nickname %s" % nickName)
        print(nickName)
        return "success"
    def real_GET(self, request):
        nickName = request.args.get('nickName')[0]
        rundata = request.args.get('rundata')[0]
        sessionKey = request.args.get('sessionKey')[0]
        print(sessionKey)
        iv = request.args.get('iv')[0]
        print('iv=%s' % iv)
        import requests

        url = 'https://api.weixin.qq.com/sns/oauth2/access_token?appid=%s&secret=ddf03c948cfe2610dd8d1ae125b212ea&' \
              'code=%s&grant_type=authorization_code' % (appId, sessionKey)
        res = requests.get(url)
        print(res.content)
        pc = WXBizDataCrypt(appId, sessionKey)
        print("rundata = %s" % rundata)
        print(pc.decrypt(rundata, iv))
        logging.info("nickname %s" % nickName)
        print(nickName)
        return "success"

def main():
    appId = 'wx4f4bc4dec97d474b'
    sessionKey = 'tiihtNczf5v6AKRyjwEUhQ=='
    encryptedData = 'CiyLU1Aw2KjvrjMdj8YKliAjtP4gsMZMQmRzooG2xrDcvSnxIMXFufNstNGTyaGS9uT5geRa0W4oTOb1WT7fJlAC+oNPdbB+3hVbJSRgv+4lGOETKUQz6OYStslQ142dNCuabNPGBzlooOmB231qMM85d2/fV6ChevvXvQP8Hkue1poOFtnEtpyxVLW1zAo6/1Xx1COxFvrc2d7UL/lmHInNlxuacJXwu0fjpXfz/YqYzBIBzD6WUfTIF9GRHpOn/Hz7saL8xz+W//FRAUid1OksQaQx4CMs8LOddcQhULW4ucetDf96JcR3g0gfRK4PC7E/r7Z6xNrXd2UIeorGj5Ef7b1pJAYB6Y5anaHqZ9J6nKEBvB4DnNLIVWSgARns/8wR2SiRS7MNACwTyrGvt9ts8p12PKFdlqYTopNHR1Vf7XjfhQlVsAJdNiKdYmYVoKlaRv85IfVunYzO0IKXsyl7JCUjCpoG20f0a04COwfneQAGGwd5oa+T8yO5hzuyDb/XcxxmK01EpqOyuxINew=='
    iv = 'r7BXXKkLb8qrSNn05n0qiA=='

    pc = WXBizDataCrypt(appId, sessionKey)

    print(pc.decrypt(encryptedData, iv))

main()