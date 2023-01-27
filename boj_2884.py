H, M = map(int, input().split()) # 0<=H<=23, 0<=M<=59
if M < 45:
    if H != 0:
        H -= 1
        M += 15
    else:
        H = 23
        M += 15
else:
    M -= 45
print(H, M)
