import time

input("엔터를 누르고 10초를 셉니다")
start = time.time()
input("10초후에 다시 엔터를 누릅니다")
end = time.time()
et = end - start
print("실제 시간 : ", et)
print("차이 : ", abs(et-10))