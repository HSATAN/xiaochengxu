# _*_ coding:utf-8 _*_
import base64
import json
from Crypto.Cipher import AES
import re
import logging
class WXBizDataCrypt:
    def __init__(self, appId, sessionKey):
        self.appId = appId
        self.sessionKey = sessionKey

    def decrypt(self, encryptedData, iv):
        # base64 decode
        sessionKey = base64.b64decode(self.sessionKey)
        encryptedData = base64.b64decode(encryptedData)
        iv = base64.b64decode(iv)

        cipher = AES.new(sessionKey, AES.MODE_CBC, iv)
        data = cipher.decrypt(encryptedData)
        # logging.info(data)
        data = '{"rundata":[{' + re.findall('"timestamp.+', data)[0]
        data = re.findall('\[.+\]', data)[0]
        print data
        return json.loads(data)

        # if decrypted['watermark']['appid'] != self.appId:
        #     raise Exception('Invalid Buffer')
        #
        # return decrypted

    def _unpad(self, s):
        return s[:-ord(s[len(s)-1:])]
