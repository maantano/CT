# 11번 E-book

import sys

input = sys.stdin.readline

n = int(input())
arr =[0] * n





# print(arr)
for i in range(n):
    arr[i] = int(input())

stack =[]
num=1
result =True
answer =''


for i in range(n):
    su = arr[i]
    if su >= num:
        while su >= num:
            stack.append(num)
            num +=1
            answer += "+\n"
        stack.pop()
        answer += "-\n"
    else:
        n = stack.pop()
        if n > su:
            print('NO')
            result = False
            break
        else:
            answer +="-\n"
if result:
    print(answer)




# 오큰수 구하기
#  17298번


# 크기가 N인 수열 A[1], A[2], ... , A[N] 이 있다. 수열의 각 원소 A[i]에 관련된 오큰수 NGE(i)를 구하려고 한다.
# A[i]의 오큰수는 오른쪽에 있으면서 A[i]보다 큰 수 중 가장 왼쪽에 있는 수를 의미한다.
# 이러한 수가 없을때 오큰수는 -1이다.

# 크기가 N인 수열 A = A[1], ... A[N]
# A[N]에 관련된 오큰수 NGE(i)를 구하려 한다.
# A[i]의 오큰수는 오른쪽에 있으면서 큰수중 가장 왼쪽에 있는 수를 의미한다. 이런수가 없을때는 오큰수는 -1이다.

# 1번 줄에 수열의 크기 A
# 2번 줄에 A의 원소 A[1] , ...,A[N]

# 4
# 3 5 2 7
# 5 7 7 -1

# 4
# 9 5 4 8
# -1 8 8 -1

# 스택에 새로 들어오는 수가 Top에 존재하는 수보다 크면 그 수는 오큰수가 된다.
# 오큰수를 구한 후 수열에서 오큰수가 존재하지 않는 숫자에 -1을 출력해야한다.

# 실패 ==> 답은 나오는데, 타임아웃
# import sys
# input = sys.stdin.readline
# n = int(input())

# arr = list(map(int,input().split()))
# stack =[0]*n
# result = ''
# for i in range(n):
#     for j in range(i+1,n):
#         if arr[i]<arr[j]:
#             stack[i] = arr[j]
#             break
#         else:
#             stack[i] = -1
#     if i+1 == n:
#         stack[i] = -1
#     # result += str(stack[i]) + ' '
    
# result = ' '.join(map(str, stack))

# print(result)

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
result = [-1] * N
stack = []

for i in range(N):
    while stack and arr[stack[-1]] < arr[i]:
        result[stack.pop()] = arr[i] 
    stack.append(i)

print(*result)

