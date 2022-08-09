N, K = map(int, input().split())
A = list(map(int, input().split()))

visited = [-1] * N
loops = []
to_loops = []

now = 1
for _ in range(2*N):
    if visited[now-1] == 1:
        break

    if visited[now-1] == 0:
        loops.append(now)

    if visited[now-1] == -1:
        to_loops.append(now)

    visited[now-1] += 1
    now = A[now-1]

to_loop = visited.count(0)
loop_count = visited.count(1)

if K <= to_loop:
    print(to_loops[K])
else:
    K -= to_loop
    K %= loop_count
    print(loops[K])
