#-*-coding:utf-8-*-

print "Python继承和多态的学习"
print "其实我更关注的其实是语法形式，因为我学的是C++，实际继承和多态是什么已经明白了"

class Animal(object):
	"""docstring for Animal"""
	def __init__(self):
		super(Animal, self).__init__()

	def run(self):
		print "Animal is running..."
		pass

class Dog(Animal):
	"""docstring for Dog"""
	def __init__(self):
		super(Dog, self).__init__()

	#重载覆盖了基类的相同函数
	def run(self):
		print "Dog is running..."
		pass

class Cat(Animal):
	"""docstring for Cat"""
	def __init__(self):
		super(Cat, self).__init__()

	def run(self):
		print "Dog is running..."
		pass
	#继承可以增加基类没有的功能
	def eat(self):
		print "Cat is eating fish..."
		pass
		

dog = Dog()
dog.run()
		
cat = Cat()
cat.run()


print "多态的说明"
def polyMethon(animal):
	'''
	print animal.run()
	这个形式会返回两行的结果
	Animal is running...
	None

	Animal is running...来自run()函数本身自带的print输出
	None是因为run()没有return语句，默认返回值是None, print animal.run() 打印出来的就是一个None
	'''
	animal.run()

polyMethon(Animal())
polyMethon(Dog())
polyMethon(Cat())