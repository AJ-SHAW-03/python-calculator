import tkinter as tk
def click(event) :
    text = event.widget.cget("text")
    if text == "=":
        try:
            expression = entry_var.get()
            result =  eval(expression)
            entry_var. set(result)
        except expection as e:
            entry_var. set("Error")
                
                
    elif text == "C":
        entry_var.set("")
                    
                    
    else:
        entry_var.set(entry.get() + str(text))


root = tk.Tk()
root.title("calculator")
root.geometry("300x400")

entry_var = tk.StringVar()
entry = tk.Entry(root,
textvariable=entry_var , font="arial 20")
entry.pack(fill="both", ipadx=8, pady=10,
padx=10)


buttons = [
"7", "8", "9", "/",
"4", "5", "6", "*",
"1", "2", "3", "-",
"0", ".", "=", "+",
"C"
]

frame = tk.Frame(root)
frame.pack()

row = 0
col = 0

for button in buttons:
    b = tk.Button(frame, text=button,
font="arial 18", width=5, height=2)
    b.grid(row=row, column=col)
    b.bind("<Button-1>", click)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
