# 1. 학생정보를 list자료형에 입력, 수정, 삭제, 리스트로 출력하는 기능을 구현하시오
#  한 학생의 정보는 학번, 이름, 학과, 전화번호, 주소를 가진다. 

students = [
    {'stno':1, 'name':'kim', 'major':'computer', 'phone':'010-0000-0000', 'addr':'aaa'},
    {'stno':2, 'name':'lee', 'major':'economy', 'phone':'010-0000-0000', 'addr':'bbb'},
    {'stno':3, 'name':'park', 'major':'philosopy', 'phone':'010-0000-0000', 'addr':'ccc'},
]

while True:
    choice=input('''
다음 중에서 하실 일을 골라주세요
I - 학생 정보 입력
U - 학생 정보 수정
D - 학생 정보 삭제
L - 학생 정보 목록
Q - 프로그램 종료
>>> ''').upper()

    if choice=="I":        
        print("새 학생정보 입력")
        student = {}
        student['stno'] = int(input("학번을 입력하시오 >> "))
        student['name'] = input("이름를 입력하시오 >> ")
        student['major'] = input("전공을 입력하시오 >> ")
        student['phone'] = input("전화번호를 입력하시오 >> ")
        student['addr'] = input("주소를 입력하시오 >> ")

        students.append(student)

    elif choice=="U": 
        print("학생정보 수정")
        stno = int(input("수정할 학번을 입력하시오 >> "))
        for i in range(len(students)):
            if students[i]['stno'] == stno:
                students[i]['name'] = input("수정할 이름를 입력하시오 >> ")
                students[i]['major'] = input("수정할 전공을 입력하시오 >> ")
                students[i]['phone'] = input("수정할 전화번호를 입력하시오 >> ")
                students[i]['addr'] = input("수정할 주소를 입력하시오 >> ")
                break
        
    elif choice=='D':
        print("학생정보 삭제")
        stno = int(input("수정할 학번을 입력하시오 >> "))
        for i in range(len(students)):
            if students[i]['stno'] == stno:
                del students[i]
                break

    elif choice == 'L':
        for student in students:
            print(student)

    elif choice=="Q":
        print("프로그램 종료")
        break
    

