import tkinter as tk
root=tk.Tk()
root.title('My Window')#タイトルを設定
root.geometry('600x400')#大きさを設定
#文字出力のためのラベルを作成
label=tk.Label(root,text='Hello World!',font=('Arial',50))
#labelを配置
label.place(x=100,y=100)
root.mainloop()
