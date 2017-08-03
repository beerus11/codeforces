n,m=map(int,raw_input().split(" "))
arr=map(int,raw_input().split(" "))
diff=10000
arr.sort()
for k,v in enumerate(arr):
	if k+n-1<len(arr) and arr[k+n-1]-arr[k]<diff:
		diff=arr[k+n-1]-arr[k]
print diff