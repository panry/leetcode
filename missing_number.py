class Solution(object):
	# def missingNumber(self, nums):
	# 	a = 0
	# 	for i in nums:
	# 		if i != a:
	# 			return a			
	# 		a += 1

	def missingNumber(self, nums):
		if len(nums) == 0:
			return 0
		n = len(nums)
		return int(n*(n+1)/2 -sum(nums))




nums = [0,1,2,3,4,5,6,8,9]
a = Solution()
b = a.missingNumber(nums)
print("233333333333333333")
print(b)
