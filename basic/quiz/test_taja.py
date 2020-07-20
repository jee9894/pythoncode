import random
import time
import pickle
import json

# words = [
#     "김말이","선생님","대한민국","능지처참","파이썬","프로그래밍",
#     "빅파이","컴퓨터","마우스","아파트","산울림","햄버거","다이어리",
#     "바밤바","세종실록지리지","6월민주항쟁","민주주의","자본주의",
#     "양자역학","소고기","타로카드","대구광역시","서울특별시","타자게임",
#     ]

words = []
ranking = []
count = 0
while True:
    print("""   
    1.타자게임 
    2.문제불러오기 
    3.문제저장하기 
    4.단어 등록, 수정, 삭제 
    5.순위 
    6.종료하기"""
    )
    menu = input("메뉴를 선택하세요 >> ")
    if menu == '1':
        if not words:
            print("문제를 먼저 불러와주세요")
            continue
        count = 0
        input("엔터를 눌러서 게임 시작")
        start = time.time()
        while count < 3:
            sel = random.choice(words)
            while True:
                print(sel)
                res = input(">>>")
                if sel == res:
                    print("정답!")
                    count += 1
                    break
                else:
                    print("오답! 다시하세요")
        end = time.time()
        totalTime = end - start
        print("걸린시간 : {:.2f}s".format(totalTime))

        name = input("순위 등록을 위해 이름을 입력하세요 >> ")

        with open("./basic/quiz/ranking.pickle", "rb") as f:
            try:
                ranking = pickle.load(f)
            except EOFError:
                ranking = []

        with open("./basic/quiz/ranking.pickle", "wb") as f:
            temp = {
                'name': name,
                'time': totalTime
            }
            ranking.append(temp)
            pickle.dump(ranking, f)

    if menu == '2':
        with open("./basic/quiz/words.pickle", "rb") as f:
            words = pickle.load(f)
        print("문제를 불러왔습니다")

    if menu == '3':
        with open("./basic/quiz/words.pickle", "wb") as f:
            pickle.dump(words, f)
        print("문제를 저장했습니다")

    if menu == '4':
        print(words)
        print("1.등록, 2.수정, 3.삭제")
        sel = input("입력하세요 >> ")
        if sel == '1':
            words.append(input("추가할 단어를 입력하세요"))

        elif sel == '2':
            word = input("수정할 단어를 입력하세요")
            if word in words:
                i = words.index(word)
                words[i] = input("바꿀 단어를 입력하세요")
            else :
                print("해당 단어가 없습니다")

        elif sel == '3':
            word = input("삭제할 단어를 입력하세요")
            if word in words:
                words.remove(word)
            else :
                print("해당 단어가 없습니다")
        else:
            print("메뉴를 잘못 입력하셨습니다")

    if menu == '5':
        with open("./basic/quiz/ranking.pickle", "rb") as f:
            temp = pickle.load(f)
            temp.sort(key=lambda x : x.get('time'))
            i = 1
            for li in temp:
                print("%d위" % i)
                print("이름 : %s" % li['name'])
                print("시간 : %.2fs" % li['time'])
                print()
                i += 1

    if menu == '6':
        print("종료합니다")
        break
