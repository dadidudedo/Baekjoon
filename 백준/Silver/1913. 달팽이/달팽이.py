N = int(input())
target = int(input())
snail = [[0 for i in range(N)] for j in range(N)]

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
r = 0
c = 0
d = 0
cur = N*N

while cur > 0:
    snail[r][c] = cur
    if cur == target:
        target_r = r+1
        target_c = c+1

    cur -= 1
    nr = r + dr[d]
    nc = c + dc[d]

    if (nr < 0) or (nc < 0) or (nr >= N) or (nc >= N) or (snail[nr][nc] != 0):
        d = (d+1) % 4

    r = r + dr[d]
    c = c + dc[d]



for i in range(N):
    for j in range(N):
        print(snail[i][j], end=' ')
    print()

print(target_r, target_c)