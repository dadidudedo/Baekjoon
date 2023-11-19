def solution(n, wires):
    ans = n
    A = [[] for i in range(n + 1)]
    for wire in wires:
        w1 = wire[0]
        w2 = wire[1]
        A[w1].append(w2)
        A[w2].append(w1)

    for wire in wires:

        stack = list()
        visited = [False for i in range(n + 1)]
        w1 = wire[0]
        w2 = wire[1]

        # w1에 대해 dfs
        cnt = 1
        stack.append(w1)
        visited[w1] = True
        while len(stack) > 0:
            curWire = stack.pop()

            for connectedWire in A[curWire]:
                if (not visited[connectedWire]) and (connectedWire != w2):
                    visited[connectedWire] = True
                    cnt += 1
                    stack.append(connectedWire)

        if abs(n - 2 * cnt) < ans:
            ans = abs(n - 2 * cnt)

    return ans