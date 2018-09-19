import os
dir = "myDir"
if os.path.exists(dir):
    os.rmdir(dir)
    print(dir + " 目錄已刪除")
else:
    print(dir + " 目錄未建立")