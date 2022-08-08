N = int(input())
A = [1, 1]
mod = 10**9 + 7

for i in range(2, N):
    an = A[i - 1] + A[i - 2]
    A.append(an % mod)

print(A[N - 1])
