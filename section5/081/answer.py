N = int(input())

ten_thousand = N // 10000
N %= 10000
five_thousand = N // 5000
N %= 5000
one_thousand = N // 1000

print(ten_thousand + five_thousand + one_thousand)
