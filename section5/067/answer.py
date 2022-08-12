H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

sum_H = []
for i in range(H):
    sum_H.append(sum(A[i]))

sum_W = []
for i in range(W):
    total = 0
    for j in range(H):
        total += A[j][i]
    sum_W.append(total)

ans = [[] for _ in range(H)]

for i in range(H):
    for j in range(W):
        ans[i].append(sum_H[i] + sum_W[j] - A[i][j])

for i in range(H):
    print(*ans[i])
