import re

def Word_Chain():
    s = input("글자를 입력하시오.")
    num = re.findall('\d', s)
    word = re.findall('\D', s)
    print("숫자: ", end="")
    for i in range(len(num)):
        print(num[i], end="")
    print(' ')
    print("문자: ", end="")
    for j in range(len(word)):
        print(word[j], end="")
    print(" ")
    cont = "Y"
    while cont == "Y":
        cont = (input("계속하시겠습니까? Y/N ")).upper()
        if cont == 'Y':
            Word_Chain()
        elif cont == 'N':
            print("STOP")
            break
        else:
            print('다시 입력하십시오.')
            cont = "Y"

Word_Chain()