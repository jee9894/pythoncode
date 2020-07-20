# 숫자를 입력받아서 짝수인지 홀수인지 판별한다
number = input("input number >>")

if number.isdecimal() == True:
    number = int(number)
    if number % 2 == 0:
        print("your number is even number")
    else:
        print("your number is odd number")
else:
    print("your input is not number")