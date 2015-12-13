#-*-coding:utf-8-*-
import functools
print "偏函数的学习"
print "偏函数的作用就是，把一个函数的某些参数(默认参数)给固定住，返回一个新的函数，以致调用这个函数更简单"

#Eg:
y = int("12345") #默认是十进制 意味着传入的字符串是二进制
print y
print int("100", 2)#使用二进制 意味着传入的字符串的内容是二进制

#如果我们想传入大量的二进制字符串的话，需要每次都指定字符串是2进制的，好麻烦
#第一我们可以写一个函数
def int2(x, base = 2):
	int(x, base)
#第二我们可以使用仿函数
int2 = functools.partial(int, base = 2)

#实际上固定了int()函数的关键字参数base,也就是
int2("100")
#等价于
kw = {"base": 2}
int("100", **kw)

#当传入
max2 = functools.partial(max, 10)
#实际上会把10作为*args的一部分自动加到左边，也就是
max2(5, 6, 7)
#相当于
args = (10, 5, 6, 7)
print max(*args)
max2(5,6,7,10)