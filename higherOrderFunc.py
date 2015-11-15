#-*-coding:utf-8-*-

print "函数本身也是变量，可以传给另外一个函数，那么接受函数作为参数的函数称为高阶函数"

'''
def f(a):
    return 2*a #2a is synax error
'''

def add(a, b, f):
    return f(a) + f(b)

#函数f在这里定义也是可以的
def f(a):
    return 2*a #2a is synax error

print add(8, -8, f)
