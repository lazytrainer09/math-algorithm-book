from pprint import pp


N = int(input())

ans_dict = {0: 6, 1: 2, 2: 4, 3: 8}

print(ans_dict[N % 4])
