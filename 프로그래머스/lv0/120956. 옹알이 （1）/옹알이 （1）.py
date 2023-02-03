def solution(babbling):
    answer = 0
    lst = ["aya", "ye", "woo", "ma"]
    for b in babbling:
        for word in lst:
            if word == b:
                answer += 1
        for i in range(4):
            for j in range(4):
                if lst[i] + lst[j] == b:
                    answer += 1
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    if lst[i] + lst[j] + lst[k] == b:
                        answer += 1
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    for l in range(4):
                        if lst[i] + lst[j] + lst[k] + lst[l] == b:
                            answer += 1
    return answer