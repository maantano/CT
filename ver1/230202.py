# 병합정렬

# 병합 정렬(merge sort) 분할 정복(devide and conquer) 방식을 사용해 데이터를 분할하고 분할한 집합을 정렬하며 합치는 알고리즘 이다.
# 병합 정렬의 시간 복잡도는 O(nlogn)이다.

# 병합 정렬의 핵심 이론 수행방식

# 최초에는 8개의 그룹으로 나뉘는데, 이 상태에서 2개씩 그룹을 합치며 오름차순으로 정렬한다.
# 1. [32,42,24,60,5,15,45,90]
# 2. [(32,42),(24,60),(5,15),(45,90)]
# 3. [(24,32,42,60),(5,15,45,90)]
# 4. [(5,15,24,32,42,45,60,90)]
# 병합 정렬은 코딩테스트의 정렬 문제에서 자주 등장한다. 특히 2개의 그룹을 병합하는 원리는 꼭 숙지 해야한다.


# 2개의 그룹을 병합 하는 과정
# 투 포인터 개념을 사용하여 왼쪽, 오른쪽 그룹을 병합합니다. 왼쪽 포인터와 오르녹 포인터의 값을 비교하여 작은 값을 결과 배열에 추가하고 포인트를 오른쪽으로 한칸 이동시킨다.


# 수 정렬하기2
# 2751번
# N개의 수가 주어졌을 때 이를 오름차순 정렬하는 프로그램을 정렬하시오.
# 1번 줄에 수의 개수 N, 2번째 줄부터 N의의 줄에 숫자가 주어진다.
# input
# 5
# 5
# 4
# 3
# 2
# 1

# output
# 1
# 2
# 3
# 4
# 5

# n = int(input())
# arr =[]
# for i in range(n):
#     arr.append(int(input()))

# # print(arr)
# mid = n //2
# stack = []
# def merge_sort(arr,mid):
#     if mid ==0:
#         return
#     g1= arr[:mid]
#     g2= arr[mid:]
#     while  g1:
#         if

# import sys
# # print = sys.stdout.write
# input = sys.stdin.readline
# n =int(input())
# arr = []
# for i in range(n):
#     arr.append(int(input()))
# arr.sort()
# for i in range(n):
#     print(arr[i])

# 1037번
# 양수 A가 N의 진짜 약수가 되려면, N이 A의 배수이고,
# A가 1과 N이 아니어야 한다. 어떤 수 N의 진짜 약수가 모두 주어질 때, N을 구하는 프로그램을 작성하시오.
# 첫째 줄에 N의 진짜 약수의 개수가 주어진다. 이 개수는 50보다 작거나 같은 자연수이다. 둘째 줄에는 N의 진짜 약수가 주어진다. 1,000,000보다 작거나 같고, 2보다 크거나 같은 자연수이고, 중복되지 않는다.

# input
# 2
# 4 2
# output
# 8

# 6
# 3 4 2 12 6 8

# 24
import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

# print(arr)
arr.sort()
tmp = arr[0]* arr[-1]
print(tmp)
