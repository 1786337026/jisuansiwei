n=int(input())
vis=[]
prime=[]
def init(n):
    global vis
    for i in range(0, n + 1):
        vis.append(0)
def oula(n):
    global prime,vis
    init(n)
    for i in range(2,n+1):
        if vis[i]==0:
            vis[i]=1
            prime.append(i)
        for j in range(len(prime)):
            if prime[j]*i>n:
                break
            vis[prime[j]*i]=True
            if i%prime[j]==0:
                break

oula(n)
print(prime)