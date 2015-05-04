#coding:utf8



#时间复杂度为O(n**2),空间复杂度为O(n)
def s1():
	s1 = raw_input("Please input s1:")
	s2 = raw_input("Please input s2:")
	s1 = list(s1)     #str类型为immutable，所以需要先转为list后才能对其进行删除操作
	s2 = list(s2)
	for i in s1:
		if i not in s2:  #i in list的操作时间复杂度为O(n)
			return False
		id = s2.index(i) #只会返回第一个index值，所以刚刚好每次只删除一个
		del s2[id]
	return True

#时间复杂度O(n*log(n))，空间复杂度为O(n)
def s2():
	s1 = raw_input("Please input s1:")
	s2 = raw_input("Please input s2:")
	s1 = sorted(s1)  #最快的排序算法时间复杂度为O(n*log(n)),注意返回的是list类型
	s2 = sorted(s2)
	if s1==s2:       #判断两个list相等也需要O(n)
		return True	
	else:
		return False

#时间复杂度为O(n),空间复杂度为O(n)
def s3():
	s1 = raw_input("Please input s1:")
	s2 = raw_input("Please input s2:")
	s1_dict = {}
	s2_dict = {}

	for i in s1:
		s1_dict.setdefault(i,0)
		s1_dict[i]+=1
	for i in s2:
		s2_dict.setdefault(i,0)
		s2_dict[i]+=1
	if s1_dict == s2_dict:
		return True
	else:
		return False

#虽然时间和空间复杂度和s3解法一样，但在实际操作过程中还是list比dict存储效率更高一些
def s4():
	s1 = raw_input("Please input s1:")
	s2 = raw_input("Please input s2:")
	s1_list = [0]*256
	s2_list = [0]*256
	for i in s1:
		num = ord(i)
		s1_list[num]+=1
	for i in s2:
		num = ord(i)
		s2_list[num]+=1	
	if s1_list == s2_list:
		return True
	else:
		return False

#此方法复杂又可读性不强，还耗时。
#时间复杂度为O(n**2)，主要是在迭代那里也需要一
#个O(n)的时间复杂度，使得整个时间复杂度上升。
#空间复杂度可以认为是O(1)

def s5():
	s1 = raw_input("Please input s1:")
	s2 = raw_input("Please input s2:")
	checker1,checker2 = 0,0
	for i in s1:
		num = ord(i)

		j = 1
		'''def isExisted(j):
			if	(checker1 & (1<<(num+256*j))):
				j +=1
				j = isExisted(j)		
			return j			

		j = isExisted(j)'''
		while(checker1 & (1<<(num+256*j))):
			j += 1

		checker1 |= (1<<(num+256*j))

	for i in s2:
		num = ord(i)

		j = 1
		'''def isExisted(j):
			if	(checker2 & (1<<(num+256*j))):
				j +=1
				j = isExisted(j)	
			return j				

		j = isExisted(j)'''

		while(checker2 & (1<<(num+256*j))):
			j += 1

		checker2 |= (1<<(num+256*j))

	if checker1 == checker2:
		return True
	else:
		return False

import hashlib
def s6():
	s1 = raw_input("Please input s1:")
	s2 = raw_input("Please input s2:")
	s1_md5,s2_md5 = 0,0
	for i in s1:
		s1_md5 += int(hashlib.md5(i).hexdigest(),16)
	for i in s2:
		s2_md5 += int(hashlib.md5(i).hexdigest(),16)
	return True if s1_md5==s2_md5 else False
