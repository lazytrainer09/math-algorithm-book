a, b, c = map(int, input().split())

if c == 1:
    print("No")
    exit()

left = a
right = c
cnt = 1
while left >= right and cnt < b:
    right *= c
    cnt += 1

if left < right:
    print("Yes")
else:
    print("No")
