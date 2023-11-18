import sys
sys.setrecursionlimit(100000)

n = int(input())
m = int(input())

A = [[] for _ in range(n+1)]
visited = [False] * (n+1)
count = 0

def DFS(v):
    global count
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            count += 1
            DFS(i)

for _ in range(m):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)

DFS(1)
print(count)