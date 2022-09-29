from fileinput import close
import json

# 建議直接用第二種寫法
# 第一種寫法，寫入並讀取，這種寫法就會一直咬著資源，直到close釋放為止
_file=open("test.txt",mode="w",encoding="utf-8")
_file.write("hello world")
_file.close()

_output = open("test.txt",mode="r")
print(_output.read())
_output.close()

# 第二種寫法，較快速，並且會自動加上close把資源釋放
with open("test2.txt", mode="w",encoding="utf-8") as _file2:
    _file2.write("this is second hellp\o world")

with open("test2.txt", mode="r",encoding="utf-8") as _output2:
    print(_output2.read())