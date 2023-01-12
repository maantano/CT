# N개의 수로 된 수열 A[1],A[2], .... , A[N] 이 있다.
# 수열의 i 번째 수부터 j 번째 수까지의 합 A[i] + A[i+1] + .... + A[j-1] + A[j] 가 M이 되는 경우의 수를 구하시오

# arr(i,j) = sum[i+1][j+1] - sum

import sys

input = sys.stdin.readline

n,m = map(int,input().split())
arr = list(map(int,input().split()))


sum = arr[0]
start, end = 0,1
count =0


while True:
    if sum < m:
        if end <n:
            sum += arr[end]
            end +=1
        else:
            break
    elif sum == m:
        count+=1
        sum -=arr[start]
        start +=1
    else:
        sum -= arr[start]
        start +=1
        
    if sum == m:
        count+=1
        sum -= arr[end]
        start+=1
    elif sum > m:
        sum -= arr[start]
        start+=1
    else:
        if end < n:
            sum += arr[end]
            end+=1
        else:
            break

print(count)


    
    

# while n != end:
#     if sum == m:
#         count += 1
#         sum -= arr[start]
#         start += 1
#     elif sum > m:
#         sum -= arr[start]
#         start +=1
#     else:
#         sum += arr[end]
#         end+=1

# print(count)

# while True:
#     if sum < m:
#         if end < n:
#             sum += arr[end]
#             end += 1
#         else:
#             break
#     elif sum == m:
#         count += 1
#         sum -= arr[start]
#         start += 1
#     else:
#         sum -= arr[start]
#         start += 1

# print(count)
        
# while True:
#     if sum < m:
#         if end < n:
#             sum += arr[end]
#             end+=1
#         else:
#             break
#     elif sum == m:
#         sum -= arr[start]
#         start +=1
#         count+=1
#     else:
#         sum -= arr[start]
#         start +=1

    # if sum >= m:
    #     sum -= arr[start]
    #     start+=1
    # else:
    #     end+=1


