#usr/bin/python
#coding:utf-8
import third
import linecache
import chardet
a = [1,2,3]
print a
# d = "哈哈".decode("utf-8")
# print len(d)
a = U"哈哈" #标识Unicode编码
r = r"\n" #不对字符串进行转义
print a
a = "this is {whose} {fruit}".format(whose="my",fruit="apple")
print a
print "ahahh"