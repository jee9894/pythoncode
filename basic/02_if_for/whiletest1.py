prompt = '''-------------------------
   coffee machine menu
-------------------------
    1. add coffee menu
    2. delete coffee menu 
    3. coffee menu select
    4. coffee menu list
    5. exit
-------------------------
    select menu >> '''

dic = {'americano':2000}

while True:
    print(prompt, end='')
    menu = input()
    if menu == '1':
        key = input("input menu title >> ")
        value = int(input("input menu price >> "))
        dic[key] = value
    elif menu == '2':
        key = input("input menu title you wanna delete >> ")
        del dic[key]
    elif menu == '3':
        sel = input("input menu you want to >> ")
        # if sel not in dic:
        if dic.get(sel) is None:
            print("%s is not in our menu list" % sel)
            continue    
        money = int(input("input money >> "))
        if money >= dic[sel]:
            print("here is %s you odered" % sel)
            print("here is change : ", money - dic[sel])
        else :
            print("you don't pay enough money")
    elif menu == '4':
        for k, v in dic.items(): 
            print("name : %s, price : %d" % (k, v))
    else:
        print("exit program")
        break
