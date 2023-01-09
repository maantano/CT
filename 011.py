# 스택과 큐

# 스택과 큐는 리스트에서 조금 더 발전한 형태의 자료구조 이다. 스택과 큐는 구조는 비슷하지만 처리 방식이 다르다.

# 스택과 큐의 핵심 이론

# 스택
# 스택은 삽입과 삭제 연산이 후입선출(LIFO)로 이루어 져있는 자료 구조이다.
# 후입선출은 삽입과 삭제가 한쪽에서만 일어나는 특징이 있다.

# 파이썬의 스택
    # 위치
    # - top : 삽입과 삭제가 일어나는 위치를 뜻한다.
    # 연산
        # - s.append(data) : top 위치에 새로운 데이터를 삽입하는 연산이다.
        # - s.pop(): top위치에 현재 있는 데이터를 삭제하고 확인하는 연산이다.
        # - s[-1]: top 위치에 있는 현재 있는 데이터를 단순 확인하는 연산이다.
    # 스택은 깊이 우선 탐색(DFS - Depth First Search), 백트래킹 종류의 코딩 테스트에 효과적이므로 반드시 알아두어야한다.
    # 후입선출은 개념 자체가 재귀 함수 알고리즘 원리와 일맥상통하기 때문이다.

# 큐
# 큐는 삽입과 삭제 연산이 선입선출(FIFO)로 이루어지는 자료구조이다. 스택과 다르게 먼저 들어온 데이터가 먼저 나간다. 그래서 삽입과 삭제가 양방향에서 이루어진다.
    # 위치
    # - rear : 큐에서 가장 끝 데이터를 가르키는 영역(입력)
    # - front : 큐에서 가장 앞의 데이터를 가르키는 영역(출력)
    # 연산
    # - s.append(data) : rear 부분에 새로운 데이터를 삽입하는 연산
    # - s.popleft() : front 부분에 있는 데이터를 삭제하고 확인하는 연산
    # - s[0]: 큐의 맨앞(front)에 있는 데이터를 확인할 때 사용하는 연산이다.

    # 큐는 너비 우선 탐색(BFS: Breath First Search)에서 자주 사용되므로 잘 알아야 한다.

# +
    # 우선순위 큐
    # 우선순위 큐(priority queue)는 값이 들어간 순서와 상관없이 우선순위가 높은 데이터가 먼저 나오는 자료구조이다.
    # 큐 설정에 따라 front에 항상 최댓값 또는 최솟값이 위치한다.
    # 우선순위 큐는 일반적으로 힙(heap)을 이용해 구현한다.
    
# ------------------------------------------------------------------------------------------------------------------------

#  스택으로 수열 만들기
#  1874번

    # 1부터 n까지의 수를 스택에 저장하고 출력하는 방식으로 하나의 수열을 만들 수 있다.
    # 이때 스택에 push하는 순서는 반드시 오름차순을 지키도록 한다고 가정한다.
    # 수열이 주어졌을 때 이러한 방식으로 스택을 이용해 주어진 수열을 만들 수 있는지 확인하고 만들 수 있다면 어떤 순서로 push와 pop을 수행하여야하는지 확인하는 프로그램

# 입력
# 1번째 줄에는 수열의 개수 n
# 2번째 줄에는 n개의 줄에는 수열을 이루는 1이상 n이하의 정수가 1개씩 순서대로 주어진다. 이때 같은 정수가 두 번 이상 나오지 않는다.

# 출력
# 수열을 만들기 위한 연산 순서를 출력한다. push 연산은 +, pop 연산은 -로 출력하고, 불가능할 때는 no를 출력한다.


# 문제 분석하기
# 스택의 원리를 정확하게 알고 있는지를 묻는 문제이다. 이 문제는 스택의 pop,push 연산과 후입선출 개념을 이해하고 있다면 쉽게 풀 수 있다.


# 스택 연산 수행 방법
#  현재 수열 값 >= 자연수
# 현재 수열 값이 자연수보다 크거나 같을 때까지 자연수를 1씩 증가시키며 자연수를 스택에 push(append)한다. 그리고 push(append)가 끝나면 수열을 출력하기 위해 마지막 1회만 pop한다.

# 8
# 4 3 6 8 7 5 2 1 

import sys
input = sys.stdin.readline
def solution():
    N = int(input())
    # arr=[0] *N
    A=[0] *N
    
    for i in range(N):
            A[i] = int(input()) 

    # start,j = 0,0
    # arr2,arr3 = [],[]

    stack = []
    num =1
    result = True
    answer = ''


    for i in range(N):
        su = A[i]
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
                answer += '-\n'
    if result:
        print(answer)

        # if arr[j] >= start:
        #     while arr[j] >= start:
        #         arr2.append(start)
        #         start+=1
        #         arr3.append('+')
        #     start= arr2.pop()
        #     arr3.append('-')
        # else:
        #     while arr[j] < start:
        #         start = arr2.pop()
        #         if start > N:
        #             print('NO')
        #         else:
        #             arr3.append('-')
                

        # while arr[j] >= start:
    


solution()

