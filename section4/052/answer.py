x, y = map(int, input().split())
mod = 10**9 + 7


def integer_divided_by_3(num):
    if num < 0:
        print(0)
        exit()

    if num % 3 != 0:
        print(0)
        exit()

    return num // 3


a = integer_divided_by_3(2 * y - x)
b = integer_divided_by_3(2 * x - y)
total = a + b

factorials = [1]

for i in range(1, total + 1):
    factorials.append(factorials[i - 1] * i % mod)

top = factorials[total] % mod
bottom = factorials[a] % mod * factorials[b] % mod

print(top * pow(bottom, mod - 2, mod) % mod)
