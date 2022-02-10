# new_id = ".!D..a@!!r#...k1230-1"
new_id ="=. ="
def solution(new_id):
    answer = ""
    check = []
#1 대문자 >> 소문자
    if new_id.islower() is False:
        new_id = new_id.lower()
#2 특정문자 제거
    for i in range(len(new_id)):
        if new_id[i] == "-" or new_id[i] == "_" or new_id[i] == "." or (ord("z")>=ord(new_id[i])>=ord("a")) or (ord("9")>=ord(new_id[i])>=ord("0")):
            check.append(new_id[i])
    new_id = ''.join(check)
#3 .이반복되면 1개로
    while '..' in new_id:
        new_id = new_id.replace('..','.')
#4 .이 처음에잇으면 삭제
    new_id = new_id.strip('.')
    
#5. new_id가 빈문자열이면 a를 대입
    if new_id == '':
        new_id="a"
#6. 15글자를 넘으면 그뒤에 문자 제거
    if len(new_id)>15:
        new_id=new_id[:15].strip('.')
#7  3글자이하면 마지막 문자 반복해서 3글자될때까지
    while len(new_id) < 3:
        new_id+=new_id[len(new_id)-1]

    answer = new_id
    return answer
print(solution(new_id))
