N = int(input())
A = list(map(int, input().split()))

counts = {1: 0, 2: 0, 3: 0}

for i in range(N):
    counts[A[i]] += 1


def n_c_2(x):
    return x * (x - 1) // 2


ans = n_c_2(counts[1]) + n_c_2(counts[2]) + n_c_2(counts[3])

print(ans)
