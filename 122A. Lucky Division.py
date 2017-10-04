luck_no=[4,7,44,47,74,77,444,447,474,477,744,747,774,777]
t=input()
if t in luck_no or len(filter(lambda x: (t%x==0),luck_no))>0:
	print "YES"
else:
	print "NO"