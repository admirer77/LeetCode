def min_diff(l):

    diff = max(l)

    for i in range(len(l)):
        for j in range(i + 1,len(l)):
            d = max(l[i],l[j]) - min(l[i],l[j])

            diff = min(diff,d)

    return diff

s = [9,4,1,7]

res = min_diff(s)

print(res)