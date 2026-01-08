n = int(input())
m = int(input())
def sum_series(n, m):
    sum = 0
    for x in range(n, m+1, 2):
        sum = sum+x
    return sum

print(sum_series(n,m))
k = sum_series(n, m)
