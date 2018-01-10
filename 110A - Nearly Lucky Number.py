arr=map(int,list(raw_input()))
ln=0
def isLucky(no):
	return (no.count("4")+no.count("7")==len(no))
for i in arr:
	if i==4 or i==7:
		ln+=1
print "YES" if isLucky(str(ln)) else "NO"