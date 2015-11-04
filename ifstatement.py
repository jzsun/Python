#-*-coding:utf-8-*-

age = raw_input("Please input your age !")
print age
if age >= 18:
    print("adult") #此时就算输入16的话，同样输出adult，这是错误的
#因为raw_iput返回的是字符串，必须转型int(age)
elif age > 12:
    print("teenager")
else:
   print("Child")
