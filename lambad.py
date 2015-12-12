#-*-coding:utf8-*-

print "python中匿名函数的用法，所谓匿名函数就是不去显示的去定义函数"
#比如之前的f(x) = x^2的函数

def f(x):
	return x * x 
	pass
#改成匿名函数就是lambda x: x * x

print map(f, [1, 2, 3, 4, 5]) 
#就可以写成

print map(lambda x: x * x, [1, 2, 3, 4, 5])

print "lambda x: x * x", " lambda是一个关键字, : 前面的是参数，而后面的返回值"
print "匿名函数有一个限制，只能有一个表达式，不用写return，也不能写return"
print "匿名函数也是一个函数对象，可以赋值给别的变量"

f1 = lambda x: x * x
print f1(2)

print "当然也可以作为返回值"
def build(x, y):
	return lambda x, y : x * x + y * y

print build(3, 4)
f2 = build(3, 4)
print f2(3, 4)