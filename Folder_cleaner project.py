import tkinter
from tkinter import *
import os,shutil
def fun():
    source=src_path_entry.get()                 #C:\Users\Desktop\source\
    dest=destination_path_entry.get()           #C:\Users\Desktop\destination\
    for(path,dirs,files) in os.walk(source):
        print(path)
        for file in files:
            extension=file.split('.')[1]
            if os.path.exists(dest+extension):
                shutil.copy(path+'\\'+file,dest+extension)
            else:
                os.makedirs(dest+extension)
                shutil.copy(path+'\\'+file,dest+extension)
        print("task done")
    heading=Label(window,text=" TASK DONE" , font=("Algerian",18),bg="light grey", relief=RAISED, borderwidth=5)
    heading.place(x=180 ,y=500)
    
    
window=tkinter.Tk()
window.geometry('661x670+500+10')
window.title("FOLDER_CLEANER")
window.resizable(0,0)
window.configure(bg='gold')
heading=Label(window,text=" Enter Source Path " , font=("Algerian",18),bg="light grey", relief=RAISED, borderwidth=5) 
heading.place(x=50 ,y=50)
src_path_entry=Entry(window,font=('Times New Roman',20),bg="sky blue",fg="black")
src_path_entry.place(x=100 ,y=115 , height=50 , width=500)
destination_path=Label(window,text="  Enter destination path  " , font=("Algerian",18), bg="light grey" , relief=RAISED ,  borderwidth=5) 
destination_path.place(x=50,y=215)
destination_path_entry=Entry(window,font=('Times New Roman',20),bg="sky blue",fg="black")
destination_path_entry.place(x=100,y=285 , height=50 , width=500)
connect=Button(window,text=" CLICK" , font=("Algerian",18),bg="light grey", relief=RAISED, borderwidth=5,command=fun)
connect.place(x=180 , y=400 )

