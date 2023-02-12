N = int(input())
graphs = []
sum = 0
for n in range(N):
    L, H = map(int, input().split())
    graphs.append((L, H))
graphs.sort()
# 제일 긴 그래프
max_H = max(graphs, key=lambda x:x[1])
sum += max_H[1]
max_i = graphs.index(max_H)
# 제일 긴 그래프의 왼쪽 탐색
while max_i > 0:
    max_i = graphs.index(max(graphs[:max_i], key=lambda x:x[1]))
    sum += (max_H[0] - graphs[max_i][0]) * graphs[max_i][1]
    max_H = graphs[max_i]

# 제일 긴 그래프의 오른쪽 탐색
max_H = max(graphs, key=lambda x:x[1])
max_i = graphs.index(max_H)
while max_i < N - 1:
    max_i = graphs.index(max(graphs[max_i + 1:], key=lambda x:x[1]))
    sum += (graphs[max_i][0] - max_H[0]) * graphs[max_i][1]
    max_H = graphs[max_i]

print(sum)