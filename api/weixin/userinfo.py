# _*_ coding:utf-8 _*_

from __future__ import print_function
from baseresource.greenresource import BaseResource
from lxml import etree
import random
import logging
from config.default import appId
from WXBizDataCrypt import WXBizDataCrypt
import json
from config.default import RUN_TABLE
import requests
from common.function import timestamp_to_date, get_day
from database.mysql import MysqlDB
import ujson, time

class UserInfo(BaseResource):

    def real_POST(self, request):
        openid = request.args.get('openid')[0]
        day = get_day(time.time())
        data = MysqlDB.run_query("select * from  %s where openid='%s' and runday=%s" % (RUN_TABLE, openid))

        return data[0]
