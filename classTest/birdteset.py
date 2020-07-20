class Bird:
    def fly(self):
        raise NotImplementedError

# b = Bird()
# b.fly()

class B(Bird):
    def fly(self):
        print("bird")

# b1 = B()
# b1.fly()

class MyError(Exception):
    def __init__(self, *args, **kwargs):
        print("바보는 나쁜말")
    
    def __str__(self):
        return '허용되지 않은 별명'

def say_nick(nick):
    if nick=='바보':
        raise MyError()
    print(nick)

try:
    say_nick('바보')
except MyError as err:
    print(err)
finally:
    print('프로그램종료')