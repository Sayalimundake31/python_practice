for i in range (10):
    print(i)


for i in range (1,12,1):
    print(i)

a=range(5)
for i in a:
    print(i)


for i in range (10,0,-1):
    print(i)


for i in range (33,60,2):
    print(i)


st="welcome to pune"
n=len(st)
for i in range (n):
    print(i,"=",st[i])

st = "this is python class 10 times"
n = len(st)
for i in range(n):
    print(i,"=",st[i])

st = "this is python class"
for i in range(10):
     print(st)


for i in range(111,900):
    if i%3==0 and i%5==0 and i%7==0:
        print(i,end=" ")


num=int(input("enter the given no"))
for i in range (1,24):
    print(num*i)