import sys
from itertools import permutations
input = sys.stdin.readline
sys.stdin = open('P2.txt')


T = int(input())

def is_Run(arr):
    n = int(arr[0])
    for i in range(1,len(arr)):
        if n+1 != int(arr[i]):
            return False
        n = int(arr[i])
    return True

def is_Triplet(arr):
    n = arr[0]
    if arr.count(n) == len(arr):
        return True
    return False

for tc in range(T):
    perms = list(map(int, input()))


for perm in perms:
    front = ''.join(perm[:3])
    back = ''.join(perm[3:])
    if is_Run(front) or is_Triplet(front):
        if is_Run(back) or is_Triplet(back):
            print("Yes")
            exit(0)

print("No")