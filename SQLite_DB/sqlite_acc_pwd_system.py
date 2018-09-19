#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def menu():
    os.system("clear")
    print("帳號、密碼管理系統")
    print("----------------------------")
    print("1. 輸入帳號、密碼")
    print("----------------------------")
    print("2. 顯示帳號、密碼")
    print("----------------------------")
    print("3. 修改密碼")
    print("----------------------------")
    print("4. 刪除帳號、密碼")
    print("----------------------------")
    print("0. 離開程式")
    print("----------------------------")


def disp_data():
    cursor = conn.execute("SELECT * FROM password")
    print("帳號\t密碼")
    print("====================")
    for row in cursor:
        print("{}\t{}".format(row[0], row[1]))
    input("按任意鍵返回主選單")


def input_data():
    while True:
        sql_name = input("請輸入帳號（Enter => 停止輸入）：")
        if sql_name == "":  
            break   
        # 先搜尋是不是有相同帳號存在
        sqlstr = "SELECT * FROM password WHERE name = '{}'".format(sql_name) 
        cursor = conn.execute(sqlstr)
        # 只會有一筆，所以用 fetchone
        row = cursor.fetchone() 
        # 如果帳號不存在，會回傳 None，表示沒有資料，跳出迴圈
        if row != None: 
            print("{} 此帳號已存在".format(sql_name))
            continue

        sql_pass = input("請輸入密碼：")
        sqlstr = ("INSERT INTO password VALUES ('{}', '{}')".format(sql_name, sql_pass))
        conn.execute(sqlstr)

        conn.commit()
        print("{} 已儲存完畢".format(sql_name))


def edit_data():
    while True:
        sql_name = input("請輸入要修改的帳號（Enter => 停止輸入）：")
        if sql_name == "":
            break
        # 先搜尋是不是有相同帳號存在
        sqlstr = "SELECT * FROM password WHERE name = '{}'".format(sql_name)
        cursor = conn.execute(sqlstr)
        row = cursor.fetchone()
        # 如果回傳空值，代表沒有此帳號資料，就重新此迴圈
        if row == None:
            print("{} 帳號不存在".format(sql_name))
            continue
        # 如果有資料，進行輸入新密碼
        print("原來的密碼為 {}".format(row[1]))
        sql_pass = input("請輸入新密碼：")
        sqlstr = "UPDATE password SET pass = '{}' WHERE name = '{}'".format(sql_pass, sql_name)
        conn.execute(sqlstr)
        conn.commit()
        print("密碼更改完畢，請按任意鍵返回主選單")
        break


def delete_data():
    while True:
        sql_name = input("請輸入要刪除的帳號（Enter => 停止輸入）")
        if sql_name == "":
            break
        sqlstr = "SELECT * FROM password WHERE name = '{}'".format(sql_name)
        cursor = conn.execute(sqlstr)
        row = cursor.fetchone()
        if row == None:
            print("{} 帳號不存在".format(sql_name))
            continue
        print("確定刪除 {} 的資料？：".format(sql_name))
        yn = input("（Y/N）？")
        if (yn == "Y" or yn == "y"):
            sqlstr = "DELETE FROM password WHERE name = '{}'".format(sql_name)
            conn.execute(sqlstr)
            conn.commit()
            input("已刪除完畢，請按任意鍵返回主選單")
            break


# Main Code
import sqlite3
import os

conn = sqlite3.connect('password.sqlite')
while True:
    menu()
    choice = input("請輸入您的選擇：")
    print()
    if choice == '1':
        input_data()
    elif choice == '2':
        disp_data()
    elif choice == '3':
        edit_data()
    elif choice == '4':
        delete_data()
    else:
        break

conn.close()
print("程式執行完畢！")
