# _*_ coding:utf-8 _*_
from __future__ import print_function
from Tkinter import *

def callback(event):
    print ("clicked ad ", event.x, event.y)
def key(event):
    print ("pressed ", repr(event.char))
import requests
def get_data(event):
    res = requests.get(url='http://blog.csdn.net/aa1049372051/article/details/51890105')
    print (res.content)
def stopevent(event):
    text.insert(INSERT, '\n' + "执行暂停")
    print("暂停中")

root = Tk()
root.title("数据管理软件")
stopbutton = Button(root,text="暂停",width=20)
huifubutton = Button(root,text="恢复运行",width=20)
clearbutton = Button(root,text="去掉重复",width=20)
exportbutton = Button(root,text="导出结果",width=20)
export_domain_button = Button(root,text="导出域名",width=20)
export_domain_head_button = Button(root,text="导出域名和标题",width=20)
export_link = Button(root,text="导出链接",width=20)
stopbutton.bind("<Button-1>", stopevent)
stopbutton.grid(row=0)
clearbutton.grid(row=1)
exportbutton.grid(row=2)
export_link.grid(row=3)
export_domain_button.grid(row=4)
export_domain_head_button.grid(row=5,padx=10)
text = Text(root)
text.grid(row=0,rowspan=6, column=1,padx=10)
text.insert(INSERT, 'test')
text.insert(INSERT, '\ntest')
root.mainloop()