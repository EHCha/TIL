def perm(row, chosen):
    if row == r:
        print(chosen)
        return

    for i in range(N):  # 서로 다른 N개의 수
        if i in chosen:  # 앞의 row에서 이미 이 column을 선택했었으면
            continue
        chosen[row] = i # 선택하지 않았으면 이 row에서 이 column을 선택했음을 표시하고
        # chosen[row] = a[i] # index가 아니라 해당 데이터를 선택하는 경우
        perm(row+1, chosen) # 다음 row 로 간다
        chosen[row] = -1

N = 3




# 조합을 구해보자
# 조합
print("*" * 20, "Combination")
def comb(row, chosen, j):           # [1, 2, 3, 4]
    if row == r:
        print(chosen)
        return
    else:
        for i in range(j, len(a)):
            # chosen[row] = a[i]        #  n자리에 뽑은 후 입력
            chosen[row] = i
            comb(row + 1, chosen, i + 1)        # n+1자리로 이동, 인덱스를 그 이후의 것을 받도록 1 증가시킴

r = 2                       # 2개 뽑기
chosen = [-1] * r           # 조합을 만들 저장소 [-1, -1]
comb(0, chosen, 0)




### 자리 바꿈으로 순열을 구하는 경우
# permutation - 자리바꿈으로 순열을 만드는 경우(nPn)