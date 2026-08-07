import tkinter as tk
import re

def check_password():
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z0-9]).{8,}$"
    password = entry.get()
    if re.match(pattern, password):
        result_label.config(text="Password is valid", fg="green")
    else:
        result_label.config(text="Password is invalid", fg="red")

root = tk.Tk()
root.title("Password Checker")

entry = tk.Entry(root, width=40)
entry.pack(padx=10, pady=10)

result_label = tk.Label(root, text="", fg="black")
result_label.pack(pady=10)

check_button = tk.Button(root, text="Check Password", command=check_password)
check_button.pack(pady=10)

root.mainloop()