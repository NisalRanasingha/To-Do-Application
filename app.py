import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Todo App")
root.geometry('400x500')
root.resizable(False, False)
root.iconbitmap('todo.ico')

heading = ttk.Label(root, text="All Tasks",font=("times new roman", 20, "bold"))
heading.pack()

frame = ttk.Frame(root,width=400,height=50)
frame.pack(pady=20)

task_entry = ttk.Entry(frame,font=("times new roman", 15),width=25)
task_entry.pack()

# list to keep track of tasks
task_list = []

def add_task(event):
    task = task_entry.get()
    task_entry.delete(0, tk.END)
    if task != "":
        listbox.insert(tk.END, task)
        task_list.append(task)


task_entry.bind("<Return>", add_task)

frame2 = ttk.Frame(root,width=200,height=100)
frame2.pack()

listbox = tk.Listbox(frame2,font=("times new roman", 15),width=30,height=12)
listbox.pack()

s = ttk.Style()
s.configure('TButton', font=('times new roman', 15), borderwidth=4)
delete_button = ttk.Button(root, text='Delete Task',style='TButton')
delete_button.pack(side='bottom', pady=10,ipadx=5,ipady=5)
root.mainloop()