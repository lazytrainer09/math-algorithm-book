N, X = map(int, input().split())

cnt = 0
for a in range(1, N - 1):
    for b in range(a + 1, N):
        c = X - a - b
        if not (b < c <= N):
            continue
        cnt += 1

print(cnt)
