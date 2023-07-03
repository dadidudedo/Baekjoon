import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000) #재귀허용치


def DFS(v):
    visited[v] = True
    DP[v] = A[v][parent[v]]
    tmp = 0
    for i in range(N+1):
        if (not visited[i]) and A[v][i] != 0:
            parent[i] = v
            DFS(i)
            tmp += DP[i]
    if tmp != 0:
        DP[v] = min(tmp, DP[v])


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    A = [[0 for i in range(N+1)] for j in range(N+1)]
    DP = [0] * (N+1)
    visited = [False] * (N+1)
    visited[0] = True
    parent = [0] * (N+1)
    for m in range(M):
        n1, n2, d = map(int, input().split())
        A[n1][n2] = d
        A[n2][n1] = d
    DFS(1)
    ans = 0
    for i in range(2, N+1):
        if A[1][i] != 0:
            ans += DP[i]

    print(ans)