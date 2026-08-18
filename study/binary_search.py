def binary_search1(arr, num):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] < num:
            left = mid + 1
        if arr[mid] > num:
            right = mid - 1
        if arr[mid] == num:
            return mid
    
    return -1


def binary_search2(arr, num):
    cur = -1
    step = len(arr)

    while step != 0:
        if cur + step < len(arr) and arr[cur + step] <= num:
            cur += step
        step //= 2

    return cur

print(f"binary_search1 = {binary_search1([1, 3, 3, 4, 5, 7, 9, 10, 11, 13, 16], 10)}")
print(f"binary_search2 = {binary_search2([1, 3, 3, 4, 5, 7, 9, 10, 11, 13, 16], 10)}")