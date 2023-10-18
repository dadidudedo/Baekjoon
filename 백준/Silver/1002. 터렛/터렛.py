from math import sqrt

def sumOfPow(x1, y1, x2, y2):
    return (x1-x2)**2 + (y1-y2)**2

T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)
        continue

    disPow = sumOfPow(x1, y1, x2, y2)
    radiusSumPow = (r1+r2) ** 2
    radiusDifPow = (r1-r2) ** 2

    if disPow < radiusSumPow:
        if disPow > radiusDifPow:
            print(2)
        elif disPow < radiusDifPow:
            print(0)
        else:
            print(1)
    elif disPow > radiusSumPow:
        print(0)
    else:
        print(1)
