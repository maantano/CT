
# 슬라이딩 윈도우
# 슬라이딩 윈도우 알고리즘은 2개의 포인터로 범위를 지정한 다음, 범위(window)를 유지한 채로 이동(sliding)하며 문제를 해결한다.


# DNA 비밀먼호

# 12891번

# 입력 예제

# 문자열 문자는 {'A','C','G','T'}
# 부분 문자열에서 등장하는 문자의 개수가 특정 개수 이상이어야 비밀번호로 사용할 수 있다.
# 'AAACCTGCCAA'이고 민호가 뽑을 문자열의 길이는 4라고 가정하보면, A는 1개이상, C는 1개 이상, G는 한개이상, T는 0개 이상 등장해야 비밀번호로 사용할 수 있다고 가정하면,
# ACCT는 G가 한개 이상 등장해야한다는 조건을 만족하지 못해 비밀번호로 사용할 수 없지만, GCCA는 모든 조건을 만족하므로 비밀번호로 사용할 수 있다.

# 1번 줄에 민호가 임의로 만든 DNA 문자열의 길이 ISI와 
# 비밀번호로 사용할 부분 문자열의 길이 IPI가 주어진다.

# 2번째 줄에 민호가 임의로 만든 DNA문자열이 주어진다.
# 3번째 줄에 부분 문자열에 포함되어야 할 {A,C,G,T}의 최소 개수 공백 문자를 사이에 두고 주어진다.

# ==> 각각의 수는 ISI보다 작거나 같은 음이 아닌 정수로, 총합은 ISI보다 작거나 같다는 것이 보장된다.




# 9 8
# CCTGGATTG
# 2 0 1 1

# 4 2
# GATA
# 1 0 0 1



import sys
input = sys.stdin.readline

checkList = [0]*4
myList = [0]*4
checkSecret = 0


def myadd(c):
    global checkList,myList,checkSecret

    if c == 'A':
        myList[0]+=1
        if myList[0] == checkList[0]:
            checkSecret +=1
    elif c =='C':
        myList[1]+=1
        if myList[1] == checkList[1]:
            checkSecret +=1
    elif c =='G':
        myList[2]+=1
        if myList[2] == checkList[2]:
            checkSecret +=1    
    elif c =='T':
        myList[3]+=1
        if myList[3] == checkList[3]:
            checkSecret +=1

def myremove(c):
    global checkList,myList,checkSecret

    if c == 'A':
        if myList[0] == checkList[0]:
            checkSecret -=1
        myList[0]-=1
    elif c =='C':
        if myList[1] == checkList[1]:
            checkSecret -=1
        myList[1]-=1
    elif c =='G':
        if myList[2] == checkList[2]:
            checkSecret -=1    
        myList[2]-=1
    elif c =='T':
        if myList[3] == checkList[3]:
            checkSecret -=1
        myList[3]-=1


S,P = map(int,input().split())
A = str(input())
checkList = list(map(int,input().split()))
result = 0

for i in range(4):
    if checkList[i] ==0:
        checkSecret +=1

for i in range(P):
    myadd[A[i]]

if checkSecret ==4:
    result +=1

for i in range(P,S):
    j = i-P
    myadd[A[i]]
    myremove[A[j]]
    if checkSecret ==4:
        result += 1

print(result)


# tmp = 1
# for i in d:
#     if(tmp <= n):
#         arr.append(i)
#         tmp+=1

# print(arr)


    


    





"""
슈도 코드
    checkList(비밀번호 체크 리스트)
    myList(현재 상태 리스트)
    checkSecret(몇 개의 문자와 관련된 개수를 충족했는지 판단하는 변수)


    myadd(문자 더하기 함수):
        myList에 새로운 값을 더하고 조건에 따라 checkSecret값 업데이트
    myRemove(문자 빼기 함수):
        myList에 새로운 값을 제거하고 조건에 따라 checkScreret값 업데이트

    S(문자열크기) P(부분 문자열의 크기)
    A(문자열 데이터)

    checkList 데이터 받기
    checkList를 탐색하여 값이 0인 데이터의 개수만큼 checkSecret 값 증가

    P 범위(0~P~1)만큼 myList 및 checkSecret에 적용하고, 유효한 비밀번호인지 판단


    for i 를 P에서 S까지 반복:
        j 선언(i - P)
        한 칸씩 이동하면서 제거되는 문자열과 새로 들어오는 문자열을 처리
        유효한 비밀번호인지(checkSecret ==4) 판단해 결괏괎을 업데이트
        




"""