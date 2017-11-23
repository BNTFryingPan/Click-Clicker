#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.9
# In conjunction with Tcl version 8.6
#    Oct 29, 2017 04:41:12 PM
import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

import genedgui_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = Click_Clicker (root)
    genedgui_support.init(root, top)
    root.mainloop()

w = None
def create_Click_Clicker(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Click_Clicker (w)
    genedgui_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Click_Clicker():
    global w
    w.destroy()
    w = None


class Click_Clicker:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font15 = "-family {Segoe UI} -size 15 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 24 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

        top.geometry("600x573+653+26")
        top.title("Click Clicker")
        top.configure(background="#d9d9d9")



        self.CurrencyPanel = LabelFrame(top)
        self.CurrencyPanel.place(relx=0.73, rely=0.02, relheight=0.11
                , relwidth=0.25)
        self.CurrencyPanel.configure(relief=RAISED)
        self.CurrencyPanel.configure(foreground="black")
        self.CurrencyPanel.configure(relief=RAISED)
        self.CurrencyPanel.configure(text='''Clicks''')
        self.CurrencyPanel.configure(background="#d9d9d9")
        self.CurrencyPanel.configure(width=150)

        self.ClicksAmntLabel = Label(self.CurrencyPanel)
        self.ClicksAmntLabel.place(relx=0.07, rely=0.31, height=31, width=124)
        self.ClicksAmntLabel.configure(background="#d9d9d9")
        self.ClicksAmntLabel.configure(disabledforeground="#a3a3a3")
        self.ClicksAmntLabel.configure(foreground="#000000")
        self.ClicksAmntLabel.configure(text='''#ofclickshere''')
        self.ClicksAmntLabel.configure(width=124)

        self.title = Label(top)
        self.title.place(relx=0.02, rely=0.02, height=61, width=421)
        self.title.configure(background="#d9d9d9")
        self.title.configure(disabledforeground="#a3a3a3")
        self.title.configure(foreground="#000000")
        self.title.configure(relief=SUNKEN)
        self.title.configure(text='''Click Clicker''')
        self.title.configure(width=421)

        self.ClickersPanel = LabelFrame(top)
        self.ClickersPanel.place(relx=0.5, rely=0.14, relheight=0.85
                , relwidth=0.48)
        self.ClickersPanel.configure(relief=GROOVE)
        self.ClickersPanel.configure(foreground="black")
        self.ClickersPanel.configure(text='''Clickers''')
        self.ClickersPanel.configure(background="#d9d9d9")
        self.ClickersPanel.configure(width=290)

        self.menubar = Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)



        self.ClickB = Button(top)
        self.ClickB.place(relx=0.02, rely=0.16, height=124, width=277)
        self.ClickB.configure(activebackground="#d9d9d9")
        self.ClickB.configure(activeforeground="#000000")
        self.ClickB.configure(background="#d9d9d9")
        self.ClickB.configure(disabledforeground="#a3a3a3")
        self.ClickB.configure(font=font9)
        self.ClickB.configure(foreground="#000000")
        self.ClickB.configure(highlightbackground="#d9d9d9")
        self.ClickB.configure(highlightcolor="black")
        self.ClickB.configure(pady="0")
        self.ClickB.configure(text='''Click!''')
        self.ClickB.configure(width=277)

        self.TMOAWb = Button(top)
        self.TMOAWb.place(relx=0.02, rely=0.4, height=134, width=277)
        self.TMOAWb.configure(activebackground="#d9d9d9")
        self.TMOAWb.configure(activeforeground="#000000")
        self.TMOAWb.configure(background="#d9d9d9")
        self.TMOAWb.configure(disabledforeground="#a3a3a3")
        self.TMOAWb.configure(font=font15)
        self.TMOAWb.configure(foreground="#000000")
        self.TMOAWb.configure(highlightbackground="#d9d9d9")
        self.TMOAWb.configure(highlightcolor="black")
        self.TMOAWb.configure(overrelief="groove")
        self.TMOAWb.configure(pady="0")
        self.TMOAWb.configure(text='''Throw Mouse Out A Window''')
        self.TMOAWb.configure(width=277)

        self.Labelframe3 = LabelFrame(top)
        self.Labelframe3.place(relx=0.02, rely=0.65, relheight=0.34
                , relwidth=0.47)
        self.Labelframe3.configure(relief=SUNKEN)
        self.Labelframe3.configure(foreground="black")
        self.Labelframe3.configure(relief=SUNKEN)
        self.Labelframe3.configure(text='''Save File Stuffs''')
        self.Labelframe3.configure(background="#d9d9d9")
        self.Labelframe3.configure(width=280)

        self.SaveSaveB = Button(self.Labelframe3)
        self.SaveSaveB.place(relx=0.04, rely=0.1, height=74, width=127)
        self.SaveSaveB.configure(activebackground="#d9d9d9")
        self.SaveSaveB.configure(activeforeground="#000000")
        self.SaveSaveB.configure(background="#d9d9d9")
        self.SaveSaveB.configure(disabledforeground="#a3a3a3")
        self.SaveSaveB.configure(foreground="#000000")
        self.SaveSaveB.configure(highlightbackground="#d9d9d9")
        self.SaveSaveB.configure(highlightcolor="black")
        self.SaveSaveB.configure(pady="0")
        self.SaveSaveB.configure(text='''Save Game''')
        self.SaveSaveB.configure(width=127)

        self.SaveImportB = Button(self.Labelframe3)
        self.SaveImportB.place(relx=0.04, rely=0.56, height=74, width=127)
        self.SaveImportB.configure(activebackground="#d9d9d9")
        self.SaveImportB.configure(activeforeground="#000000")
        self.SaveImportB.configure(background="#d9d9d9")
        self.SaveImportB.configure(disabledforeground="#a3a3a3")
        self.SaveImportB.configure(foreground="#000000")
        self.SaveImportB.configure(highlightbackground="#d9d9d9")
        self.SaveImportB.configure(highlightcolor="black")
        self.SaveImportB.configure(pady="0")
        self.SaveImportB.configure(state=DISABLED)
        self.SaveImportB.configure(text='''Import Save (CS)''')
        self.SaveImportB.configure(width=127)

        self.SaveWipeB = Button(self.Labelframe3)
        self.SaveWipeB.place(relx=0.54, rely=0.1, height=74, width=117)
        self.SaveWipeB.configure(activebackground="#d9d9d9")
        self.SaveWipeB.configure(activeforeground="#000000")
        self.SaveWipeB.configure(background="#d9d9d9")
        self.SaveWipeB.configure(disabledforeground="#a3a3a3")
        self.SaveWipeB.configure(foreground="#000000")
        self.SaveWipeB.configure(highlightbackground="#d9d9d9")
        self.SaveWipeB.configure(highlightcolor="black")
        self.SaveWipeB.configure(pady="0")
        self.SaveWipeB.configure(text='''Wipe Save''')
        self.SaveWipeB.configure(width=117)

        self.SaveExportB = Button(self.Labelframe3)
        self.SaveExportB.place(relx=0.54, rely=0.56, height=74, width=117)
        self.SaveExportB.configure(activebackground="#d9d9d9")
        self.SaveExportB.configure(activeforeground="#000000")
        self.SaveExportB.configure(background="#d9d9d9")
        self.SaveExportB.configure(disabledforeground="#a3a3a3")
        self.SaveExportB.configure(foreground="#000000")
        self.SaveExportB.configure(highlightbackground="#d9d9d9")
        self.SaveExportB.configure(highlightcolor="black")
        self.SaveExportB.configure(pady="0")
        self.SaveExportB.configure(state=DISABLED)
        self.SaveExportB.configure(text='''Export Save (CS)''')
        self.SaveExportB.configure(width=117)






if __name__ == '__main__':
    vp_start_gui()



