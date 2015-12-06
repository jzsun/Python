#-*-coding:utf-8-*-

print "map-reduce的学习"

#map
#map接受两个参数，一个是函数，一个序列，map将传入的函数依次作用到序列的每一个元素，并把结果\作为新的list返回

"""
"""

def f(x):
	return x * x

print map(f, [1, 2, 3, 4])

print "有时可能会觉得用for循环依然能够实现这个功能"
L = []
for n in [1, 2, 3, 4, 5]:
	L.append(f(n))
print L

print "但是上面的代码不能让我们一眼看明白将f(x)作用到每一个元素并把结果生成一个新的list？，\
不可以，而map事实上就是把运算规则抽象了，我们不仅可以计算x^2,页可以计算任意复杂的函数，\
都是作用于序列的每一个元素"
'''
而下面的转换为字符串却只需要一行代码
'''
print map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])

#reduce
print "reduce把一个函数作用在一个序列上必须[x1, x2, x3, x4...],这个函数必须一次接受两个参数，\
reduce把结果和序列的下一个元素做累计计算"

#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1,x2) ,x3),x4)
#写法是f(, x4)->f(f( ,x3) ,x4)->f(f(f(,x2) ,x3), x4)->f(f(f(x1, x2),x3),x4)
#第一个参数总是上一个函数的结果


#求和
def  add(x, y):
	return x + y

sum = reduce(add, [1,  3, 5, 7, 9])
print sum

#Note: python有内建的求和函数sum

#当然要将序列[1, 3, 5, 7, 9]变成证书13579的话，reduce就可以排上用场
def fn(x, y):
	return x*10 + y

convertToNum = reduce(fn, [1, 3, 5, 7, 9])
print convertToNum

#上面的例子上级上用的会很少，但是考虑到str同样是一个序列，对上面的列子改动的话，
#就可以写出str转化为数字的函数

def char2num(s):
	return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[s]
	pass

print reduce(fn, map(char2num, '13579'))#map函数相当于将字符串序列转化为了单个数字的序列

#整理成一个函数str2int
def str2int(s):
	def fn(x, y):
		return x*10 + y
	def char2num(s):
		return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[s]
	return reduce(fn, map(char2num, s))

print str2int("123456789")

	
#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
#输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']

#在这里我是忘记str转化为大小写的的相关用法的，我就是去通过CMD去查的 help(str),会给出我想要的信息的
def convertName(s):
	str1 = s[0].upper()
	str2 = s[1:].lower()
	return str1 + str2
	pass

print convertName("vHello")
print map(convertName, ['adam', 'LISA', 'barT'])