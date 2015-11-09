#-*-coding:utf-8-*-

print "递归函数就是函数调用自身"

print "一个好的递归函数必须有结束条件"

print "递归函数1：阶乘"
print "n! = 1x2x3x4x...xn"

'''

'''
def fact(n):
    if  n == 1:
        return 1
    else:
        return fact(n-1) * n

print fact(2)

print fact(3)

print "递归利用的栈， 当递归调用的次数过多的话，会导致栈的溢出"
#print fact(1000)

print "在python中，任何递归函数都存在栈溢出的问题,尾递归也不行，python没有对其优化"
