from collections import deque

N, M = map(int, input().split())

relations = [[] for _ in range(N)]

ages = [120] * N
ages[0] = 0

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    relations[a].append(b)
    relations[b].append(a)

Q = deque()
Q.append(0)

while len(Q) > 0:
    i = Q.popleft()
    for j in relations[i]:
        if ages[j] != 120:
            continue

        ages[j] = min(ages[i] + 1, ages[j])
        Q.append(j)

for age in ages:
    print(age)
