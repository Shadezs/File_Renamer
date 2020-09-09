# import tkinter module
import os
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory
import csv

# creating main tkinter window/toplevel
extention = '.STEP'
master = Tk()
master.geometry('600x200')


def renameall():
    i = 0
    ind = 0;
    print('starte the rename')
    print(len(listoffilenames))
    while i < len(listoffilenames):
        filename = listoffilenames[i][0:12]  # This gets just the first 12 charates of the filename and puts in filename
        filespath = filedir + '/' + listoffilenames(i)
        print("first while")
        while ind < len(lpartn_name):  # this loop checks filename to partnumber
            print('second while')
            partnumber = lpartn_name[ind][0]
            partname = lpartn_name[ind][1]
            if filename == partnumber:
                dst = filespath + '/' + partname + extention
                src = filespath
                src = os.path.abspath(src)
                dst = os.path.abspath(dst)
                if os.path.exists(src):
                    if os.path.exists(dst) != True:
                        # File_name.write(src + " was change to ")
                        # File_name.write(dst + "\n")
                        os.rename(src, dst)
                        # number_of_renames += 1
                        print('file rename')
                        ind += 1
                        i += 1
                    else:
                        print("file already exist")
                        i += 1
                else:
                    print("file not there")
            ind += 1
        ind = 0
        i += 1


# print(number_of_renames)
# File_name.close()


def log(file, list, path):
    File_log = open(file, "w")
    list1 = list
    for count in list1:
        fullname = path + "\\" + count
        fullname = os.path.abspath(fullname)
        File_log.write(fullname + "\n")
    File_log.close()


def getfilepath():
    filedir = askdirectory()
    print(filedir)
    lfilenames = os.listdir(filedir)
    print(lfilenames)
    listoffilenames=lfilenames
    e2.insert(0, filedir)


def open_file():
    filePath = askopenfilename()
    e1.insert(0, filePath)
    if filePath is not None:
        with open(str(filePath), newline='') as Partnum:
            reader = csv.reader(Partnum)
            lpartn_name = list(reader)
    print(lpartn_name)
    # this wil create a label widget


l1 = Label(master, text="Parts number and name csv:")
l2 = Label(master, text="Path:")

# grid method to arrange labels in respective
# rows and columns as specified
l1.grid(row=0, column=0, sticky=W, pady=2)
l2.grid(row=1, column=0, sticky=W, pady=2)

# entry widgets, used to take entry from user
e1 = Entry(master)
e2 = Entry(master)

# this will arrange entry widgets
e1.grid(row=0, column=1, pady=2)
e2.grid(row=1, column=1, pady=2)

# checkbutton widget
c1 = Button(master, text="Path", command=lambda: getfilepath())
c1.grid(row=2, column=0, sticky=W, columnspan=2)

# button widget
b1 = Button(master, text="Rename", command=lambda: renameall())
b2 = Button(master, text='Open cvs', command=lambda: open_file())

# arranging button widgets
b1.grid(row=2, column=2, sticky=E)
b2.grid(row=2, column=3, sticky=E)

# infinite loop which can be terminated
# by keyboard or mouse interrupt

mainloop()
lpartn_name = []
filedir=''
filepath = ''
listoffilenames = []
