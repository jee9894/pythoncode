str1 = "abcdefgh"
list1 = [1,2,3,4,5,6,]
tuple1 = (1,2,3,4,5,6,)
dic1 = {1:"first", 2:"second"}
set1 = set([1,2,3,4,5,6,])

for i in range(2,10):
    for j in range(1,10):
        print(i, "X", j, "=", i*j)
    print()

for i in range(1,10):
    for j in range(2,10):
        print(j, "X", i, "=", i*j, end='\t')
    print()

a = [1,2,3,4,5]
result = [num*3 for num in a if num % 2 == 0]
print(result)
result=[]

for num in a:
    if num % 2 ==0:
        result.append(num*3)
print(result)