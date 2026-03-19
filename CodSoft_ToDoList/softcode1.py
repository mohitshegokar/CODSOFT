from tkinter import * 
from tkinter import messagebox 

root = Tk()
root.title("To-Do List")
root.geometry("400x400")

def add_task():
    task = entry.get() 
    if task != "":
        listbox.insert(END, task) 
        entry.delete(0, END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def remove_task():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
    except:
        messagebox.showwarning("Warning", "Please select a task!")

def delete_all():
    confirm = messagebox.askyesno("Confirm", "Delete all tasks?")
    if confirm:
        listbox.delete(0, END)

def close_app():
    root.destroy() 

title = Label(root, text="My To-Do List", font=("Arial", 16))
title.pack(pady=10)


entry = Entry(root, width=30)
entry.pack(pady=10)
add_btn = Button(root, text="Add Task", width=20, command=add_task)
add_btn.pack(pady=5)
remove_btn = Button(root, text="Remove Selected Task", width=20, command=remove_task)
remove_btn.pack(pady=5)
delete_btn = Button(root, text="Delete All Tasks", width=20, command=delete_all)
delete_btn.pack(pady=5)
exit_btn = Button(root, text="Exit", width=20, command=close_app)
exit_btn.pack(pady=5)
listbox = Listbox(root, width=40, height=10)
listbox.pack(pady=20)
root.mainloop()