#-*-coding:utf-8-*-
import sys

print "打印出该版本python支持的系统Modules"
#查看方式1
print sys.modules

#查看方式2
for module in sys.modules:
    print module


print "而在Python里面一个py文件就是一个模块"
print "关注如何获取一些信息，比如函数的使用说明，比如第三方的Module的说明"

