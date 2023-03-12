#亲自出码2代码文件

import tkinter as tk
from PIL import ImageTk

#请在下方书写你的代码
#题目：在已经预留好的<我的世界>窗口中，点击绿色按钮, 实现窗口的跳转。
#提示：两个窗口的宽高和标题相同

#定义开始游戏函数



# tkinter实现界面
# 窗口标题:'我的世界' 窗口宽800  高450
global window
window = tk.Tk()
window.title('我的世界')
window.geometry('800x450')

# 设置背景图片 图片路径'./images/worldBg.jpg'  宽800  高450
bgPath = "./images/worldBg.jpg"
bgImg = ImageTk.PhotoImage(file=bgPath)
bg = tk.Label(window,width=800,height=450,image=bgImg)
bg.pack()

# 添加按钮
btnPath = "./images/worldBtn.png"
btnImg = ImageTk.PhotoImage(file=btnPath)
#请在下方书写你的代码，绑定事件函数
btn = tk.Button(window,image=btnImg,bd=0,width=140,height=50)
# 按钮位置
btn.place(x=350,y=300)

# 显示窗口
window.mainloop()

