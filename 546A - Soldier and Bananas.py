a,b,c=map(int,raw_input().split(" "))
t=(a*c*(c+1))/2
if b>=t:
	print "0"
else :
	print t-b