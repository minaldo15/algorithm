A, B = map(int, input().split())
C = int(input())
if C >= 60:
    if B + C % 60 >= 60:
        A = A + C // 60 + 1
        B = B + C % 60 - 60
    else:
        A = A + C // 60
        B = B = B + C % 60
else:
    if B + C >= 60:
        A = A + 1
        B = B + C - 60
    else:
        B = B + C
A = A % 24
print(A, B)