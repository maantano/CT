# N개의 수로 이루어진 수열 A[1], A[2], …, A[N]이 있다. 이 수열에 대해서 버블 소트를 수행할 때,
# Swap이 총 몇 번 발생하는지 알아내는 프로그램을 작성하시오.

# 버블 소트는 서로 인접해 있는 두 수를 바꿔가며 정렬하는 방법이다.
# 예를 들어 수열이 3 2 1 이었다고 하자.
# 이 경우에는 인접해 있는 3, 2가 바뀌어야 하므로 2 3 1 이 된다.
# 다음으로는 3, 1이 바뀌어야 하므로 2 1 3 이 된다. 다음에는 2, 1이 바뀌어야 하므로 1 2 3 이 된다. 그러면 더 이상 바꿔야 할 경우가 없으므로 정렬이 완료된다.

# 첫째 줄에 N(1 ≤ N ≤ 500,000)이 주어진다. 다음 줄에는 N개의 정수로 A[1], A[2], …, A[N]이 주어진다. 각각의 A[i]는 0 ≤ |A[i]| ≤ 1,000,000,000의 범위에 들어있다.

# input
# 3
# 3 2 1

# output
# 3

# import sys
# input = sys.stdin.readline
# n = int(input())
# arr = list(input().split())

# cnt = 0

# for i in range(n):
#     for j in range(i+1,len(arr)):
#         if arr[i] > arr[j]:
#             arr[i],arr[j] = arr[j],arr[i]
#             cnt+=1
# print(cnt)
        
# ---------------------------------------------


# import sys

# read = lambda: sys.stdin.readline().rstrip()


# def merge_sort(start, end):
#     global swap_count, A

#     if start < end:
#         mid = (start + end) // 2
#         merge_sort(start, mid)
#         merge_sort(mid + 1, end)

#         a, b = start, mid + 1
#         temp = []

#         while a <= mid and b <= end:
#             if A[a] <= A[b]:
#                 temp.append(A[a])
#                 a += 1
#             else:
#                 temp.append(A[b])
#                 b += 1
#                 swap_count += (mid - a + 1)

#         if a <= mid:
#             temp = temp + A[a:mid + 1]
#         if b <= end:
#             temp = temp + A[b:end + 1]

#         for i in range(len(temp)):
#             A[start + i] = temp[i]


# swap_count = 0
# N = int(read())
# A = list(map(int, read().split()))
# merge_sort(0, N - 1)
# print(swap_count)

# 1075번
# 두 정수 N과 F가 주어진다. 
# 지민이는 정수 N의 가장 뒤 두 자리를 적절히 바꿔서 N을 F로 나누어 떨어지게 만들려고 한다. 만약 가능한 것이 여러 가지이면, 뒤 두 자리를 가능하면 작게 만들려고 한다.

# 예를 들어, N=275이고, F=5이면, 답은 00이다. 200이 5로 나누어 떨어지기 때문이다. N=1021이고, F=11이면, 정답은 01인데, 1001이 11로 나누어 떨어지기 때문이다.
# 첫째 줄에 N, 둘째 줄에 F가 주어진다. N은 100보다 크거나 같고, 2,000,000,000보다 작거나 같은 자연수이다. F는 100보다 작거나 같은 자연수이다.
# 

# input
# 1000
# 3
# output 
# 02

# n = int(input())
# m = int(input())

arr=[]
# print(n)

a = 2341234

for i in range(a):
    print(i)
# for i in range(str(n)):
#     arr.append(i)
# print(arr)
# print(n)
# tmp = 0
# # print(n%m)

# if n % m < 10:
#     tmp = m - (n%m)
    
# print(tmp)
# print(n)