import sys

# book={'idx':0,'name':'','pub':'','writter':'','ex':'','stock':0}

def Enrollment(booklist):
    book={}
    while True:
        idx=input("책번호를 입력하세요 >> ")
        if idx.isdecimal():
            idx=int(idx)
            break
        else:
            print("숫자를 입력해주세요")
    name=input("책이름을 입력하세요 >> ")
    pub=input("출판사를 입력하세요 >> ")
    writter=input("저자를 입력하세요 >> ")
    ex=input("책설명을 입력하세요 >> ")
    while True:
        stock=input("재고를 입력해주세여 >> ")
        if stock.isdecimal():
            stock=int(stock)
            break
        else:
            print("숫자를 입력해주세요")

    book['idx']=idx
    book['name']=name
    book['pub']=pub
    book['writter']=writter
    book['ex']=ex
    book['stock']=stock

    booklist.append(book)

    print(booklist)

def Update(booklist):
    book={}
    print("책정보를 수정합니다.")
    idx=int(input("수정할 책번호를 입력하세요 >> "))
    for i in range(0,len(booklist)):
        if booklist[i]['idx']==idx:
            name=input("책이름을 입력하세요 >> ")
            pub=input("출판사를 입력하세요 >> ")
            writter=input("저자를 입력하세요 >> ")
            ex=input("책설명을 입력하세요 >> ")
            stock=int(input("재고를 입력해주세여 >> "))

            book['idx'] = idx
            book['name']=name
            book['pub']=pub
            book['writter']=writter
            book['ex']=ex
            book['stock']=stock

            booklist[i]=book
            break
    print(booklist)

def Delete(booklist):
    idx=int(input("삭제할 책번호를 입력하세요 >> "))
    for i in range(0,len(booklist)):
        if booklist[i]['idx']==idx:
            del booklist[i]
            break

def List(booklist):
    for i in range(0,len(booklist)):
        print(booklist[i])

def Quit():
    print("종료합니다.")
    sys.exit()