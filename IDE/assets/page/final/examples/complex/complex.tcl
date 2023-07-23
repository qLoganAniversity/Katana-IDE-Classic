#############################################################################
# Generated by SEEMAN version 7bb
#  in conjunction with Tcl version 8.6
#  Nov 19, 2021 10:07:38 PM PST  platform: Linux
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
set vTcl(actual_gui_bg) #f5deb3
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #f4bcb2
set vTcl(actual_gui_menu_analog) #85d845
set vTcl(actual_gui_menu_bg) #f5deb3
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #b2c9f4
set vTcl(analog_color_p) #eaf4b2
set vTcl(analog_color_m) #f4bcb2
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #f4bcb2
set vTcl(actual_gui_menu_active_fg)  #000000
set vTcl(pr,autoalias) 1
set vTcl(pr,relative_placement) 0
set vTcl(mode) Relative
}




proc vTclWindow.top37 {base} {
    global vTcl
    if {$base == ""} {
        set base .top37
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
    wm geometry $top 565x513+659+261
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1905 1050
    wm minsize $top 1 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    set toptitle "Complex Example"
    wm title $top $toptitle
    namespace eval ::widgets::${top}::ClassOption {}
    set ::widgets::${top}::ClassOption(-toptitle) $toptitle
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    ttk::style configure TPanedwindow -background $vTcl(actual_gui_bg)
    ttk::style configure TPanedwindow -foreground $vTcl(actual_gui_fg)
    ttk::style configure TPanedwindow -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::style configure TPanedwindow -background $vTcl(actual_gui_bg)
    ttk::style configure TPanedwindow.Label -background $vTcl(actual_gui_bg)
    ttk::style configure TPanedwindow.Label -foreground $vTcl(actual_gui_fg)
    ttk::style configure TPanedwindow.Label -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::panedwindow $top.tPa38 \
        -width 200 -height 200 
    vTcl:DefineAlias "$top.tPa38" "TPanedwindow1" vTcl:WidgetProc "Toplevel1" 1
    ttk::style configure TLabelframe.Label -background $vTcl(actual_gui_bg)
    ttk::style configure TLabelframe.Label -foreground $vTcl(actual_gui_fg)
    ttk::style configure TLabelframe.Label -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::style configure TLabelframe -background $vTcl(actual_gui_bg)
    ttk::labelframe $top.tPa38.p1 \
        -text {Pane 1} -width 200 -height 75 
    vTcl:DefineAlias "$top.tPa38.p1" "TPanedwindow1_p1" vTcl:WidgetProc "Toplevel1" 1
    set site_4_0 $top.tPa38.p1
    $top.tPa38 add $top.tPa38.p1 
    $top.tPa38 pane $top.tPa38.p1 -weight 0
    ttk::style configure TLabelframe.Label -background $vTcl(actual_gui_bg)
    ttk::style configure TLabelframe.Label -foreground $vTcl(actual_gui_fg)
    ttk::style configure TLabelframe.Label -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::style configure TLabelframe -background $vTcl(actual_gui_bg)
    ttk::labelframe $top.tPa38.p2 \
        -text {Pane 2} -width 200 -height 125 
    vTcl:DefineAlias "$top.tPa38.p2" "TPanedwindow1_p2" vTcl:WidgetProc "Toplevel1" 1
    set site_4_1 $top.tPa38.p2
    ttk::style configure TPanedwindow -background $vTcl(actual_gui_bg)
    ttk::style configure TPanedwindow.Label -background $vTcl(actual_gui_bg)
    ttk::style configure TPanedwindow.Label -foreground $vTcl(actual_gui_fg)
    ttk::style configure TPanedwindow.Label -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::panedwindow $site_4_1.tPa39 \
        -orient horizontal -width 200 -height 200 
    vTcl:DefineAlias "$site_4_1.tPa39" "TPanedwindow2" vTcl:WidgetProc "Toplevel1" 1
    ttk::style configure TLabelframe.Label -background $vTcl(actual_gui_bg)
    ttk::style configure TLabelframe.Label -foreground $vTcl(actual_gui_fg)
    ttk::style configure TLabelframe.Label -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::style configure TLabelframe -background $vTcl(actual_gui_bg)
    ttk::labelframe $site_4_1.tPa39.p1 \
        -text {Pane 1} -width 85 -height 200 
    vTcl:DefineAlias "$site_4_1.tPa39.p1" "TPanedwindow2_p1" vTcl:WidgetProc "Toplevel1" 1
    set site_6_0 $site_4_1.tPa39.p1
    $site_4_1.tPa39 add $site_4_1.tPa39.p1 
    $site_4_1.tPa39 pane $site_4_1.tPa39.p1 -weight 0
    ttk::style configure TLabelframe.Label -background $vTcl(actual_gui_bg)
    ttk::style configure TLabelframe.Label -foreground $vTcl(actual_gui_fg)
    ttk::style configure TLabelframe.Label -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::style configure TLabelframe -background $vTcl(actual_gui_bg)
    ttk::labelframe $site_4_1.tPa39.p2 \
        -text {Pane 2} -width 115 -height 200 
    vTcl:DefineAlias "$site_4_1.tPa39.p2" "TPanedwindow2_p2" vTcl:WidgetProc "Toplevel1" 1
    set site_6_1 $site_4_1.tPa39.p2
    ttk::style configure TNotebook -background $vTcl(actual_gui_bg)
    ttk::style configure TNotebook.Tab -background $vTcl(actual_gui_bg)
    ttk::style configure TNotebook.Tab -foreground $vTcl(actual_gui_fg)
    ttk::style configure TNotebook.Tab -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::style map TNotebook.Tab -background [list disabled $vTcl(actual_gui_bg) selected $vTcl(complement_color)]
    ttk::notebook $site_6_1.tNo40 \
        -width 300 -height 200 -takefocus {} 
    vTcl:DefineAlias "$site_6_1.tNo40" "TNotebook1" vTcl:WidgetProc "Toplevel1" 1
    frame $site_6_1.tNo40.t0 \
        -background $vTcl(actual_gui_bg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    vTcl:DefineAlias "$site_6_1.tNo40.t0" "TNotebook1_t0" vTcl:WidgetProc "Toplevel1" 1
    $site_6_1.tNo40 add $site_6_1.tNo40.t0 \
        -padding 0 -sticky nsew -state normal -text {Page 1} -image {} \
        -compound none -underline -1 
    set site_8_0  $site_6_1.tNo40.t0
    label $site_8_0.lab46 \
        -activebackground #ffffcd -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #b8a786 \
        -font $vTcl(actual_gui_font_dft_desc) \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {First Page} 
    vTcl:DefineAlias "$site_8_0.lab46" "Label1" vTcl:WidgetProc "Toplevel1" 1
    button $site_8_0.but47 \
        -activebackground $vTcl(analog_color_m) -activeforeground black \
        -background $vTcl(actual_gui_bg) -command qqq \
        -disabledforeground #b8a786 -font $vTcl(actual_gui_font_dft_desc) \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Redo 
    vTcl:DefineAlias "$site_8_0.but47" "Button2" vTcl:WidgetProc "Toplevel1" 1
    place $site_8_0.lab46 \
        -in $site_8_0 -x 40 -y 40 -anchor nw -bordermode ignore 
    place $site_8_0.but47 \
        -in $site_8_0 -x 110 -y 100 -anchor nw -bordermode ignore 
    frame $site_6_1.tNo40.t1 \
        -background $vTcl(actual_gui_bg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    vTcl:DefineAlias "$site_6_1.tNo40.t1" "TNotebook1_t1" vTcl:WidgetProc "Toplevel1" 1
    $site_6_1.tNo40 add $site_6_1.tNo40.t1 \
        -padding 0 -sticky nsew -state normal -text {Page 2} -image {} \
        -compound none -underline -1 
    set site_8_1  $site_6_1.tNo40.t1
    message $site_8_1.mes45 \
        -background $vTcl(actual_gui_bg) \
        -font {-family {DejaVu Sans Mono} -size 14} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {Second Page} -width 157 
    vTcl:DefineAlias "$site_8_1.mes45" "Message1" vTcl:WidgetProc "Toplevel1" 1
    place $site_8_1.mes45 \
        -in $site_8_1 -x 70 -y 60 -width 157 -relwidth 0 -height 33 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_6_1.tNo40 \
        -in $site_6_1 -x 20 -y 30 -anchor nw -bordermode ignore 
    $site_4_1.tPa39 add $site_4_1.tPa39.p2 
    $site_4_1.tPa39 pane $site_4_1.tPa39.p2 -weight 0
    set vTcl(sashtop,$top) $top
    bind $site_4_1.tPa39 <Map> "
        $site_4_1.tPa39 sashpos 0 85
        bind $site_4_1.tPa39 <Map> {}
    "
    place $site_4_1.tPa39 \
        -in $site_4_1 -x 40 -y 30 -width 430 -relwidth 0 -height 280 \
        -relheight 0 -anchor nw -bordermode ignore 
    $top.tPa38 add $top.tPa38.p2 
    $top.tPa38 pane $top.tPa38.p2 -weight 0
    set vTcl(sashtop,$top) $top
    bind $top.tPa38 <Map> "
        $vTcl(sashtop,$top).tPa38 sashpos 0 75
        bind $vTcl(sashtop,$top).tPa38 <Map> {}
    "
    ttk::style configure TSizegrip -background $vTcl(actual_gui_bg)
    vTcl::widgets::ttk::sizegrip::CreateCmd $top.tSi43 \
        -cursor bottom_right_corner 
    vTcl:DefineAlias "$top.tSi43" "TSizegrip1" vTcl:WidgetProc "Toplevel1" 1
    button $top.but44 \
        -activebackground $vTcl(analog_color_m) -activeforeground black \
        -background $vTcl(actual_gui_bg) -command quit \
        -disabledforeground #b8a786 -font $vTcl(actual_gui_font_dft_desc) \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Quit 
    vTcl:DefineAlias "$top.but44" "Button1" vTcl:WidgetProc "Toplevel1" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.tPa38 \
        -in $top -x 30 -y 30 -width 500 -relwidth 0 -height 410 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.tSi43 \
        -in $top -x 0 -relx 1 -y 0 -rely 1 -anchor se -bordermode inside 
    place $top.but44 \
        -in $top -x 250 -y 460 -anchor nw -bordermode ignore 
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
Window show .top37 $btop1
if {$vTcl(borrow)} {
    $btop1 configure -background plum
}

