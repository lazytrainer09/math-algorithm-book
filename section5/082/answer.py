N = int(input())

times = []

for _ in range(N):
    l, r = map(int, input().split())
    times.append([r, l])

times.sort()

now = 0
count = 0

for i in range(N):
    end, begin = times[i]
    if now <= begin:
        count += 1
        now = end

print(count)
