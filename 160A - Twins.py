t=input()
array=map(int,raw_input().split(" "))
array.sort(reverse=True)
count=0
for i in range(len(array)):
	if sum(array[:i])>sum(array[i:]):
		break
	count+=1
print count