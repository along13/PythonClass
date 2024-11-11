import json

data = '''
[{"name": "小明",
    "height": "170",
    "age": "18"
}, {
     "name": "小红",
    "height": "165",
    "age": "20"
    }]
'''

print(type(data))
#json类型的数据转化为python类型的数据
new_data = json.loads(data)
#获取数据
name = new_data[0]['name']
new_name = new_data[0].get('name')
#打印转化后的数据类型
print(type(new_data))

print(name)
print(new_name)