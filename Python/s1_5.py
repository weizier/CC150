#coding:utf8






'''
下面的方法都是理解错了题目的意思，我的做法是将每个字符都计数，
然后按照该计数将字符串输出来，但是实际原题的意思是不应该将字符
在源字符串中的顺序弄乱,所以以下方法都不能用。

解决办法：对s3()方法中的排序去掉就行
'''








#O(n)
#此方法实际暗含了对字符串按照字符进行排序的功能
def s1():
	s = raw_input('Please input s=')
	s_list = [0]*256
	for c in s:
		num = ord(c)
		s_list[num] +=1
	s1 = ''
	for i in range(len(s_list)):
		s1 += ('%c%d' % (chr(i),s_list[i])) if s_list[i]>0 else '' 
		#这里必须判断是否大于1否则会是一个重大的bug
	if len(s1)<len(s):
		return s1
	else:
		return s


#O(n)
def s2():
	s = raw_input('Please input s=')
	s_dict = {}
	for c in s:
		s_dict.setdefault(c,0)
		s_dict[c]+=1
	s1 = ''
	for key,value in s_dict.items():
		s1+=('%c%d' % (key,value))
	return s1 if len(s1)<len(s) else s


#O(n*log(n))   #排序了才是这个时间复杂度，没排序的话是O(n)
def s3():
	s = raw_input("Please input s=")
	#s_list = sorted(s)  #这是对字符串中的所有字符都计数
	s_list = list(s)     #这是对字符串中的连续出现的重复字符才计数
	s1,j='',''
	num=0
	s_list.append(0)  
	#想想为什么要加这个，用意何在？不加这个的话会使得排序之后
	#的最后一个元素退出了但是不会添加到结果字符串当中去

	for i in s_list:
		if i!=j:
			if(j != ''):
				s1+=('%c%d' % (j,num))
			num = 1
			j = i
		else:
			num += 1
	return s1 if len(s1)<len(s) else s


#实际是O(256*n)，因为总共的字符个数为256个，所以为O(n)
#如果是Unicode编码，几乎可以认为是O(n**2)，反正此种方法效率没有以上高，
#并且返回的字符串没有排序
def s4():
	s = raw_input("Please input s=")
	s_set = set(s)
	s1=''
	for c in s_set:
		num = s.count(c)   #主要是这里计数每次都要O(n)的时间复杂度
		s1 += ('%c%d' % (c,num))
	return s1 if len(s1)<len(s) else s


