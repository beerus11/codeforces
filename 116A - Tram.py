t=input()
mx=0
count=0
for i in range(t):
	a,b=map(int,raw_input().split(" "))
	count-=a
	count+=b
	if count>mx:
		mx=count
print mx