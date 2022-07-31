N, Q = map(int, input().split())
floor_diff = [0] * (N - 1)

for _ in range(Q):
    l, r, x = map(int, input().split())
    l -= 1
    r -= 1
    if l != 0:
        floor_diff[l-1] += x
    if r != N - 1:
        floor_diff[r] -= x

ans = ""

for i in range(N-1):
    if floor_diff[i] < 0:
        ans += ">"
    elif floor_diff[i] == 0:
        ans += "="
    else:
        ans += "<"

print(ans)
