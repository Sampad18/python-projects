from tkinter import *
from PIL import Image
from tkinter import filedialog
root=Tk()
canvas1=Canvas(root,width=300,height=300,bg="azure3",relief="raised")
canvas1.pack()
label1=Label(root,text="file converter",bg="white")
label1.config(font=("helvetica",20))
canvas1.create_window(150,60,window=label1)

def getPNG():
    global img1
    import_file_path=filedialog.askopenfilename()
    img1=Image.open(import_file_path)

Button_PNG=Button(text="  Import JPG file  ",command=getPNG,bg="royalblue",fg="white",font=("helvetica",12,"bold"))
canvas1.create_window(150,130,window=Button_PNG)

def convertJPG():
    global img1
    export_file_path=filedialog.asksaveasfilename(defaultextension=".png")
    img1.save(export_file_path)

save_JPG=Button(text="  Save PNG  ",command=convertJPG,bg="royalblue",fg="white",font=("helvetica",12,"bold"))
canvas1.create_window(150,180,window=save_JPG)

root.mainloop()
