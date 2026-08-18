def sum_func1(n):
    res = 0
    for i in range(1, n+1):
        res += i
    
    return res

def sum_func2(n):
    if n == 1:
        return 1    # base case
    return sum_func2(n-1) + n   # recursive case

print(sum_func1(10))
print(sum_func2(10))