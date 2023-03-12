#一码当先代码文件

import tkinter as tk
from PIL import ImageTk

# tkinter实现界面
# 窗口标题:'我的世界' 窗口宽800  高450
window = tk.Tk()
window.title('我的世界')
window.geometry('800x450')

# 设置背景图片 图片路径'./images/worldBg.jpg'  宽800  高450
bgPath = "./images/worldBg.jpg"
bgImg = ImageTk.PhotoImage(file=bgPath)
bg = tk.Label(window,width=800,height=450,image=bgImg)
bg.pack()

#请在下方书写你的代码
#题目：给<我的世界>添加按钮。
#提示：按钮位置: x=350, y=300  按钮尺寸: 140 x 50
#     图片路径: "./images/worldBtn.png"



# 显示窗口
window.mainloop()

