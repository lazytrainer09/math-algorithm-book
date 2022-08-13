N = int(input())

X = []
Y = []

for _ in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

X.sort(reverse=True)
Y.sort(reverse=True)

ans = 0

for i in range(N):
    ans += (N - i - 1) * X[i]
    ans += (N - i - 1) * Y[i]

    ans -= i * X[i]
    ans -= i * Y[i]

print(ans)
