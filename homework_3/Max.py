n=int(input())
a=[]
def Max (num):
    max=0
    for i in range(num):
        if i>max:
            max=i

for i in range(n):
    t=int(input())
    a.append(t)
print(max(a))