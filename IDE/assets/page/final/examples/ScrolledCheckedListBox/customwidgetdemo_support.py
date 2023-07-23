#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by SEEMAN version 7m
#  in conjunction with Tcl version 8.6
#    Aug 09, 2021 12:06:47 PM PDT  platform: Linux
# ======================================================
#     customwidgetdemo_support.py
#  ------------------------------------------------------
# Created for the Learning Page Book Project
# Written by G.D. Walters
# Copyright (c) 2018 by G.D. Walters
# This source code is released under the MIT License
# (See MIT_License.txt)
# Version 1.0
# ======================================================
# MANY thanks to Don Rozenberg for his help in getting the
# ScrolledCheckedListBox widget working without modifying the
# main GUI.py file
# ======================================================
# Updated to the new code scheme by Don Rozenberg 6/13/21

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
from ScrolledCheckedListBox import ScrolledCheckedListBox

import customwidgetdemo

def main(*args):
    '''Main entry point for the application.'''
    global root
    root = tk.Tk()
    root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
    # Creates a toplevel widget.
    global _top39, _w39
    _top39 = root
    _w39 = customwidgetdemo.formCustomDemo(_top39)
    init(_top39, _w39)
    root.mainloop()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top
    # ======================================================
    # Our init code
    # ======================================================
    global ListInfo, ListInfo2
    # =======================================================
    # Create the list of text items for the ScrolledCheckBox
    # =======================================================
    ListInfo = ['Appetizer', 'Snack', 'Barbecue', 'Cake', 'Candy', 'Beverages',
                'Breads', 'Canning & Freezing', 'Cookies', 'Desserts', 'Meats',
                'Main Dish', 'Snacks', 'Rice', 'Poultry', 'Sauces', 'Soups',
                'American', 'Mexican', 'Asian']
    ListInfo2 = [['Appetizer', 1], ['Snack', 2], ['Barbecue', 3], ['Cake', 4],
                 ['Candy', 5], ['Beverages', 6], ['Breads', 7],
                 ['Canning & Freezing', 8], ['Cookies', 9], ['Desserts', 10],
                 ['Eggs & Cheese', 11], ['Fish & Seafood', 12], ['Meats', 13],
                 ['Pies', 14], ['Poultry', 15], ['Rice', 16], ['Pasta', 17],
                 ['Cereal', 18], ['Salads & Dressings', 19], ['Sauces', 20]]

    initialize_custom_widget()

def on_click(s=None):
    # ======================================================
    # On event, scrolled frame returns a list containing:
    #    item number selected
    #    text of checkbox selected
    # ======================================================
    update_label()
    print(w.Custom1.get())

def on_btnClearChecks(*args):
    w.Custom1.clear()
    w.Message1.configure(text='')


def on_btnExit(*args):
    destroy_window()


def on_btnGetChecks(*args):
    lst = w.Custom1.get()
    print(lst)


def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top
    # ======================================================
    # Our init code
    # ======================================================
    global ListInfo, ListInfo2
    # =======================================================
    # Create the list of text items for the ScrolledCheckBox
    # =======================================================
    ListInfo = ['Appetizer', 'Snack', 'Barbecue', 'Cake', 'Candy', 'Beverages',
                'Breads', 'Canning & Freezing', 'Cookies', 'Desserts', 'Meats',
                'Main Dish', 'Snacks', 'Rice', 'Poultry', 'Sauces', 'Soups',
                'American', 'Mexican', 'Asian']
    ListInfo2 = [['Appetizer', 1], ['Snack', 2], ['Barbecue', 3], ['Cake', 4],
                 ['Candy', 5], ['Beverages', 6], ['Breads', 7],
                 ['Canning & Freezing', 8], ['Cookies', 9], ['Desserts', 10],
                 ['Eggs & Cheese', 11], ['Fish & Seafood', 12], ['Meats', 13],
                 ['Pies', 14], ['Poultry', 15], ['Rice', 16], ['Pasta', 17],
                 ['Cereal', 18], ['Salads & Dressings', 19], ['Sauces', 20]]

    initialize_custom_widget()


def initialize_custom_widget():
    w.Custom1.cback = on_click
    # To use a single list of item names comment out the next line and
    # uncomment the second line down.
    w.Custom1.load(ListInfo2)
    # w.Custom1.load(ListInfo)
    clear_label()
    set_labels()


# ======================================================
# function set_labels()
# ------------------------------------------------------
# This calls the .set() method of the ScrolledCheckBox
# class.  That method allows items selected on initialization
# of a form.  Useful when loading a list of items for editing or
# showing already selected items from a database.
# ======================================================
def set_labels():
    w.Custom1.set(['Appetizer', 'Candy', 'Breads'])
    update_label()


# ======================================================
# function UpdateLabel()
# ------------------------------------------------------
# This function will update the message widget with the
# text of each selected item for quick visual reference.
# Usually not needed.
# ======================================================
def update_label():
    dat = w.Custom1.get()
    lst = []
    for x in dat:
        # print(len(x),x)
        if len(x) == 2:
            t = x[0]
            k = x[1]
            lst.append(t)
        else:
            lst.append(x)
    s = ", ".join(lst)
    w.Message1.configure(text=s)


# ======================================================
# function ClearLabel()
# ------------------------------------------------------
# simply clears the message widget
# ======================================================
def clear_label():
    w.Message1.configure(text="")


def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None


Custom = tk.Frame  # To be updated by user with name of custom widget.
Custom = ScrolledCheckedListBox



def initialize_custom_widget():
    w.Custom1.cback = on_click
    # To use a single list of item names comment out the next line and
    # uncomment the second line down.
    w.Custom1.load(ListInfo2)
    # w.Custom1.load(ListInfo)
    clear_label()
    set_labels()


# ======================================================
# function set_labels()
# ------------------------------------------------------
# This calls the .set() method of the ScrolledCheckBox
# class.  That method allows items selected on initialization
# of a form.  Useful when loading a list of items for editing or
# showing already selected items from a database.
# ======================================================
def set_labels():
    w.Custom1.set(['Appetizer', 'Candy', 'Breads'])
    update_label()


# ======================================================
# function UpdateLabel()
# ------------------------------------------------------
# This function will update the message widget with the
# text of each selected item for quick visual reference.
# Usually not needed.
# ======================================================
def update_label():
    dat = w.Custom1.get()
    lst = []
    for x in dat:
        # print(len(x),x)
        if len(x) == 2:
            t = x[0]
            k = x[1]
            lst.append(t)
        else:
            lst.append(x)
    s = ", ".join(lst)
    w.Message1.configure(text=s)


# ======================================================
# function ClearLabel()
# ------------------------------------------------------
# simply clears the message widget
# ======================================================
def clear_label():
    w.Message1.configure(text="")


def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None


Custom = tk.Frame  # To be updated by user with name of custom widget.
Custom = ScrolledCheckedListBox

if __name__ == '__main__':
    customwidgetdemo.start_up()




