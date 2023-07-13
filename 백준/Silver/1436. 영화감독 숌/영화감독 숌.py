import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
tmp = 665
while cnt != n:
    tmp += 1
    if str(tmp).count('666') > 0:
        cnt += 1

print(tmp)