K = int(raw_input())

digits = raw_input().split()
digits = [int(x) for x in digits]
sum0 = sum(digits)
sum_left = [0]*K
sum_left[0] = digits[0]
sum_right = [0]*K
sum_right[K-1] = digits[K-1]
for i in range(K-1):
	sum_left[i+1] = sum_left[i] + digits[i+1]
	sum_right[K-2-i] = sum_right[K-1-i] + digits[K-2-i]

print sum_left,"\n", sum_right
cur_min_left = 0
cur_sum = -5000
cur_index_left = -1
cur_index_right = -1
for i in range(K):
	if cur_min_left > sum_left[i]:
		cur_min_left = sum_left[i]
		cur_min_right = min(sum_right[i:])
		if cur_sum > cur_min_left+cur_min_right:
			cur_sum = cur_min_left+cur_min_right
			cur_index_left = 

print sum0-cur_sum,
			
