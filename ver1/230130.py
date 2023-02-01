# 퀵 정렬
# 퀵 정렬(quick sort)은 기준값(pivot)을 선정해 해당 값보다 작은 데이터와 큰 데이터로 분류하는 것을 반복해 정렬하는 알고리즘이다.
# 기준값이 어떻게 선정되는지가 시간 복잡도에 많은 영향을 미치고, 평균적인 시간 복잡도는 O(nlogn) 이며 촤악의 경우 O(n2)이 된다
# 기준값을 피벗(pivot) 이라고 한다

# 퀵 정렬 핵심 이론
# pivot을 중심으로 계속 데이터를 2개의 집합으로 나누면서 정렬하는것이 퀵 정렬의 핵심

# 퀵 정렬 과정
# 1. 데이터를 분할하는 pivot을 설정한다.
# 2. pivot을 기준으로 다음 a~e 과정을 거쳐 데이터를 2개의 집합으로 분리한다.
#     a. start가 가리키는 데이터가 pivot이 가리키는 데이터보다 작으면 start 오른쪽으로 1칸 이동한다.
#     b. end가 가리키니는 데이터가 pivot보다 크면 end를 왼쪽으로 1칸 이동한다.
#     c. start가 가리키는 데이터가 pivot이 가리키는 데이터보다 크고, end가 가리키는 데이터보다 작으면 start, end가 가리키는 데이터를 swap 하고 start는 오른쪽, end는 왼쪽으로 1칸씩 이동한다.
#     d. start와 end가 만날때 까지 a~c를 반복한다.
#     e. start 와 end가 만나면 만난 지점에서 가리키는 데이터와 pivot이 가리키는 데이터를 비교하여 pivot이 가리키는 데이터가 크면 만난 지점의 오른쪽에, 작으면 왼쪽에 pivot이 가리키는 데이터를 삽입한다.
# 3. 분리 집합에서 각각 다시 pivot을 선정한다.
# 4. 분리 집합이 1개 이하가 될 때 까지 1~3 과정을 반복한다.


# 퀵 정렬의 시간 복잡도는 비교적 준수하므로 코딩테스트에서도 종종 응용한다. 재귀 함수의 형태로 직접 구현해 볼것을 추천!

# 19번
# K번째 수 구하기.
# 11004번

# 수 N,K가 주어진다. A를 오름차순 정렬했을 때 앞에서부터 K번쨰에 있는 수를 구하는 프로그램을 작성하시오.
# 1번째 줄에 N, 2번째 줄에 A[1] ... A[N]이 주어진다.

# input
# 5 2
# 4 1 2 3 5

# output
# 2



# import sys
# input = sys.stdin.readline

# n,k = map(int,input().split())
# arr = list(map(int,input().split()))


# def quickSort(s,e,k):
#     global a
#     if s < e:
#         pivot = partition(s,e)
#         if pivot == k:
#             return
#         elif

# def quick(arr,pi):
#     start = arr[0]
#     end = arr[pi-1]
#     tmp = 0
#     while start != end:
#         if pi > start:
#             start +=1
#         elif pi < end:
#             end +=1
#         elif start > pi and end < pi:
#             tmp = arr[start]
#             arr[start] = arr[end]
#             arr[end] = tmp
#             start+=1
#             end+=1
#     if pi > tmp:
#         arr.insert(start+1,tmp)
#     else:
#         arr.insert(start-1,tmp)
    
#     quick(arr,pi)
    


d = [6,8,3,9,10,1,2,4,7,5]

def aaa(d):
    n = len(d)
    if n <=1:
        return d
    print('n====>',n)
    mid = n //2
    print('mid ====>',mid)
    print(d[:mid])
    print('----------------------------------------')
    aaa(d[:mid])

aaa(d)