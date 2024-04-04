def rep_dna(s):

    seen = set()
    res = set()

    for i in range(len(s) - 9):
        substr = s[i:i+10]

        if substr in seen:
            res.add(substr)
        
        seen.add(substr)
    
    return list(res)

s = "AAAAACCCCCAAAAACCCCCAAAAAsoidnisen"

print(rep_dna(s))