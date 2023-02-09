lst = list(map(int, input().split()))
ans = ['ascending', 'descending', 'mixed']
for i in range(len(lst)-1):
    if lst[i] > lst[i + 1]:
        if 'ascending' in ans:
            ans.remove('ascending')
    elif lst[i] < lst[i + 1]:
        if 'descending' in ans:
            ans.remove('descending')
print(ans[0])