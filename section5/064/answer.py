N, K = map(int, input().split())
A = list(map(int, input().split()))

total = sum(A)

if total > K or total % 2 != K % 2:
    print("No")
    exit()

print("Yes")
