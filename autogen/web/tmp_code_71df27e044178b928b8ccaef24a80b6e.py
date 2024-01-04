from tkinter import *
root = Tk()
root.title("Output")

def output():
    text = text_entry.get()
    print(text)

button = Button(root, text="Submit", command=output)
button.pack()

text_entry = Entry(root)
text_entry.pack()

root.mainloop()