from collections import Counter

def all_ana(s,p):
    k = len(p)
    pval = Counter(p)
    res = []

    for i in range(len(s) - k + 1):
        if Counter(s[i : i+k]) == pval:
            res.append(i)
    
    return res

s = "abab"
p = "ab"

print(all_ana(s,p))