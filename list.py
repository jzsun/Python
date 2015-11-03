#-*-coding:utf-8-*-

#list
numbers=["1", "2", "3", "4"]
print numbers

print "list numbers的长度", len(numbers)

print numbers[0]

print numbers[-1] #最后一个元素

#print numbers[4] #IndexError: list index out of range越界

numbers.append("5")

print numbers

numbers.insert(1, "0")

print numbers

numbers.pop()#删除末尾元素

print numbers

numbers.pop(1)#删除指定位置的元素

print numbers

numbers[1] = "oo" #把某个位置的元素,意味着list里面的数据类型可以不同

print numbers

s = ["a", numbers]
print s
print len(s)
#print s.len()#error
