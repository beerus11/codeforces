t=input()
string=list(raw_input())
count=0
i=0
while i<len(string)-1 :
	if string[i]==string[i+1]:
		del string[i+1]
		count+=1
	else:
		i+=1
print count
	
	