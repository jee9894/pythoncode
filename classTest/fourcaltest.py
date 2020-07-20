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

    def devide(self):
        result = self.first / self.second
        return result

class MoreFourCal(FourCal):
    def power(self):
        result = self.first ** self.second
        return result

    def devide(self):
        if self.second == 0:
            return 0
        else :
            return super.devide()

cal1 = MoreFourCal(1,4)
cal2 = MoreFourCal(5,0)

print(cal1.add())
print(cal2.devide())
print(cal1.power())
print(cal2.power())