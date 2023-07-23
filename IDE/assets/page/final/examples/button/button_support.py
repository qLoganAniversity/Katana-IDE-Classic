#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by SEEMAN version 7v
#  in conjunction with Tcl version 8.6
#    Sep 12, 2021 09:10:57 AM PDT  platform: Linux

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import button

def main(*args):
    '''Main entry point for the application.'''
    global root
    root = tk.Tk()
    root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
    # Creates a toplevel widget.
    global _top34, _w34
    _top34 = root
    _w34 = button.Toplevel1(_top34)
    root.mainloop()

def quit(*args):
    print('button_support.quit')
    for arg in args:
        print ('another arg:', arg)
    sys.stdout.flush()
    sys.exit()

if __name__ == '__main__':
    button.start_up()




