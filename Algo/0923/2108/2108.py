import sys
from collections import Counter
sys.stdin = open('2108.txt')
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):  # N개의 숫자들 arr 리스트에 받아 주고 정렬
    n = int(input())
    arr.append(n)
arr.sort()


JaneDoe = Counter(arr)  # 카운터를 이용해 최빈값 찾기
mode = JaneDoe.most_common()
rng = max(arr)-min(arr)

# 출력
print(round(sum(arr)/N))  # 산술 평균
print(arr[len(arr)//2]) # 중앙값

if N == 1:  # N개의 숫자가 하나라면 인덱스 에러를 피하기 위해 지정
    print(arr[0])
elif mode[0][1] == mode[1][1]:  # 최빈값 중 여러 개가 있다면 두번째로 작은 숫자 출력
    print(mode[1][0])
else:
    print(mode[0][0])
print(rng)  # 범위

