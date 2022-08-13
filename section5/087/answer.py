N = int(input())
mod = 10**9 + 7
num = N * (N + 1) // 2
ans = num % mod * num % mod
print(ans)
