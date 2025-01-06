import numpy as np

#使用数组标量类型
dt = np.dtype(np.int32)
print(dt)

# int8，int16，int32，int64 可替换为等价的字符串 'i1'，'i2'，'i4'，以及其他。
dt = np.dtype('i4')
print (dt)

#使用端记号
dt = np.dtype('>i4')
print (dt)

#首先创建结构化数据类型
dt = np.dtype([('age', np.int8)])
print (dt)
#再用于nparray对象
a = np.array([(10,),(20,),(30,)], dtype = dt)
print (a)
#文件名称可用于访问age列的内容
print (a['age'])

student = np.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4')])
print(student)


#shape返回数组维度
a = np.array([[1,2,3],[4,5,6]])
print(a.shape)
#调整数组大小
a.shape = (3,2)
print(a)

#reshape调整数组大小
b = a.reshape(3,2)
print(b)

#等间隔数字的数组
a = np.arange(24)
print(a)
#3维数组
b = a.reshape(2,4,3)
print(b)