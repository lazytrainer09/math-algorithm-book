N = int(input())
A = list(map(int, input().split()))

def euclidean_algorithm(a, b):
  if b == 0:
    return a
  else:
    return euclidean_algorithm(b, a%b)

ans = A[0]

for i in range(1, N):
  ans = euclidean_algorithm(ans, A[i])

print(ans)
