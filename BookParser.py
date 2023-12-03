import tkinter as tk
import tkinter.font as tkFont
from pyquery import  PyQuery as pq

class App:
    def __init__(self, root):      # __init__ 會在 App() 建構時候主動執行
        #setting title
        root.title("最新電腦書籍資訊")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()   #你pc目前的螢幕解析度
        screenheight = root.winfo_screenheight()
        print(screenheight)
        print(screenwidth)
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_668=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_668["font"] = ft
        GLabel_668["fg"] = "#333333"
        GLabel_668["justify"] = "center"
        GLabel_668["text"] = "請輸入網址:"
        GLabel_668.place(x=10,y=20,width=70,height=25)  # 採用絕對位置設計 如果螢幕大小調整  有些元素可能因此看不見

        GLineEdit_355=tk.Entry(root)
        GLineEdit_355["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_355["font"] = ft
        GLineEdit_355["fg"] = "#333333"
        GLineEdit_355["justify"] = "left"
        GLineEdit_355["text"] = "https://"
        GLineEdit_355.place(x=100,y=20,width=433,height=30)

        GListBox_917 = tk.Listbox(root)
        GListBox_917["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GListBox_917["font"] = ft
        GListBox_917["fg"] = "#333333"
        GListBox_917["justify"] = "center"
        GListBox_917.place(x=20, y=130, width=560, height=354)

        GButton_506=tk.Button(root)
        GButton_506["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_506["font"] = ft
        GButton_506["fg"] = "#000000"
        GButton_506["justify"] = "center"
        GButton_506["text"] = "擷取"
        GButton_506.place(x=460,y=70,width=70,height=25)
        GButton_506["command"] = self.GButton_506_command

    def GButton_506_command(self):
        ua = {"user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:77.0) Gecko/20190101 Firefox/77.0"}
        bookPage = pq(url="https://www.tenlong.com.tw/zh_tw/recent" , encoding="utf8", headers=ua)
        #取出網頁內的 div.list-wrapper 內容
        bookList = bookPage.find('div.list-wrapper')
        #取出所有 li 項目
        bookLi = bookList.find('li').items() # 拆解出來後 每一個 li 轉換成 pyquery 才能使用 pyquery 的方法拆內部資料
        for eachBook in bookLi:
            print("書名: " + eachBook.find('strong.title a').text())
            #使用 split 去分解 原價與折扣後價錢 , python 會依據 空白 或是換行符號 決定如何拆
            pstring = eachBook.find('div.pricing').text()
            bprices = pstring.split() # 根據 enter換行切割
            print("原價: " + bprices[0] +  "  折扣後: " + bprices[1] )
            print("--------------")




if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
