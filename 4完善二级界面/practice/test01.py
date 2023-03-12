#码上回顾代码文件

import tkinter as tk
from tkinter import ttk

#请在下方书写你的代码
#题目：给窗口中的下拉列表添加事件函数showMsg, 选择城市后, 在控制台打印输入对应的城市
#定义事件函数showMsg


global window
window = tk.Tk()
window.title('中国城市')
window.geometry('800x500')

#添加下拉列表框
cbox= ttk.Combobox(window,width=15)
cbox['values'] = ['请选择城市','北京','上海','广州','深圳']
cbox['state'] = 'readonly'
cbox.current(0)
cbox.place(x=0,y=0)

#请在下方书写你的代码
#下拉列表框绑定选择事件函数


#显示窗口
window.mainloop()



