import pickle

f = open("input.txt", "rb")
lines = pickle.load(f)
f.close()

menu = 0
friends = {}
friends.update(lines)
while menu != 9:
    print("--------------------")
    print("1. 친구 리스트 출력")
    print("2. 친구추가")
    print("3. 친구삭제")
    print("4. 이름변경")
    print("5. 연락처변경")
    print("9. 종료")

    try:
        menu = int(input("메뉴를 선택하시오: "))

        if menu == 1:
            print(friends)
        elif menu == 2:
            name = input("이름을 입력하시오: ")
            number = int(input("연락처를 입력하시오: "))
            friends[name] = number
        elif menu == 3:
            del_name = input("삭제하고 싶은 이름을 입력하시오:  ")
            if del_name in friends:
                friends.pop(del_name)
            else:
                print("이름이 발견되지 않았음")
        elif menu == 4:
            old_name = input("변경하고 싶은 이름을 입력하시오: ")
            if old_name in friends:
                new_name = input("새로운 이름을 입력하시오: ")
                friends[new_name] = friends.get(old_name)
                friends.pop(old_name)
            else:
                print("이름이 발견되지 않았음")
        elif menu == 5:
            old_name = input("연락처를 변경하고 싶은 이름을 입력하시오: ")
            if old_name in friends:
                new_number = int(input("새로운 연락처를 입력하시오: "))
                new_name = old_name
                friends.pop(old_name)
                friends[new_name] = new_number
            else:
                print("이름이 발견되지 않았음")

    except ValueError as e:
        print("잘못된 값!")

print("종료!")

f = open("input.txt", "wb")
pickle.dump(friends, f)
f.close()



