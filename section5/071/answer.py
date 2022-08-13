N = int(input())
combs = [list(map(int, input().split())) for _ in range(N)]

cross = []

for i in range(N):
    ai, bi, ci = combs[i]
    for j in range(N):
        if i == j:
            continue

        aj, bj, cj = combs[j]

        if ai * bj == aj * bi:
            continue

        x = (bj * ci - bi * cj) / (bj * ai - bi * aj)
        y = (ai * cj - aj * ci) / (bj * ai - bi * aj)

        cross.append([x, y])


def condition_judge(x, y):
    for i in range(N):
        ai, bi, ci = combs[i]
        if ai * x + bi * y > ci:
            return False

    return True

ans = -10*10**9
for p in cross:
    if condition_judge(p[0], p[1]):
        ans = max(ans, sum(p))

print(ans)
