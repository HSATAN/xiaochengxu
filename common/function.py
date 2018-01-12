# _*_ coding:utf-8 _*_

def timestamp_to_date(timestamp):
    import time
    localtime = time.localtime(timestamp)
    date = time.strftime("%Y-%m-%d %H:%M:%S", localtime)
    return date