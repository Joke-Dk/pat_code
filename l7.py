K = int(raw_input())

digits = raw_input().split()
digits = [int(x) for x in digits]
cur_sum = 0
ret_sum = -1
cur_left = 0
ret_left = -1
ret_right = -1
for i in range(K):
	if cur_sum<=0:
		cur_sum = digits[i]
		cur_left = i
	else:
		cur_sum += digits[i]
	if ret_sum < cur_sum:
		ret_sum = cur_sum
		ret_left = cur_left
		ret_right = i

if ret_left <0:
	ret_left = 0
	ret_right = K-1
	ret_sum = 0
print ret_sum,digits[ret_left], digits[ret_right]
			
