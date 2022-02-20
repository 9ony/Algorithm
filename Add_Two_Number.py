def solution():
    answer = []
    i=0
    # input1 = [2,4,3]
    # input2 = [5,6,4]
    input1 = [9,9,9,9,9,9,9]
    input2 = [9,9,9,9]
    output = []
    while len(input1)!=len(input2):
        if len(input1)>len(input2) :
            input2.append(0)
        elif len(input1)<len(input2):
            input1.append(0)
        else :
            continue
    print(input1)
    print(input2)
    while True:
        try:
            check = input1[i] + input2[i]
            # if input1[i+1] is not True:
            #         input1.append(0)
            #         input2.append(0)
            # elif input1[i+1]:
            #     print("input1[i+1]= ",input1[i+1])
            print(check)
            if check>9 :
                check = str(check)
                input1[i+1] = input1[i+1]+int(check[0])
                output.append(int(check[1]))
            else :
                output.append(int(check))
        except IndexError:
            input1.append(0)
            input2.append(0)
        i+=1
        if i>len(input1) and check>9:
            continue
        print(output)
        for i in range(len(output)): 
            i=i+1
            answer.append(str(output[len(output)-i]))
        answer = ''.join(answer)
        return answer

print(solution())