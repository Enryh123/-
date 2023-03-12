#亲自出码1代码文件

import tkinter as tk
from PIL import ImageTk

#题目：点击<王者荣耀>窗口中的开始游戏按钮, 实现窗口的跳转！
#提示：使用command属性为按钮绑定事件函数
#     窗口的大小为800x500,标题为'王者荣耀'

#请在下方书写你的代码



# tkinter实现界面
# 窗口标题:'王者荣耀' 窗口宽800  高500
global window
window = tk.Tk()
window.title('王者荣耀')
window.geometry('800x500')
# 设置背景图片 图片路径'./images/kingBg.png'  宽800  高500
bgPath = "./images/kingBg.png"
bgImg = ImageTk.PhotoImage(file=bgPath)
bg = tk.Label(window,width=800,height=500,image=bgImg)
bg.pack()

# 开始按钮
btnPath = "./images/kingBtn.png"
btnImg = ImageTk.PhotoImage(file=btnPath)
#请在下方书写你的代码，绑定事件函数
btn = tk.Button(window,image=btnImg,bd=0,width=250,height=50)
btn.place(x=290,y=350)

# 显示窗口
window.mainloop()

