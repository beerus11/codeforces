t=input()
string = raw_input()
s = sum([-1 if i=="A" else 1  for i in list(string)])
if s<0:
    print "Anton"
elif s==0:
    print "Friendship"
else :
    print "Danik"