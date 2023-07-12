import sys
input = sys.stdin.readline

# 실패코드: 나눗셈을 여러번 할수록 오차가 커져??
# def nCr(n, r):
#     ans = 1
#     for _ in range(r):
#         ans = ans * n / r
#         n -= 1
#         r -= 1
#     return int(ans)

def nCr(n, r):
    tmp1 = 1
    tmp2 = 1
    for i in range(1, r+1):
        tmp1 *= n
        tmp2 *= i
        n -= 1
    return tmp1//tmp2


test = int(input())
for _ in range(test):
    N, M = map(int, input().split())
    print(nCr(M, N))