# 1075번

# 두 정수 N과 F가 주어진다. 지민이는 정수 N의 가장 뒤 두 자리를 적절히 바꿔서 N을 F로 나누어 떨어지게 만들려고 한다.
# 만약 가능한 것이 여러 가지이면, 뒤 두 자리를 가능하면 작게 만들려고 한다.

# 예를 들어, N=275이고, F=5이면, 답은 00이다.
# 200이 5로 나누어 떨어지기 때문이다. N=1021이고, F=11이면, 정답은 01인데, 1001이 11로 나누어 떨어지기 때문이다.

# 예제 입력 1 
# 1000
# 3
# 예제 출력 1 
# 02

# 예제 입력 2 
# 2000000000
# 100
# 예제 출력 2 
# 00

# 예제 입력 3 
# 23442
# 75
# 예제 출력 3 
# 00

import sys

# input = sys.stdin.readline1

n = input()
f = int(input())
temp = int(n[:-2]+'00')
while True:
    if temp % f ==0:
        break
    temp +=1

print(str(temp)[-2:])




# 472
# 385

# 2360
# 3776
# 1416
# 181720
# 2588반
import sys
input = sys.stdin.readline

n = int(input())
m = list(input().rstrip())
tmp = 0
for i in range(1,len(m)+1):
    print(int(m[-i])*n)
    tmp+=int(str(int(m[-i])*n)+('0'*(i-1)))
print(tmp)


