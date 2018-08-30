num=int(input())
l=[int(x) for x in input().split()]
sum=0
for i in range(1,num+1):
    sum=sum+i
print(sum//num)
