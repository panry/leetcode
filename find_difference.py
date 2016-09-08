import random
# def findTheDifference(s, t): 
# 	s = 'abcd'
# 	t = 'abcde'
# 	b = set()
# 	for i in s:
# 		b.add(i)
# 	for j in t:	
# 		if j not in b:
# 			print(j)
# 			return j
def findTheDifference(s, t): 
	for j in t:	
		if j not in s:
			return j
if __name__ == '__main__':
	s = 'abcd'
	t = 'abcde'
	d = findTheDifference(s,t)
	print(d)