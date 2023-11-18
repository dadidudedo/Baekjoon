def solution(id_list, reports, k):
    n = len(id_list)
    targets = []
    datas = [[False for i in range(n)] for j in range(n)]
    for report in reports:
        user, target = report.split(' ')
        user = id_list.index(user)
        target = id_list.index(target)
        datas[target][user] = True

    for i in range(n):
        if sum(datas[i]) >= k:
            targets.append(i)

    answer = [0 for i in range(n)]
    for target in targets:
        for i in range(n):
            if datas[target][i]:
                answer[i] += 1

    return answer
