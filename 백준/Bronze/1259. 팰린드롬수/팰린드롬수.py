while True:
    lst = list(input())
    if lst == ['0']:
        break
    else:
        flag = 1
        for i in range(len(lst)//2):
            if lst[i] != lst[-1 - i]:
                flag = 0
                break
    if flag == 1:
        print('yes')
    else:
        print('no')