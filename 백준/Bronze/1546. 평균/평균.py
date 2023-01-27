N = int(input())
scores = list(map(int, input().split()))
average = sum(scores)/N
new_average = average/max(scores)*100
print(new_average)