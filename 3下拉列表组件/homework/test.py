#一码当先代码文件

import tkinter as tk
from tkinter import ttk
from PIL import ImageTk

global window
window = tk.Tk()
window.title('和平精英')
window.geometry('800x476')
# 设置背景图片路径
bgPath = "./images/hpjy.jpg"
bgImg = ImageTk.PhotoImage(file=bgPath)
bg = tk.Label(window, width=800, height=476, image=bgImg)
bg.pack()
btnPath = "./images/start.png"
btnImg = ImageTk.PhotoImage(file=btnPath)
btn = tk.Button(window, image=btnImg, bd=0, width=133, height=44)
# 按钮位置
btn.place(x=340, y=350)

#请在下方书写你的代码
#题目：在<和平精英>窗口左上角添加下拉列表、默认显示项为'请选择武器'


# 显示窗口
window.mainloop()


