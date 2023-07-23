#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 7m
#  in conjunction with Tcl version 8.6
#    Aug 09, 2021 09:04:39 AM PDT  platform: Linux

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import vrex
from tkinter import filedialog

def main(*args):
    '''Main entry point for the application.'''
    global root
    root = tk.Tk()
    root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
    # Creates a toplevel widget.
    global _top1, _w1
    _top1 = root
    _w1 = vrex.Vrex(_top1)
    init(root, _w1)
    root.mainloop()

def init(tk_root,gui):
    global w, root
    w = gui
    root = tk_root
    # This is executed after the GUI is drawn.
    global colors, color_noreport, color_lookahead, levels, o_e, o_s, o_m
    # Define the object names for the three text windows;
    o_e = w.Expression
    o_s = w.Sample
    o_m = w.Matches
    # the colors for the different matching groups
    colors = ['red', 'blue', 'darkgreen', 'magenta', 'sienna', 'purple',
              'firebrick', 'deeppink', 'deeppink', 'deepskyblue1']
    # background color to visualize the non-reporting group (?:...)
    color_noreport = 'cyan'
    # background color to visualize the lookhead group (?=...) and (?!...)
    color_lookahead = 'plum'
    # define levels
    levels = ['e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9']
    # configure the tags to be used.
    for i in range(len(levels)):
        o_e.tag_configure(levels[i], foreground=colors[i])
        o_s.tag_configure(levels[i], foreground=colors[i])
        o_m.tag_configure(levels[i], foreground=colors[i])
    o_e.tag_configure('lookahead', background=color_lookahead)
    o_e.tag_configure('noreport', background=color_noreport)

def display(*args):
    go()
    clear_textbox(o_m)
    level = args[0]
    for i in range(len(mo)-1):
        if mo[i] == None:
            insert_text(o_m, "Match failed\n")
        else:
            if level <= len(mo[i].groups()):
                # Insert the text corresponding to the match group.
                start, end = mo[i].span(level)
                str = s_lines[i][start:end]
                insert_text(o_m, str+'\n')
                line = '%d.0' % (i+1,)
                last = '%d.%d' % (i+1,end)
                o_m.tag_add(levels[level], line, last) # Colorize text.

def do_match():
    import re
    global mo, rexp, sample, s_lines
    rexp = read_textbox(o_e)
    rexp = rexp.strip()
    sample = read_textbox(o_s)
    s_lines = sample.split('\n')
    rc = re.compile(rexp)
    mo = []
    for line in s_lines:
        mo.append(rc.search(line))

def go(*args):
    regexp_colorize()
    do_match()
    sample_colorize()


def load_regular_expression(*args):
    regex_file = filedialog.askopenfilename(filetypes=[("all files", "*")])
    if regex_file:
        clear_textbox(o_e)
        rd = open(regex_file)
        exp = rd.read()
        o_e.insert('end',exp)
        rd.close()

def load_sample(*args):
    sample_file = filedialog.askopenfilename(filetypes=[("all files", "*")])
    if sample_file:
        clear_textbox(o_s)
        sd = open(sample_file)
        sample = sd.read()
        sample = sample.rstrip()
        o_s.insert('end',sample)

def quit(*args):
    import sys
    sys.exit()

def read_textbox(o):
    # Note how one can read all of the characters from a text box. The
    # 1.0 refers to the first character (line position 0) in vTclthe first
    # line (line 1).
    return o.get(1.0, 'end')

def regexp_colorize():
    global nblevels
    import types
    stack = []
    indicies = []
    # The format of indicies is a list of tuple each looking like
    # (type, min, max). Type can be report, no report, or lookahead.
    exp = read_textbox(o_e).rstrip()
    indicies.append(('report', 0, len(exp)))
    nblevels = 1
    for i in range(len(exp)):
        c = exp[i]
        if c == '\\':
            i += 1
            continue
        elif c == '(':
            c = exp[i+1]
            if c == '?':
                what = exp[1+2]
                if what == ':':
                    type = 'lookahead'
                else:
                    type = 'noreport'
            else:
                type = 'report'
            nblevels += 1
            min = i
            max = 0
            indicies.append((type, min, max))
            stack.append(len(indicies)-1)
        elif c == ')':
            idx = stack.pop()
            type, min, max = indicies[idx]
            indicies[idx] = (type, min, i)
    # Remove old colors.
    for level in range(nblevels):
        o_e.tag_remove(levels[level], 1.0, 'end')
    o_e.tag_remove("lookahead", 1.0, 'end')
    o_e.tag_remove("noreport", 1.0, 'end')
    # Colorize the regular expression
    i = 0
    for type,min,max in indicies:
        min_c = '1.0+%dchars' % min
        max_1 = max + 1
        max_c = '1.0+%dchars' % max_1
        o_e.tag_add(levels[i], min_c, max_c)
        i += 1
    # Colorize special items.
    for type,min,max in indicies:
        if type == 'report':
            continue
        min_c = '1.0+%dchars' % min
        max_1 = max + 1
        max_c = '1.0+%dchars' % (max + 1,)
        o_e.tag_add(type, min_c, max_c)

def sample_colorize():
    # Remove colors
    for level in range(nblevels):
        o_s.tag_remove(levels[level], 1.0, 'end')
    for i in range(len(mo)):
        if mo[i] == None:
            continue
        # Add the new colors
        if level <= len(mo[i].groups()):
            for level in range(nblevels):
                start, end = mo[i].span(level)
                min_c = '%d.0+%dchars' % (i+1, start)
                max_c = '%d.0+%dchars' % (i+1, end)
                o_s.tag_add(levels[level], min_c, max_c)


def save_regular_expression(*args):
    regex_file = tkFileDialog.asksaveasfilename(filetypes=[("all files", "*")])
    if regex_file:
        rd = open(regex_file, 'w')
        rxp = read_textbox(o_e)
        rd.write(rxp)
        rd.close()

def save_sample(*args):
    sample_file = tkFileDialog.asksaveasfilename(filetypes=[("all files", "*")])
    if sample_file:
        sd = open(sample_file, 'w')
        sample = read_textbox(o_s)
        sd.read(sample)
        sd.close()

def sync_matches(*args):
    ''' Function which makes sure that line in Matches corresponding
        to the like selected with button-1 in Sample is visible.'''
    index = w.Sample.index('current')
    w.Matches.see(index)

def sync_sample(*args):
    ''' Function which makes sure that line in Sample corresponding to
        the like selected with button-1 in Matches is visible.'''
    index = w.Matches.index('current')
    line, char = index.split('.')
    w.Sample.see(index)


def clear_textbox(o):
    o.delete(1.0, 'end')

def insert_text(o, str):
    o.insert('end', str)

def help(*args):
    # Creates toplevel Help widget.
    global _top94, _w94
    _top94 = tk.Toplevel(root)
    _w94 = vrex.Help(_top94)
    load_vrex_help(_w94.TScrolledtext1)

def load_vrex_help(o):
    help = '''
Vrex is a program for testing Python regular expressions.  The GUI is made up of a menu and a paned window with three adjustable sub-windows each of which contains a scrolled test window and a row of buttons which control the action of the program. The GUI may be resized as may this window.

One enters the regular expression under test into the top text box, and the sample which is the subject of the regular expression match into the middle text box.  One may use the File menu to load file into the text boxes, one may directly type entries or use the normal cut and paste facilities of the operating system

Pressing the Go button causes the match to be attempted.  Also, colorization is applied to both the regular expression and to the sample. The regular expression is colorized to show the portions of the regular expression which can be extracted individually. This has been called grouping. And if the match is successful the corresponding groups within the sample are displayed in the same colors as in the regular expression window.

By selecting one of the row of buttons marked match, 1, 2, ..., 9, the portions of the s v_help_support.py ample corresponding to extracted groups are displayed in the match window.

You can use the File menu to load to save both the regular expression and the sample as well as invoke this help window.

The Quit Button terminates the program. The File menu also has a Quit entry that terminates the program.

In normal usage, one loads a sample and a regular expression an experiments by incrementally changing both and then testing by hitting the go button. When you are satisfied, you can save the regular expression or put it on the clipboard by selecting the characters that make up the regular expression

You can also enter a whole file of sample strings using File->Load Sample. In that case, when you select Go, the regular expression candidate will be applied to each line individually in the sample an the sample will be colorized accordingly.  In the Matches window you will see the individual match results for each line. The two window can be synchronized by clicking in either the Sample window or the Matches window and the corresponding line will be visible in the other window. You can add build a set of samples by adding them to the sample window and saving the sample to a file.
'''

    o.insert('end', help)


def close(*args):
    print('vrex_support.close')
    sys.stdout.flush()
    _top94.destroy()

if __name__ == '__main__':
    vrex.start_up()



