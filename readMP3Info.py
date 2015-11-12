#-*-coding:utf-8-*-
#encoding=utf8
import os
import os.path
'''
os.walk()可以得到一个三元tupple(dirpath, dirnames, filenames)，其中第一个为起始路径，第二个为起始路径下的文件夹，第三个是起始路径下的文件。
其中dirpath是一个string，代表目录的路径，dirnames是一个list，包含了dirpath下所有子目录的名字。filenames是一个list，包含了非目录文件的名字。这些名字不包含路径信息，如果需要得到全路径，需要使用os.path.join(dirpath, name).

'''
def getID3(fileName):
    fp = open(fileName, "r")
    fp.seek(-128, 2)
    fp.read(3)
    title = fp.read(30)
    fp.close()
    print title
    return {"title" : title}

def mqms2Remove(filename):
    ignoreStr1 = "[mqms2]"
    ignoreStr2 = "[mqms]"
    if ignoreStr1 in filename:
        return filename.replace(ignoreStr1,"")
    elif  ignoreStr2 in filename:
        return filename.replace(ignoreStr2, "")
    else:
        return filename

def handle(path, writefile):
    wf = file(writefile, "a+")
    wf.truncate()#每次清空文件
    for parent, dirnames, filenames in os.walk(path):
        for dirname in dirnames:
            """
            strParent = "parent is:" + parent + "\n"
            strDirname = "dirnames is" + dirname + "\n"
            print strParent
            print strDirname
            wf.write(strParent)
            wf.write(strDirname)
            """
        for filename in filenames:
            fullname =  os.path.join(parent, filename)
            #print getID3(fullname)
           
            #print strParent 
            print filename
            #print fullname
            
            #wf.write(strParent)
            filename =  mqms2Remove(filename) + "\n"
            wf.write(filename)
            #wf.write(fullname)

if __name__=="__main__":
    readPath = "/home/sundashe/song"
    writefile = "/home/sundashe/mp3.info"
    handle(readPath, writefile)

