N = int(input())
A = list(map(int, input().split()))
M = int(input())

posi = [0]

for i in range(N - 1):
    posi.append(posi[i] + A[i])

ans = 0
bef_B = int(input())-1
for _ in range(M - 1):
    aft_B = int(input())-1
    ans += abs(posi[aft_B] - posi[bef_B])
    bef_B = aft_B

print(ans)
