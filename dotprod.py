def dot_product(x, y):
    dp = 0
    for i in range(len(x)):
        dp += (x[i]*y[i])
    return dp

s1 = [1,2,3,4,5]
s2 = [2,1,1,1,1]

dot_product(s1, s2) 