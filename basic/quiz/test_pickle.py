import pickle

data = {1:'python', 2:'you need'}


with open("./basic/quiz/test.pickle", "wb") as f:
    pickle.dump(data, f)

with open("./basic/quiz/test.pickle", "rb") as f:
    data = pickle.load(f)
    print(type(data))
    print(data)