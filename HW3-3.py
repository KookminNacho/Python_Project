x, y = map(int, input("숫자 두개를 입력하시오").split())
if y > x:
    x, y = y, x
print(x,y)
for i in range(y,x+1):
    print("-------",i,'단---------')
    for j in range(1,10):
        print(i,"*",j,'=',i*j)
print("끝")