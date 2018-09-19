import os
import shutil
cur_path = os.path.dirname(__file__) #get pwd
destfile = cur_path + "/" + "newFile.py"
shutil.copyfile("shutil.py", destfile)