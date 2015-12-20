#-*-coding:utf-8-*-

print "开始面向对象编程的学习"

class student(object):
	"""docstring for student"""
	def __init__(self, name, score):
		super(student, self).__init__()
		self.name = name
		self.score = score

	'''
	def printStudentInfo():
			print self.name, self.score
			pass

	没有self的话，会出现调用错误

	Traceback (most recent call last):
	  File "oop.py", line 17, in <module>
	    lip.printStudentInfo()
	TypeError: printStudentInfo() takes no arguments (1 given)

	'''
	def printStudentInfo(self):
		print self.name, self.score
		pass
		

lip = student("Lip", 85)
lip.printStudentInfo()


#能够直接操做类的内部数据
lip.name = "sundashe"
lip.printStudentInfo()

#设置变量的访问权限
class student2(object):
	"""docstring for student2"""
	def __init__(self, name, score):
		super(student2, self).__init__()
		self.__name = name
		self.__score = score

	def printStudent2Info(self):
		print self.__name, self.__score
		pass

sundashe = student2("sundashe", 99)

sundashe.printStudent2Info()
#sundashe.__name 直接这样会报错
'''
不会报错，但是没有修改的效果
'''	
sundashe.__name = "lip"
sundashe.printStudent2Info()

#实际上python把__name修改成了_student2__name
sundashe._student2__name = "lip"
sundashe.printStudent2Info()	

#但是不建议这么干，因为不同的解释器可能翻译的变量名buyiy
#Python本身没有强制的机制，需要自觉