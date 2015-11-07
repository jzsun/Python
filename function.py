#-*-coding:utf-8-*-
import types

print "------------------------------------------------------"
print "查看所有的系统内建函数的方式"
print "方式1，去官网查看"
print "方式2， dir(__builtins__)"
"""
#多行注释的方式
for fName in dir(__builtins__):
    print fName
"""

print "查看某个内建函数的用法, 比如abs，使用help(abs)"
#print help(abs)

print "当我们传入的参数类型不对，或者参数不匹配的话，都会报错"

#函数的别名
print "函数名其实就hi一个指向函数对象的引用，完全可以赋值给另外一个变量，相当于给函数起了一个别名"
pyabs = abs
print pyabs(-1)

print "------------------------------------------------------"
print "函数的定义"
#pyhon代码的换行，在需要换行的地方加上\就行
print "在python中的定义一个函数需要使用def语句，依次写出->\
函数名，括号，括号中的参数和冒号:,\
然后在缩进块中编写函数体，函数的返回值用return语句返回\
"

def custom_abs(x):#其实需要类型判断,见39-47行的注释
    if x >= 0:
        return x
    else:
        return -x

print custom_abs(1)
print custom_abs(-1)

'''
print types
print dir(types)
print types.__doc__
if type(1) is types.IntType:
    print True
else:
    print False
'''

print "当函数没有返回值，意味这返回值是None,而显示返回return None 可以简写为return"

print "python在表现形式上可以返回多个值"
def custom_swap(x, y):
    x, y = y, x #通过异或可以交换值
    return x, y

x, y = custom_swap(1, 2)
print x, y


print "实际上依然是一个值,返回的是一个元组"
val = custom_swap(1, 2)
print val


print "------------------------------------------------------"
print "函数参数的说明"
print "说明使用默认参数的思想，减少函数使用的复杂度"
print "默认参数必须指向不可变对象，不然会有bug发生" #详细说明line 89

def power(x, n = 2):
    s =  1
    while n > 0:
        n -= 1
        s *= x
    return s

print power(2,2)
print power(2)

print "默认参数一定要放在所有可变参数后面"

"""
def errorFun(x = 3, y):
    return
"""
print "如果你传入一个参数的话，系统会认为你是在修改第一个默认值\
，而第二个参数相当于没有传参"


print "默认参数必须指向不可变对象，不然会有bug发生"

def add_end(L = []):
    L.append("End")
    return L

print "正常调用不会有问题"
print add_end([1, 3, 4])
print add_end(["x", "y", "z"])

print "使用默认值"
print add_end()
print add_end()

print "第二次的结果显然是错误的，我们函数默认只有一个元素"

print "why?"

print "因为函数在定义的时候， 默认参数L的值就被计算出来了即[]\
,而默认参数L也是一个变量，它指向对象[],每次调用该函数，如果\
改变了L的内容，下次再次调用的时候，默认参数的内容就改变了，不在是[]"

print "Howto"

def add_end(L = None):
    if L is None:
        L = []
    L.append("End")
    return L

print add_end()
print add_end()

print "python的可变参数"

