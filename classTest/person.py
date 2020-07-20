class Person:
    count = 0 # 클래스 변수
    def __init__(self, name, age=1):
        self.name = name
        self.__age = age # private
        Person.count += 1
        print(self.name + "(" + str(self.__age) + ") is init")

    def work(self, company):
        print(self.name + " is working in " + company)
        self.__getage()

    def sleep(self):
        print(self.name + " is sleeping")

    def __getage(self): # private
        print(self.name + " is " + str(self.__age))

    @classmethod
    def getCount(cls):
        return cls.count

    @classmethod
    def setCount(cls, num):
        cls.count = num


# a = Person('hong')
# b = Person('kim', 20)

# a.work('google')
# b.sleep()

# a._Person__age = 10

# print(a._Person__age)
# print(b._Person__age)

# print()
# print(Person.count)
# print(a.count)
# print(b.count)

# Person.count = 10

# print()
# print(Person.count)
# print(a.count)
# print(b.count)

# a.setCount(15)

# print()
# print(Person.count)
# print(a.count)
# print(b.count)
