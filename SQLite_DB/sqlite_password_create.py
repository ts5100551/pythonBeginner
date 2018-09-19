import sqlite3
conn = sqlite3.connect('password.sqlite') # 建立資料庫
cursor = conn.cursor()
# 建立資料表
sqlstr = 'CREATE TABLE IF NOT EXISTS password ("name" VARCHAR PRIMARY KEY NOT NULL, "pass" VARCHAR NOT NULL)'
cursor.execute(sqlstr)

# 新增三筆資料
name = ["Adia", "Lucky", "Pig"]
pwd = ["st5100551", "ilu851101", "pigpig"]
for i in range(3):
    sqlstr = 'INSERT INTO password values ("{}", "{}")'.format(name[i], pwd[i])
    cursor.execute(sqlstr)

# 完成
conn.commit()
conn.close()