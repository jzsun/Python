#-*-coding:utf-8-*-

print "你好, 元组"
print "元组的外在形式就是()界定边界，内部元素以,逗号分隔"
print "原则一旦初始化后，就不能改变(实际上是指向不能变,见本节后文例子)，没有insert,和append之类的函数"

t = ()
print t

classmates = ("zhao", "qian", "sun")
print classmates

print "定义一个元素的元组的形式是(1, ) 而不是(1)"

oneE = (1, )
print oneE

print oneE[0]

print "(1)=", (1)

print "‘可变’的元组","(1, 2, [3, 4])"

t = (1, 2, [3, 4])

print t 
print "元组所谓的不变也只是指向不能变","list里面的值是可以改变的，保证真正不变的话，必须元素也不能改变"
t[2][0] = 5

print t
