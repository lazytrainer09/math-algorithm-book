import math

x1, y1, r1 = map(int, input().split())
x2, y2, r2 = map(int, input().split())

dist = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

add_r = r1 + r2
sub_r = abs(r1 - r2)

if sub_r > dist:
    ans = 1
elif sub_r == dist:
    ans = 2
elif sub_r < dist < add_r:
    ans = 3
elif add_r == dist:
    ans = 4
else:
    ans = 5

print(ans)
