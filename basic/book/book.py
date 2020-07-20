import sys

# book={'idx':0,'name':'','pub':'','writter':'','ex':'','stock':0}
class Book:
    def __init__(self):
        self.booklist=[
                {'idx':1,'name':'a','pub':'d','writter':'o','ex':'x','stock':1},
                {'idx':2,'name':'b','pub':'e','writter':'p','ex':'y','stock':1},
                {'idx':3,'name':'c','pub':'f','writter':'q','ex':'z','stock':1},
        ]

    def Enrollment(self):
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

        self.booklist.append(book)

        print(self.booklist)

    def Update(self):
        book={}
        print("책정보를 수정합니다.")
        idx=int(input("수정할 책번호를 입력하세요 >> "))
        for i in range(0,len(self.booklist)):
            if self.booklist[i]['idx']==idx:
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

                self.booklist[i]=book
                break
        print(self.booklist)

    def Delete(self):
        idx=int(input("삭제할 책번호를 입력하세요 >> "))
        for i in range(0,len(self.booklist)):
            if self.booklist[i]['idx']==idx:
                del self.booklist[i]
                break

    def List(self):
        for i in range(0,len(self.booklist)):
            print(self.booklist[i])

    def Quit(self):
        print("종료합니다.")
        sys.exit()

    def exe(self, menu):
        if menu=='1':
            self.Enrollment()

        elif menu=='2':
            self.Update()

        elif menu=='3':
            self.Delete()

        elif menu=='4':
            self.List()

        elif menu=='5':
            self.Quit()


book = Book()

while True:
    menu=input('''
    1. 책등록
    2. 수정
    3. 삭제
    4. 목록
    5. 종료
    ''')

    book.exe(menu)
