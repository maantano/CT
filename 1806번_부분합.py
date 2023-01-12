
# 부분합은 투포인트로 품

import sys
input = sys.stdin.readline




#  투포인터 소스 코드 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# N,S = (map(int,input().split())) # N,S 선언
# arr = list(map(int,input().split())) # 수열 리스트 선언

# start, end = 0,0 # 포인터 선언
# sum =0 # 합 변수 선언
# answer  = 1000001 # 최대값 길이로 지정
# # min_length = sys.maxsize # 최대값 길이로 지정



# while True:
#     if sum >= S:
#         answer = min(answer,end-start)
#         sum -= arr[start]
#         start +=1
#     elif end == N:
#         break
#     else:
#         sum += arr[end]
#         end +=1

# if answer == 1000001:
#     answer = 0
# print(answer)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 부분 합 소스 코드

n,s = map(int,input().split())
_list = list(map(int,input().split()))

prefix = [0] * (n+1)
start,end = 0,1

for i in range(1,n+1):
    prefix[i] = prefix[i-1] + _list[i-1]
print(prefix)
answer = 1000001
while start < n:
    if prefix[end] - prefix[start] >= s:
        answer = min(answer,end-start)
        start +=1
    else:
        if end <n:
            end+=1
        else:
            start +=1
if answer == 1000001:
    print(0)
else:
    print(answer)




    



# while start < N: # 모든 부분합에 대해서 확인
#     # 만약 총 합이 S가 넘는다면, left를 하나씩 옮겨보면서 어디까지 길이가 줄어드나 확인
#     if sum >= S: # 부분합이  >= S이면
#         min_length = min(min_length, end - start) # end - start 의 최소 값(부분합의 길이 중 가장 짧은것을 찾아야 함)
#         sum -= arr[start] # 합에서 빼줌
#         start+=1 # 
#     elif end == N: #
#         break #
#     # 만약 총합이 S를 넘지 않는다면, right 을 오른쪽으로 한칸씩 옮기며 총합이 S를 넘을때까지 더함
#     else: 
#         sum += arr[end] #
#         end +=1 #

# if min_length == sys.maxsize: #
#     print(0) #
# else:
#     print(min_length)





