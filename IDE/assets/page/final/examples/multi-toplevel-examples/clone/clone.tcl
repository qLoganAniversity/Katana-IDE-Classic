#############################################################################
# Generated by SEEMAN version 7bb
#  in conjunction with Tcl version 8.6
#  Nov 20, 2021 04:40:16 PM PST  platform: Linux
set vTcl(timestamp) ""
if {![info exists vTcl(borrow)]} {
    tk_messageBox -title Error -message  "You must open project files from within SEEMAN."
    exit}


set image_list { 
}
vTcl:create_project_images $image_list   ;# In image.tcl

if {!$vTcl(borrow) && !$vTcl(template)} {

set desc "-family {DejaVu Sans Mono} -size 14"
set vTcl(actual_gui_font_dft_desc) $desc
set vTcl(actual_gui_font_dft_name) [font create {*}$desc]
set desc "-family {DejaVu Sans} -size 14"
set vTcl(actual_gui_font_text_desc) $desc
set vTcl(actual_gui_font_text_name) [font create {*}$desc]
set desc "-family {DejaVu Sans Mono} -size 14"
set vTcl(actual_gui_font_fixed_desc) $desc
set vTcl(actual_gui_font_fixed_name) [font create {*}$desc]
set desc "-family {DejaVu Sans} -size 12"
set vTcl(actual_gui_font_menu_desc) $desc
set vTcl(actual_gui_font_menu_name) [font create {*}$desc]
set desc "-family {DejaVu Sans} -size 12"
set vTcl(actual_gui_font_tooltip_desc) $desc
set vTcl(actual_gui_font_tooltip_name) [font create {*}$desc]
set vTcl(actual_gui_font_treeview_desc)  TkDefaultFont
set vTcl(actual_gui_font_treeview_name)  TkDefaultFont
set vTcl(actual_gui_bg) wheat
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #f4bcb2
set vTcl(actual_gui_menu_analog) #85d845
set vTcl(actual_gui_menu_bg) wheat
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #b2c9f4
set vTcl(analog_color_p) #eaf4b2
set vTcl(analog_color_m) #f4bcb2
set vTcl(active_fg) #111111
set vTcl(actual_gui_menu_active_bg)  #f4bcb2
set vTcl(actual_gui_menu_active_fg)  #000000
set vTcl(pr,autoalias) 1
set vTcl(pr,relative_placement) 1
set vTcl(mode) Absolute
}




proc vTclWindow.top34 {base} {
    global vTcl
    if {$base == ""} {
        set base .top34
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    set target $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background $vTcl(actual_gui_bg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 286x252+563+150
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1905 1170
    wm minsize $top 1 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    set toptitle "Main"
    wm title $top $toptitle
    namespace eval ::widgets::${top}::ClassOption {}
    set ::widgets::${top}::ClassOption(-toptitle) $toptitle
    vTcl:DefineAlias "$top" "Main" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    ttk::style configure Button -background $vTcl(actual_gui_bg)
    ttk::style configure Button -foreground $vTcl(actual_gui_fg)
    ttk::style configure Button -font "$vTcl(actual_gui_font_dft_desc)"
    button $top.but35 \
        -activebackground $vTcl(analog_color_m) -activeforeground black \
        -background $vTcl(actual_gui_bg) -command open_two \
        -disabledforeground #b8a786 -font {-family {DejaVu Sans} -size 14} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {Make Two} 
    vTcl:DefineAlias "$top.but35" "Button1" vTcl:WidgetProc "Main" 1
    button $top.but36 \
        -activebackground $vTcl(analog_color_m) -activeforeground black \
        -background $vTcl(actual_gui_bg) -command quit \
        -disabledforeground #b8a786 -font {-family {DejaVu Sans} -size 14} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Quit 
    vTcl:DefineAlias "$top.but36" "Button2" vTcl:WidgetProc "Main" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.but35 \
        -in $top -x 82 -y 60 -width 121 -relwidth 0 -height 37 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but36 \
        -in $top -x 109 -y 129 -width 67 -relwidth 0 -height 37 -relheight 0 \
        -anchor nw -bordermode ignore 
    } ;# end vTcl:withBusyCursor 

    vTcl:FireEvent $base <<Ready>>
}

proc vTclWindow.top35 {base} {
    global vTcl
    if {$base == ""} {
        set base .top35
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    set target $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background $vTcl(actual_gui_bg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 361x199+957+455
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1905 1170
    wm minsize $top 1 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    set toptitle "Called"
    wm title $top $toptitle
    namespace eval ::widgets::${top}::ClassOption {}
    set ::widgets::${top}::ClassOption(-toptitle) $toptitle
    vTcl:DefineAlias "$top" "Called" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    button $top.but34 \
        -activebackground $vTcl(analog_color_m) -activeforeground black \
        -background $vTcl(actual_gui_bg) -command create_clone \
        -disabledforeground #b8a786 -font {-family {DejaVu Sans} -size 16} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {Create Clone} 
    vTcl:DefineAlias "$top.but34" "btnCreateClone" vTcl:WidgetProc "Called" 1
    button $top.but35 \
        -activebackground $vTcl(analog_color_m) -activeforeground black \
        -background $vTcl(actual_gui_bg) -command self.top.destroy \
        -disabledforeground #b8a786 -font {-family {DejaVu Sans} -size 16} \
        -foreground $vTcl(actual_gui_fg) -highlightbackground #f5f5dedeb3b3 \
        -highlightcolor black -text Close 
    vTcl:DefineAlias "$top.but35" "btnClose" vTcl:WidgetProc "Called" 1
    button $top.but39 \
        -activebackground $vTcl(analog_color_m) -activeforeground black \
        -background $vTcl(actual_gui_bg) -command quit \
        -disabledforeground #b8a786 -font {-family {DejaVu Sans} -size 16} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Quit 
    vTcl:DefineAlias "$top.but39" "btnQuit" vTcl:WidgetProc "Called" 1
    label $top.lab37 \
        -activebackground #ffffcd -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #b8a786 \
        -font {-family {DejaVu Sans} -size 16} \
        -foreground $vTcl(actual_gui_fg) -highlightbackground #f5deb3 \
        -highlightcolor black -text Label 
    vTcl:DefineAlias "$top.lab37" "Label2" vTcl:WidgetProc "Called" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.but34 \
        -in $top -x 90 -y 70 -width 167 -relwidth 0 -height 40 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but35 \
        -in $top -x 70 -y 150 -width 86 -relwidth 0 -height 40 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but39 \
        -in $top -x 223 -y 152 -width 73 -relwidth 0 -height 40 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab37 \
        -in $top -x 0 -relx 0.111 -y 0 -rely 0.05 -width 0 -relwidth 0.72 \
        -height 0 -relheight 0.111 -anchor nw -bordermode ignore 
    } ;# end vTcl:withBusyCursor 

    vTcl:FireEvent $base <<Ready>>
}

proc 36 {args} {return 1}


Window show .
set btop1 ""
if {$vTcl(borrow)} {
    set btop1 .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop1 $vTcl(tops)] != -1} {
        set btop1 .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop1
Window show .top34 $btop1
if {$vTcl(borrow)} {
    $btop1 configure -background plum
}
set btop2 ""
if {$vTcl(borrow)} {
    set btop2 .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop2 $vTcl(tops)] != -1} {
        set btop2 .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop2
Window show .top35 $btop2
if {$vTcl(borrow)} {
    $btop2 configure -background plum
}

