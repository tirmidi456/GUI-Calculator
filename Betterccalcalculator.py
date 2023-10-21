import tkinter as tk
from tkinter import messagebox

def on_button_click(button):
    current_text = result_var.get()
    
    if button == "=":
        try:
            result = eval(current_text)
            result_var.set(result)
        except Exception as e:
            result_var.set("Error")
            messagebox.showerror("Error", f"An error occurred: {e}")
    elif button == "C":
        result_var.set("0")
    else:
        if current_text == "0":
            result_var.set(button)
        else:
            result_var.set(current_text + button)

root = tk.Tk()
root.title("Scientific Calculator")

result_var = tk.StringVar()
result_var.set("0")

result_entry = tk.Entry(root, textvariable=result_var, font=("Helvetica", 20))
result_entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10, ipadx=10, ipady=10)

buttons = [
    '7', '8', '9', '/', 'C',
    '4', '5', '6', '*', 'sqrt',
    '1', '2', '3', '-', 'x^2',
    '0', '.', '=', '+', 'exp',
    '(', ')', 'x^y', 'log', 'ln'
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(root, text=button, font=("Helvetica", 15), command=lambda b=button: on_button_click(b)).grid(row=row_val, column=col_val, padx=5, pady=5)
    col_val += 1
    if col_val > 4:
        col_val = 0
        row_val += 1

root.mainloop()
