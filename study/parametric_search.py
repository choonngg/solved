def parametric_search1(arr):
    ret = -1

    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == True: 
            left = mid + 1
            ret = mid
        else: 
            right = mid - 1

    return ret


def parametric_search2(arr):
    cur = -1
    step = len(arr)
    
    while step != 0:
        while (cur + step < len(arr) and arr[cur + step] == True): 
            cur += step
        step //= 2
        
    return cur

arr = [True, True, True, True, True, True, True, True, False, False, False, False]
print(parametric_search1(arr))
print(parametric_search2(arr))