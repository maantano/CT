
# 오큰수 구하기
#  17298번


# 크기가 N인 수열 A[1], A[2], ... , A[N] 이 있다. 수열의 각 원소 A[i]에 관련된 오큰수 NGE(i)를 구하려고 한다.
# A[i]의 오큰수는 오른쪽에 있으면서 A[i]보다 큰 수 중 가장 왼쪽에 있는 수를 의미한다.
# 이러한 수가 없을때 오큰수는 -1이다.

# 입력
#  1번째 줄에 수열 A의 크기 N
#  2번째 줄에 수열 A의 원소 A[1], ... , A[N]이 주어진다.


# 4
# 3 5 2 7
# => 5 7 7 -1

# 4
# 9 5 4 8
# => -1 8 8 -1


import sys
input = sys.stdin.readline

n = int(input())
ans = [0]*n
A = list(map(int,input().split()))
stack = []

for i in range(n):
    while stack and A[stack[-1]] < A[i]:
        ans[stack.pop()] = A[i]
    stack.append(i)


# for i in range(N):
#     for j in range(i+1,):
#         if stack[i] >= stack[j]:
#             sol.append(stack.pop())
#             break;
#         else:
#             sol.append(-1)
# print(sol)
# for i in range(N):
#     for j in range(i+1,N):
#         if stack[i] <= stack[j]:
#             num = stack[j]
#             break;
#         elif stack[i] > stack[j]:
#             num = stack[i]
#     newStack.append(num)
# print(newStack)
        





# for i in range(N):
    
