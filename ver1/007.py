
# 주몽의 명령

# 1940번

# 입력 예제
# 첫번째 줄에 재료의 개수 N
# 두번째 줄에 갑옷을 만드는데 필요한 수 M
# 세번째 줄에 N개의 재료들이 가ㅣㄴ 고유한 번호들이 공백을 사이에 두고 주어진다.
# N = 6
# M = 9
# arr = 2 7 4 1 5 3

import sys
input = sys.stdin.readline
n,m = map(int,input().split())
arr = sorted(list(map(int,input().split())))

i = 0
j = n-1
count = 0

while i < j:
    if arr[i] + arr[j] == m:
        count +=1
        i+=1
        j-=1
    elif arr[i] + arr[j] >= m:
        j -= 1
    else:
        i += 1

print(count)

    


    





# """
#     aaa


# """