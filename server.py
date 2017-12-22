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

from api.weixin.auth import AuthWeiXin

back_data = "你好"
with open('honglou.txt') as f:
    data = f.read()
    data = data.split('　　')
    back_data = list(set(data))
    back_data.remove('')
print("-----------服务器启动")

class Root(Resource):

    def __init__(self):
        Resource.__init__(self)

        self.putChild("", AuthWeiXin(back_data))


if __name__ == '__main__':
    logfile = 'log'
    try:
        import platform
        if 'linux' in platform.system().lower():

            logfile = '/home/log/twistserverlog/log'
    except:
        pass
    formats = '[%(asctime)s] [%(filename)s L%(lineno)d] [%(levelname)s] %(message)s'
    logging.basicConfig(level=logging.INFO, format=formats, filename=logfile)
    reactor.listenTCP(8888, Site(Root()))
    reactor.run()