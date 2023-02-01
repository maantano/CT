def merge_sort(a):
    n = len(a)
    if n <= 1:
        return a
    
    mid = n//2
    
    g1 = merge_sort(a[:mid])
    print(g1)
    g2 = merge_sort(a[mid:])
    result = []
    while g1 and g2:
        if g1[0] < g2[0]:
            result.append(g1.pop(0))
        else:
            result.append(g2.pop(0))       
    while g1:
        result.append(g1.pop(0))
    while g2:
        result.append(g2.pop(0))
    return result


d = [6,8,3,9,10,1,2,4,7,5]
print(merge_sort(d))

# 1. 
# n =10
# mid = 5
# g1 = merge_sort(a[0:5])
# # g1 = merge_sort(a[5:끝])

# 2. 
# n =6
# mid = 2
# g1 = merge_sort(a[0:2])
# # g2 = merge_sort(a[2:끝])

# 3. 
# n = 3
# # mid =