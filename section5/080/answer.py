import heapq

N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    G[a - 1].append([b - 1, c])
    G[b - 1].append([a - 1, c])

INF = 10**19
dist = [INF] * N
used = [False] * N

Q = []
dist[0] = 0
heapq.heappush(Q, [0, 0])

while len(Q) > 0:
    _, i = heapq.heappop(Q)
    if used[i]:
        continue

    used[i] = True

    for j, c in G[i]:
        if dist[j] > dist[i] + c:
            dist[j] = dist[i] + c
            heapq.heappush(Q, [dist[j], j])

if dist[N - 1] != INF:
    print(dist[N - 1])
else:
    print(-1)
