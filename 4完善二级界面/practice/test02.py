#亲自出码代码文件

import tkinter as tk
from PIL import ImageTk

global window
window = tk.Tk()
window.title('登录')
window.geometry('556x557')
bgPath = "./images/login.jpg"
bgImg = ImageTk.PhotoImage(file=bgPath)
bg = tk.Label(window,width=556,height=557,image=bgImg)
bg.pack()

#请在下方书写你的代码
#题目：在界面中添加两个Label组件，分别显示文字'用户名:'和'密 码:'。
#提示：字体路径：fontPath = "./font/simhei.ttf"
#     背景颜色：color = '#ffffff'


#请在下方书写你的代码
#题目：在界面中两个Label组件后面，分别添加两个Entry组件
#提示：Entry1组件坐标(200,168)
#     Entry2组件坐标(200,238)


# 显示窗口
window.mainloop()



