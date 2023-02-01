
# 11004번
# 5 2
# 4 1 2 3 5

# output
# 2


# import sys
# input = sys.stdin.readline


# n,k = map(int,input().split())
# arr = list(map(int,input().split()))
# arr.sort()
# print(arr[k-1])




# 1026번
# 옛날 옛적에 수학이 항상 큰 골칫거리였던 나라가 있었다. 이 나라의 국왕 김민지은 다음과 같은 문제를 내고 큰 상금을 걸었다.

# 길이가 N인 정수 배열 A와 B가 있다. 다음과 같이 함수 S를 정의하자.

# S = A[0] × B[0] + ... + A[N-1] × B[N-1]

# S의 값을 가장 작게 만들기 위해 A의 수를 재배열하자. 단, B에 있는 수는 재배열하면 안 된다.

# S의 최솟값을 출력하는 프로그램을 작성하시오.

# 첫째 줄에 N이 주어진다. 둘째 줄에는 A에 있는 N개의 수가 순서대로 주어지고, 셋째 줄에는 B에 있는 수가 순서대로 주어진다.
# N은 50보다 작거나 같은 자연수이고, A와 B의 각 원소는 100보다 작거나 같은 음이 아닌 정수이다.

# n = 5
# a = 1 1 1 6 0
# b = 2 7 8 3 1

# ->18

# 3
# 1 1 3
# 10 30 20

# ->80



# arr = [5,3,2,1,4]
# for i in range(1,len(arr)+1):
#     print(arr[(-1*i)])
# import sys
# input = sys.stdin.readline

# n = int(input())

# a = list(map(int,input().split()))
# b = list(map(int,input().split()))
# sum_arr = [0]*n
# a.sort(reverse=True)
# b.sort()
# for i in range(n):
#     sum_arr[i] = a[i] * b[i]

# print(sum(sum_arr))




# 1032번

# 시작 -> 실행 -> cmd를 쳐보자. 검정 화면이 눈에 보인다. 여기서 dir이라고 치면 그 디렉토리에 있는 서브디렉토리와 파일이 모두 나온다. 이때 원하는 파일을 찾으려면 다음과 같이 하면 된다.

# dir *.exe라고 치면 확장자가 exe인 파일이 다 나온다.
# "dir 패턴"과 같이 치면 그 패턴에 맞는 파일만 검색 결과로 나온다.
# 예를 들어, dir a?b.exe라고 검색하면 파일명의 첫 번째 글자가 a이고, 세 번째 글자가 b이고, 확장자가 exe인 것이 모두 나온다.
# 이때 두 번째 문자는 아무거나 나와도 된다. 예를 들어, acb.exe, aab.exe, apb.exe가 나온다.

# 이 문제는 검색 결과가 먼저 주어졌을 때,
# 패턴으로 뭘 쳐야 그 결과가 나오는지를 출력하는 문제이다. 패턴에는 알파벳과
# "." 그리고 "?"만 넣을 수 있다. 가능하면 ?을 적게 써야 한다. 그 디렉토리에는 검색 결과에 나온 파일만 있다고 가정하고, 파일 이름의 길이는 모두 같다.


# 첫째 줄에 파일 이름의 개수 N이 주어진다. 둘째 줄부터 N개의 줄에는 파일 이름이 주어진다.
# N은 50보다 작거나 같은 자연수이고 파일 이름의 길이는 모두 같고 길이는 최대 50이다. 파일이름은 알파벳 소문자와 '.' 로만 이루어져 있다.

# 3
# config.sys
# config.inf
# configures

# config????

# 2
# contest.txt
# context.txt

# conte?t.txt


# 3
# c.user.mike.programs
# c.user.nike.programs
# c.user.rice.programs

# c.user.?i?e.programs

# import sys
# input = sys.stdin.readline

# n = int(input())


n = int(input())
a = list(input())
a_len = len(a)
print(a)
print(a_len)
for i in range(n - 1):
    b = list(input())
    for j in range(a_len):
        if a[j] != b[j]:
            a[j] = '?'
print(''.join(a))