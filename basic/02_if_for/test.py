import random
import time

operator = ["+","-","/","*"]
cnt = 0
start = time.time()

for i in range(3):
    i1 = random.randint(1,50)
    i2 = random.randint(1,50)
    op = random.choice(operator)
    result = "%d %s %d"%(i1,op,i2)
    inp = int(input(result+" = "))
    if eval(result) == inp:
        cnt = cnt+1
        print("right")
    else:
        print("wrong")

end = time.time()
print("you hit %d times" % cnt)
print("It takes", end-start, "sec")