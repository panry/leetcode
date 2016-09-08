def add(a,b):
	if a==~b+1:
		return 0
	carry=1
	while(carry!=0):
		rst=a^b
		carry=(a&b)<<1
		a=rst
		b=carry
	return rst


def gts(a, b):
	if a==(~b+1) and a!=b:
		return 0
	# if c<0:
	# 	b=c
	# if a<0:
	# 	a=c
	while b:
		a = a ^ b
		b = a & b << 1
	print (a)

# gts(-1,1)
# gts(2,-2)
gts(3,-4)
gts(-5,2)