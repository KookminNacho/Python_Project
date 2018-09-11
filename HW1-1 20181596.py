import turtle

Myturtle = turtle
color_list = ["RED","ORANGE","YELLOW","GREEN","CYAN","BLUE","PURPLE","BLACK"]
#펜 위치, 두께 설정
Myturtle.width(3)
Myturtle.speed(15)
Myturtle.penup()
Myturtle.setposition(0,-100)
Myturtle.pendown()
#원 그리기 시작.
for i in range(12):
    Myturtle.forward(30)
    Myturtle.right(30)
    Myturtle.color("BLUE")
    Myturtle.circle(50)
    Myturtle.color("RED")
    Myturtle.circle(30)
    Myturtle.color("CYAN")
    Myturtle.circle(20)
    Myturtle.color("GREEN")
    Myturtle.circle(10)
    Myturtle.color("YELLOW")
    Myturtle.circle(5)
    Myturtle.color("BLACK")
    Myturtle.forward(50)
    #작은 원 그리기 시작
    for j in range(8):
        Myturtle.color(color_list[j])
        Myturtle.right(45)
        Myturtle.forward(5)
        Myturtle.circle(10)
        Myturtle.forward(10)
#첫번째 그림 끝, 다음 그림 준비
Myturtle.penup()
Myturtle.setposition(0,100)
Myturtle.pendown()
Myturtle.left(35)
Myturtle.color("RED")
#두번재 그림 그리기 시작
for k in range(10):
    Myturtle.circle(200,100)
    Myturtle.right(280)
    Myturtle.circle(200,100)
    Myturtle.circle(10)
#그림이 바로 꺼지는 것을 방지하기 위해 투명한 원 100바퀴 그리기
Myturtle.color("BLACK")
Myturtle.penup()
for l in range(100):
    Myturtle.circle(10)




