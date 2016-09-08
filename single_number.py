import binascii  
class Solution(object):
	def singleNumber(self, nums):
		b = 0
		for i in nums:
			print(i)
			b ^= i
		return b

# nums = ['b','a','b','a','c']
# a = Solution()
# b = a.singleNumber(nums)
# print("233333333333333333")
# print(b)
    
