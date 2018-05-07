string = raw_input()
pos = string.find("AB")
if pos >= 0:
	str1 = string.replace("AB","",1)
	if str1.find("BA") >=0:
		print "YES"
	else:
		print "NO"
else :
	print "NO"
