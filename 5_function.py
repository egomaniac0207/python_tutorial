# 1. def範例
def test(value1, value2):
    return value2

# 呼叫時可以使用dict方式，避免參數過長不知道是指哪一個
print(test(value1=1,value2=3))
# 因為支援dict，所以傳值順序可以不依照function設定
print(test(value2=3,value1=2))

#-------------------------
# 2. def 預設值
def test2(value=2):
    return value
# 使用傳入的值為先
print(test2("3"))
# 使用預設
print(test2())

#-------------------------
# 3. def支援支援*參數方式，可以支援傳入多參數方式
def test3(*value):
    ttl=0
    for i in value:
        ttl=ttl+i
    print(ttl/len(value))

test3(1,3,5)