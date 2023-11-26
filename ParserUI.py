from tkinter import  *
from ParserEngine import GetYahooStock


winUI = Tk()
winUI.title("股市爬蟲")
winUI.geometry("800x700")

lab1 = Label(winUI, text="網址:" , font=('Arial',15), bg="yellow", fg="red")   #第一個加入視窗 win 的物件
lab1.pack()
okBtn = Button(winUI ,font=('Arial',15), text="下載" , fg='blue' , command=GetYahooStock)
okBtn.pack()
winUI.mainloop()