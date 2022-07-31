import math
N = int(input())
dots = []

for _ in range(N):
    dot = list(map(int, input().split()))
    dots.append(dot)


def return_dist(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


min_dist = 10**19

for i in range(N):
    for j in range(i, N):
        if i == j:
            continue

        min_dist = min(min_dist, return_dist(*dots[i], *dots[j]))

print(min_dist)
