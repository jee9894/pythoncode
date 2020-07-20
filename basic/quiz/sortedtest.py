sorted("hello")

sorted([5,2,1,3,4])
sorted([[2,1,3],[3,2,1],[1,2,3],[1,2,4]])

sorted({3,2,1})

sorted((3,2,1))

sorted({3:1,2:3,1:4})

myDic = {3:5, 2:3, 1:4, 100:1, 20:6, 80:2}

sorted(myDic.items(), key=lambda x : x[1])

temp = (5,3)
temp[2]

sorted(['hello', 'world', 'python'], key=lambda x: x[3], reverse=True)
