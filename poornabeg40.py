X= int(input())
n1=1
n2=1
count=0
while count<X:
    print(n1,end=(' '))
    nth=n1+n2
    n1=n2
    n2=nth
    count+=1
