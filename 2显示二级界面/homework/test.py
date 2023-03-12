#一码当先代码文件

import tkinter as tk
from PIL import ImageTk

#请在下方书写你的代码
#题目：点击下面左图中的开始游戏按钮，完成跳转界面的功能
#提示：使用按钮的command属性绑定事件函数
#     使用window.destroy()关闭窗口
#定义函数startGame


# tkinter实现界面
# 窗口标题:'和平精英' 窗口宽800  高476
global window
window = tk.Tk()
window.title('和平精英')
window.geometry('800x476')

# 设置背景图片 图片路径'./images/hpjy.jpg'  宽800  高476
bgPath = "./images/hpjy.jpg"
bgImg = ImageTk.PhotoImage(file=bgPath)
bg = tk.Label(window,width=800,height=476,image=bgImg)
bg.pack()

# 添加按钮
btnPath = "./images/start.png"
btnImg = ImageTk.PhotoImage(file=btnPath)
#请在下方书写你的代码，绑定事件函数
btn = tk.Button(window,image=btnImg,bd=0,width=133,height=44)
# 按钮位置
btn.place(x=340,y=350)

# 显示窗口
window.mainloop()


