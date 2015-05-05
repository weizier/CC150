#coding:utf8

#Here,the operation 'in' in Python is equivalent to 'isSubstring' in this Problem.
def s1():
	s1 = "waterbottle"
	s2 = "erbottlewat"
	s1 += s1
	return (s2 in s1)