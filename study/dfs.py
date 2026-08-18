N = 5   # 노드 개수

# DFS 함수
def dfs(node):
    global adj_list, visited

    # base case
    if visited[node]:
        return
    visited[node] = True
    print(node, end=' ')

    # recursive case
    for adj_node in adj_list[node]:
        dfs(adj_node)


adj_list = [[] for _ in range(N)]
visited = [False] * N

adj_list[0].append(1); adj_list[0].append(2)
adj_list[1].append(4); adj_list[1].append(3)
adj_list[2].append(3)
adj_list[3].append(0)

dfs(0)