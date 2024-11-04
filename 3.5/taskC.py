n = int(input())
a = list(map(int, input().split(" ")))


def merge_sort(arr_length, arr):
    if arr_length <= 1:
        return arr

    mid = arr_length // 2
    
    left = merge_sort(mid, arr[:mid])
    right = merge_sort(arr_length - mid, arr[mid:])

    return merge(left, right)

def merge(left, right):
    sorted_array = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])

    return sorted_array


print(" ".join(map(str, merge_sort(n, a))))