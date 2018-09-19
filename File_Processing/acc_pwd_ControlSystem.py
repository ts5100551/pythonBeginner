#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 18:16:03 2018

@author: ts5100551
"""

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


def readData():
    with open('password.txt', 'r', encoding = 'UTF-8-sig') as f:
        fileData = f.read()
        if fileData != "":
            data = ast.literal_eval(fileData)
            return data
        else:
            return dict()


def disp_data():
    print("帳號\t密碼")
    print("====================")
    for key in data:
        print("{}\t{}".format(key, data[key]))
    input("按任意鍵返回主選單")


def input_data():
    while True:
        name = input("請輸入帳號（Enter => 停止輸入）：")
        if name == "":
            break
        if name in data:
            print("{} 帳號已存在".format(name))
            continue
        password = input("請輸入密碼：")
        data[name] = password

        with open('password.txt', 'w', encoding = 'UTF-8-sig') as f:
            f.write(str(data))
            print("{} 已被儲存完畢".format(name))


def edit_data():
    while True:
        name = input("請輸入要修改的帳號（Enter => 停止輸入）：")
        if name == "":
            break
        if not name in data:
            print("{} 帳號不存在！".format(name))
            continue
        print("原來的密碼是：{}".format(data[name]))
        password = input("請輸入新密碼：")
        data[name] = password

        with open('password.txt', 'w', encoding = 'UTF-8-sig') as f:
            f.write(str(data))
            print("密碼更改完畢，請按任意鍵返回主選單")
            break


def delete_data():
    while True:
        name = input("請輸入要刪除的帳號（Enter => 停止輸入）")
        if name == "":
            break
        if not name in data:
            print("{} 帳號不存在！".format(name))
            continue
        print("確定刪除 {} 的資料？：".format(name))
        yn = input("（Y/N）？")
        if (yn == "Y" or yn == "y"):
            del data[name]

            with open('password.txt', 'w', encoding = 'UTF-8-sig') as f:
                f.write(str(data))
                input("已刪除完畢，請按任意鍵返回主選單")
                break


### 主程式從這開始 ###
import os, ast
data = dict()

data = readData() #讀取文字檔後轉成 dict
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

print("程式執行完畢！")




