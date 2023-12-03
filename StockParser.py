import requests
from pyquery import PyQuery as pq
#視窗元件清單
from tkinter import Tk   # 代表視窗本身
from tkinter import Label
from tkinter import Button
from tkinter import *
from tkinter import StringVar

#
def StockQueryClick():  # 下載網頁


def clearURLEntry():


#
# 動態變數 必須要在 Tk() 產生後才可以宣告
#dataVar = StringVar()

win = Tk()  # 建立視窗物件

win.title("視窗版股票價格爬蟲範例")
win.geometry("800x300") # 呼叫 geometry 設定視窗大小

# 動態變數與 UI 物件綁定 一旦變數的內容有變動 會自動更新UI畫面
# 省去每次要呼叫 config(text='新內容') 的行為
resultMsg = StringVar()
# 產生一個新的面板(frame) 把所有標籤與 entry 放入此 frame 在與 主視窗綁定
win1 = Frame(win)
btnFrame = Frame(win)
# 加入標籤
lab1 = Label(win1,text="台積電:" , font=('Arial',15), bg="yellow", fg="red")   #第一個加入視窗 win 的物件
lab1.grid(column=0, row=0, padx=10)
lab2 = Label(win1, text="智邦:" , font=('Arial',15), bg="yellow", fg="red")   #第一個加入視窗 win 的物件
lab2.grid(column=0, row=1, padx=10)
lab3 = Label(win1, text="聯發科:" , font=('Arial',15), bg="yellow", fg="red")   #第一個加入視窗 win 的物件
lab3.grid(column=0, row=2, padx=10)
#加入 股票文字框輸入
_2330Price = Entry(win1, font=('Arial',15), fg='blue',width=40)
_2330Price.grid(column=1,row=0)
_2345Price = Entry(win1, font=('Arial',15), fg='blue',width=40)
_2345Price.grid(column=1,row=1)
_2545Price = Entry(win1, font=('Arial',15), fg='blue',width=40)
_2545Price.grid(column=1,row=2)
# 顯示在畫面上
#lab1.pack()
#lab2.pack()
#lab3.pack()
#_2330Price.pack()
#_2345Price.pack()
#_2545Price.pack()
# 請注意 lab3 用 textvariable 與動態變數綁定 只要變數改變 訊息就會顯示在 畫面上
#第三個物件 : 按鈕
okBtn = Button(btnFrame ,font=('Arial',15), text="更新" , fg='blue', command=StockQueryClick)
okBtn.grid(column=0, row=0)
#okBtn.pack()
closeBtn = Button(btnFrame ,font=('Arial',15), text="停止" , fg='blue', command=clearURLEntry)
closeBtn.grid(column = 1, row = 0)
#clearBtn.pack()

#win.resizable(0,0)

win1.pack()
btnFrame.pack()
win.mainloop()   # 啟動視窗執行 並無窮執行直到 user關閉
# mainloop 是無窮迴圈 寫在下方的程式 無法執行

#