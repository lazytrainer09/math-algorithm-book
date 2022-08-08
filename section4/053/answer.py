N = int(input())
mod = 10**9 + 7

top = pow(4, N + 1, mod) - 1
bottom = pow(3, mod - 2, mod)

print(top * bottom % mod)
