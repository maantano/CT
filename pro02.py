# 배열 회전시키기
# https://school.programmers.co.kr/learn/courses/30/lessons/120844

# 정수가 담긴 배열 numbers와 문자열 direction가 매개변수로 주어집니다.
# 배열 numbers의 원소를 direction방향으로 한 칸씩 회전시킨 배열을 return하도록 solution 함수를 완성해주세요.


from collections import deque

numbers = [1, 2, 3]
direction = 'right'
# [3, 1, 2]

# numbers = [4, 455, 6, 4, -1, 45, 6]
# direction = "left"
# [455, 6, 4, -1, 45, 6, 4]


def rotate(numbers,direction):
    dq = deque(numbers)
    if direction =='right':
        dq.appendleft(dq.pop())
        #  numbers.rotate(1)
    else:
        dq.append(dq.popleft())
        #  numbers.rotate(-1)
    return list(dq)
    # return [numbers[-1]] + numbers[:-1] if direction == 'right' else numbers[1:] + [numbers[0]]
    
    
rotate(numbers,direction)

