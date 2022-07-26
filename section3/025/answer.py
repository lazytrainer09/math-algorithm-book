N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0

for i in range(N):
    ans += (2 * A[i] + 4 * B[i]) / 6

print(ans)
