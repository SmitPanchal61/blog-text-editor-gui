import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import font


# functions for the buttons

# Open a file for editing function
def open_file():
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Thecleverprogrammer - {filepath}")

# Save the current file as a new file function
def save_file():
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
    window.title(f"Thecleverprogrammer - {filepath}")

# creating text bold function
def bolds():
    # creating our font
    bold_font = font.Font(txt_edit, txt_edit.cget("font"))
    bold_font.configure(weight="bold")

    # configure a tag
    txt_edit.tag_configure("bold",font=bold_font)

    #define current tag
    current_tags = txt_edit.tag_names("sel.first")

    # if statement to check boldness
    if "bold" in current_tags:
        txt_edit.tag_remove("bold","sel.first","sel.last")
    else:
        txt_edit.tag_add("bold","sel.first","sel.last")

# creating text italic function
def italics():
    # creating our font
    italics_font = font.Font(txt_edit, txt_edit.cget("font"))
    italics_font.configure(slant="italic")

    # configure a tag
    txt_edit.tag_configure("italic",font=italics_font)

    #define current tag
    current_tags = txt_edit.tag_names("sel.first")

    # if statement to check italicness
    if "italic" in current_tags:
        txt_edit.tag_remove("italic","sel.first","sel.last")
    else:
        txt_edit.tag_add("italic","sel.first","sel.last")

# clearing everything function
def Clear():
   txt_edit.delete("1.0","end")

# closing the text editor
def close_file():
    exit()

# creating the main root window
window = tk.Tk()
window.title("article editor")
window.rowconfigure(0, minsize=600, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

# selecting image as a label
x = tk.PhotoImage(file = "Record_your_thoughts.png")
y = tk.Label(image=x, relief=tk.RAISED)

# creating textbox
txt_edit = tk.Text(window,undo=True)
txt_edit.configure(font=("Times New Roman", 20))

# creating frame for the buttons
fr_buttons = tk.Frame(window, bd=2, bg="#d4edf4")

# defining font size for the buttons
myFont = font.Font(size=15)

# buttons

# open button
btn_open = tk.Button(fr_buttons, text="Open",bg='#0052cc', fg='#ffffff', command=open_file)
btn_open['font'] = myFont

# save button
btn_save = tk.Button(fr_buttons, text="Save As...",bg='#0052cc', fg='#ffffff', command=save_file)
btn_save['font'] = myFont

# bold button
btn_bold = tk.Button(fr_buttons, text="Bold",bg='#0052cc', fg='#ffffff', command=bolds)
btn_bold['font'] = myFont

# italic button
btn_italic = tk.Button(fr_buttons, text="Italic",bg='#0052cc', fg='#ffffff', command=italics)
btn_italic['font'] = myFont

# undo button
btn_undo = tk.Button(fr_buttons, text="Undo",bg='#0052cc', fg='#ffffff', command=txt_edit.edit_undo)
btn_undo['font'] = myFont

# clear button
btn_clear = tk.Button(fr_buttons, text="Clear",bg='#0052cc', fg='#ffffff', command=Clear)
btn_clear['font'] = myFont

# close window button
btn_close = tk.Button(fr_buttons, text="Close", command=close_file , bg="red")
btn_close['font'] = myFont

# packing stuff in grid form

# packing the image
y.grid(row=0,column=2, sticky="ew")

# packing the buttons and applying padding
btn_open.grid(row=0, column=0, sticky="ew", padx=20, pady=20)
btn_save.grid(row=1, column=0, sticky="ew", padx=20, pady=20)
btn_bold.grid(row=2, column=0, sticky="ew", padx=20, pady=20)
btn_italic.grid(row=3, column=0, sticky="ew", padx=20, pady=20)
btn_clear.grid(row=4, column=0, sticky="ew", padx=20, pady=20)
btn_undo.grid(row=5, column=0, sticky="ew", padx=20, pady=20)
btn_close.grid(row=6, column=0, sticky="ew", padx=20, pady=20)

# packing the frame
fr_buttons.grid(row=0, column=0, sticky="ns")

# packing the textbox
txt_edit.grid(row=0, column=1, sticky="nsew")

# making window appear as fullscreen on startup
window.attributes('-fullscreen', True)

# main eventloop
window.mainloop()