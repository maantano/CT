# 배열의 평균값
# https://school.programmers.co.kr/learn/courses/30/lessons/120817
# 정수 배열 numbers가 매개변수로 주어집니다.
# numbers의 원소의 평균값을 return하도록 solution 함수를 완성해주세요.


	
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = 5.5
# numbers = [89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
# result = 94.0

# numbers의 원소들의 평균 값은 5.5입니다.

#  pip install numpy를 해야지 사용할수 있음, 그렇지만 python을 설치 했을때 다 설치 된듯 함
import numpy 
import statistics
def solution(numbers):
    result = sum(numbers)
    print(result / len(numbers))
    result2 = numpy.mean(numbers)
    print(result2)
    result3 = statistics.mean(numbers)
    print(result3)
solution(numbers)
