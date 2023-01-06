# 주사위의 개수
# https://school.programmers.co.kr/learn/courses/30/lessons/120845

# 머쓱이는 직육면체 모양의 상자를 하나 가지고 있는데 이 상자에 정육면체 모양의 주사위를 최대한 많이 채우고 싶습니다.
# 상자의 가로, 세로, 높이가 저장되어있는 배열 box와 주사위 모서리의 길이 정수 n이 매개변수로 주어졌을 때, 
# 상자에 들어갈 수 있는 주사위의 최대 개수를 return 하도록 solution 함수를 완성해주세요.
		
# box = [1, 1, 1]
# n = 1
# result=1

box = [10, 8, 6]
n = 3
# result=12


from itertools import permutations

def solution(box,n):
    return (int(box[0]//n) * int(box[1]//n)*int(box[2]//n))


import math

def solution2(box, n):
    return math.prod(map(lambda v: v//n, box))

# math.prod()
# math.prod() : ()안에 있는 모든 iterable 요소들의 곱을 구한다.
# 위의 코드를 해석하자면, box안에 있는 모든 값 v들을 n으로 나눈 값의 몫을 모두 곱하는 값을 구한다.



print(solution(box,n))

