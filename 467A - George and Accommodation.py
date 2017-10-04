t=input()
count=0
for i in range(t):
	a,b=map(int,raw_input().split(" "))
	if b-a>=2:
		count+=1
print count