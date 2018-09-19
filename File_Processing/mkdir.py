import os
dir = "myDir"
if not os.path.exists(dir):
    os.mkdir(dir)
    print("建立目錄 " + dir)
else:
    print("此目錄已存在")
