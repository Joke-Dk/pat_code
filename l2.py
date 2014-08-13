dict1 = {};
for i in range(2):
	list1 = raw_input().split()
	for j in range(int(list1[0])):
		temp_int   = 	int(list1[2*j+1])
		temp_float = 	float(list1[2*j+2])
		if temp_int in dict1.keys():
			dict1[temp_int] += temp_float
			if dict1[temp_int] == 0:
				del(dict1[temp_int])
		else:
			dict1[temp_int] = temp_float

print len(dict1),
items = dict1.keys()
items.sort()
for item in reversed(items):
	print "%d %.1f" %(item, dict1[item]),
