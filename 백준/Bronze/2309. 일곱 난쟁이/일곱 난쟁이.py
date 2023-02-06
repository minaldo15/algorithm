lst = []
for n in range(9):
    a = int(input())
    lst.append(a)

for i in range(1<<9):
    sub_set = []
    for j in range(9):
        if i & (1<<j):
            sub_set.append(lst[j])
        # print(sub_set)
    if len(sub_set) == 7 and sum(sub_set) == 100:
        ans = sub_set
        # print(ans)
ans.sort()
for num in ans:
    print(num, end = '\n')