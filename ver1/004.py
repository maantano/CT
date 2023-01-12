# 구간의 합

# 11660번

# 구간 합 구하기 2

# 입력 예제

# N * N 개의 수가 N * N 크기의 표에 채워져 있다. 표 안의 수 중 (X1, Y1)에서 (X2,Y2) 까지의 합을 구하려 한다. X는 행을, Y는 열을 의미한다.
# 1번째 줄에 표의 크기 N과 합을 구해야하는 M이 주어진다.
# 4 3  / 2차원 배열의 크기, 구간 합 질문 개수
# 1 2 3 4 / 배열 요소
# 2 3 4 5 / 배열 요소
# 3 4 5 6 / 배열 요소
# 4 5 6 7 / 배열 요소
# 2 2 3 4 / 질문 1 (2,2) ~ (3,4) 까지 구간 합
# 3 4 3 4 / 질문 2 (3,4) ~ (3,4) 까지 구간 합
# 1 1 4 4 / 질문 3 (1,1) ~ (4,4) 까지 구간 합


import sys
input = sys.stdin.readline
n,m = map(int,input().split()); """n : 리스트 크기 , m : 질의 수 """
# [0]*숫자 ===> [0,0,...0]
a = [[0]*(n+1)];  """ 원본 배열 """
# _는 i랑 같은 거 앞에 [0]*(n+1)를 의미함 ==> [0]*(n+1)를 range(n+1) 만큼 반복 하겠다.
d = [[0]*(n+1) for _ in range(n+1)];  """ 합배열 배열 """


for i in range(n):
    # print('====>',input().split())
    # print('=====>',int(x) for x in input().split())
    a_row = [0] + [int(x) for x in input().split()]
    a.append(a_row)


for i in range(1, n+1):
    for j in range(1, n+1):
        # 합 배열 구하기
        d[i][j] = d[i][j-1] + d[i-1][j] - d[i-1][j-1] + a[i][j]
        


for _ in range(m):
    x1,y1,x2,y2 = map(int,input().split())
    # print('x1===>',x1)
    # print('x2===>',x2)
    # print('y1===>',y1)
    # print('y2===>',y2)
    result = d[x2][y2] - d[x1-1][y2] - d[x2][y1-1] + d[x1-1][y1-1]
    print(result)

# b = [0]
# b_row= [0]+[4]
# b.append(b_row)
# print(b)


"""
Key.


슈도 코드
    suNo(숫자,개수)
    quizNo(질문 개수)
    prefix_sum 합 배열 선언
    temp 변수 선언

    for 저장한 숫자 데이터 차례대로 탐색(더함):
        temp에 현재 숫자 데이터 더해 주기
        합 배열에 temp값 저장
    for 질의 개수만큼 반복:
        질의 범위 받기(s~e)
        구간 합 출력 하기(prefix_sum[e]-prefix_sum[s-1])
"""

