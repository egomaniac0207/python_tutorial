# 1. 數字
3
4.5

#-------------------------
# 2. 字串
"123"

#-------------------------
# 3. list清單，用[]來代表，裡面的值可以調整
[1, 2, 3]
fruit_list = ["apple","banana","melon"]
print(fruit_list[1])
print(fruit_list[0]*2)

# 3-1. 刪除list項目
del fruit_list[2]
print(fruit_list)

# 3-2. len項目數量
print(len(fruit_list))

# 3-3. max, min取得最大與最小
number_list = [0,4,6,2,7,4]
print(max(number_list))
print(min(number_list))

# 3-4. 新增list項目
number_list.append("new")
print(number_list)

#-------------------------
# 4. tuple清單，有別於list，用()來顯示，主要差別是不能調整，效能較快
companies_tuple=("aaa","bbb","ccc")
print(companies_tuple)

# 4-1. tuple轉換成list
companies_list=list(companies_tuple)
print(companies_list)

#-------------------------
# 5. dict，常見key value功能
_dict = {"apple":123,"bababa":"ccc"}
print(_dict["apple"])

#-------------------------
# 6. 平方
print(3**2)