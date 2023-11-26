import requests
from pyquery import PyQuery as pq
#視窗元件清單
from tkinter import Tk   # 代表視窗本身
from tkinter import Label
from tkinter import Button

win = Tk()  # 建立視窗物件
win.title("這是視窗版爬蟲範例")
win.geometry("800x600") # 呼叫 geometry 設定視窗大小
# 加入標籤
lab1 = Label(win, text="網址:")   #第一個加入視窗 win 的物件
lab1.pack()
lab2 = Label(win, text="目標:")   #第二個加入視窗 win 的物件

#第三個物件 : 按鈕
okBtn = Button(win)

#win.resizable(0,0)
win.mainloop()   # 啟動視窗執行 並無窮執行直到 user關閉


#response = requests.get(url="https://tw.stock.yahoo.com/")
# print(response.text)