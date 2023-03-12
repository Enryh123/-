import tkinter as tk

from PIL import ImageTk



def nameSign():
    #创建窗口
    global window
    window = tk.Tk()
    window.geometry('1050x660')
    window.resizable(0, 0)
    #设置标题
    window.title('艺术签名')
    #设置背景图片的路径
    bgPath = "./images/bg1.jpg"
    #加载背景图片
    bgImg = ImageTk.PhotoImage(file=bgPath)
    #设置窗口背景
    bg = tk.Label(window,width=1050,height=660,image=bgImg)
    bg.pack()
    #设置开始按钮的图片路径
    startPath = "./images/start.png"
    #加载开始按钮
    startImg = ImageTk.PhotoImage(file=startPath)
    #添加开始按钮
    start = tk.Button(window,image=startImg,bd=0,width=179,height=70)
    start.place(x=438,y=466)
    window.mainloop()

# 请在下方书写你的代码

# 程序开始
nameSign()
