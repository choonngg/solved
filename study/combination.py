# N = 10
# R = 5
# lst = [1,2,3,4,5,6,7,8,9,10]
# choose = []

# def combination(index, level):
#     if level == R:
#         print(choose)
#         return
    
#     for i in range(index, N):
#         choose.append(lst[i])
#         combination(i+1, level+1)
#         choose.pop()

# print(choose)


# def combination(n, r):
#     return permutation(n, r) / permutation(r, r)

# def permutation(n, r):
#     rst = 1
#     for i in range(r):
#         rst = rst * (n - i)
#     return rst

# print(permutation(4,3))
# print(combination(4,3))

N = 4
R = 3
lst = [1, 2, 3, 4]
choose = [] # 선택한 원소를 보관

def combination(index, level):
	if level == R:
		# 선택한 R 개의 원소를 출력
		print(choose)
		return

	# for문
	for i in range(index, N): 
		choose.append(lst[i]) # 인덱스가 i인 원소를 선택(추가)
		combination(i+1, level+1) # 다음 for 문으로 들어가는 역할
		choose.pop() # (넣었던) 인덱스가 i인 원소를 제거

combination(0, 0)