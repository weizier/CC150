#coding:utf8

#第一个解法
#时间复杂度为O(n**2)
def s1():
	s = raw_input("Please input string s:")
	for i in range(len(s)):
		for j in range(len(s)):
			if i==j:
				continue
			elif s[i]==s[j]:
				return False
	return True

#第二个解决方法， 实际该方法已经不符合题目要求了，因为利用了其他的数据结构
#O(n),该时间复杂度主要在于set(s)这里，而len()的时间复杂度为O(1)
def s2():
	s = raw_input("Please input string s:")
	s1 = set(s)
	if len(s1)<len(s): #直接判断不等即可
		return False
	else:
		return True


#第三种解决办法，依然借助了其他的数据结构
#转化为list后再sort的时间复杂度为n*log(n)+n,但是比较省空间，因为sort直接在原list上做排序
#直接用string做sorted的时间复杂度为n*log(n)+n.(?) 不太确定是否分析正确。
def s3():
	s = raw_input("Please input string s:")
	s = sorted(s,key=lambda x:x) #这里也可以先将s转化为list后，再对该list进行sort()
	#其实直接用 s=sorted(s) 即可
	for i in range(len(s)-1):
		if s[i] == s[i+1]:
			return False
	return True


#第四个解法，实际为第一个解法的改进版
#个人认为时间复杂度是O(n*(n+1)/2)
def s4():
	s = raw_input("Please input string s:")
	for i in range(len(s)):
		for j in range(i+1,len(s)): #非常简单的一个改进，但是对于时间复杂度来说是成倍的提高
			if i==j:
				continue
			elif s[i]==s[j]:
				return False
	return True



#第五种解法，为参考答案后转化为python来实现
#感觉很多O(n)的解法都是跟位操作相关的
#最开始想到用字典来表征，即字母用作key，value表示该字母是否出现过，
#后来想到要在dict中判断是否存在key，这也会带来时间复杂度。所以不能用

#还有一个非常重要的点是：必须问面试官string的编码格式是ascii还是Unicode。
#这二者有很大区别
#O(n)的时间复杂度 O(1)的空间复杂度
def s5():
	s = raw_input("Please input string s:")
	if len(s)>256:
		return False    #由于ascii编码字符总共才256个

	d = [False]*256          #其内用False和True来表示比用0和1来表征要节省空间
	for i in s:
		num = ord(i)         #python中要得到字符对应的数字，必须使用ord(),反之用chr()
		if d[num]:
			return False
		else:
			d[num] = True
	return True


#该方法比s5方案要节省空间，但是时间复杂度仍然O(n)，并且此时还只能处理小写字母。
def s6():
	s = raw_input("Please input string s:")
	if len(s)>256:
		return False

	checker = 0
	for i in s:
		num = ord(i)
		val = num - 97
		if checker & (1 << val): #在相应的bit位上进行位与
			return False
		checker |= (1 << val)    #相应位上存储下来
	return True


#充分利用了python中的long不限制长度的特点
#O(n)，但是比较节省space
def s7():
	s = raw_input("Please input string s:")
	checker = 0
	for i in s:
		num = ord(i)
		if checker & (1<<num):
			return False
		checker |= (1<<num)
	return True


#看到有人用字典的办法，那我也来实现一个吧。
#字典的i in d时间复杂度为O(1)，所以总的时间复杂度为O(n)
#set的本质和dict的本质都是hash table
def s8():
	s = raw_input("Please input string s:")
	d = {}
	for i in s:
		if i in d:
			return False
		else:
			d[i] = True
	return True