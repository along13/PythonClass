#定义一个学生类
class Student(object):
    # __init__是一个特殊方法用于在创建对象时进行初始化操作
    # 通过这个方法我们可以为学生对象绑定name和age两个属性
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):# 绑定的实例方法
        print('%s正在学习%s.' % (self.name, course_name))
def main():# 主函数

    s = Student('xiao',20)
    print(s.name)
    print(s.age)
    s.study('Python')
    # PEP 8要求标识符的名字用全小写多个单词用下划线连接
    # 但是部分程序员和公司更倾向于使用驼峰命名法(驼峰标识)
main()