#coding:utf8

#时间复杂度为O(n)
def s1(s):
	for i in range(len(s)):
		if s[i]==' ':
			s[i]='%20'
	return ''.join(s)


#时间复杂度为O(n)
#此方法要求传入进来的是原始字符串，所以还不如干脆自己输入，不从main函数调用
def s2(s):
	s = raw_input("Please input s:")
	s = s.split(' ')
	return '%20'.join(s)

#时间复杂度为O(n**n)，不能有比这个更差的方案了
#刚做完实验，比如字符串内超过一千个空格后，该程序就不能运行要报错了
def s3(s):
	try:
		s[s.index(' ')] = '%20'
		return s3(s)
	except ValueError,e:
		return ''.join(s)



def main():
	s = raw_input("Please input s:")
	s = list(s)
	s = s3(s)
	print s

