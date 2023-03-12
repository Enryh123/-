#亲自出码1代码文件

import tkinter as tk
from tkinter import ttk
from PIL import ImageTk

global window
window = tk.Tk()
window.title('王者荣耀')
window.geometry('800x500')
bgPath = "./images/kingBg.png"
bgImg = ImageTk.PhotoImage(file=bgPath)
bg = tk.Label(window,width=800,height=500,image=bgImg)
bg.pack()
btnPath = "./images/kingBtn.png"
btnImg = ImageTk.PhotoImage(file=btnPath)
btn = tk.Button(window,image=btnImg,bd=0,width=250,height=50)
btn.place(x=290,y=350)

#请在下方书写你的代码
#题目：在<王者荣耀>窗口左上角添加下拉列表
#提示：默认显示'请选择英雄'、设置为只读模式


# 显示窗口
window.mainloop()

