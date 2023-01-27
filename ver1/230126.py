# 버블(bubble) 정렬 : 데이터의 인접 요소끼리 비교하고, swap 연산을 수행하며 정렬하는 방식
# 선택(selection) 정렬 : 대상에서 가장 크거나 작은 데이터를 찾아가 선택을 반복하면서 정렬하는 방식
# 삽입(insertion) 정렬 : 대상을 선택해 정렬된 영역에서 선택 데이터의 적절한 위치를 찾아 삽입하면서 정렬하는 방식
# 퀵(quick) 정렬 : pivot 값을 선정해 해당 값을 기준으로 정렬하는 방식
# 병합(merge) 정렬 : 이미 정렬된 부분 집합들을 효율적으로 병합해 전체를 정렬하는 방식
# 기수(radix) 정렬 : 데이터의 자릿수를 바탕으로 비교해 데이터를 정렬 하는 방식


# 버블 정렬 핵심 이론

# 버블 정렬(bubble sort)은 두 인접한 데이터의 크기를 비교해 정렬하는 방법이다. 간단하게 구현 할 순 있지만,
# 시간 복잡도는 O(n2)으로 다른 정렬 알고리즘보다 속도가 느린 편이다. 다음 그림과 같이 루프를 돌면서 인접한 데이터 간의 swap연산으로 정렬한다.

# 버블 정렬 과정

# 1. 비교 연산이 필요한 루프 범위를 설정한다.
# 2. 인접한 데이터 값을 비교한다.
# 3. swap 조건에 부합하면 swap 연산을 수행한다.
# 4. 루프 범위가 끝날때 까지 2~3을 반복한다.
# 5. 정렬 영역을 설정한다. 다음 루프를 실행할 때는 이 영역을 제외한다.
# 6. 비교 대상이 없을 떄 까지 1~5를 반복한다.

# 만약 특정한 루프의 전체 영역에서 swap이 한 번도 발생하지 않았다면 그 영역 뒤에 있는 데이터가 모두 정렬됐다는 뜻이므로 프로세스를 종료해도 된다.

# 수 정렬하기
# 2750번

# N개의 수가 주어졌을 때 이를 오름차순 정렬하는 프로그램을 작성하시오

# 1번째 줄에 수의 개수 N, 2번째 줄부터 N개의 줄에 숫자가 주어진다. 이 절댓값이 1000보다 같거나 같은 정수이다.
# 입력
# 5
# 5
# 2
# 3
# 4
# 1

# 출력
# 1
# 2
# 3
# 4
# 5


# import sys
# input = sys.stdin.readline
# n = int(input())
# arr = []
# for i in range(n):
#     arr.append(int(input()))

# tmp = 0
# for i in range(n): 
#     for j in range(i,len(arr)):
#         if arr[i]>arr[j]:
#             tmp = arr[j]
#             arr[j] = arr[i]
#             arr[i] = tmp
#     print(arr[i])


# 버블정렬 프로그램1
# 1377번
# bool change = false;
# for(int i =1; i<=n+1;,i++){
#     change = false;
#     for(int   j<n-1;j++){
#         if(a[j] > a[j+1]){
#             change = true;
#             swap(a[j],a[j+1]);
#         }
#     }
#     if(change == false){
#         cout << i << '\n'
#         break
#     }
# }
# 위 코드에서 n은 배열의 크기, a는 수가 들어있는 배열이다. 수는 배열의 1번 방부터 채운다. 위와같은 코드를 실행 시켰을때, 어떤 값이 출력되는지를 구하는 프로그램을 작성하시오

# 1번째 줄에는 N,
# 2번째 줄부터 N개의 줄에 A[1] 부터  A[N] 까지 1개씩 주어진다.

# 입력
# 5
# 10
# 1
# 5
# 2
# 3

# 출력
# 3

# 시간 초과 Fail
# import sys
# inout = sys.stdin.readline

# n = int(input())
# arr=[]
# for i in range(n):
#     arr.append(int(input()))


# tmp =0

# for i in range(n):
#     swap = False
#     for j in range(n-1):
#         # if arr[i] > arr[j+1]:
#         if arr[j] > arr[j+1]:
#             tmp = arr[j+1]
#             arr[j+1] = arr[j]
#             arr[j] = tmp
#             swap = True
#     if swap == False:
#         print(str(i+1)+'\n')
#         break
        

import sys
inout = sys.stdin.readline

n = int(input())
arr=[]
arr2=[]
for i in range(n):
    arr.append(int(input()))
max = 0
sortedArr = sorted(arr)

for i in range(n):
    if max < sortedArr[i][1]-i:
        max = sortedArr[i][1]-i

print(max+1)
# 마지막 for문 한바퀴를 더해야한다.