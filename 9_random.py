import random

#  seq中隨機取值
print(random.choice([1,3,5]))

#  seq中，隨機取2值
print(random.sample([1,3,5],2))

# 將既有的seq隨幾排序
_list = [20, 16, 10, 5]
random.shuffle(_list)
print (_list)

#  0-1之間隨意取值
print(random.random())

# 隨機取這兩數（float）之間任一值
print(random.uniform(10, 14))