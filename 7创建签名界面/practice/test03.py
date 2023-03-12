#亲自出码2代码文件

from PIL import ImageTk
import tkinter as tk

def change():
    pic = ImageTk.PhotoImage(file="./images/img2.jpg")
    bg.config(image=pic)
    bg.image = pic

window = tk.Tk()
window.title('冒险岛2')
window.geometry('500x565')
window.resizable(0,0)
bgImg = ImageTk.PhotoImage(file="./images/img1.jpg")
bg = tk.Label(window,width=500,height=565,image=bgImg)
bg.pack()

#请在下方书写你的代码
#题目：为程序添加一个按钮，实现更换背景图片的功能
#提示：图片路径："./images/button.jpg"、图片大小：宽度 120，高度 47
#     绑定事件：command=change、按钮放置位置：x=360  y=510



window.mainloop()


