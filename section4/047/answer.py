from collections import deque

N, M = map(int, input().split())

G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

# 未訪問を-1, 二部グラフの状態を0, 1で管理
flags = [-1]*N

def color_flags(x):
    flags[x] = 0

    Q = deque()
    Q.append(x)

    while len(Q) > 0:
        i = Q.popleft()
        for j in G[i]:
            if flags[j] == -1:
                flags[j] = flags[i] ^ 1
                Q.append(j)
                continue

            if flags[i] == flags[j]:
                print("No")
                exit()

for f in flags:
    if f != -1:
        continue
    color_flags(f)

print("Yes")
