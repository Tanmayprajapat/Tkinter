import tkinter as tk


root = tk.Tk() 

main_frame = tk.Frame(root)

entry_box = tk.Entry(main_frame, font=('Times', 25, 'bold'))
entry_box.config(fg='black', bg='#f5eeda', relief=tk.RAISED, bd=5)
entry_box.pack(fill=tk.BOTH, padx=20, pady=30)

def result():
    eq = entry_box.get()
    entry_box.delete(0, tk.END)
    result_label.config(text=f"Result: {eval(eq):.2f}")


button = tk.Button(main_frame, text='Result', command = result )
button.config(width=30, relief=tk.RAISED, bd=5, bg='red', fg='white', height=2, font=('Courier', 15, 'bold'))
button.pack()
result_label = tk.Label(main_frame, text="Result: _______")
result_label.config(font=('Courier', 20, 'bold'), fg='#123456', relief=tk.FLAT, )

result_label.pack(fill=tk.X, pady=30)
exit_button = tk.Button(root, font=('Courier', 15, 'bold'))
exit_button.config(bg='#123456',text='EXIT', fg='#eeeeee', height=2, command=root.quit)
exit_button.pack(side=tk.BOTTOM, fill=tk.X)

main_frame.pack(side=tk.TOP, fill=tk.BOTH, )
root.title('Calculator')
root.minsize(400, 400)
root.maxsize(400, 400)
root.mainloop()