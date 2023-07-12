import sys
input = sys.stdin.readline


def plus(expression):
    nums = map(int, expression.split('+'))
    return sum(nums)

tmp = input().split('-')
ans = plus(tmp[0]) * 2
for x in tmp:
    ans -= plus(x)

print(ans)
