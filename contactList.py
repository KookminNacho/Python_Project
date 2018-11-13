import pickle

def selectMenu():
    print("--------------------")
    print("1. 친구 리스트 출력")
    print("2. 친구추가")
    print("3. 친구삭제")
    print("4. 이름변경")
    print("5. 번호변경")
    print("9. 종료")
    try:
        selection = int(input("메뉴를 선택하시오: "))
    except:
        print("숫자를 입력해 주세요")
        return 6
    return selection

def readFile():
    try:
        inputfliename = "contact.txt"
        infile = open(inputfliename, 'rb')
        try:
            npdb = pickle.load(infile)
        except:
            print("피클로 불러오기 실패")
            return []
        else:
            print("목록 불러오기 성공")
            return npdb
    except EOFError:
        print("파일 비어있음")
        return []
    except:
        newfile = open(inputfliename, 'w')
        newfile.close()
        print("파일이 존재하지 않아 새로 생성합니다.")
        return []

def writeFile(myList):
    outputfilename = "contact.txt"
    outfile = open(outputfilename,'wb')
    pickle.dump(myList, outfile)
    outfile.close()


print("Welcome to Friend Phone numer Management")

menu = 0
friends = []
friends = readFile()
while menu != 9:
    menu = selectMenu()
    if menu == 1:
        for i in range(len(friends)):
            print(friends[i])
    elif  menu== 2:
        inputstr = input("이름과 번호를 입력하시오: ")
        parse = inputstr.split(" ")
        if len(parse) == 2:
            try:
                pass
            except:
                print("이름에는 글자, 번호에는 숫자만 입력하세요")
            else:
                record = {"이름":str(parse[0]), '번호':str(parse[1])}
                friends += [record]
            print(parse[0],parse[1], "추가되었습니다")
        else:
            print("<이름> <번호>의 형식으로 입력하시오")

    elif  menu == 3:
        deleted = 0
        del_name = input("삭제하고 싶은 이름을 입력하시오:  ")
        for i in friends:
            if i['이름'] == del_name:
                friends.remove(i)
                deleted = 1
            else:
                pass
        if deleted == 1:
            print('삭제 완료.')
        else:
            print("이름이 발견되지 않음")
    elif  menu == 4:
        old_name = input("변경하고 싶은 이름을 입력하시오:  ")
        for i in friends:
            if i['이름'] == old_name:
                try:
                    old_name = str(old_name)
                except:
                    print('올바른 이름을 입력해 주세요')
                else:
                    new_name = input("새로운 이름을 입력하시오: ")
                    i['이름'] = str(new_name)
                    break
        else:
            print("이름이 발견되지 않았음")
    elif menu == 5:
        change_name = input("번호를 바꿀 사용자의 이름을 입력하시오: ")
        for i in friends:
            if i["이름"] == change_name:
                new_number = str(input("새로운 번호를 입력하시오: "))
                i['번호'] = new_number
                print("번호가 "+i['번호']+" 로 변경되었습니다.")
                break
    elif menu == 9:
        writeFile(friends)
        print("프로그램을 종료합니다.")
    elif menu == 6:
        continue
    else:
        print("메뉴에 있는 알맞은 숫자를 입력해 주세요")