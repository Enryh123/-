#亲自出码1代码文件

import tkinter as tk
from PIL import ImageTk

# tkinter实现界面
# 窗口标题:'王者荣耀' 窗口宽800  高500
window = tk.Tk()
window.title('王者荣耀')
window.geometry('800x500')

# 设置背景图片 图片路径'./images/kingBg.png'、宽800、高500
bgPath = "./images/kingBg.png"
bgImg = ImageTk.PhotoImage(file=bgPath)
bg = tk.Label(window, text='', width=800, height=500, image=bgImg)
bg.pack()

#请在下方书写你的代码
#题目：给<王者荣耀>窗口添加开始游戏按钮
#提示: 按钮位置: x=290, y=350、按钮尺寸: 250x50
#     按钮图片路径: "./images/kingBtn.png"



# 显示窗口
window.mainloop()

