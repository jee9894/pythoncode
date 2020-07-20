# FileNotFoundError:
# f=open("./classTest/text.txt", "r")

# ZeroDivisionError:
# 3/0

# IndexError:
# li = [2,3,4]
# li[100]

try:
    # f=open("./classTest/text.txt", "r")
    # li = [2,3,4]
    # li[100]
    3/0
except IndexError as err:
    print(err)
except ZeroDivisionError as err:
    print(err)
except FileNotFoundError as err:
    print(err)
finally:
    print("finally")