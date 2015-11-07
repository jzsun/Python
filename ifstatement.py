#-*-coding:utf-8-*-

age = raw_input("Please input your age !")
print age
if age >= 18:
    print("adult") #此时就算输入16的话，同样输出adult，这是错误的
#因为raw_iput返回的是字符串，必须转型int(age)
elif age > 12:
    print("teenager")
elif age >= 0:
   print("Child")
else:
    pass #pass是个占位符，一个空分支会报语法错误

print "这个功能是错误的，因为我们没有考虑到raw_input()返回的是字符串。必须转型"
