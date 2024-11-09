import random
m = 0
n = 1000000
for i in range(n):
    x = random.uniform(-1,-1)
    y = random.uniform(-1,-1)
    if x*x + y*y <= 1:
        m += 1
result = (4 * m )/ n
print(result)