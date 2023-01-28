import sys
num_lst = list(map(int, input().split()))
num_lst.sort()
max = num_lst[0] * num_lst[1] * num_lst[2]
for multi_num in range(1, max + 1):
    count = 0
    for num in num_lst:
        if multi_num % num == 0:
            count += 1
            if count == 3:
                print(multi_num)
                sys.exit(0)