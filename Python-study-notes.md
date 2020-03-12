# Python Study Notes
## Notices for programming environment configuration
- 储存程序的文件夹名字不要包含`'`之类字符，Visual Studio Code这类的编译环境可能无法找到路径

### 递归(Recursion)函数

[递归](https://zh.wikipedia.org/wiki/%E9%80%92%E5%BD%92)，又译为递回，在数学与计算机科学中，是指在函数的定义中使用函数自身的方法。递归一词还较常用于描述以自相似方法重复事物的过程。例如，当两面镜子相互之间近似平行时，镜中嵌套的图像是以无限递归的形式出现的。也可以理解为自我复制的过程。

**Tips:**
- 使用递归函数需要注意防止栈溢出
### 切片（Slice）
*Slice-1.py*
```py
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
print(Character_String) # prints ABC
```
### 迭代(Iteration)
迭代作为一种循环，是是程序中对一组指令（或一定步骤）的重复，利用变量的原值推算出变量的一个新值，这种改变赋值——或者叫做可变状态——是迭代的特征。与递归不同的是，递归是在函数中不断调用自身，迭代是A不停的调用B。通俗地讲迭代是通过循环来遍历给定了一个对象。
*Iteration-1.py*
```py
# NameAge dict
NameAge = {'Jack':20, 'Tony':30, 'Mary':40, 'John':50}
for key in NameAge:
    print(key)
'''
dict 默认按key迭代
prints  Jack
        Tony
        Mary
        John
'''
print("------分隔------")
# 按value迭代
for value in NameAge.values():
    print(value)
'''
prints  20
        30
        40
        50
'''
print("------分隔------")
# 按key-value迭代
for key, value in NameAge.items():
    print(key, value)
'''
prints  Jack 20
        Tony 30
        Mary 40
        John 50
'''
```

#### 如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断
*Iteration-2.py*
```py
# 判断对象是否可迭代
from collections.abc import Iterable
print(isinstance('abc', Iterable))
print(isinstance([1,2,3], Iterable))
print(isinstance(123, Iterable))
'''
prints
True
True
False
'''
```
#### Python内置的enumerate函数可以把一个list变成索引-元素对
```py
# 下标循环
for i, value in enumerate(['A', 'B', 'C']):
     print(i, value)
'''
prints
0 A
1 B
2 C
'''
```

[递归和迭代的区别](https://blog.csdn.net/swliao/article/details/5337896)

## Reference
[Python](https://docs.python.org/3.8/library/index.html)
[廖雪峰Python教程](https://www.liaoxuefeng.com/wiki/1016959663602400)
[Programiz]https://www.programiz.com/python-programming
[learnpython.org](https://www.learnpython.org/)

## 写在最后
此文档为本人学习Python的纪录材料，感谢文档中涉及知识的贡献者。若文档内容对您有所帮助我倍感荣幸，但由于本人水平有限，难免挂一漏万，存在错误讹说，还盼望读者批评指正。