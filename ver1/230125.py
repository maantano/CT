# 13번
# 카드 게임
# N장의 카드가 있다. 각각의 카드는 차례로 1에서 N까지의 번호가 붙어 있으며, 1번 카드가 가장 위, N번 카드가 가장 아래인 상태로 넣여있다.

# 먼저 가장 위에 있는 카드르 바닥에 버린다. 그 다음 가장 위에 있는 카드를 가장 아래에 있는 카드 밑으로 옮긴다.
# 예를들어 N이 4일때 카드는 가장 위에서 부터 1,2,3,4의 순서대로 놓여 있다.
# 1을 버리면 2,3,4가 남는다. 여기서 2를 가장 아래로 옮기면 순서가 3,4,2가 된다. 3을 버리면 4,2가 남고 순서가 2,4가 된다. 마지막 2를 버리면 카드 4가 남는다. N이 주여졌을때 가장 마지막에 남는 카드를 구하는 프로그램을 작성해라
#  =6
# import sys

# input = sys.stdin.readline
# from collections import deque

# N =int(input())
# arr = []


# for i in range(1,N+1):
#     arr.append(i)
# dq = deque(arr)


# # for i in range(10):
#     # dq.insert(-1,dq.popleft())
#     # # print(dq)
#     # # print('==============================')
#     # # arr.pop()
#     # # arr.insert(-1,arr.pop())
#     # print('==============================')
#     # print(dq)

# while len(dq) > 1:
#     dq.popleft()
#     dq.append(dq.popleft())
# print(dq[0])

# ==========================================================================================
# 14번
# 절대값 힙 구현하기

# 힙은 다음과 같은 연산을 지원한다.
# 1. 배열에 정수 x를 넣는다.
# 2. 배열에서 절대값이 가장 작은 값을 출력한 후 그 값을 배열에서 제거 한다.
#    절대값이 가장 작은 값이 여러개일 경우, 그 중에서 가장 작은 수를 출력하고, 그 값을 배열에서 제거한다.

# 1번째 줄에 연산의 개수 N이 주어진다.
# 다음 N개의 줄에는 연산과 관련된 정보를 나타내는 정수 x가 주어진다. 만약 x가 0이 아니라면 배열에 x라는 값을 추가하고, x가 0이라면 배열에서 절댓값이 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다.

# x가 0일 때, 큐가 비어있을때는 0을 출력하고, 비어있지 않을 때는 절댓값이 최소인 값을 출력한다. 단, 절댓값이 같다면 음수를 우선하여 출력한다.
# x가 1일때, put으로 큐에 새로운 값을 추가하고 우선순위 큐 정렬 기준으로 자동 정렬한다.

# 18
# 1
# -1
# 0
# 0
# 0
# 1
# 1
# -1
# -1
# 2
# -2
# 0
# 0
# 0
# 0
# 0
# 0
# 0

# ===============================================================
# 
from queue import PriorityQueue 
import sys

print = sys.stdout.write
input = sys.stdin.readline

n = int(input())
dq = PriorityQueue()

for i in range(n):
    request = int(input())
    if request == 0:
        
        if dq.empty():
            print('0\n')
        else:
            temp = dq.get()
            
            print(str((temp[1]))+'\n')
    else:
        dq.put((abs(request),request))
