import math

A, B, H, M = map(int, input().split())

hour_theta = math.pi * (60 * H + M) / 360
minute_theta = math.pi * M / 30

hour_x = A * math.sin(hour_theta)
hour_y = A * math.cos(hour_theta)

minute_x = B * math.sin(minute_theta)
minute_y = B * math.cos(minute_theta)

dist = math.sqrt((hour_x - minute_x) ** 2 + (hour_y - minute_y) ** 2)

print(dist)
