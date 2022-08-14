N = int(input())

class1 = [0] * N
class2 = [0] * N

for i in range(N):
    c, p = map(int, input().split())
    if c == 1:
        class1[i] = p
    else:
        class2[i] = p

sum_class1 = [0]
sum_class2 = [0]

for i in range(N):
    sum_class1.append(sum_class1[i] + class1[i])
    sum_class2.append(sum_class2[i] + class2[i])

Q = int(input())
for i in range(Q):
    l, r = map(int, input().split())
    a = sum_class1[r] - sum_class1[l - 1]
    b = sum_class2[r] - sum_class2[l - 1]
    print(a, b)
