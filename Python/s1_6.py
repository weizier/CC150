#coding:utf8


#O(n**2)，由于这里本身就有n**2个数据，所以这已经是最小的时间复杂度了
#但是该方法有一个不好的点在于会消耗额外的内存，那有没有更好的方案呢？
def s1():
	previousList = [[1,3,5,7],[2,4,6,8],[3,7,5,9],[4,8,6,2]]
	currentList  = []
	n = len(previousList)
	for i in range(n):
		currentList.append([previousList[j][n-i-1] for j in range(n)])
	return currentList


def s2():
	a = [[1,3,5,7],[2,4,6,8],[3,7,5,9],[4,8,6,2]]
	n = len(a)
	for i in range(n/2):
		first = i
		last = n - i
		for j in range(first,last-1):
			top = a[i][j]
			a[i][j] = a[j][last-1]
			a[j][last-1] = a[last-1][first+last-1-j]
			a[last-1][first+last-1-j] = a[first+last-1-j][first]
			a[first+last-1-j][first] = top
	return a