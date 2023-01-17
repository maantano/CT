
# panpalindrome
# x = 121
# x = -121
x = 10
if x <0:
    answer = False
else:
    ori = x
    reverse=0
    while x:
        remainder = x % 10
        x=x//10
        reverse=reverse*10+remainder
    if reverse == ori:            
        answer=True
    else:
        answer=False

print(answer)