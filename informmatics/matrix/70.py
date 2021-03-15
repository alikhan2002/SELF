n=int(input())
l=[]
for i in range(1):
    l=list(map(int,input().split()))
list_adj=[]
if len(l)%2==0:
    for i in range(0,len(l)-1,2):
        list_adj.append(l[i+1])
        list_adj.append(l[i])
else:
     for i in range(0,len(l),2):
        if i==len(l)-1:
            list_adj.append(l[i])
            break
        list_adj.append(l[i+1])
        list_adj.append(l[i])
for i in list_adj:
    print(i,end=" ")
