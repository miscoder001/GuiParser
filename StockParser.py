import requests
from pyquery import PyQuery as pq
#視窗元件清單
from tkinter import Tk   # 代表視窗本身
from tkinter import Label
from tkinter import Button
from tkinter import *
from tkinter import StringVar
from pyquery import  PyQuery as pq
from time import sleep
#
def StockQueryClick():  # 下載網頁
    slist = [2330, 2345, 2454]
    ua = {"user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:77.0) Gecko/20190101 Firefox/77.0"}
    for sid in slist:
        # headers 送出 瀏覽器識別字串 以防被偵測為 爬蟲
        page = pq(url="https://www.google.com/search?q=" + str(sid), encoding="utf8", headers=ua)
        sprice = page.find('span.IsqQVc.NprOob.wT3VGc').text()
        #python 3.11 提供 switch/case寫法  之前的版本必須使用 if elif 判斷
        if sid==2330:
            #_2330Price.config(text= sprice)
            _2330PVar.set(sprice)
        elif sid==2345:
            #_2345Price.config(text=sprice)
            _2345PVar.set(sprice)
        elif sid==2454:
            #_2454Price.config(text=sprice)
            _2454PVar.set(sprice)

        # 建議暫停各n秒 以免因為過度傳送查詢被偵測到 爬蟲撈股票資料
        sleep(1)  # 每次查詢完後暫停兩秒


def CloseAppClick():
    win.destroy()

#
# 動態變數 必須要在 Tk() 產生後才可以宣告
#dataVar = StringVar()

win = Tk()  # 建立視窗物件

win.title("視窗版股票價格爬蟲範例")
win.geometry("400x300") # 呼叫 geometry 設定視窗大小

# 動態變數與 UI 物件綁定 一旦變數的內容有變動 會自動更新UI畫面
# 省去每次要呼叫 config(text='新內容') 的行為
_2330PVar = StringVar()
_2345PVar = StringVar()
_2454PVar = StringVar()
# 產生一個新的面板(frame) 把所有標籤與 entry 放入此 frame 在與 主視窗綁定
winFrame = Frame(win)
btnFrame = Frame(win)
# 加入標籤
lab1 = Label(winFrame,text="台積電:" , font=('Arial',15), bg="yellow", fg="blue")   #第一個加入視窗 winFrame 的物件
lab1.grid(column=0, row=0, padx=10)
lab2 = Label(winFrame, text="智邦:" , font=('Arial',15), bg="yellow", fg="blue")   #第一個加入視窗 winFrame 的物件
lab2.grid(column=0, row=1, padx=10)
lab3 = Label(winFrame, text="聯發科:" , font=('Arial',15), bg="yellow", fg="blue")   #第一個加入視窗 winFrame 的物件
lab3.grid(column=0, row=2, padx=10)
#加入 股票文字框輸入
_2330Price = Entry(winFrame, font=('Arial',15), fg='red',width=10, textvariable=_2330PVar) # 將 entry與 StrigVar綁定後  修改StringVar 的值主動會更新到視窗畫面中
_2330Price.grid(column=1,row=0)
_2345Price = Entry(winFrame, font=('Arial',15), fg='red',width=10, textvariable=_2345PVar)
_2345Price.grid(column=1,row=1)
_2454Price = Entry(winFrame, font=('Arial',15), fg='red',width=10, textvariable=_2454PVar)
_2454Price.grid(column=1,row=2)
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
okBtn.grid(column=0, row=0, padx=10)
#okBtn.pack()
closeBtn = Button(btnFrame ,font=('Arial',15), text="停止" , fg='blue', command=CloseAppClick)
closeBtn.grid(column = 1, row = 0)
#clearBtn.pack()

#win.resizable(0,0)


winFrame.pack()
btnFrame.pack()
win.mainloop()   # 啟動視窗執行 並無窮執行直到 user關閉
# mainloop 是無窮迴圈 寫在下方的程式 無法執行

#