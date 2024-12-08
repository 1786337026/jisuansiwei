n=int(input("输入数据数量：n"))
a=[0]
for i in range(1,n+1):
    k=int(input())
    a.append(k)
for i in range(1,n+1):
    for j in range(n,i,-1):
        if a[j-1]>a[j]:
            a[j-1],a[j] = a[j],a[j-1]
print(a)
