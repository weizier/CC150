#coding:utf8

def s1(s):
	for i in range(len(s)):
		if s[i]==' ':
			s[i]='%20'
	return ''.join(s)

#此方法要求传入进来的是原始字符串，所以还不如干脆自己输入，不从main函数调用
def s2(s):
	s = raw_input("Please input s:")
	s = s.split(' ')
	return '%20'.join(s)


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

