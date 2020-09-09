import os
import csv

# get path to where files are store, will change latter to working dir and ask user for path
Extention = ".STEP"
# Realpath =os.path.abspath(Folder_Path)
# create list where filename will be stored
ind = 0
number_of_renames = 0


# class for reading file dir
class FileNames:
    def __init__(self, path):
        self.lfiles = []
        self.Path = path
        Folder_Path = self.Path
        with os.scandir(Folder_Path) as listt:  # scan path for files , if it is a file then it gets added to the list
            for file in listt:
                if file.is_file():
                    self.lfiles.append(file.name)

    def folderlist(self):
        return self.lfiles

    def leng(self):
        return len(self.lfiles)

    def realpa(self, i):
        fullpath = self.Path + "\\" + self.lfiles[i]
        return os.path.abspath(fullpath)

    def fold(self):
        return self.Path

    # child class of the above , just for overing a fuction . why do this python!!!!!!!!!

    def Folderlistindex(self, numlend=12, i=0):
        filepartnum = self.lfiles[i][0:numlend]
        return filepartnum


class soucerpartname:
    def __init__(self, files):
        self.Lpartn_name = []
        self.file = files
        filename = self.file

    def readcsvfile(self):
        with open(filename, newline='') as Partnum:
            reader = csv.reader(Partnum)
            self.Lpartn_name = list(reader)

    def listfn(self):
        return self.Lpartn_name

    def lend(self):
        return len(self.Lpartn_name)

    def partnumber(self, i=0):
        return self.Lpartn_name[i][0]

    def partname(self, i=0):
        return self.Lpartn_name[i][1]


lfiles = soucerchild("C:\\Users\\battl\\Downloads\\VEX IQ Structure, Motion Elements")
sourceparts = soucerpartname("newParts.csv")
splist = sourceparts.listfn()
filelist = lfiles.folderlist()


# this loop gets the part number from a list of csv
def log(file, list, path):
    File_log = open(file, "w")
    list1 = list
    for count in list1:
        fullname = path + "\\" + count
        fullname = os.path.abspath(fullname)
        File_log.write(fullname + "\n")
    File_log.close()


index2 = 0
File_name = open(r"rename_files.txt", "w")
i = 0
log("logone.txt", filelist, lfiles.fold())
# todo
# make this a fuction or just leave it like this ,not sure yet
while i < lfiles.leng():
    filename = filelist[i][0:12]  # This gets just the first 12 charates of the filename and puts in filename
    filepath = lfiles.realpa(i)
    while ind < sourceparts.lend():  # this loop checks filename to partnumber
        partnumber = sourceparts.partnumber(ind)
        partname = sourceparts.partname(ind)
        if filename == partnumber:
            dst = lfiles.fold() + "\\" + partname + Extention
            src = filepath
            src = os.path.abspath(src)
            dst = os.path.abspath(dst)
            if os.path.exists(src):
                if os.path.exists(dst) != True:
                    File_name.write(src + " was change to ")
                    File_name.write(dst + "\n")
                    os.rename(src, dst)
                    number_of_renames += 1
                    ind = 0
                    i += 1
                else:
                    print("file already exist")
                    i += 1
            else:
                print("file not there")
        ind += 1
    ind = 0
    i += 1
print(number_of_renames)
File_name.close()
