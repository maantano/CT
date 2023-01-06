"""
최빈값 구하기

최빈값은 주어진 값 중에서 가장 자주 나오는 값을 의미합니다. 
정수 배열 array가 매개변수로 주어질 때,
최빈값을 return 하도록 solution 함수를 완성해보세요. 최빈값이 여러 개면 -1을 return 합니다.

////////////////////////////////////////
입력 예제.

array=[1, 2, 3, 3, 3, 4]
result=3

array=[1, 1, 2, 2]
result=-1

array=[1]
result=1

////////////////////////////////////////

"""


def solution(array: list) -> int:
    dict = {}
    # for 반복문으로 입력 list 순회
    for num in array:
        # 딕셔너리에 현재 값이 할당되있지 않다면 1 할당
        if num not in dict:
            dict[num] = 1
        # 그렇지 않을 시, 증감
        else:
            dict[num] += 1
    
    # print(dict)
            
    # 딕셔너리의 벨류값 기준으로 desc 정렬
    result = sorted(dict.items(), key=lambda x: x[-1], reverse=True)
    
    # print(result)
    # print(len(result))
    
    if len(result) <= 1:
        return result[0][0]
    # 최빈값이 여러개면, -1 반환
    return result[0][0] if result[0][-1] != result[1][-1] else -1


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 



array=[1, 2, 3, 3, 3, 4]
print(solution(array))


