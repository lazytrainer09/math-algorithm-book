N, M = map(int, input().split())

conditions = [0]*N

for _ in range(M):
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a

    conditions[b-1] += 1

ans = 0

for c in conditions:
    if c == 1:
        ans += 1

print(ans)
