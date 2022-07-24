n, r = map(int, input().split())

ans = 1
r = min(n-r, r)
for i in range(r):
  ans *= (n-i)
for i in range(1, r+1):
  ans //= i

print(ans)
