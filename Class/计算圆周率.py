import math
#近似计算圆周率
PI = 0.0
k = 1.0
flag = 1
while (1 / k) > 1e-6:
    print(PI)
    PI += flag * (1 /k)
    flag = -flag
    k += 2
print(PI * 4)