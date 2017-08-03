n,a,b,c=map(int,raw_input().split(" "))
cuts=[a,b,c]
cuts.sort()
inf=2**64
dp=[-inf]*(n+1)
if n>=cuts[0]:
	dp[cuts[0]]=1
if n>=cuts[1]:
	dp[cuts[1]]=1
if n>=cuts[2]:
	dp[cuts[2]]=1
for i in range(n+1):
	for k in cuts:
		if i>k :
			dp[i]=max(dp[i-k]+dp[k],dp[i])
print dp[n]