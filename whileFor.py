#-*-coding:utf-8-*-

print "python中循环语句的使用"

names = ["zhao", "qian", "sun"]
for name in names:
    print name

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum += x
print sum

sumS = 0
numbers = range(10) 
#(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]也行
for x in numbers:
    sumS += x
print sumS

print range(5)

sum = 0
n = 10
while n > 0:
    sum += n
    n = n - 1
print sum
