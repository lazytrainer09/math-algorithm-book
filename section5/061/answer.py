N = int(input())

k = N + 1

while k % 2 == 0:
    k //= 2

if k == 1:
    print("Second")
else:
    print("First")
