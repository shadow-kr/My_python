import tkinter as tk
from tkinter import messagebox




app = tk.Tk()
app.title("Task Manager")
file_for_task = "C:/Users/toshiba/Documents/my_Python_codes/Ressource/fichier de test.txt"
app.configure(background="grey")
#---------------------------------------------------------->Functions

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")


def remove_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove.")


def cross_off_item():
    task_listbox.itemconfig(task_listbox.curselection(), fg="#FF0000")
    task_listbox.selection_clear(0, tk.END)

def write_file():
    
    file1 = open(file_for_task, "w")
    file_content = task_listbox.get(0, tk.END)
    file_content ='\n'.join(file_content)
    file1.write(str(file_content))
    file1.close()
    print("Task saved to file")
    
def load_file():
    file1 = open(file_for_task, "r")
        
    task = file1.readlines()
    # print(type(task))
    for value in task :
        task_listbox.insert(tk.END, value)

    file1.close()

    


#---------------------------------------------------------->widgets

# Create a text entry field for adding tasks
task_entry = tk.Entry(app, width=40)
task_entry.pack(pady=10)

# Create a listbox to display tasks
task_listbox = tk.Listbox(app, width=40)
task_listbox.pack()

#---------------------------------------------------------->Bouton

add_button = tk.Button(app, text="Add Task", command=add_task, bg="#ADD8E6", font=("arial", 10, "bold"))
add_button.pack(padx=5, pady=5)

remove_button = tk.Button(app, text="Remove Task", command=remove_task, bg="#FF0000", font=("arial", 10, "bold"))
remove_button.pack(padx=5, pady=15, side=tk.LEFT)

cross_off_button = tk.Button(app, text="Cross Off Item", command=cross_off_item, bg="#7ADF20", font=("arial", 10, "bold"))
cross_off_button.pack(padx=5, pady=25, side=tk.LEFT)

saving_button = tk.Button(app, text="save to file", command=write_file, bg="#FFB6C1", font=("arial", 10, "bold"))
saving_button.pack(padx=5, pady=35, side=tk.LEFT)

load_button = tk.Button(app, text="load from file", command=load_file, bg="#FFB6C1", font=("arial", 10, "bold"))
load_button.pack(padx=5, pady=45, side=tk.LEFT)


#---------------------------------------------------------->main
app.mainloop()
