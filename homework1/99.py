a=[[i*j for j in range(10)] for i in range(10)]
for i in range(1,10):
    a[0][i]=i
for i in range(1,10):
    a[i][0]=i
for i in range(0,10):
    for j in range(0,10):
        if i==0 and j==0:
            print('{0:<5}'.format(''),end='')
            continue
        if i<=j or i==0 or j==0:
            print('{0:<5}'.format(a[i][j]), end='')
        else :
            print('{0:<5}'.format(""), end='')
    print("")