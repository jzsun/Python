#-*-coding:utf-8-*-
import os
import os.path


print "列出特定目录下所于的文件列表，带有子文件夹的需要列出子文件夹得名字src/hello.py这样的形式"
print "因为我需要特定目录下的文件列表，一个个拷贝太麻烦"

def  handleFiles(path, prefix = ""):
	print path
	clearFile()
	for root, dirs, files in os.walk(path):
		print root
		writeFileInfo(root)
		for fileName in files:
			if fileName.endswith("cpp"):
				print fileName
				writeFileInfo(prefix + fileName + "\\");
		for fileName in files:
			if fileName.endswith(".h"):
				print fileName
				writeFileInfo(prefix + fileName + "\\");
		for d in dirs:
			print d
	pass

def  writeFileInfo(fileName):
	with open("info.txt", "a") as f: #位于python程序目录下面
		f.write(fileName+"\n");
	f.close()

def clearFile():
	with open("info.txt", "a") as f:
		f.truncate();
	f.close()
	pass
if __name__ == "__main__":
	path = "D:/qtcreatorGit/alpahaEditor/QScintilla-gpl-2.9.1/src"
	handleFiles(path, "./QScintilla-gpl-2.9.1/src/")
