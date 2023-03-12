import tkinter as tk
from tkinter import ttk
from PIL import ImageTk
import requests
from bs4 import BeautifulSoup
from PIL import Image
import random

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
    start = tk.Button(window,image=startImg,bd=0,width=179,height=70,
                      command=inputName)
    start.place(x=438,y=466)
    window.mainloop()

# 按钮事件函数inputName
def inputName():
    fontList = ['jfcs.ttf','qmt.ttf','bzcs.ttf','yqk.ttf']
    def showMsg(*args):
        print(cbox.get())
        name = entry.get()
        if cbox.get() == '个性签':
            print('个性签',name)
            download(fontList[0],name)
        elif cbox.get() == '连笔签':
            print('连笔签',name)
            download(fontList[1],name)
        elif cbox.get() == '潇洒签':
            print('潇洒签',name)
            download(fontList[2],name)
        elif cbox.get() == '可爱签':
            print('可爱签',name)
            download(fontList[3],name)
    def download(style,name):
        url = 'http://www.uustv.com/'
        if not name:
            return
        data = {
            'word': name,
            'sizes':'60',
            'fonts':style
        }
        response = requests.post(url,data=data)
        response.encoding='utf-8'
        result = response.text
        print(result)

        # 解析
        soup = BeautifulSoup(result,'html.parser')
        tempUrl = soup.select('img')[0]['src']
        imgUrl = url + tempUrl
        path = "./temp/temp.jpg"
        imgContent = requests.get(imgUrl).content
        with open(path,'wb') as f:
            f.write(imgContent)

    global window
    window.destroy()
    #创建窗口
    window = tk.Tk()
    window.geometry('1050x660')
    window.resizable(0,0)
    #窗口标题
    window.title('艺术签名')
    bgImg = ImageTk.PhotoImage(file="./images/bg3.jpg")
    bg = tk.Label(window,width=1050,height=660,image=bgImg)
    bg.pack()
    #字体路径
    fontPath = "./font/simhei.ttf"
    #颜色字符
    color = '#ffd46c'
    name = tk.Label(window,text='姓名',bg=color,font=(fontPath,18))
    style = tk.Label(window,text='样式',bg=color,font=(fontPath,18))
    name.place(x=370,y=165)
    style.place(x=370,y=235)
    #姓名输入框
    entry = tk.Entry(window,font=("./font/simhei.ttf",15))
    entry.place(x=430,y=170)
    #添加样式下拉列表
    cbox = ttk.Combobox(window,width=26)
    cbox['values'] = ['请选择签名样式','个性签','连笔签','潇洒签','可爱签']
    cbox.place(x=430,y=240)
    #设置默认列表项
    cbox.current(0)
    #设置下拉列表的只读模式
    cbox['state'] = 'readonly'
    cbox.bind('<<ComboboxSelected>>',showMsg)
    #添加ok按钮
    okImg = ImageTk.PhotoImage(file="./images/ok.png")
    ok = tk.Button(window,image=okImg,bd=0,width=179,height=70,command=design)
    ok.place(x=436,y=465)
    window.mainloop()

def design():
    #关闭二级界面
    global window
    window.destroy()
    window = tk.Tk()
    window.title('艺术签名')
    window.geometry('1050x660')
    window.resizable(0,0)
    bgImg = ImageTk.PhotoImage(file="./images/bg3.jpg")
    bg = tk.Label(window,width=1050,height=660,image=bgImg)
    bg.pack()
    #绘制签名图片
    signImg = ImageTk.PhotoImage(file="./temp/temp.jpg")
    signLabel = tk.Label(window,width=535,height=205,image=signImg)
    signLabel.place(x=250,y=170)
    #添加保存按钮
    saveImg = ImageTk.PhotoImage(file="./images/save.png")
    saveBtn = tk.Button(window,image=saveImg,width=179,height=70)
    saveBtn.place(x=436,y=465)
    window.mainloop()

#请在下方书写你的代码


# 程序开始
nameSign()
