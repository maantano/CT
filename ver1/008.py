
# '좋은 수' 구하기

# 주어진 N개의 수에서 다른 두 수의 합으로 표현되는 수가 있다면 그 수를 좋은 수 라고 한다.
# N개의 수중 총 좋은 수는 몇개인가

# 1253번

# 입력 예제
# 1번 줄에 수개의 개수 N
# 2번 줄에 N개의 수의 값(Ai)이 주어진다.
# n = 10
# arr= 1 2 3 4 5 6 7 8 9 10

import sys
input = sys.stdin.readline
n = int(input())
arr = sorted(list(map(int,input().split())))


count = 0
for k in range(n):
    sum = arr[k]
    i = 0
    j = n-1

    while i < j:
        if arr[i] + arr[j] == sum:
            if i != k and j != k:
                count+=1
                print('---------- i != k and j != k ---------')
                print('arr[i] :',arr[i],' | arr[j] :',arr[j])
                print('i ==>',i)
                print('j ==>',j)
                print('k ==>',k)
                print('sum ==>',sum)
                break
            elif i == k:
                i +=1
                print('---------- i == k  ---------')
                print('arr[i] :',arr[i],' | arr[j] :',arr[j])
                
                print('i ==>',i)
                print('j ==>',j)
                print('k ==>',k)
                print('sum ==>',sum)
            elif j == k:
                j -=1
                print('---------- j == k  ---------')
                print('arr[i] :',arr[i],' | arr[j] :',arr[j])
                
                print('i ==>',i)
                print('j ==>',j)
                print('k ==>',k)
                print('sum ==>',sum)
        elif arr[i] + arr[j] < sum:

            i+=1
            print('---------- arr[i] + arr[j] < sum ----------')  
            print('arr[i] :',arr[i],' | arr[j] :',arr[j])
            print('i ==>',i)
            print('j ==>',j)
            print('k ==>',k)
            print('sum ==>',sum)
        else:
            j-=1
            print('---------- else arr[i] + arr[j] > sum ----------')  
            print('arr[i] :',arr[i],' | arr[j] :',arr[j])
            print('i ==>',i)
            print('j ==>',j)
            print('k ==>',k)
            print('sum ==>',sum)
#     if arr[i] + arr[j] == m:
#         count +=1
#         i+=1
#         j-=1
#     elif arr[i] + arr[j] >= m:
#         j -= 1
#     else:
#         i += 1
print(count)
# print(count)

