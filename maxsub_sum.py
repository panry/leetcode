class Solution(object):
	def MaxSubSum(self, nums):
		MaxSum = 0
		Cursum = 0
		z = 1
		FuSum = nums[0]
		flag = True
# if the element are all nagative 
		for j in nums:			
			if j < 0:
				if FuSum  < j:
					FuSum = j
			else:
				flag = False
				break
		if flag is True:
			return FuSum
# find the MaxSum
		for i in nums:			
			Cursum += i
			if Cursum > MaxSum:
				MaxSum = Cursum
			if Cursum < 0:
				Cursum = 0
		return MaxSum

	# def MaxSubSum(self, nums):
	# 	MaxSum = nums[-1]
	# 	print(MaxSum)
	# 	Cursum = MaxSum
	# 	for i  in range( len(nums)-2,0):
	# 		Cursum += nums[i]
	# 		if Cursum < 0:
	# 			Cursum =0
	# 		Cursum = Cursum + nums[i]
	# 		if Cursum >= MaxSum:
	# 			MaxSum = Cursum
	# 		i -= 1
	# 	return MaxSum

nums = [-8,7,-3,-1,-6]
# nums = [7,8,3,-7,-9,10]
a = Solution()
b = a.MaxSubSum(nums)
print("233333333333333333")
print(b)