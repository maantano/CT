
# 투 포인터
# 투 포인터는 2개의 포인터로 알고리즘의 시간 복잡도를 최소화 합니다.


# 연속된 자연수의 합 구하기

# 2018번

# 입력 예제
# 15

n = int(input())
count = 1
sum = 1
start_index = 1
end_index =1

while end_index != n:
    if sum==n:
        count +=1
        end_index +=1
        sum += end_index
    elif sum > n:
        sum -= start_index
        start_index += 1
    else:
        sum += end_index
        end_index +=1
print(count)
    





"""
    문제 분석
    시간 복잡도 분석으로 사용할 알고리즘의 범위부터 줄여야한다. 우선 문제에 주어진 시간은 2초이다 그런데, 최댁값은 10,000,000으로 매우 크게 잡혀 있다. 이런 상황에서는 O(nlogn)의 시간 복잡도 알고리즘을 사용하면 제한 시간을 초과하므로 0(n)의 시간 복잡도 알고리즘을 사용해야한다.
    이런 경우 자주 사용하는 방법이 투 포인터 이다. 연속된 자연수의 합을 구하는 것이 문제이므로 시작 인덱스와 종료 인덱스를 지정하여 연속된 수를 표현하겠다. 시작 인덱스 ,종료 인덱스를 투 포인터로 지정한 후 문제에 접근해본다.
    count를 1로 초기화 한 이유는 N 혼자일 경우를 미리 초기화 한다.

    sum == N / count++, end_undex++, sum = sum+end_index
    sum > N / sum = sum - start_index; , start_index++,
    sum < N / end_index++, sum= sum + end_index,

    슈도코드
    n 변수 저장
    사용 변수 초기화(count = 1, start_index=1, end_index=1,sum=1)
    
    while end_index != n:
        if sum == n: sum값 변경, end_index++, count++
        elif sum > n: sum값 변경 , start_index++
        else: end_index증가, sum 변경


    count 출력


"""

