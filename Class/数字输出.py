a = input("请输入一个5位数字:")
if len(a) != 5:
    print("输入的数字不是5位数")
else:
    # 判断是否为数字
    if a.isdigit():
        # 输出数字的十位和个位
        print("十位数字是：", a[3])
        print("个位数字是：", a[4])
    else:
        print(str(a)+"不是数字")
