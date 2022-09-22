

def swap(prize, i, j):
    # itoa
    prize_arr = [0] * prize_len
    for k in range(prize_len-1, -1, -1):
        prize_arr[k] = prize % 10
        prize //= 10
    # swap
    prize_arr[i], prize_arr[j] = prize_arr[j], prize_arr[i]
    # atoi
    prize = 0
    for k in range(prize_len):
        prize = prize * 10 + prize_arr[k]
    return prize


def find_max(n, k, prize):
    global ans, cnt


    if n == k: # 최댓값유지
        if prize > ans:
            ans = prize # 재귀
    else: # 숫자판길이에서 2를 선택
        for i in range(0, prize_len - 1):
            for j in range(i+1, prize_len):
                find_max(n, k + 1, swap(prize, i, j)) # 123 0 1


T = int(input())
for tc in range(1, T+1):
    # 숫자판, 횟수
    prize, N = map(int, input().split())
    ans = 0
    # 숫자판의 길이
    prize_len = 0
    t = prize
    while t:
        t //= 10
        prize_len += 1


    find_max(N, 0, prize)
    print(f'#{test + 1} {ans}')