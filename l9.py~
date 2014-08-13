l1 = raw_input().split()
p1 = [[int(x) for x in l1[1::2]] ,[float(x) for x in l1[2::2]]]
# print p1
l2 = raw_input().split()
p2 = [[int(x) for x in l2[1::2]] ,[float(x) for x in l2[2::2]]]
# print p2

dict1 = {}
for i in range(len(p1[0])):
	for j in range(len(p2[0])):
		product_digit0 = p1[0][i]+p2[0][j]
		product_digit1 = p1[1][i]*p2[1][j]
		if product_digit0 in dict1.keys():
			dict1[product_digit0] += product_digit1
			if dict1[product_digit0] == 0:
				del dict1[product_digit0]
		else:
			dict1[product_digit0] = product_digit1

print len(dict1),
items = dict1.keys()
items.sort()
for item in reversed(items):
	print "%d %.1f" %(item, dict1[item]),
