import re
import sys

class Customer:
    def __init__(self):
        self.custlist = [
            {'name': 'aaa', 'gender': 'M',
                'email': 'aaaaa@aaaaa.aaa', 'birthyear': 2000},
            {'name': 'bbb', 'gender': 'M',
                'email': 'bbbbb@bbbbb.bbb', 'birthyear': 2000},
            {'name': 'ccc', 'gender': 'F',
                'email': 'ccccc@cccc.ccc', 'birthyear': 2000},
            {'name': 'ddd', 'gender': 'F',
                'email': 'ddddd@ddddd.ddd', 'birthyear': 2000},
        ]
        self.page = 3

    def insertData(self):
        print("고객 정보 입력")
        customer_dic = {}
        customer_dic['name'] = input("이름을 입력하세요 >> ")

        while True:
            gender = input("성별을 입력하세요(m,M,f,F) >> ")
            if gender == 'm' or gender == 'M' or gender == 'f' or gender == 'F':
                gender = gender.upper()
                customer_dic['gender'] = gender
                break
            else:
                print("잘못 입력하셨습니다")

        while True:
            email = input("이메일을 입력하세요 >> ")
            check = 0
            for temp in self.custlist:
                if temp['email'] == email:
                    check = 1
            if check == 0:
                p = re.compile('[a-z][a-zA-Z0-9]{4,}@[a-z]{2,}[.][a-z]{2,}')
                if p.match(email):
                    customer_dic['email'] = email
                    break
                else:
                    print("이메일 형식이 일치하지 않습니다")
            else:
                print("중복된 이메일이 있습니다")
        while True:
            birthyear = input("출생연도를 입력하세요(4자리숫자) >> ")
            if len(birthyear) == 4 and birthyear.isdecimal():
                customer_dic['birthyear'] = int(birthyear)
                break
            else:
                print("잘못 입력하셨습니다")

        self.custlist.append(customer_dic)
        self.page += 1  # page = page + 1

        # return self.page

    def curSearch(self):
        print("현재 고객 정보 조회")
        if self.page >= 0:
            print("현재 페이지는 {}쪽 입니다".format(self.page + 1))
            customer = self.custlist[self.page]
            print("이름 : %s" % customer['name'])
            print("성별 : %s" % customer['gender'])
            print("이메일 : %s" % customer['email'])
            print("출생연도 : %d" % customer['birthyear'])
        else:
            print("입력된 정보가 없습니다")

    def preSearch(self):
        print("이전 고객 정보 조회")
        if self.page <= 0:
            print("첫 번 째 페이지 이므로 이전 페이지로 이동이 불가합니다")
            self.page = 0
        else:
            self.page -= 1
        print("현재 페이지는 {}쪽 입니다".format(self.page + 1))
        customer = self.custlist[self.page]
        print("이름 : %s" % customer['name'])
        print("성별 : %s" % customer['gender'])
        print("이메일 : %s" % customer['email'])
        print("출생연도 : %d" % customer['birthyear'])

        # return self.page

    def nextSearch(self):
        print("다음 고객 정보 조회")
        if self.page >= len(self.custlist) - 1:
            print("마지막 페이지 이므로 다음 페이지로 이동이 불가합니다")
            self.page = len(self.custlist) - 1
        else:
            self.page += 1
        print("현재 페이지는 {}쪽 입니다".format(self.page + 1))
        customer = self.custlist[self.page]
        print("이름 : %s" % customer['name'])
        print("성별 : %s" % customer['gender'])
        print("이메일 : %s" % customer['email'])
        print("출생연도 : %d" % customer['birthyear'])

        # return self.page

    def deleteData(self):
        print("고객 정보 삭제")
        delok = 0
        email = input("삭제할 이메일을 입력하세요 >> ")
        for temp in self.custlist:
            if temp['email'] == email:
                print("{} 고객님의 정보가 삭제 되었습니다".format(temp['name']))
                self.custlist.remove(temp)
                if self.page >= len(self.custlist) - 1:
                    self.page = len(self.custlist) - 1
                delok = 1
                break
        if delok == 0:
            print("일치하는 이메일이 없습니다")

        # return self.page

    def updateData(self):
        print("고객 정보 수정")
        idx = -1
        email = input("수정할 이메일을 입력하세요 >> ")
        for i in range(len(self.custlist)):
            if self.custlist[i]['email'] == email:
                idx = i
                break
        if idx == -1:
            print("일치하는 이메일이 없습니다")
        else:
            name = input("수정할 이름을 입력하세요 >> ")
            if name == "exit":
                name = self.custlist[idx]['name']
            gender = input("수정할 성별을 입력하세요 >> ")
            if gender == "exit":
                gender = self.custlist[idx]['gender']
            email = input("수정할 이메일을 입력하세요 >> ")
            if email == "exit":
                email = self.custlist[idx]['email']
            birthyear = input("수정할 출생년도를 입력하세요 >> ")
            if birthyear == "exit":
                birthyear = self.custlist[idx]['birthyear']

            self.custlist[idx]['name'] = name
            self.custlist[idx]['email'] = email
            self.custlist[idx]['gender'] = gender
            self.custlist[idx]['birthyear'] = birthyear

    def quit(self):
        print("프로그램 종료")
        sys.exit()

    def exe(self, choice):
        if choice == 'I':
            self.insertData()

        elif choice == 'C':
            self.curSearch()

        elif choice == 'P':
            self.preSearch()

        elif choice == 'N':
            self.nextSearch()

        elif choice == 'U':
            self.updateData()

        elif choice == 'D':
            self.deleteData()

        elif choice == 'Q':
            self.quit()


customer = Customer()

while True:
    choice = input('''
다음 중에서 하실 일을 골라주세요
I - 고객 정보 입력
C - 현재 고객 정보 조회
P - 이전 고객 정보 조회
N - 다음 고객 정보 조회
U - 고객 정보 수정
D - 고객 정보 삭제
Q - 프로그램 종료
>>>''').upper()

    customer.exe(choice)
