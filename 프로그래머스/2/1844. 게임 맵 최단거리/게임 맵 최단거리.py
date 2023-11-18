from collections import deque


def solution(maps):
    target_r = len(maps) - 1
    target_c = len(maps[0]) - 1

    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    queue = deque()
    maps[0][0] = 0
    queue.appendleft((0, 0, 1))

    while len(queue) > 0:
        cur_r, cur_c, cur_dist = queue.pop()
        if cur_r == target_r and cur_c == target_c:
            return cur_dist

        for i in range(4):
            nr = cur_r + dr[i]
            nc = cur_c + dc[i]

            if (nr < 0) or (nc < 0) or (nr > target_r) or (nc > target_c) or (maps[nr][nc] == 0):
                continue

            maps[nr][nc] = 0
            queue.appendleft((nr, nc, cur_dist+1))

    return -1


print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
