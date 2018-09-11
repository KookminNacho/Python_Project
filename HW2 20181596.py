first = int(input("초를 입력하시오"))

#초
if first // 60 >= 1:
    sec = first % 60
    second = first // 60
    temp = second
    #분
    if temp // 60 >= 1:
        minute = temp % 60
        hour = temp // 60
        #시
        if hour // 24 >= 1:
            third = hour % 24
            day = hour // 24
            #일
            print(day, "일", third, "시", minute, "분", sec, "초")
        else:
            third = hour
            print(third,"시간",minute,"분", sec,"초")
    else:
        print(second, "분", sec, "초")
else:
    print(first,"초")
