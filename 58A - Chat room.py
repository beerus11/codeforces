string=list(raw_input())
check=['o','l','l','e','h']
i=0
while i < len(string) and len(check)>0 :
	if string[i]==check[-1]:
		check.pop()
	i+=1
	
print "YES" if len(check)==0 else "NO"