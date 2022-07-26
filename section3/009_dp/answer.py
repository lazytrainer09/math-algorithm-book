N, S = map(int, input().split())
A = list(map(int, input().split()))

dp = [[False]*(S+1)  for _ in range(N+1)]

dp[0][0] = True

for i in range(N):
  for j in range(S+1):
    if dp[i][j]:
      dp[i+1][j] = True
    if j - A[i] >= 0 and dp[i][j-A[i]]:
      dp[i+1][j] = True

ans = "No"
for i in range(N):
  if dp[i+1][S]:
    ans = "Yes"

print(ans)
