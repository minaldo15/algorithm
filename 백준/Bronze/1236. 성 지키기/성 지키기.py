M, N = input().split()
dic_M = {}
dic_N = {}
count_N = 0
count_M = 0
for m in range(1, int(M) + 1):
        dic_M[m] = list(input().rstrip())

for n in range(1, int(N) + 1):
    lst_n = []
    for m in range(1, int(M) + 1):
        lst_n.append(dic_M[m][n-1])
        dic_N[n] = lst_n

for n in range(1, int(N) + 1):
    if 'X' not in dic_N[n]:
        count_N += 1

for m in range(1, int(M) + 1):
    if 'X' not in dic_M[m]:
        count_M += 1

print(max(count_N, count_M))