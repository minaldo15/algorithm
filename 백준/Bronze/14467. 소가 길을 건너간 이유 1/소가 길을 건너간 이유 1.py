N = int(input())
check = [0]*10
cnt = 0
set_num = []
for i in range(N):
    num, loc = map(int, input().split())
    if num not in set_num:
        set_num.append(num)
        check[num-1] = loc
    else:
        if loc != check[num-1]:
            cnt += 1
            check[num-1] = loc
print(cnt)