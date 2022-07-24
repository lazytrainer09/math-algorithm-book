from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

counts = defaultdict(int)

for i in range(N):
    counts[A[i]] += 1

ans = 0

for i in range(1, 50001):
    if i == 50000:
        ans += counts[i] * (counts[i] - 1) // 2
        continue

    ans += counts[i] * counts[100000 - i]

print(ans)
