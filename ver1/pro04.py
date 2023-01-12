# 옹알이
# https://school.programmers.co.kr/learn/courses/30/lessons/120956
# https://velog.io/@zinu/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%98%B9%EC%95%8C%EC%9D%B4-1%ED%8C%8C%EC%9D%B4%EC%8D%AC

# 머쓱이는 태어난 지 6개월 된 조카를 돌보고 있습니다. 
# 조카는 아직 "aya", "ye", "woo", "ma" 네 가지 발음을 최대 한 번씩 사용해 조합한(이어 붙인) 발음밖에 하지 못합니다.
# 문자열 배열 babbling이 매개변수로 주어질 때, 머쓱이의 조카가 발음할 수 있는 단어의 개수를 return하도록 solution 함수를 완성해주세요.



can = ["aya", "ye", "woo", "ma"]
babbling = ["aya", "yee", "u", "maa", "wyeoo"]
result=1
# ["aya", "yee", "u", "maa", "wyeoo"]에서 발음할 수 있는 것은 "aya"뿐입니다. 따라서 1을 return합니다.


# babbling = ["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]
# result=3
# ["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]에서 발음할 수 있는 것은 "aya" + "ye" = "ayaye", "ye", "ye" + "ma" + "woo" = "yemawoo"로 3개입니다. 따라서 3을 return합니다.

# from itertools import permutations

# A = ['a', 'b', 'c', 'd']
# P = list(permutations(A, 2))

# P = [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]



from itertools import permutations

def sayit(babbling):
    can = ["aya", "ye", "woo", "ma"]
    answer = 0
    word = []
    for i in range(1,len(can)+1):
        for j in permutations(can,i):
            word.append(''.join(j))
    for i in babbling:
        if i in word:
            answer +=1
    return answer

sayit(babbling)


