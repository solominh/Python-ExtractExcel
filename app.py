from tkinter import Tk, Frame, Label, Entry, Button, messagebox, LEFT, RIGHT, TOP, BOTTOM, NORMAL,DISABLED
import validators


def run_automation():
    global URLEntry, AutomationButton
    
    url = URLEntry.get()
    if not validators.url(url) == True:
        messagebox.showerror('ERROR', 'Please enter a valid URL')
        return

    AutomationButton.config(state=DISABLED)
    messagebox.showinfo('RESULT', url)


root = Tk()
# root.minsize(width=500, height=100)
frame = Frame(root)
frame.pack()

bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)

URLLabel = Label(frame, text="URL")
URLLabel.pack(side=LEFT)

URLEntry = Entry(frame, bd=5, width=100)
URLEntry.pack(side=RIGHT)
URLEntry.get

AutomationButton = Button(
    bottomframe, text="Automate", command=run_automation)
AutomationButton.pack(side=BOTTOM)

root.mainloop()
