num = list(range(5))
value = ['E', 'A', 'B','C','D']
ans = dict(zip(num, value))
for n in range(3):
    t = list(map(int, input().split()))
    cnt = 0
    for i in t:
        if i == 0:
            cnt += 1
    print(ans[cnt])
