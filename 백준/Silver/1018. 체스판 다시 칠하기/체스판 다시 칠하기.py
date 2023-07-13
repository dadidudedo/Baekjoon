# board의 가장 좌측 상단에 8*8 영역을 초기값으로 하여
# 한 칸씩 옮겨가며 가장 적은 횟수를 찾을 것.
# 시간제한이 2초이기 때문에, 4중 반복문을 써도 된다.

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [[] for _ in range(N)]
for i in range(N):
    board[i] = list(input())

# 초기값 세팅
cnt = 0
ans = 64
for i in range(N-7):
    for j in range(M-7):
        for k in range(8):
            for l in range(8):
                x = i+k
                y = j+l
                if (x+y) % 2 == 0 and board[x][y] == 'W':
                    cnt += 1
                elif (x+y) % 2 != 0 and board[x][y] == 'B':
                    cnt += 1
        cnt = cnt if cnt < 32 else 64 - cnt
        if cnt < ans:
            ans = cnt
        cnt = 0

print(ans)