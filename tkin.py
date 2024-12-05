import tkinter as tk
from tkinter import messagebox
def add():
    try:
        num1=float(entry1.get())
        num2=float(entry2.get())
        result=num1+num2
        messegebox.showinfo("result",result)
    except ValueError:
        messagebox.showerror("Error","please enter valid number")
root=tk.Tk()
root.title("calculator")
tk.Label(root,text="number 1:").grid(row=0,column=0,padx=10,pady=10)
tk.Label(root,text="number 2:").grid(row=1,column=0,padx=10,pady=10)
entry1=tk.Entry(root)
entry1.grid(row=0,column=1,padx=10,pady=10)
entry2=tk.Entry(root)
entry2.grid(row=1,column=1,padx=10,pady=10)
add_btn=tk.Button(root,text="+",command=add())
add_btn.grid(row=2,column=0,columnspan=2,padx=10,pady=10)
root.mainloop()
            