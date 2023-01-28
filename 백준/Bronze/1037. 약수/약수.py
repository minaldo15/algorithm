n = int(input())
lst_mea = (list(map(int,input().split())))
if len(lst_mea) == 1:
    N = int(lst_mea[0])**2
else:
    lst_mea.sort()
    N = lst_mea[0] * lst_mea[-1]
print(N)