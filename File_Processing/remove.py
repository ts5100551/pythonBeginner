import os
file = "myfile.txt"
if os.path.exists(file):
    os.remove(file)
    print("成功刪除 " + file)
else:
    print("尚未建立 %s 檔案" %file)