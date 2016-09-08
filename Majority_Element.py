class Solution(object):
	def majorityElement(self, nums):
		r = 0
		majority = 0
		for i in nums:
			# print(i)			
			if r == 0:				
				majority = i
				r = r + 1
			else:
				if majority == i:
					r = r + 1
				else: 
					r = r - 1
		return majority
	# if __name__ == '__main__':
	# 	nums = ['b','a','b','a','c','a','c','c','a','a','a','c','a','a']
	# 	print("233333333333333333")
	# 	print(majorityElement(nums))


# class Solution:  
#     # @param num, a list of integers  
#     # @return an integer  
# 	def majorityElement(self, num):  
# 		dict = {}  
# 		maxnum = len(num)/2+1  
# 		for i in num:  
# 			if i in dict:  
# 				dict[i]+=1  
# 			else:  
# 				dict[i]=1  
# 				for i in dict:  
# 					if dict[i]>= maxnum:  
# 						return i
nums = ['b','a','b','a','c','a','c','c','a','a','a','c','a','a']
a = Solution()
b = a.majorityElement(nums)
print("233333333333333333")
print(b)