#一码当先代码文件

import tkinter as tk
from tkinter import ttk
from PIL import ImageTk

#请在下方书写你的代码
#题目：在界面中添加下拉列表，设置列表选项，若点击选项则触发事件函数
#     在控制台上打印出选择的列表项
#定义下拉列表事件函数showMsg


global window
window = tk.Tk()
window.title('迷你世界')
window.geometry('800x450')

bgPath = "./images/game.jpg"
bgImg = ImageTk.PhotoImage(file=bgPath)
bg = tk.Label(window,width=800,height=450,image=bgImg)
bg.pack()

#请在下方书写你的代码
#添加下拉列表

#为下拉列表绑定事件函数


# 显示窗口
window.mainloop()




