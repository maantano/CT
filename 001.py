# 빅-오메가 Ω(n): 최선일(best case) 때의 연산 횟수를 나타낸 표기법
# 빅-세타  Θ(n): 보통일(average case) 때의 연산횟수를 나타낸 표기법 
# 빅-오 Ο(n) : 최악일 때(worst case)의 연산 횟수를 나타낸 표기법


# 11720번

# 숫자의 합
# 입력 예제
# 1 1 = 1
# 5 54321 = 11
# 25 7000000000000000000000000000 = 7
# 11 10987654321 = 46

n = input()
numbers = list(input())
print(numbers)
sum = 0
for i in numbers:
    sum = sum + int(i)
print(sum)

"""
Key.
    list(input()) 이렇게 input에 list를 붙이면 54321 을 입력 하면 ['5', '4', '3', '2', '1'] 이렇게 들어감

슈도 코드
    n값 받기
    numbers 변수에 list 함수를 이용하여 숫자를 한 자리씩 나누어 받기
    sum 변수 선언

    for numbers 탐색:
        sum 변수에 numbers에 있는 각 자릿수를 가져오 ㅏ더하기
    sum 출력
"""

