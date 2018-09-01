n,k=map(int, input().split())
lis=[int(x) for x in input().split()]
temp=0
for i in range(0,n):
    if(lis[i]==k):
        print('yes')
        break
else:
    print('no')
