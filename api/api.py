# _*_ coding:utf-8 _*_

from account.login import Login
from baseresource.greenresource import BaseResource
from weixin.auth import AuthWeiXin
class Api(BaseResource):

    def __init__(self):
        BaseResource.__init__(self)
        self.putChild("login", Login())


    pass


