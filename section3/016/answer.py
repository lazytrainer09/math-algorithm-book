N = int(input())
A = list(map(int, input().split()))

def euclidean_algorithm(a, b):
  while a >= 1 and b >= 1:
    if a >= b:
      a %= b
    else:
      b %= a

  if a != 0:
    return a

  return b

ans = A[0]

for i in range(1, N):
  ans = euclidean_algorithm(ans, A[i])

print(ans)
