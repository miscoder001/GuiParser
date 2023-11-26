import requests
from pyquery import PyQuery as pq
#視窗元件清單
from tkinter import Tk   # 代表視窗本身
from tkinter import Label
from tkinter import Button
from tkinter import *

#
def URLGetClick():  # 下載網頁
    # 取得文字框Entry內的URL
    urlStr = urlEntry.get()
    response = requests.get(url=urlStr)
    # lab2 的內容顯示為 urlStr 下載成功
    print(response.text)

def clearURLEntry():
    urlEntry.delete(0,5)
#

win = Tk()  # 建立視窗物件
win.title("這是視窗版爬蟲範例")
win.geometry("800x600") # 呼叫 geometry 設定視窗大小

# 加入標籤
lab1 = Label(win, text="網址:" , font=('Arial',15), bg="yellow", fg="red")   #第一個加入視窗 win 的物件
lab1.pack()
#加入 網址文字框輸入
urlEntry = Entry(win, font=('Arial',15), fg='blue',width=40)
urlEntry.pack()
# 結果通知
lab2 = Label(win, text="目標:")   #第二個加入視窗 win 的物件
lab2.pack()
#第三個物件 : 按鈕
okBtn = Button(win ,font=('Arial',15), text="下載" , fg='blue', command=URLGetClick)
okBtn.pack()
clearBtn = Button(win ,font=('Arial',15), text="x" , fg='blue', command=clearURLEntry)
clearBtn.pack()

#win.resizable(0,0)


win.mainloop()   # 啟動視窗執行 並無窮執行直到 user關閉
# mainloop 是無窮迴圈 寫在下方的程式 無法執行

#