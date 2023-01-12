# https://school.programmers.co.kr/learn/courses/30/lessons/120847
# 최댓값 만들기 (1)

# 정수 배열 numbers가 매개변수로 주어집니다.
# numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록 solution 함수를 완성해주세요.

# numbers	result
# [1, 2, 3, 4, 5]	20
# [0, 31, 24, 10, 1, 9]	744

# 입출력 예 #1
# numbers = [1, 2, 3, 4, 5]
numbers = [0, 31, 24, 10, 1, 9]
# 두 수의 곱중 최댓값은 4 * 5 = 20 입니다.

def solution(numbers):
    
    arr = sorted(numbers, reverse=True)
    
    return arr[0]*arr[1]


solution(numbers)