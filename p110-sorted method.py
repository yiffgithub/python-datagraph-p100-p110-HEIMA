'''
ガ展列sort方法
在学习了将函数作为参数传递后，我们可以学习列表的s0下t方法来对列表进行自定义排序
'''

mylist = [["a",33],["b",54],["c",41]]
#排序，基于待命函数

def choose_sort_key(element):
    return element[1]

mylist.sort(key=choose_sort_key,reverse= True)
print(mylist)

# or second way of lambda 函数
mylist.sort(key=lambda element:element[0],reverse=True)
print(mylist)