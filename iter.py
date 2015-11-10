#-*-coding:utf-8-*-

print "pythoh中迭代器的使用"
print "在python中，迭代器是通过for in来完成的"

d = {"a":1, "b":2, "c":3}

print "我们迭代的是key"
for key in d:
    print key,d[key]

print "我们也可以取迭代value"
for value in d.itervalues():
    print value

print "同时迭代key和value"
for key,value in d.iteritems():
    print key, value

print "字符串同样是可迭代对象"
for char in "abcd":
    print char

print "for循环只要作用与一个可迭代对象，那么循环就能正常运行，而不用关心数据类型"

print "如何判断一个对象是否为可i迭代对象"

from collections import Iterable
print isinstance("abc", Iterable)
print isinstance([1, 2, 3], Iterable)
print isinstance(123, Iterable)

print "如果想同时迭代list的索引和元素怎么办呢？ 需要用到enumerate，不用我没想到为什么要迭代list的索引和元素"

for i, value in enumerate(["a", "b", "c"]):
    print i, value

print "for 循环里面同时引用两个数据是很常见的事"
for x,y in [(1,1), (2, 4), (3, 9)]:
    print x, y
