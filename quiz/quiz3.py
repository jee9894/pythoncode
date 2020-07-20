import sys

class Student:
    def __init__(self):
        self.students = [
            {'stno':1, 'name':'kim', 'major':'computer', 'phone':'010-0000-0000', 'addr':'aaa'},
            {'stno':2, 'name':'lee', 'major':'economy', 'phone':'010-0000-0000', 'addr':'bbb'},
            {'stno':3, 'name':'park', 'major':'philosopy', 'phone':'010-0000-0000', 'addr':'ccc'},
        ]

    def Insert(self):
        print("새 학생정보 입력")
        student = {}
        student['stno'] = int(input("학번을 입력하시오 >> "))
        student['name'] = input("이름를 입력하시오 >> ")
        student['major'] = input("전공을 입력하시오 >> ")
        student['phone'] = input("전화번호를 입력하시오 >> ")
        student['addr'] = input("주소를 입력하시오 >> ")

        self.students.append(student)

    def Update(self):
        print("학생정보 수정")
        stno = int(input("수정할 학번을 입력하시오 >> "))
        for i in range(len(self.students)):
            if self.students[i]['stno'] == stno:
                self.students[i]['name'] = input("수정할 이름를 입력하시오 >> ")
                self.students[i]['major'] = input("수정할 전공을 입력하시오 >> ")
                self.students[i]['phone'] = input("수정할 전화번호를 입력하시오 >> ")
                self.students[i]['addr'] = input("수정할 주소를 입력하시오 >> ")
                break

    def Delete(self):
        print("학생정보 삭제")
        stno = int(input("수정할 학번을 입력하시오 >> "))
        for i in range(len(self.students)):
            if self.students[i]['stno'] == stno:
                del self.students[i]
                break

    def List(self):
        for student in self.students:
            print(student)

    def Quit(self):
        print("프로그램 종료")
        sys.exit()

    def exe(self, choice):
        if choice=="I":        
            self.Insert()

        elif choice=="U": 
            self.Update()
            
        elif choice=='D':
            self.Delete()

        elif choice == 'L':
            self.List()

        elif choice=="Q":
            self.Quit()
    
student = Student()

while True:
    choice=input('''
다음 중에서 하실 일을 골라주세요
I - 학생 정보 입력
U - 학생 정보 수정
D - 학생 정보 삭제
L - 학생 정보 목록
Q - 프로그램 종료
>>> ''').upper()
    student.exe(choice)
    

