A, B, C = map(int, input().split())
mod = 998244353


def sigma(n):
    return n * (n + 1) // 2


ans = sigma(A) % mod * sigma(B) % mod * sigma(C) % mod
print(ans)
