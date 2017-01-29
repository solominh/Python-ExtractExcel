from tkinter import Tk, Frame, Label, Entry, Button, messagebox, LEFT, RIGHT, TOP, BOTTOM, NORMAL, DISABLED
import validators
from download_service import find_downloadurl_in, download_file_from_url
from excel_service import extract_data
import os
import datetime


def run_automation():
    global URLEntry, AutomationButton

    url = URLEntry.get()
    if not validators.url(url) is True:
        messagebox.showerror('ERROR', 'Please enter a valid URL')
        return

    AutomationButton.config(state=DISABLED)
    automate(url)
    messagebox.showinfo('RESULT', url)


def automate(url):
    download_url = find_downloadurl_in(url)
    if not download_url:
        return False

    savedir = 'C:/Extracted Excel'
    filename = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    savepath = os.path.join(savedir, filename)
    is_success = download_file_from_url(download_url, savepath)
    if not is_success:
        return False

    extract_data(savepath)


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
