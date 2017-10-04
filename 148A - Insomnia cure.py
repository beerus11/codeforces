arr=[input(),input(),input(),input()]
t=input()
array=[1]*t
for i in arr:
	j=i
	while (j-1)<len(array):
		array[j-1]=-1
		j+=i
print t-len([i for i in array if i!=-1])