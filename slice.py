#-*-coding:utf-8-*-

print "本文了解Python的切片操作"

L = ["zhao", "qian", "sun", "li", "zhou"]
print L

print "对于这个list，我们想取元素，不是很麻烦，直接L[0], L[1],之类的都行"
print "如果是100个，或者是一千个元素，我们取前n个元素，用while/for循环也是可以实现的，但是`\
 太麻烦，Pyhon提供了一个Slice的特性，方便我们随意截取一段元素"
"""
for i in L:
    print i
"""
print "用Slice来提供前三个元素L[0:2]"
print L[0:3]
print "需要注意的是[a, b]在数学上属于左闭又开区间[)"
print "L[0, 3]不包含索引3，只有0,1,2"
print "0作为第一个索引可以省略L[:3] = L[0:3]"

print "可以从第一个元素开始，也可以从最后一个开始-1, -1作为结束边界[:-1],不包含最后一个元素"

print L[-4:-1]
print L[-4:]

print "初始化一个0-99的数列"
L = range(100)
print L

print "取前十个数"
print L[0:10]
print L[:10]

print "取后十个数[-10:] 而不是[-10:-1], 同样不包含右边界"
print L[-10:-1]
print L[-10:]

print '第十个到第二十个元素'
print L[10:20]

print "切片可以指定步长，默认是1"

print "每隔两十个元素取一个"
print L[::20]

print "通过切片复制list"
print L[:]

print "tuple也是一种list只是不可变，tuple同样可以切片操作，只是结果仍是tuple"

print (1,2,3)[0:3]

print "str同样可以进行切片操作"
print "ABCD"[0:3]
