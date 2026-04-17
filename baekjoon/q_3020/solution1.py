def search(arr, num):
    cur = -1
    step = len(arr)

    while step != 0:
        while cur + step < len(arr) and arr[cur+step] <= num:
            cur += step
        step //= 2

    return cur

N, H = map(int, input().split())
tops = []
bots = []

for i in range(N):
    if i % 2 == 0:
        bots.append(int(input()))
    else:
        tops.append(int(input()))

bots = sorted(bots)
tops = sorted(tops)

mn = int(1e8)
mn_cnt = 0
for h in range(1, H+1):
    bot_cnt = len(bots) - (search(bots, h-1) + 1)
    top_cnt = len(tops) - (search(tops, H-h) + 1)

    if mn == bot_cnt + top_cnt:
        mn_cnt += 1
    
    if mn > bot_cnt + top_cnt:
        mn = bot_cnt + top_cnt
        mn_cnt = 1

print(mn, mn_cnt)