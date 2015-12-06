#-*-coding:utf-8-*-

print "pyhon中返回函数的说明"
print "高阶函数不仅可以把函数作为参数，也可以把函数作为返回值"

'''
普通的求和函数
'''

def calc_sum(*args):
	ax = 0
	for n in args:
		ax += n
	return ax

"""
但是当我们不想要立即求和，而是在后面的代码中，根据
需要再计算怎么办？不返回求和的结果，只是返回求和的函数
"""
def lazy_sum(*args):
	def sum():
		ax = 0
		for n in args:
			ax = ax + n
		return ax
	return sum

"""
当我们调用lazy_sum()事返回的并不是求和的结果，而是求和的函数
"""
f = lazy_sum(1, 3, 5, 7, 9)
print f

print f()
"""
调用函数f时才真正得到结果
"""
print "而且值得注意的是就算我们两次传入相同的参数，返回的函数也是不同的"

f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print "f1 == f2 = " ,f1 == f2

"""
闭包的概念
参考: http://www.cnblogs.com/ma6174/archive/2013/04/15/3022548.html

"""
print "闭包就是根据不同的配置信息得到不同的结果"

"""
闭包: 是词法闭包(Lexical Closure)的简写,是引用了自由变量的函数。这个被引用的自由变量讲和这个函数一同存在，即使已经离开了创造它的环境也不例外。所以另一种说法是认为闭包是由函数和与其相关的引用环境组合而成的实体

"""

def make_adder(addend):
	def adder(augend):
		return augend + addend
	return adder

p = make_adder(22)
q = make_adder(44)

print p(100)
print q(100)

print "结果分别是122，144"

print "make_adder做作为一个函数，返回另外一个函数，而且这个函数携带的\
外部传来的一个参数addend，我们可以将这个参数当做函数a返回dder的一个配置信息\
，配置信息的不同p = make_adder(22), q = make_adder(44)传递的信息不同，返回的adder携带的配置信息就不同，那么当我们调用返回函数时，传入相同的参数得到的结果也是不同的,p(100)得到是 100 +22 q(100)得到的是 100 + 44"


def hellocounter(name):
	count = [0]#不能定义为count,会报错
	def counter():
		count[0] += 1
		print "hello,",name,",",str(count[0]) + " access!"
	return counter

hello = hellocounter("yy")
hello()
hello()
hello()


def makebold(fn):
	def wrapped():
		return "<b>" + fn() + "</b>"
	return wrapped

def makeitalic(fn):
	def wrapped():
		return "<i>" +  fn() + "</i>"
	return wrapped

@makebold
@makeitalic

def hello():
	return "hello python"

print hello()

"""
上面的函数意味着装饰器就是闭包的一种
"""
