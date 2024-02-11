def solution(num):
    if num % 2 == 0 :
        answer = "Even"
    elif num % 2 !=0 :
        answer = "Odd"
    elif num == 0 :
        answer = "Even"
    elif num < 0 :
        return
    return answer