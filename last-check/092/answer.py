import math

N = int(input())

limit = math.floor(math.sqrt(N))

ans = 10**19
for i in range(1, limit+1):
    if N % i == 0:
        ans = min(ans, i * 2 + N // i * 2)

print(ans)
