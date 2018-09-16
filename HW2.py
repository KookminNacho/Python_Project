import random
lefthand = input("왼손의 (가위, 바위, 보)중에서 하나를 선택하시오: ")
righthand = input("오른손의 (가위, 바위, 보)중에서 하나를 선택하시오: ")

finalhand = []

print("-----------------------------------------")
print("사용자의 왼손: ", lefthand)
print("사용자의 오른손: ",righthand)

handnumber = ["가위","바위","보"]

random.shuffle(handnumber)
comleft = handnumber[0]
comright = handnumber[1]
print("컴퓨터의 왼손: ",comleft)
print("컴퓨터의 오른손: ",comright)

comhand = random.choice([True,False])

comcom = []

if comhand == True:
    comcom.append(comleft)
else:
    comcom.append(comright)

print("--------------------------------------")

byehand = input("뺄 손을 고르시오(오른손 왼손): ")
if byehand == "오른손":
    finalhand.append(lefthand)
elif byehand == "왼손":
    finalhand.append(righthand)
else:
    print("오른손, 왼손 둘중에 하나만 가능")

match = (finalhand[0],comcom[0])
ans = (match[0]+" "+match[1])
print("-------------------------------------")
print("사용자의 손: "+finalhand[0])
print("컴퓨터의 손: "+comcom[0])

if ans == "가위 바위":
    print("졌습니다.")
elif ans == "보 가위":
    print("졌습니다.")
elif ans == "바위 보":
    print("졌습니다.")
elif ans == "보 바위":
    print("이겼습니다.")
elif ans == "가위 보":
    print("이겼습니다.")
elif ans == "바위 가위":
    print("이겼습니다.")
elif ans == "바위 바위":
    print("비겼습니다.")
elif ans == "보 보":
    print("비겼습니다.")
elif ans == "가위 가위":
    print("비겼습니다.")