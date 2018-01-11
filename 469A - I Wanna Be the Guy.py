t=input()
l1=map(int,raw_input().split(" ")[1:])
l2=map(int,raw_input().split(" ")[1:])
l1.extend(l2)
print "I become the guy." if len(set(l1))==t else "Oh, my keyboard!"