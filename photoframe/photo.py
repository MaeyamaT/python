import tkinter as tk
index=0
def change_img():
    global index
    canvas.delete("PIC")
    canvas.create_image(400,300,image=photos[index % len(photos)],tag="PIC")
    index+=1
    root.after(5000,change_img)
root=tk.Tk()
root.title("デジタルフォトフレーム")
canvas=tk.Canvas(width=800,height=600)
canvas.pack()
photos=[tk.PhotoImage(file=f'cat0{i}.png')for i in range(4)]
"""
photos=[
        tk.PhotoImage(file='cat01.png')
        tk.PhotoImage(file='cat02.png')
        tk.PhotoImage(file='cat03.png')
        tk.PhotoImage(file='cat04.png')
        ]
"""
change_img()
root.mainloop()
    
