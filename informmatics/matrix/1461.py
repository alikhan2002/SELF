l=list(map(int,input().split()))
res=0
N=len(l)
for i in range(len(l)-2):
    R=i+1
    L=i
    while(l[R]==l[L]):
        cnt=2
        while((L-1 >= 0) and (l[L] == l[R])): 
            cnt+=1
            L-=1
        while((R+1<N ) and (l[R] == l[L+1])):
            cnt+=1
            R+=1
        if(cnt < 3): 
            break
        res += cnt
    if(res):
        print(res)
        exit()
print(0)

