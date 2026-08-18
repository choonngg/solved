# data = list(map(int, input().split()))

# lst1 = sorted(data, reverse=True)
# lst2 = sorted(data)

# print(f"내림차순 => {" ".join(map(str, lst1))}")
# print(" ".join(map(str, lst2)))

n = int(input())
# data = []
# for i in range(n):
#     data.append(input())
data = [input() for _ in range(n)]
print()
sorted_data = sorted(data)
for sd in sorted_data:
    print(sd)