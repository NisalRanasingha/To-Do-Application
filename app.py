import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Todo App")
root.geometry('400x500')
root.resizable(False, False)
root.iconbitmap('todo.ico')

dispaly_width = root.winfo_screenwidth()
display_height = root.winfo_screenheight()

left = int((dispaly_width / 2) - (400 / 2))
top = int((display_height / 2) - (500 / 2))
root.geometry(f'400x500+{left}+{top}')


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
        with open("tasks.txt", "a") as file:
            file.write(task + "\n")
        listbox.insert(tk.END, task)
        task_list.append(task)

#delete task function
def deletetask():
    task = listbox.get(tk.ANCHOR)
    listbox.delete(tk.ANCHOR)
    task_list.remove(task)
    with open("tasks.txt", "w") as file:
        for t in task_list:
            file.write(t + "\n")

# open task function
def open_task():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            for task in tasks:
                task = task.strip()
                if task != "":
                    listbox.insert(tk.END, task)
                    task_list.append(task)
    except FileNotFoundError:
        open("tasks.txt", "w").close()

# edit task function
def edit_task():
    try:
        selected_index = listbox.curselection()[0]
        selected_task = listbox.get(selected_index)

        # Put the selected task into entry field
        task_entry.delete(0, tk.END)
        task_entry.insert(0, selected_task)

        # Replace add function temporarily
        def save_edit(event):
            new_text = task_entry.get()
            task_entry.delete(0, tk.END)

            # Update listbox
            listbox.delete(selected_index)
            listbox.insert(selected_index, new_text)

            # Update task_list
            task_list[selected_index] = new_text

            # Save to file
            with open("tasks.txt", "w") as file:
                for t in task_list:
                    file.write(t + "\n")
                    
            task_entry.bind("<Return>", add_task)

        task_entry.bind("<Return>", save_edit)

    except IndexError:
        pass  

task_entry.bind("<Return>", add_task)

frame2 = ttk.Frame(root,width=200,height=100)
frame2.pack()

listbox = tk.Listbox(frame2,font=("times new roman", 15),width=30,height=12)
listbox.pack()

open_task()
s = ttk.Style()
s.configure('TButton', font=('times new roman', 15), borderwidth=4)
delete_button = ttk.Button(root, text='Delete Task',style='TButton',command=deletetask)
delete_button.pack(side='bottom', pady=10,ipadx=5,ipady=5)

edit_button = ttk.Button(root, text='Edit Task', style='TButton', command=edit_task)
edit_button.pack(side='bottom', pady=5, ipadx=5, ipady=5)

root.mainloop()