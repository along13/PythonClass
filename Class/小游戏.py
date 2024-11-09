#开发一个循环5次的小游戏，每次随机产生两个100以内的数字，让用户计算两个数字之和并输入结果，如果输入正确，则加一分，如果计算结果错误不加分。如果正确率大于等于80%，则成功
import random
score = 0
for i in range(5):
    a = random.randint(1,100)
    b = random.randint(1,100)
    print(a,b)
    c = int(input("请输入结果："))
    if c == a+b:
        score += 1
        print("正确")
    else:
        print("错误")
if score >= 4:
    print("闯关成功")
else:
    print("闯关失败")
