import requests
from pyquery import PyQuery as pq
#視窗元件清單
from tkinter import Tk   # 代表視窗本身
from tkinter import Label
from tkinter import Button
from tkinter import *
from tkinter import StringVar

#
def URLGetClick():  # 下載網頁
    # 取得文字框Entry內的URL
    urlStr = urlEntry.get()
    response = requests.get(url=urlStr)
    # lab2 的內容顯示為 urlStr 下載成功
    print(response.text)
    lab2.config(text='下載成功', fg='red')
    resultMsg.set(urlStr)

def clearURLEntry():
    urlEntry.delete(0,5)
#
# 動態變數 必須要在 Tk() 產生後才可以宣告
#dataVar = StringVar()

win = Tk()  # 建立視窗物件

win.title("這是視窗版爬蟲範例")
win.geometry("800x600") # 呼叫 geometry 設定視窗大小

# 動態變數與 UI 物件綁定 一旦變數的內容有變動 會自動更新UI畫面
# 省去每次要呼叫 config(text='新內容') 的行為
resultMsg = StringVar()

# 加入標籤
lab1 = Label(win, text="網址:" , font=('Arial',15), bg="yellow", fg="red")   #第一個加入視窗 win 的物件
lab1.pack()
#加入 網址文字框輸入
urlEntry = Entry(win, font=('Arial',15), fg='blue',width=40)
urlEntry.pack()
# 結果通知
lab2 = Label(win, text="結果通知:", font=('Arial',15))   #第二個加入視窗 win 的物件
lab2.pack()
# 請注意 lab3 用 textvariable 與動態變數綁定 只要變數改變 訊息就會顯示在 畫面上
lab3 = Label(win, textvariable= resultMsg , font=('Arial',15))   #第二個加入視窗 win 的物件
lab3.pack()
resultMsg.set('準備下載....')
#第三個物件 : 按鈕
okBtn = Button(win ,font=('Arial',15), text="下載" , fg='blue', command=URLGetClick)
okBtn.pack()
clearBtn = Button(win ,font=('Arial',15), text="x" , fg='blue', command=clearURLEntry)
clearBtn.pack()

#win.resizable(0,0)


win.mainloop()   # 啟動視窗執行 並無窮執行直到 user關閉
# mainloop 是無窮迴圈 寫在下方的程式 無法執行

#