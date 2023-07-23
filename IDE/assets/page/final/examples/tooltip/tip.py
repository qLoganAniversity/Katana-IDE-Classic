#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by SEEMAN version 7.4j
#  in conjunction with Tcl version 8.6
#    Apr 10, 2022 12:15:21 PM PDT  platform: Linux

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import tip_support

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = 'wheat'  # X11 color: #f5deb3
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#b2c9f4' # Closest X11 color: 'SlateGray2'
        _ana1color = '#eaf4b2' # Closest X11 color: '{pale goldenrod}'
        _ana2color = '#f4bcb2' # Closest X11 color: 'RosyBrown2'
        _tabfg1 = 'black' 
        _tabfg2 = 'black' 

        top.geometry("516x313+0+0")
        top.minsize(1, 1)
        top.maxsize(1905, 1050)
        top.resizable(1,  1)
        top.title("New Toplevel")
        top.configure(background="wheat")
        top.configure(highlightbackground="wheat")
        top.configure(highlightcolor="black")

        self.top = top

        self.btn_change = tk.Button(self.top)
        self.btn_change.place(relx=0.62, rely=0.447, height=33, width=89)
        self.btn_change.configure(activebackground="#f4bcb2")
        self.btn_change.configure(background="wheat")
        self.btn_change.configure(command=tip_support.change)
        self.btn_change.configure(disabledforeground="#b8a786")
        self.btn_change.configure(font="-family {DejaVu Sans} -size 12")
        self.btn_change.configure(highlightbackground="wheat")
        self.btn_change.configure(text='''Change''')

        self.btn_dest = tk.Button(self.top)
        self.btn_dest.place(relx=0.194, rely=0.447, height=33, width=64)
        self.btn_dest.configure(activebackground="#f4bcb2")
        self.btn_dest.configure(background="wheat")
        self.btn_dest.configure(disabledforeground="#b8a786")
        self.btn_dest.configure(font="-family {DejaVu Sans} -size 12")
        self.btn_dest.configure(highlightbackground="wheat")
        self.btn_dest.configure(text='''Dest''')
        self.tooltip_font = "-family {DejaVu Sans} -size 12"
        self.btn_dest_tooltip = \
        ToolTip(self.btn_dest, self.tooltip_font, '''Destination''')

        self.btn_quit = tk.Button(self.top)
        self.btn_quit.place(relx=0.388, rely=0.671, height=33, width=104)
        self.btn_quit.configure(activebackground="#f4bcb2")
        self.btn_quit.configure(background="wheat")
        self.btn_quit.configure(command=tip_support.quit)
        self.btn_quit.configure(compound='left')
        self.btn_quit.configure(disabledforeground="#b8a786")
        self.btn_quit.configure(font="-family {DejaVu Sans} -size 12")
        self.btn_quit.configure(highlightbackground="wheat")
        photo_location = "./stop.png"
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.btn_quit.configure(image=_img0)
        self.btn_quit.configure(text='''Quit''')

        self.Message1 = tk.Message(self.top)
        self.Message1.place(relx=0.155, rely=0.128, relheight=0.233
                , relwidth=0.678)
        self.Message1.configure(background="wheat")
        self.Message1.configure(font="-family {DejaVu Sans} -size 12")
        self.Message1.configure(highlightbackground="wheat")
        self.Message1.configure(text='''Select the "Change" button to modify
the "Dest" button tooltip and adds a
tooltip to the "Quit" button.''')
        self.Message1.configure(width=326)

class Toplevel1_1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = 'wheat'  # X11 color: #f5deb3
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#b2c9f4' # Closest X11 color: 'SlateGray2'
        _ana1color = '#eaf4b2' # Closest X11 color: '{pale goldenrod}'
        _ana2color = '#f4bcb2' # Closest X11 color: 'RosyBrown2'
        _tabfg1 = 'black' 
        _tabfg2 = 'black' 

        top.geometry("516x313+905+386")
        top.minsize(1, 1)
        top.maxsize(1905, 1050)
        top.resizable(1,  1)
        top.title("Copied")
        top.configure(background="wheat")
        top.configure(highlightbackground="wheat")
        top.configure(highlightcolor="black")

        self.top = top

        self.btn_change = tk.Button(self.top)
        self.btn_change.place(relx=0.62, rely=0.447, height=33, width=89)
        self.btn_change.configure(activebackground="#f4bcb2")
        self.btn_change.configure(background="wheat")
        self.btn_change.configure(command=tip_support.change)
        self.btn_change.configure(disabledforeground="#b8a786")
        self.btn_change.configure(font="-family {DejaVu Sans} -size 12")
        self.btn_change.configure(highlightbackground="wheat")
        self.btn_change.configure(text='''Change''')

        self.btn_dest = tk.Button(self.top)
        self.btn_dest.place(relx=0.194, rely=0.447, height=33, width=64)
        self.btn_dest.configure(activebackground="#f4bcb2")
        self.btn_dest.configure(background="wheat")
        self.btn_dest.configure(disabledforeground="#b8a786")
        self.btn_dest.configure(font="-family {DejaVu Sans} -size 12")
        self.btn_dest.configure(highlightbackground="wheat")
        self.btn_dest.configure(text='''Dest''')
        self.tooltip_font = "-family {DejaVu Sans} -size 12"
        self.btn_dest_tooltip = \
        ToolTip(self.btn_dest, self.tooltip_font, '''Destination''')

        self.btn_quit = tk.Button(self.top)
        self.btn_quit.place(relx=0.388, rely=0.671, height=33, width=104)
        self.btn_quit.configure(activebackground="#f4bcb2")
        self.btn_quit.configure(background="wheat")
        self.btn_quit.configure(command=tip_support.quit)
        self.btn_quit.configure(compound='left')
        self.btn_quit.configure(disabledforeground="#b8a786")
        self.btn_quit.configure(font="-family {DejaVu Sans} -size 12")
        self.btn_quit.configure(highlightbackground="wheat")
        photo_location = "./stop.png"
        global _img1
        _img1 = tk.PhotoImage(file=photo_location)
        self.btn_quit.configure(image=_img1)
        self.btn_quit.configure(text='''Quit''')

        self.Message1 = tk.Message(self.top)
        self.Message1.place(relx=0.155, rely=0.128, relheight=0.233
                , relwidth=0.678)
        self.Message1.configure(background="wheat")
        self.Message1.configure(font="-family {DejaVu Sans} -size 12")
        self.Message1.configure(highlightbackground="wheat")
        self.Message1.configure(text='''Select the "Change" button to modify
the "Dest" button tooltip and adds a
tooltip to the "Quit" button.''')
        self.Message1.configure(width=326)

# Support code for Balloon Help (also called tooltips).
# derived from http://code.activestate.com/recipes/576688-tooltip-for-tkinter/
from time import time, localtime, strftime
class ToolTip(tk.Toplevel):
    """ Provides a ToolTip widget for Tkinter. """
    def __init__(self, wdgt, tooltip_font, msg=None, msgFunc=None,
                 delay=0.5, follow=True):
        self.wdgt = wdgt
        self.parent = self.wdgt.master
        tk.Toplevel.__init__(self, self.parent, bg='black', padx=1, pady=1)
        self.withdraw()
        self.overrideredirect(True)
        self.msgVar = tk.StringVar()
        if msg is None:
            self.msgVar.set('No message provided')
        else:
            self.msgVar.set(msg)
        self.msgFunc = msgFunc
        self.delay = delay
        self.follow = follow
        self.visible = 0
        self.lastMotion = 0
        tk.Message(self, textvariable=self.msgVar, bg='#FFFFDD',
                font=tooltip_font,
                aspect=1000).grid()
        self.wdgt.bind('<Enter>', self.spawn, '+')
        self.wdgt.bind('<Leave>', self.hide, '+')
        self.wdgt.bind('<Motion>', self.move, '+')
    def spawn(self, event=None):
        self.visible = 1
        self.after(int(self.delay * 1000), self.show)
    def show(self):
        if self.visible == 1 and time() - self.lastMotion > self.delay:
            self.visible = 2
        if self.visible == 2:
            self.deiconify()
    def move(self, event):
        self.lastMotion = time()
        if self.follow is False:
            self.withdraw()
            self.visible = 1
        self.geometry('+%i+%i' % (event.x_root+20, event.y_root-10))
        try:
            self.msgVar.set(self.msgFunc())
        except:
            pass
        self.after(int(self.delay * 1000), self.show)
    def hide(self, event=None):
        self.visible = 0
        self.withdraw()
    def update(self, msg):
        self.msgVar.set(msg)
#                   End of Class ToolTip

def start_up():
    tip_support.main()

if __name__ == '__main__':
    tip_support.main()



