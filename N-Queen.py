def promising(queen, n , x):
    cnt = 0
    if n == x :
        return 1

    for i in range(n):
        queen[x] = i

        for pos in range(x):
            if queen[x] == queen[pos] :
                break
            if abs(queen[pos] - queen[x]) == (x - pos):
                break
        else:
            cnt += promising(queen, n, x + 1)

    return cnt


def solution(n):
    queen = [0] * n
    return promising(queen, n, 0)

print(solution(4))