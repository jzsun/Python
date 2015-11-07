#-*-coding:utf-8-*-

print "python里的字典相当于C++里的Map，使用键值对存储"

print "{"":"", "":""}","字典花括号为边界，key-value以：分隔，key-avl值遵循python的语法规则"

#输出顺序随机
d = {"zhao":18, "qian":17, "sun":20}
print d

d["zhao"] = 28

print d

d["sun"] = 25
d["sun"] = 26 #覆盖上一次的赋值
print d

print "print d[\"li\"]", "#key不存在报错"

#检测key值是否存在的方法
#方法1，in
print "li" in d

print "sun" in d

#2 get()方法
print d.get("li") #不存在则输出None，在交互命令行不提示
#指定不存在时的输出方式，假设输出bucunzai

print d.get("li", "bucunzai")

#输出key-val
#d.pop("li") 删除不存在的值，也会报错
d.pop("zhao")
print d

print "Note: dict的可以、必须是不可变对象"
#key = [1, 2]
#d[key] = "a list"
