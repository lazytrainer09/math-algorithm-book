N = int(input())
A = list(map(int, input().split()))
A.sort()

mod = 1000000007
ans = 0

for i in range(N):
    ans += pow(2, i, mod) * A[i]
    ans %= mod

print(ans)
