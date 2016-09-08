int guess(int num);

class Solution(object):
	def guessNumber(self, n):
		if guess(n) == 0:
			return n
		int left = 1
		int right = n
		while left < right:
			int mid = left + (right - left) / 2
			t = guess(mid)
			if t == 0:
				return mid
			elif t == 1:
				left = mid
			else right = mid
		return left
		