import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000) #재귀허용치

N = int(input())
A = [[]for _ in range(N+1)]
visited = [False] * (N+1)
DPO = [1] * (N+1)
DPX = [0] * (N+1)

for _ in range(N-1):
    U, V = map(int, input().split())
    A[U].append(V)
    A[V].append(U)


def DFS(v):
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            DFS(i)
            DPO[v] += min(DPO[i], DPX[i])
            DPX[v] += DPO[i]


DFS(1)
print(min(DPO[1], DPX[1]))