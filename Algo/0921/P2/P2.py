import sys
sys.stdin = open('P2.txt')

T = int(input())

def babygin(num, cnt_lst):
    cnt_lst[num] += 1
    flag = 0
    i = 0
    while i < 8:
        if cnt_lst[i] >= 3: # triplet check
            flag = 1
            break
        if cnt_lst[i] and cnt_lst[i + 1] and cnt_lst[i + 2]: # run check
            flag = 1
            break
        i += 1
    if flag == 1:
        return True


for tc in range(1, T+1):
    card_lst = list(map(int, input()))
    cnt_1, cnt_2 = [0]*10, [0]*10

    for i in range(0, len(card_lst), 2):
        if babygin(card_lst[i], cnt_1):
            print('True')
            break
        if babygin(card_lst[i+1], cnt_2):
            print('False')
            break

