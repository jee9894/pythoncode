# class Cookie:
#     pass
# a = Cookie()
# print(type(a))


class FourCal:
    mode = 1

    def __init__(self, first = 0, second = 0):
        self.first = first
        self.second = second
        print("Constuctor")

    def setData(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result


a = FourCal(2)
b = FourCal(4,7)
c = FourCal()

print(FourCal.mode)
print(a.mode)
print(b.mode)
print(c.mode)
print(id(FourCal.mode))
print(id(a.mode))
print(id(b.mode))
print(id(c.mode))
print()

FourCal.mode = 10
print(FourCal.mode)
print(a.mode)
print(b.mode)
print(c.mode)
print(id(FourCal.mode))
print(id(a.mode))
print(id(b.mode))
print(id(c.mode))
print()

a.mode = 11
print(FourCal.mode)
print(a.mode)
print(b.mode)
print(c.mode)
print(id(FourCal.mode))
print(id(a.mode))
print(id(b.mode))
print(id(c.mode))
print()