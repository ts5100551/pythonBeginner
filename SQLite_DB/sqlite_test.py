import sqlite3
conn = sqlite3.connect('test.sqlite') # 建立資料庫連線
cursor = conn.cursor() # 建立 cursor 物件
# 建立資料表
sqlstr = 'CREATE TABLE IF NOT EXISTS table01 ("num" INTEGER PRIMARY KEY NOT NULL, "tel" TEXT)'
cursor.execute(sqlstr)

# 新增一筆紀錄
sqlstr = 'insert into table01 values(1, "03-5100551")'
cursor.execute(sqlstr)

# 刪除資料表
sqlstr = 'DROP TABLE table01'
cursor.execute(sqlstr)

conn.commit() # 主動更新
conn.close() # 關閉連線