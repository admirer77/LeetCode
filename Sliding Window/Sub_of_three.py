def sub_3(l):

    ls = []

    for i in range(len(l)):
        lst = []
        j = i
        while j < len(l) and j < i + 3 and l[j] not in lst:
            lst.append(l[j])
            j += 1
        if len(lst) == 3:
            ls.append(lst)
    
    print(ls)

    return len(ls)

s = "abcddfghiihg"

res = sub_3(s)

print(res)