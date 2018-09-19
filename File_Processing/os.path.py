import os.path

## return file pwd
print(os.path.abspath("mkdir.py"))

## return pwd
cur_path = os.path.dirname(__file__)
print("當前路徑：" + cur_path) 