#-*-coding:utf-8-*-

print "为什么要用到列表生成式呢？，因为Python提倡用最少的代码"

print "生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"
L = range(1, 11)
print L

print "生成[1*1, 2*2, 3*3 ....]"

L = []
for x in range(1, 11):
    L.append(x * x)

print L

print "上面利用实现了for循环实现了，但是太繁琐"
print "利用列表生成器只需要一句话"

print [x * x for x in range(1, 11)]

print "列表生成器中添加if语句"
print [x * x for x in range(1, 11) if x % 2 == 0]

print "使用双层for循环"
print [strA + strB for strA in "ABC" for strB in "XYZ" ]


