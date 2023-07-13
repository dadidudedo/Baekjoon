# 에라토스테네스의 체
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
# nums[i] == 0: 방문X
# nums[i] == 1: 방문O
# nums[i] == 2: 소수.
nums = [0] * (N+1)

for i in range(2,N+1):
    if nums[i] == 1:
        continue
    nums[i] = 2
    for j in range(2*i, N+1, i):
        nums[j] = 1

for i in range(M,N+1):
    if nums[i] == 2:
        print(i)