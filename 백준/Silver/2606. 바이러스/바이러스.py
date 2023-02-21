def bfs(s):
    q = [s]
    v[s] = 1
    cnt = 0
    while q:
        t = q.pop(0)
        for i in graph[t]:
            if v[i] == 0:
                q.append(i)
                v[i] = 1
                cnt += 1
    return cnt

V = int(input())
E = int(input())
graph = [[] for _ in range(V+1)]
v = [0]*(V+1)
for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
ans = bfs(1)
print(ans)