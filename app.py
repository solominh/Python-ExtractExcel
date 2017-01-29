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
    is_success = automate(url)
    AutomationButton.config(state=NORMAL)

    if is_success:
        messagebox.showinfo(
            'SUCCESS', 'Extracted data is a newest file at C:\Extractedb data')
    else:
        messagebox.showerror('ERROR', 'Cannot extract data')


def automate(url):
    download_url = find_downloadurl_in(url)
    if not download_url:
        return False

    savedir = os.path.abspath('C:/Extracted Excel')
    if not os.path.exists(savedir):
        os.mkdir(savedir)

    filename = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S.xlsx")
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
