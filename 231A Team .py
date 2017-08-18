t=input()
q=0
for i in range(0,t):
	if sum(map(int,raw_input().strip().split(" ")))>=2:
		q+=1
print q
	