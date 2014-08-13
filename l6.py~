K = int(raw_input())

def compare_time(x, y):
	time_x = x.split(':')
	time_y = y.split(':')
	for i in range(3):
		if time_x[i] != time_y[i]:
			return int(time_x[i])>int(time_y[i])
	
time_start = ["24:00:00","none"]
time_end = ["00:00:00","none"]
for i in range(K):
	list1 = raw_input().split()
	if( compare_time( time_start[0], list1[1])):
		time_start[0:2] = list1[1::-1]
	if( not compare_time( time_end[0], list1[2])):
		time_end[0:2] = list1[2::-2]

# debug
#print "start: ",time_start[0],time_start[1]
#print "  end: ",time_end[0],time_end[1]

print time_start[1],time_end[1]
