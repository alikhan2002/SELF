n=int(input())
l=[]
for i in range(1):
    l=list(map(int,input().split()))
sum=0
for i in range(1,len(l)-1):
    if(l[i]>l[i-1] and l[i]>l[i+1]):
        sum+=1
print(sum)