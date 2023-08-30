#jason的本质就是字典和包含字典的列表在这里我们练习字典、列表转json，再转回来
import json
# 准备列表，列表每一个元素都是字典，将其转换为Json
#如果是中文就需要 ensure_ascii= False
# 列表转换成str（json）
data = [{"name": "小杨", "age": 11},{"name": "小金","age":13},{"name": "小沈" , "age":16}]
json_str = json.dumps(data , ensure_ascii= False)
print(type(json_str))
print(json_str)
#准备字典，做同样的事
#字典转换成str（json）
d = {"name": "周董", "addr":"台北"}
json_str = json.dumps(d, ensure_ascii=False)
print(type(json_str))
print(json_str)
# 将json字符串转为python数据类型{{k:v,k:v}, {k: v, K:v}}
#这是一个str
s= '[{"name": "小杨", "age": 11},{"name": "小金","age":13},{"name": "小沈" , "age":16}]'
l = json.loads(s)
print(type(l))
print(l)
# 同样的事情从str转换为dic，这样子就可以把数据当作list/dic操作了
s = '{"name": "周董", "addr":"台北"}'
d = json.loads(s)
print(type(d))
print(d)

