def fun(array):
    mx=0
    t=0
    for i in range(0,len(array)-1):
        if array[i+1]>=array[i]:
            t+=1
        else:
            t=0
        mx=max(t,mx)
    return mx+1

input()
l=map(int,raw_input().strip().split(" "))
print fun(l) 