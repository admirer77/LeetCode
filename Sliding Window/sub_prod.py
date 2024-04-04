def sub_prod(l,k):

    def prod(s):
        
        prod = 1

        for i in range(len(s)):
            prod *= s[i]
        
        return prod


    count = 0

    for i in range(len(l)):
        ls = [1]
        
        j = i

        while j < len(l) and prod(ls) < k:

            ls.append(l[j])

            if prod(ls) < k:
                count += 1
            j += 1
        
    return count


# --- Driver Code ---

l = [10,5,2,6]
k = 100

res = sub_prod(l,k)

print(res)
