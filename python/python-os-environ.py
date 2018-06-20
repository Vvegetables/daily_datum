#coding=utf-8
import os
'''
我们想要用python获得一些系统相关的各种信息的时候，就可以使用os的environ。
这里我们需要知道不同系统的差异，比如windows和linux之间的变量的区别。
'''
print os.environ.keys()
print '*' * 20
print os.environ.get('PATHEXT') #可执行文件
print os.environ.get('USERNAME') #用户名
print os.environ.get('PROMPT') #设置提示符
print os.environ.get('SYSTEMROOT') #系统主目录
print os.environ.get('LOGONSERVER') #机器名称
print os.environ.get('SECRET_KEY') or 'this is hard to guess'

#http://www.cnblogs.com/ccorz/p/osenviron-xiang-jie.html
# test = ''
# print (test | os.environ.get('USERNAME'))
