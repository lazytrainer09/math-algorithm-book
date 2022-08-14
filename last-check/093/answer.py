# 最大公約数
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


# 最小公倍数
def lcm(a, b):
    return a * b // gcd(a, b)


A, B = map(int, input().split())

ans = lcm(A, B)

if ans <= 10**18:
    print(ans)
else:
    print("Large")
