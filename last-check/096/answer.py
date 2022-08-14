N = int(input())
T = list(map(int, input().split()))

sumT = sum(T)
dp = [False] * (sumT + 1)

dp[0] = True

for i in range(N):
    for j in range(sumT, -1, -1):
        if not dp[j]:
            continue

        if j + T[i] <= sumT:
            dp[j + T[i]] = True

ans = 10**19

for i in range(1, sumT + 1):
    if not dp[i]:
        continue

    ans = min(ans, max(sumT - i, i))

print(ans)
