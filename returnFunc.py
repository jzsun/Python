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
"""
