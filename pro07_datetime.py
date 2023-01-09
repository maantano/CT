# https://school.programmers.co.kr/learn/courses/30/lessons/120820
# 나이 출력

# 머쓱이는 40살인 선생님이 몇 년도에 태어났는지 궁금해졌습니다. 나이 age가 주어질 때, 2022년을 기준 출생 연도를 return 하는 solution 함수를 완성해주세요.
		
	
# age = 40
# result=1983
age = 23
result=2000


import datetime


d = datetime.datetime.now()
# print (d)
# print (d.year,'년 ', d.month,'월 ', d.day,' 일')
# print (d.hour,'시 ',d.minute,'분 ',d.second,'초')

# now = datetime.datetime.now()

# print (now.strftime("%Y/%m(%B)/%d %A %p %I:%m:%S, 일년 중 %U 번째주, 일년 중 %j번째 날 "))
# print (now.strftime("%Y"))



def solution(age):
    now = datetime.datetime.now()
    return int(now.strftime("%Y")) - age
    


solution(age)