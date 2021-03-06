# _*_ coding:utf-8 _*_

from __future__ import print_function
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from twisted.internet import reactor
from twisted.web.resource import Resource
from twisted.web.server import Site
import json
import logging
import re
from api.weixin.userinfo import UserInfo
from api.weixin.auth import AuthWeiXin, WXRunData
from api.weixin.rankdata import RankData

back_data = "你好"

print("-----------服务器启动")

class Root(Resource):

    def __init__(self):
        Resource.__init__(self)

        self.putChild("", AuthWeiXin(back_data))
        self.putChild("rundata",WXRunData())
        self.putChild("userinfo", UserInfo())
        self.putChild("rankdata", RankData())



if __name__ == '__main__':
    logfile = 'log'
    try:
        import platform
        if 'linux' in platform.system().lower():

            logfile = '/home/log/xiaochengxu/log'
    except:
        pass
    formats = '[%(asctime)s] [%(filename)s L%(lineno)d] [%(levelname)s] %(message)s'
    logging.basicConfig(level=logging.INFO, format=formats, filename=logfile)
    reactor.listenTCP(9999, Site(Root()))
    reactor.run()