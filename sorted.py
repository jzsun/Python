#-*-coding:utf-8-*-
"""
本节主要参考
1. http://www.cnblogs.com/65702708/archive/2010/09/14/1826362.html
"""
print "list排序方法"
print "1.list的成员函数sort进行排序，在原位重新排列列表"
print "2.built-in函数sorted进行排序(version >= 2.4), 产生一个新的列表"

'''
the list.sort() method is only defined for lists. In contrast, the sorted() function accepts any iterable.

''
#help(sorted)

#help(list.sort)

L = [4, 3, 6, 8, 1]
print "----------------------------------"
print "调用sorted"
print "L = [4, 3, 6, 8, 1]"
print "调用sorted之前"
print L
print "调用sorted"
print sorted(L)
print "调用sorted之后"
print L
print "调用sort之前"
print L.sort()
print "调用sort之后"
print L

print"通过输出，可以验证sort原位排列返回的是None， sorted产生一个新的列表返回"

print "----------------------------------"
L = [("b",2), ("a",1), ("c", 3), ("d", 4)]
print L
print sorted(L, cmp=lambda x,y:cmp(x[1],y[1]))
"""
sorted 是如何根据cmp来排序的呢？ 返回的1 -1 0 在排序中是怎么利用的呢？
"""
