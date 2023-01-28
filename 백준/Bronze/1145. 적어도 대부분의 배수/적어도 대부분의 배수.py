from itertools import combinations
import math
num_lst = (list(map(int,input().split())))

# 5개 중 3개 뽑는 조합
total_case = []
data = combinations(num_lst, 3)
for case in data:
    total_case.append(case)

# 10가지 케이스의 최소공배수
total_multi = []
for case in total_case:
    a = case[0]
    b = case[1]
    c = case[2]
    total_multi.append(math.lcm(a,b,c))

# 10가지 케이스의 최소공배수 중 최솟값
print(min(total_multi))