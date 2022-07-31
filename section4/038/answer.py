N, Q = map(int, input().split())
A = list(map(int, input().split()))

S = [0]

for i in range(N):
    S.append(S[i]+A[i])

for _ in range(Q):
    l, r = map(int, input().split())
    print(S[r]-S[l-1])
