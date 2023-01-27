C = int(input())
for i in range(C):
    case = list(map(int, input().split()))
    N = case[0]
    scores = case[1:]
    average = sum(scores)/N
    lst_over_avr = []
    for score in scores:
        if score > average:
            lst_over_avr.append(score)
    ratio = len(lst_over_avr)/N*100 
    print(f'{round(ratio, 3):.3f}%')