import sys
input = sys.stdin.readline

X = int(input())
sum = 0
num = 0
while sum < X:
    num += 1
    sum += num

if num%2 == 0:
    print("" + str(num - sum + X) + "/" + str(sum - X + 1))
else:
    print("" + str(sum - X + 1) + "/" + str(num - sum + X))