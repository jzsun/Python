#-*-coding:utf-8-*-

print "why we need generator?"
print "一般通过列表生成式就能得到我们想要的内容"
print "但是内存限制，列表的内容必然是有限的，而且对于一个100万个元素的列表"
print "当我们只是访问前面几个元素时，后面的绝大多数空间都是白白浪费的"

print "如果列表元素只是在我们需要的时候才会推算，而不必创建完整的list，从而\
节省大量的空间，而生成器就是这种一边循环，一边计算的机制，从而成为生成器(generator)"


print "创建生成器的方式"
print "最简单的方式是将列表生成式的[]改为()"

L = [x*x for x in range(10)]
print L

g = (x*x for x in range(10))
print g

print "访问generator元素的方式通过不断的next()或者迭代"
print g.next()

for x in g:#g.next 已经迭代了一次，那么for循环就不是从第一个元素开始迭代了
    print x

#print g.next()#这个会报错，已经不能在迭代，for迭代完了

print "当推算的算法比较复杂，列表生成器的for不能满足时，我们可以用函数来实现"

print "斐波那契数列的处理"
print "当我们计算的斐波那契数列很大时，我们同样向通过生成器来实现，该如何处理呢"

print "通过函数可以容易实现这个算法"

def fib(num):
    n, a, b = 0, 0, 1
    while n < num:
        print b
        a, b = b, a+b
        n += 1
#fib(6)

print "我们可以看出函数是能够实现我们想要的效果, 因此python提供了另外一种定义generator的方法"

print "使用yield关键字"
def fib(num):
    n, a, b = 0, 0, 1
    while n < num:
        yield  b
        a, b = b, a+b
        n += 1
#print fib(6)

print "关键试试如何理解这个类似函数的生成器?"


def fib(num):
    n, a, b = 0, 0, 1
    while n < num:
        yield  b
        a, b = b, a+b
        n += 1

print "generator函数在用next的时候执行， 遇到yield返回，更新值，下次执行时从上次返回的yield语句处继续执行"
'''
比如对与fib(6)的执行步骤，yield之前之后分别添加一个输出语句
'''
def fibTest(num):  
    n, a, b = 0, 0, 1
    while n < num:
        print "befor--yield"
        yield  b
        print "after--yield"
        a, b = b, a+b
        n += 1

#for fib in fib(6):
#    print fib

"""
通过下面的分析，我们可以看出generator的特性
"""
fib = fibTest(6)

print fib.next() #第一次执行只会输出befor--yield

print fib.next()

print fib.next()
