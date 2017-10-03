string=list(raw_input())
array=["H","Q","9"]
print "YES" if len([True for i in string if i in array])>0 else "NO"
