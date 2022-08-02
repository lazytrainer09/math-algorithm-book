N = int(input())

div_counts = [1]*N

for i in range(2, N+1):
    for j in range(i, N+1, i):
        div_counts[j-1] += 1

ans = 0
for i in range(1, N+1):
    ans += i*div_counts[i-1]

print(ans)
