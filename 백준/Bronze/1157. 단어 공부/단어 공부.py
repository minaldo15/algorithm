from collections import Counter
word_lst = list(input().upper())
count_word = Counter(word_lst)
lst_cnt = count_word.most_common(2)
if len(lst_cnt) > 1:
    if lst_cnt[0][-1] == lst_cnt[1][-1]:
        print('?')
    else:
        print(lst_cnt[0][0])
else:
    print(lst_cnt[0][0])