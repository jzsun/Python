#-*-coding:utf-8-*-
import os
import os.path

print "列出特定目录下所于的文件列表，带有子文件夹的需要列出子文件夹得名字src/hello.py这样的形式"

def  handleFiles(path):
	print path
	for root, dirs, files in os.walk(path):
		print root
		writeFileInfo(root)
		for fileName in files:
			if fileName.endswith("cpp"):
				print fileName
				writeFileInfo(fileName + "\\");
		for fileName in files:
			if fileName.endswith(".h"):
				print fileName
				writeFileInfo(fileName + "\\");
		for d in dirs:
			print d
	pass

def  writeFileInfo(fileName):
	with open("info.txt", "a") as f:
		f.write(fileName+"\n");
	f.close()

	pass
if __name__ == "__main__":
	path = "D:/qtcreatorGit/alpahaEditor/QScintilla-gpl-2.9.1"
	handleFiles(path)