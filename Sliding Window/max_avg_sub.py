def max_avg(l,k):

    def avg(l,k):

        sum = 0

        for i in range(len(l)):

            sum += l[i]
        
        avg1 = sum/k

        return avg1

    avg_max = 0

    for i in range(len(l) - k + 1):

        avg1 = avg(l[i:i+k],k)
        avg_max = max(avg_max,avg1)
        

    return avg_max

l = [1,12,-5,-6,50,3]
k = 4

res = max_avg(l,k)

print(res)
