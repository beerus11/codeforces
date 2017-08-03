t=input()
array=map(int,raw_input().split(" "))
cnt=[0]*100005
dp=[0]*100005
for k,v in enumerate(array):
	cnt[v]+=1
dp[0]=0
dp[1]=cnt[1]
for j in range(2,100001):
	dp[j]=max(dp[j-1],dp[j-2]+cnt[j]*j)
print dp[100000]