from collections import deque

R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())

sy -= 1
sx -= 1
gy -= 1
gx -= 1

maze = []

for _ in range(R):
    maze.append(input())

moves = [[-1] * C for _ in range(R)]

moves[sy][sx] = 0

Q = deque()
Q.append([sy, sx])

while len(Q) > 0:
    iy, ix = Q.popleft()
    for dy, dx in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        jy = iy + dy
        jx = ix + dx

        if not ((0 <= jy < R) and (0 <= jx < C)):
            continue

        if maze[jy][jx] == "#":
            continue

        if moves[jy][jx] == -1:
            moves[jy][jx] = moves[iy][ix] + 1
            Q.append([jy, jx])

print(moves[gy][gx])
