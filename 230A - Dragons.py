a,b = map(int,raw_input().split(" "))
count=0
for i in range(b):
	x,y= sorted(map(int,raw_input().split(" ")))
	if a> x:
		a+=y
	else:
		break
	count+=1
print "YES" if count ==b else "NO"