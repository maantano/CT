# 카드 게임

# 2164


# N장의 카드가 있다.
# 각 카드는 차례로 1에서 N까지 번호가 붙어있고, 1번 카드는 가장 위, N번 카드가 가장 아래인 상태로 놓여있다.
# 1장 남을때 까지 반복
# 가장 위에꺼 버리고, popLeft해서 가장 아래로
from collections import deque

def solution():
    n = int(input())
    stack = list( i for i in range(1,n+1))
    ans = []
    dq = deque(stack)
    while len(dq) >1:
        dq.popleft()
        dq.append(dq.popleft())
    # while len(stack) != 1:
    #     dq.popleft()
    #     if len(dq) != 1:
    #         ans.append(dq.popleft())
    print(dq[0])
    

solution()
