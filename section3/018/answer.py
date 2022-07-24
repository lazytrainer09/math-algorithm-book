N = int(input())
A = list(map(int, input().split()))

counts = {100: 0, 200: 0, 300: 0, 400: 0}

for i in range(N):
    counts[A[i]] += 1

ans = counts[100] * counts[400] + counts[200] * counts[300]

print(ans)
