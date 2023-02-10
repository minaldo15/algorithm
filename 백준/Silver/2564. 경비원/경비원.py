X, Y = map(int, input().split())
N = int(input())
lst = []
sum = 0
for n in range(N):
    d, k = map(int, input().split())
    lst.append((d, k))
Dong, Dk = map(int, input().split())
for tup in lst:
    if tup[0] == Dong:
        sum += abs(Dk - tup[1])
    else:
        if Dong == 1 or Dong == 2:
            if tup[0] == 1 or tup[0] == 2:
                if (Dk + tup[1] + Y) > X + Y:
                    sum += ((X+Y)*2 - (Dk + tup[1] + Y))
                else:
                    sum += (Dk + tup[1] + Y)
            else:
                if tup[0] == 3:
                    if Dong == 1:
                        sum += (tup[1] + Dk)
                    else: #Dong == 2
                        sum += (Y-tup[1] + Dk)
                else: # tup[0] == 4
                    if Dong == 1:
                        sum += (tup[1] + (X - Dk))
                    else: #Dong == 2
                        sum += (Y-tup[1] + (X - Dk))
        else:
            if Dong == 3 or Dong == 4:
                if tup[0] == 3 or tup[0] == 4:
                    if (Dk + tup[1] + X) > X + Y:
                        sum += ((X + Y) * 2 - (Dk + tup[1] + X))
                    else:
                        sum += (Dk + tup[1] + X)
                else:
                    if tup[0] == 1:
                        if Dong == 3:
                            sum += (tup[1] + Dk)
                        else:  # Dong == 4
                            sum += (X - tup[1] + Dk)
                    else:  # tup[0] == 2
                        if Dong == 3:
                            sum += (tup[1] + (Y - Dk))
                        else:  # Dong == 4
                            sum += (X - tup[1] + (Y - Dk))

print(sum)