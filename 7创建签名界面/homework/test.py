#一码当先代码文件

from PIL import ImageTk
import tkinter as tk

def start():
    print('正在进入游戏中...')

window = tk.Tk()
window.title('梦幻飞仙')
window.geometry('494x282')
window.resizable(0,0)
bgImg = ImageTk.PhotoImage(file="./images/bg.jpg")
bg = tk.Label(window,width=494,height=282,image=bgImg)
bg.pack()

#请在下方书写你的代码
#题目：为梦幻飞仙程序添加一个按钮，实现在控制台上打印输出下图内容的功能
#提示：图片路径："./images/start.jpg"、图片大小：宽度 150，高度 43
#     绑定事件：command=start、按钮放置位置：x=170  y=225


window.mainloop()

