N = int(input())
A = list(map(int, input().split()))

dp = [[0, 0] for _ in range(N+1)]

for i in range(N):
  # 当日を足さないとき
  dp[i+1][0] = max(dp[i])

  # 当日を足すとき
  dp[i+1][1] = A[i]+dp[i][0]

print(max(dp[N]))
