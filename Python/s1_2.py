#coding:utf8

#如果有末尾Null字符，一定记得先丢弃它
#时间复杂度O(n)，空间复杂度也是O(n)
def s1():
	s = raw_input("Please input s:")
	s1 = ""
	for i in range(len(s)-1,-1,-1):
		s1 += s[i]
	return s1

#时间复杂度O(n)，空间复杂度也是O(n)
def s2():
	s = raw_input("Please input s:")
	s1 = ""
	for i in range(len(s)):
		s1 += s[-(i+1)]
	return s1


#这里主要是str类型不可变，所以将其转化为list后反而使得问题更加复杂了。
#出去list的额外space开销，如果str可变的话，那么space complexity将会是O(1)，
#但是额外的list显然使得space complexity重新回到O(n)
def s3():
	s = raw_input("Please input s:")
	s = list(s)
	#s1 = 'i'*len(s)
	if len(s)%2:
		medium = (len(s)-1)/2
		for i in range(1,medium+1):
			s[medium+i],s[medium-i] = s[medium-i],s[medium+i]
			#在未把字符串转化为list之前，这里会报错，python中的str数据类型是immutable的

	else:
		medium = len(s)/2
		for i in range(medium):
			s[medium-i-1],s[medium+i] = s[medium+i],s[medium-i-1]

	return ''.join(s)

#网上有说到这种方法是非常快，至少比s5要快很多
#实际的是[begin:end:step]
def s4():
	s = raw_input("Please input s:")
	return s[::-1]


#比s4慢很多
def s5():
	s = raw_input("Please input s:")
	return ''.join(reversed(s))

def s6(s):
	if s != '':
		return s[-1]+s6(s[:-1])
	else:
		return ''