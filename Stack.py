index = []
z=1
while True:
    i = input("엔터만 누르면 입력종료")
    if i is not "":
        index.append(i)
    else:
        print(index)
        break
for j in range(len(index)):
    print(index[len(index)-z])
    z+=1