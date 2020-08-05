from PIL import Image
from tkinter import *
from tkinter import filedialog
#from scipy.misc import toimage
import cv2
from numpy import *
import os
root = Tk()
cnv = Canvas(root,width=300,height=300,bg='azure3',relief='raised')
cnv.pack()
l = Label(root,text='Convert to grayscale')
l.config(font=("helvetica",20))
cnv.create_window(150,60,window=l)
#global img
#import_file_path=filedialog.askopenfilename()
#img=cv2.imread(import_file_path,0)
#cv2.imshow("Image",img)
def getimg():
    global img,gray
    import_file_path=filedialog.askopenfilename()
    img=cv2.imread(import_file_path,-1)
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Gray",gray)

open_btn=Button(text=' Open the coloured image ',command=getimg,bg='royalblue',fg='white',font=('helvetica',14,'bold'))
cnv.create_window(150,130,window=open_btn)
def saveimg():
    global gray
    global grayimg
    cv2.imwrite('gray.png',gray)
    #export_file_path=filedialog.asksaveasfilename(defaultextension='.png')
    #grayimg.save(export_file_path)
save_btn=Button(text=' Save gray image ',command=saveimg,bg="royalblue",fg='white',font=('helvetica',14,'bold'))
cnv.create_window(150,190,window=save_btn)
root.mainloop()
