# growingPlant
def solution(upSpeed, downSpeed, desiredHeight):
    day = 1
    res = 0
    while res < desiredHeight:
        res = upSpeed * day - downSpeed * (day - 1)
        day += 1
    return day -1


# Knapsack Light
def solution(v1, w1, v2, w2, maxW):
    if w1 + w2 <= maxW:
        return v1+v2
    elif w1 + w2 > maxW and w1 <= maxW and w2<=maxW:
        return max(v1, v2)
    elif w1 > maxW and w2 <= maxW:
        return v2
    elif w2 > maxW and w1 <= maxW:
        return v1
    else:
        return 0


# Bishop and Pawn
def solution(bishop, pawn):
    a = bishop[0]
    b = bishop[1]
    c = pawn[0]
    d = pawn[1]

    return abs(ord(a) - ord(c)) == abs(ord(b) - ord(d))


# buildPalindrome
def solution(st):
    if st == st[::-1]:
        return st
    else:
        st = solution(st[0]) + solution(st[1:]) + solution(st[0])
        return st


# chessKnight
def solution(cell):
    row = ord(cell[1]) - ord('0')
    column = ord(cell[0]) - ord('a') + 1
    steps = [
            [-2, -1], [-1, -2], [1, -2], [2, -1],
            [2, 1], [1, 2], [-1, 2], [-2, 1]
            ]
    answer = 0

    for i in range(8):
        tmpRow = row + steps[i][0]
        tmpColumn =  column + steps[i][1]
        if (tmpRow >= 1 and tmpRow <= 8 and
            tmpColumn >= 1 and tmpColumn <= 8):
            answer += 1

    return answer


# longestWord
import re
def solution(text):
    l = re.findall('[a-zA-Z]+', text)
    return max(l, key= lambda x: len(x))
    #return max(re.split('[^a-zA-Z]', text), key=len)



