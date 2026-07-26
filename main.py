import tkinter as tk
from tkinter import messagebox
import pyperclip
import json
import os

FILE = "clipboard.json"

def load_data():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def save_data():
    with open(FILE, "w") as f:
        json.dump(history, f, indent=4)

def add_clipboard():
    text = pyperclip.paste()
    if text and text not in history:
        history.append(text)
        save_data()
        refresh()

def refresh():
    listbox.delete(0, tk.END)
    for item in history:
        listbox.insert(tk.END, item)

def copy_selected():
    try:
        item = listbox.get(listbox.curselection())
        pyperclip.copy(item)
        messagebox.showinfo("Copied", "Copied to clipboard!")
    except:
        messagebox.showwarning("Warning", "Select an item.")

def delete_selected():
    try:
        index = listbox.curselection()[0]
        history.pop(index)
        save_data()
        refresh()
    except:
        messagebox.showwarning("Warning", "Select an item.")

history = load_data()

root = tk.Tk()
root.title("Clipboard Manager")
root.geometry("500x450")

tk.Button(root, text="Save Current Clipboard", command=add_clipboard).pack(pady=10)

listbox = tk.Listbox(root, width=65, height=15)
listbox.pack()

tk.Button(root, text="Copy Selected", command=copy_selected).pack(pady=5)

tk.Button(root, text="Delete Selected", command=delete_selected).pack()

refresh()

root.mainloop()
