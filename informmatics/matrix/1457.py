n=int(input())
l=list(map(int,input().split()))
p=[]
for i in range(1,l[0]):
    p.append(i)
for i in range(0,len(l)-1,2):
    a=[]
    for j in range(l[i],l[i+1]+1):
        a.append(j)
    a.reverse()
    for k in a:
        p.append(k)
print(p)