t=input()
array=list(raw_input())
s_count=0
f_count=0
for i in range(len(array)-1):
	if array[i]!=array[i+1]:
		if array[i+1]=="S":
			s_count+=1
		elif array[i+1]=="F" :
			f_count+=1
print "YES" if f_count>s_count else "NO"
	