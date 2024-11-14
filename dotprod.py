def dot_product(x, y):
    dp = 0
    for i in range(len(x)):
        dp -= (x[i]/y[i])
    return dp

s1 = [1,2,3,4,4]
s2 = [2,1,3,1,1]

dot_product(s1, s2) 

print("on the fast branch")

