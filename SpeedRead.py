# SpeedRead v1.0

from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox
from tkinter import colorchooser
from time import *


# Interface

FONT = 'Calibri 10'


def Cs(a):
    s = a.geometry()
    s = s.split('+')
    s = s[0].split('x')
    s[0] = str(int((a.winfo_screenwidth() - int(s[0]))/2))
    s[1] = str(int((a.winfo_screenheight() - int(s[1]))/2))
    a.geometry('+{0}+{1}'.format(s[0], s[1]))
    del s, a


def OpenFile():
    file = fd.askopenfilename()
    FPath.delete(0, END)
    FPath.insert(0, file)


def Read():
    fileName = FPath.get()
    if fileName == '':
        messagebox.showerror(title='ERROR_500', message='Select the file!!!')
    else:
        try:
            FL = open(fileName, encoding='UTF-8')
            T = FL.read()
            FL.close()
            T = T.replace('\n', ' ').replace('-', ' ').split(' ')
            T = list(filter(None, T))
            root = Tk()
            root.overrideredirect(True)
            root.geometry(str(window.winfo_screenwidth()) + 'x' + str(window.winfo_screenheight()))
            root['bg'] = nowback['bg']

            text = Label(root, font=FONT[0:len(FONT) - 2] + size.get(), text=T[0], bg=nowback['bg'], fg=nowtxt['bg'])
            text.pack(expand=1)
            root.update()
            sleep(float(slep.get())/100*2)
            for i in range(len(T)):
                text['text'] = T[i]
                root.update()
                sleep(float(slep.get())/100)
            root.destroy()

        except:
            messagebox.showerror(title='ERROR_404', message='This file was not found!!!')


def ChooseColorTxT():
    nowtxt['bg'] = colorchooser.askcolor()[1]


def ChooseColorBK():
    nowback['bg'] = colorchooser.askcolor()[1]


window = Tk()
window.geometry('700x300')
window.update_idletasks()
Cs(window)
window.iconbitmap('assets/Speed.ico')
window.title("Duda's Encryption v3.1.5.9")
window['bg'] = "gray20"
window.minsize(500, 250)

f_All = LabelFrame(window, font=FONT, text="Settings of Read: ", bg='gray20', fg='white')
f_1 = Frame(f_All, bg='gray20')
f_2 = Frame(f_All, bg='gray20')
f_3 = Frame(f_All, bg='gray20')
f_4 = Frame(f_All, bg='gray20')
f_5 = Frame(f_All, bg='gray20')
f_6 = Frame(f_All, bg='gray20')

FPath = Entry(f_1, font=FONT, width=60, bg='grey20', fg='white')
btnCF = Button(f_1, font=FONT, text='Choose file...', bg='grey25', fg='white', command=OpenFile)
warnin = Label(f_2, font=FONT, text='Note: the File must be saved in ASCII encoding!!!',  bg='grey20', fg='white')
slepL = Label(f_3, font=FONT, text='Pause between words while reading: ',  bg='grey20', fg='white')
slep = Spinbox(f_3, font=FONT, from_=11, to=30, width=3, bg='grey20', fg='white')
unit_1 = Label(f_3, text='ms',  bg='grey20', fg='white')
sizeL = Label(f_4, font=FONT, text='Font size: ', bg='grey20', fg='white')
size = Spinbox(f_4, font=FONT, from_=20, to=100, width=3, bg='grey20', fg='white')
unit_2 = Label(f_4, text='pt',  bg='grey20', fg='white')
coltxt = Button(f_5, font=FONT, text='Choose the text color', bg='grey25', fg='white', command=ChooseColorTxT)
nowtxt = Button(f_5, width=2, bg='white')
nowtxt.configure(state=DISABLED)
colback = Button(f_6, font=FONT, text='Choose the background color', bg='grey25', fg='white', command=ChooseColorBK)
nowback = Button(f_6, width=2, bg='grey25')
nowback.configure(state=DISABLED)
btnRd = Button(f_All, font=FONT, text='Read Text', height=2, bg='grey25', fg='white', command=Read)

f_All.pack(expand=1, fill=BOTH, padx=2, pady=2)
f_1.pack(anchor=SW, side=TOP, padx=2, pady=2)
f_2.pack(anchor=SW, side=TOP, padx=2, pady=5)
f_3.pack(anchor=SW, side=TOP, padx=2, pady=2)
f_4.pack(anchor=SW, side=TOP, padx=2, pady=2)
f_5.pack(anchor=SW, side=TOP, padx=2, pady=2)
f_6.pack(anchor=SW, side=TOP, padx=2, pady=2)
FPath.pack(side=LEFT)
btnCF.pack(side=LEFT, padx=2)
warnin.pack(side=LEFT)
slepL.pack(side=LEFT)
slep.pack(side=LEFT)
unit_1.pack(side=LEFT)
sizeL.pack(side=LEFT)
size.pack(side=LEFT)
unit_2.pack(side=LEFT)
coltxt.pack(side=LEFT)
nowtxt.pack(side=LEFT, padx=5)
colback.pack(side=LEFT)
nowback.pack(side=LEFT, padx=5)
btnRd.pack(anchor=SE, side=BOTTOM, padx=3, pady=3)
window.mainloop()
