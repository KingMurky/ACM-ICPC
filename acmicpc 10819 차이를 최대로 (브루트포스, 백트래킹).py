from itertools import permutations
import sys
answer=-sys.maxsize
def solve(arr):
    res=0
    for i in range(n-1):
        res+=(abs(arr[i]-arr[i+1]))
    return res
n=int(input())
nums=list(map(int,sys.stdin.readline().split()))

per=list(permutations(nums,n))

temp=0
for p in per:
    temp=solve(p)
    answer=max(answer,temp)

print(answer)
