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