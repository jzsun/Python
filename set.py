#-*-coding:utf-8-*-

print "set和dict不同，set只是key的集合，没有value，而且key不能重复，重复添加无效果"

print "创建一个set0，需要提供一个list作为输入源"

s = set([0, 2, 1, 2])
print "set([0, 2, 1, 2]"
print s
print "set过滤了重复的值"


print "连续两次添加数据3"
s.add(3)
print s

s.add(3)
print s #重复添加相同数据无效

print "remove data"
s.remove(3)
print s

print "remov a data, it is not existing"
print "s.remove(3) #keyErro"

print "set可以看做数学上无序和无重复的集合, 必然可以进行集合运算"
s1 = set([1, 2, 3])
s2 = set([2, 4, 3])
print s1 & s2 #求交集
print s1 | s2 #求并集


print "set里面不可以放入可变对象，因为可变对象无法判断是否相等，就意味着无法判断重复"

print "set([1, 2, [1, 2]])"
print "TypeError: unhashable type: 'list'"
#print set([1,2, [1, 2]])
