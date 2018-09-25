def Multiply():
    m = 0
    temp = 0
    ques = 'N'
    n = int(input("숫자를 입력하시오: "))
    if n < 1 or n  > 99:
        print("숫자가 바르지 않습니다.")
        while n < 1:
            n = int(input("양수를 입력하시오"))
    while temp < 100:
        m += 1
        temp = m * n
        if temp > 100:
            break
        print(temp, end=" ")
    print(" ")
    print(m-1, "회 곱함")
    while ques == "N":
        ques = input("계속하시겠습니까? (Y/N): ").upper()
        if ques == "Y":
            Multiply()
        elif ques == "N":
            print("종료합니다.")
            break
        else:
            print("Y와 N중 하나를 입력하시오")
            print("#에러로 인해 종료합니다.")
Multiply()