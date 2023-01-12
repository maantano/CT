# N*M의 행렬이 있다.
# 이 행렬의 부분행렬들 중 그 성분들의 합이 K로 나누어 떨어지는 경우가 몇 가지나 되는지 알아보려 함
# 부분행렬이란 어떤 행렬에서 부분적으로 뽑아낸 행렬을 의미

# 입력
# 첫째 줄에는 세개의 자연수
# N : N개의 줄에는
# M : 각 M개씩 정수들이 들어감
# K : 나누는 수

# 3 4 6
# 1 1 1 1
# 1 1 1 1
# 1 1 1 1

# 출력
# 8


import sys
input = sys.stdin.readline

N,M,K = map(int,input().split())

arr = [[0]*M]
d = [[0]*(M) for _ in range(N)]




# print(arr)