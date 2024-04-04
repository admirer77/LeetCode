
def k_beauty(n,k):

    x = str(n)

    count = 0

    for i in range(len(x)-k+1):
        if int(x[i:i+k]) != 0 and n % int(x[i:i+k]) == 0:
            count += 1
    
    return count




n = int(input())
k = int(input())

res = k_beauty(n,k)

print(res)