t=input()
string=raw_input().lower()
if t >=26 and all([1 if chr(97+i) in string else 0 for i in range(26)]):
	print "YES"
else :
	print "NO"
