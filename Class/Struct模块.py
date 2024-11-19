import struct

int_value = 123156456
float_value = 4561.1123
bool_value = True


# 整型打包以后占用四个字节
int_struct = struct.pack('i', int_value)
print(int_struct, len(int_struct))

# 浮点型打包以后占用四个字节
float_struct = struct.pack('f', float_value)
print(float_struct, len(float_struct))

# 布尔型打包以后占用四个字节
bool_struct = struct.pack('?', bool_value)
print(bool_struct, len(bool_struct))

str_value = "da456q1"

# 字符串格式需要转换成字节格式才可以打包，并且还需要提供字符串的长度，默认为1
# 提供的长度小于实际字符串的长度将打包部分数据，造成打包不完整
str_struct = struct.pack('7s', str_value.encode("utf8"))
print(str_struct, len(str_struct))

int_struct = struct.pack('i', 123156456)
float_struct = struct.pack('f', 4561.1123)
bool_struct = struct.pack('?', True)
str_struct = struct.pack('7s', "da456q1".encode("utf8"))

# 解包后类型正常
int_res = struct.unpack("i", int_struct)
print(int_res, type(int_res[0]))

float_res = struct.unpack("f", float_struct)
print(float_res, type(float_res[0]))

bool_res = struct.unpack("?", bool_struct)
print(bool_res, type(bool_res[0]))

str_res = struct.unpack("7s", str_struct)
print(str_res, type(str_res[0]))
