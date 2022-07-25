def merge_sort(array):
    if len(array) == 1:
        return array

    # 引数のarrayを二分割し、分割したもので再起
    m = len(array) // 2
    array_A = merge_sort(array[0:m])
    array_B = merge_sort(array[m : len(array)])

    idx_A = 0
    idx_B = 0
    merged_array = []

    while idx_A < len(array_A) or idx_B < len(array_B):
        if idx_A == len(array_A):
            merged_array.append(array_B[idx_B])
            idx_B += 1
        elif idx_B == len(array_B):
            merged_array.append(array_A[idx_A])
            idx_A += 1
        else:
            if array_A[idx_A] <= array_B[idx_B]:
                merged_array.append(array_A[idx_A])
                idx_A += 1
            else:
                merged_array.append(array_B[idx_B])
                idx_B += 1

    return merged_array

N = int(input())
A = list(map(int, input().split()))

print(*merge_sort(A))
