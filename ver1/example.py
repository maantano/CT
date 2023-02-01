import sys

input = sys.stdin.readline
from collections import deque

N =int(input())
arr = []

for i in range(1,N+1):
    arr.append(i)

dq = deque(arr)

while len(dq) > 1:
    dq.popleft()
    dq.append(dq.popleft())
print(dq[0])