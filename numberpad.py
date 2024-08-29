from tkinter import *
root=Tk()
root.title("Number Pad")
root.geometry("250x300")
num=[[9,8,7],[6,5,4],[3,2,1],["#",0,"*"]]
for i in range(4):
    root.columnconfigure(i,weight=1,minsize=75)
    root.rowconfigure(i,weight=1,minsize=75)
for i in range(4):
    for j in range(3):
        frame=Frame(master=root,relief=RIDGE,borderwidth=1,bg="Blue")
        frame.grid(row=i,column=j,sticky="nsew")
        l1=Label(master=frame,text=num[i][j],bg="Blue",font=('Arial',18))
        l1.pack(expand=True,fill='both',padx=5,pady=5)
root.mainloop()