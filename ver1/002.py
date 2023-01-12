# 1546번

# 평균구하기
#  제일 큰값을 기준으로 평균 구하기

# 입력 예제
# 3 , 40 80 60 = 75.0
# 3 , 10 20 30 = 66.666667
# 4 , 1 100 100 100 = 75.25
# 5 , 1 2 4 8 16 = 38.75
# 2 , 3 10 = 65.0

# ex.
#  (A / M * 100) + (B / M * 100) + (C / M *100 ) /3 === (A+B+C) + 100 / M / 3
n = input()
mylist = list(map(int,input().split()))
mymax = max(mylist)
sum = sum(mylist)





"""
Key.
    map()

    map은 리스트의 요소를 지정된 함수로 처리해주는 함수입니다(map은 원본 리스트를 변경하지 않고 새 리스트를 생성한다.)
    ex 1. 
    >>> a = [1.2, 2.5, 3.7, 4.6]
    >>> for i in range(len(a)):
    ...     a[i] = int(a[i])
    ...
    >>> a
    [1, 2, 3, 4]
    =====>

    ex 2.
    >>> a = [1.2, 2.5, 3.7, 4.6]
    >>> a = list(map(int, a))
    >>> a
    [1, 2, 3, 4]

    ex 3.
    >>> a = map(int, input().split())
    10 20 (입력)
    >>> a
    <map object at 0x03DFB0D0>
    >>> list(a)
    [10, 20]

    >>> a, b = [10, 20]
    >>> a
    10
    >>> b
    20


    split()
    input().split() ==> 공백(띄어쓰기) 자름




슈도 코드
    n에 과목의 수 입력
    mylist에 점수 정보 저장
    mymax에 mylist 정보 중 최댓값 저장
    sum에 mylist 모든 데이터 값 더하기
    sum * 100 / mymax / n 출력
"""

