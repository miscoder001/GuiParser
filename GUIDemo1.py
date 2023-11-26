import requests
from pyquery import PyQuery as pq

from tkinter import Tk   # 代表視窗本身

win = Tk()  # 建立視窗物件
win.title("這是視窗版爬蟲範例")
win.geometry("800x600") # 呼叫 geometry 設定視窗大小
win.mainloop()   # 啟動視窗執行 並無窮執行直到 user關閉


#response = requests.get(url="https://tw.stock.yahoo.com/")
# print(response.text)