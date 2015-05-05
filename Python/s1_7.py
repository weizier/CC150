#coding:utf8

def s1():
	a = [[1,3,5,0,7],[2,4,3,6,8],[3,5,0,7,9],[4,8,6,2,7]]
	record = []
	for i in range(len(a)):
		for j in range(len(a[0])):
			if a[i][j] == 0:
				record.append([i,j])
	for i,j in record:
		for x in range(len(a[0])):
			a[i][x] = 0
		for y in range(len(a)):
			a[y][j] = 0

	return a