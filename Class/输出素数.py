#输出素数
n = int(input())
def is_prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
# for i in range(2,n+1):
#     if is_prime(i):
#         print(i,end=' ')
print(is_prime(n))