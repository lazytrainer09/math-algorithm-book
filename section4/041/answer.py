T = int(input())
N = int(input())

count_by_time = [0] * (T + 1)

for _ in range(N):
    l, r = map(int, input().split())
    count_by_time[l] += 1
    count_by_time[r] -= 1

ans = 0
for i in range(T):
    ans += count_by_time[i]
    print(ans)
