# 最大公約数
def gcd(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a

# 最小公倍数
def lcm(a, b):
    return a * b // gcd (a, b)

N, K = map(int, input().split())
V = list(map(int, input().split()))

mul_cnts = 0

for i in range(1 << K):
    mul = 1
    cnt = 0
    for j in range(K):
        if i >> j & 1:
            mul = lcm(mul, V[j])
            cnt += 1

    if cnt == 0:
        continue

    if cnt % 2 == 1:
        mul_cnts += N // mul
    else:
        mul_cnts -= N // mul

print(mul_cnts)
