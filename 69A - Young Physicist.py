t=input()
x=0
y=0
z=0
for i in range(t):
	array=map(int,raw_input().split(" "))
	x+=array[0]
	y+=array[1]
	z+=array[2]
print "YES" if (x==0 and y==0 and z==0) else "NO"
