C = int(input())
for i in range(C):
    count = 0
    case = list(input())
    for j in range(len(case)):
        if case[j] == 'O':
            count += 1
            if j > 0:
                for n in range(1,j+1):
                    if case[j-n] == 'O':
                        count += 1
                    else:
                        break
        else:
            continue
    print(count)