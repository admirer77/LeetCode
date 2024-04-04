def max_erasure(l):

    ls = []

    for i in range(len(l)):
        lst = []
        j = i
        while j < len(l) and l[j] not in lst:
            lst.append(l[j])
            j += 1
        ls.append(lst)

    max1 = 0
    
    for i in range(len(ls)):
        sum1 = sum(ls[i])

        if sum1 > max1:
            max1 = sum1
    
    return max1

l = [4,2,4,5,4,6,5,7]

res = max_erasure(l)

print(res)