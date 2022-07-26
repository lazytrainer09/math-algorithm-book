N = int(input())

ans = 0

for r in range(N):
    ans += N / (N - r)

print(ans)
