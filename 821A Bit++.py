t=input()
q=0
for i in range(0,t):
	if "++" in raw_input().strip():
		q+=1
	else:
		q-=1
print q
	