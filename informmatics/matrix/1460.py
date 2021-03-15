n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
m=int(input())
if(m>0):
    l[m-1] = l[-1:-1]
print(l)