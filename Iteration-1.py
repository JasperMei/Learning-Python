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

