# animals list
animals = ['cat', 'dog', 'monkey', 'lion', 'elephant', 'tiger']

# slice the first three animals in animals list
L0 = animals[0:3] # 切片列表中的0-3（不包含3）位置的元素
print(L0) # prints ['cat', 'dog', 'monkey']

L1 = animals[:3] # 第一个索引是0可以省略
print(L1) # prints ['cat', 'dog', 'monkey'], same as above

L2 = animals[-3:-1] # 支持倒数切片
print(L2) # prints ['lion', 'elephant'] 索引倒数第三个到倒数第一个，不包含倒数第一个

L3 = animals[-3:] # 索引倒数第三个到最后一个
print(L3) # prints ['lion', 'elephant', 'tiger']

L4 = animals[:4:2] # 索引前四个，每两个取一个
print(L4) # prints ['cat', 'monkey']

L5 = animals[::2] # 索引从第一个到最后一个，每两个取一个
print(L5) # prints ['cat', 'monkey', 'elephant']

L6 = animals[:] # 原样复制了animals list
print(L6) # prints ['cat', 'dog', 'monkey', 'lion', 'elephant', 'tiger']

# fruits tuple
fruits = ('apple', 'orange', 'watermelon', 'banana', 'strawberry', 'pineapple')
# tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple
T0 = fruits[1:3]
print(T0) # prints ('orange', 'watermelon')

# 字符串'xxx'也可以看成是一种list，每个元素就是一个字符
Character_String = 'ABCDEFGHIGKLMN'[0:3]
print(Character_String)