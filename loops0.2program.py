for i in range(50,150):
    if i%5==0:
        print(i,end="\t")


st_range=1
end_range=20
print("even number in range{}to{}:")
for num in range(st_range,end_range+1):
    if num%2==0:
        print(num)


number=[1,2,3,4,5]
sum_result=0
for num in number:
    sum_result+=num
    print("sum of no in list:",sum_result)


rows=5
print("pattern:")
for i in range (1,rows+1):
    for j in range(1,i+1):
        print("*", end=" ")
    print()