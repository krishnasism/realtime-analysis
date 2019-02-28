#############################################################################
# Generated by PAGE version 4.18
#  in conjunction with Tcl version 8.6
#  Feb 28, 2019 02:19:00 PM IST  platform: Windows NT
set vTcl(timestamp) ""


if {!$vTcl(borrow)} {

set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #d9d9d9
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #d8d8d8
set vTcl(active_menu_fg) #000000
}

#############################################################################
#################################
#LIBRARY PROCEDURES
#


if {[info exists vTcl(sourcing)]} {

proc vTcl:project:info {} {
    set base .top42
    global vTcl
    set base $vTcl(btop)
    if {$base == ""} {
        set base .top42
    }
    namespace eval ::widgets::$base {
        set dflt,origin 1
        set runvisible 1
    }
    namespace eval ::widgets_bindings {
        set tagslist _TopLevel
    }
    namespace eval ::vTcl::modules::main {
        set procs {
        }
        set compounds {
        }
        set projectType single
    }
}
}

#################################
# GENERATED GUI PROCEDURES
#

proc vTclWindow.top42 {base} {
    if {$base == ""} {
        set base .top42
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -menu "$top.m53" -background {#d9d9d9} -highlightbackground {#d9d9d9} \
        -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 1366x705
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 1
    wm maxsize $top 1370 749
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "New Toplevel"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    listbox $top.lis44 \
        -background white -disabledforeground {#a3a3a3} -font font10 \
        -foreground {#000000} -height 602 -highlightbackground {#d9d9d9} \
        -highlightcolor black -selectbackground {#c4c4c4} \
        -selectforeground black -width 334 
    .top42.lis44 configure -font font10
    .top42.lis44 insert end text
    vTcl:DefineAlias "$top.lis44" "Listbox1" vTcl:WidgetProc "Toplevel1" 1
    listbox $top.lis48 \
        -background white -disabledforeground {#a3a3a3} -font font10 \
        -foreground {#000000} -height 272 -highlightbackground {#d9d9d9} \
        -highlightcolor black -selectbackground {#c4c4c4} \
        -selectforeground black -width 834 
    .top42.lis48 configure -font font10
    .top42.lis48 insert end text
    vTcl:DefineAlias "$top.lis48" "Listbox2" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab49 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -text Tweets 
    vTcl:DefineAlias "$top.lab49" "Label1" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab50 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -text Trends 
    vTcl:DefineAlias "$top.lab50" "Label2" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab51 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -text News 
    vTcl:DefineAlias "$top.lab51" "Label3" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab52 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -text Name 
    vTcl:DefineAlias "$top.lab52" "Label4" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.m53
    menu $site_3_0 \
        -activebackground {#d8d8d8} -activeforeground {#000000} \
        -background {#d9d9d9} -font font9 -foreground {#000000} -tearoff 0 
    button $top.but55 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -pady 0 -text {Start Listening..} 
    vTcl:DefineAlias "$top.but55" "Button1" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab43 \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -foreground {#000000} -text image 
    vTcl:DefineAlias "$top.lab43" "Label5" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab45 \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -foreground {#000000} -text Trends 
    vTcl:DefineAlias "$top.lab45" "Label6" vTcl:WidgetProc "Toplevel1" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.lis44 \
        -in $top -x 1020 -y 90 -width 334 -relwidth 0 -height 602 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $top.lis48 \
        -in $top -x 170 -y 420 -width 834 -relwidth 0 -height 272 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $top.lab49 \
        -in $top -x 1016 -y 60 -width 54 -relwidth 0 -height 31 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab50 \
        -in $top -x 530 -y 60 -anchor nw -bordermode ignore 
    place $top.lab51 \
        -in $top -x 170 -y 400 -anchor nw -bordermode ignore 
    place $top.lab52 \
        -in $top -x -1 -y 62 -width 64 -relwidth 0 -height 21 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but55 \
        -in $top -x 11 -y 636 -width 147 -relwidth 0 -height 54 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab43 \
        -in $top -x 20 -y 90 -width 494 -relwidth 0 -height 291 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab45 \
        -in $top -x 520 -y 100 -width 474 -relwidth 0 -height 301 \
        -relheight 0 -anchor nw -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

#############################################################################
## Binding tag:  _TopLevel

bind "_TopLevel" <<Create>> {
    if {![info exists _topcount]} {set _topcount 0}; incr _topcount
}
bind "_TopLevel" <<DeleteWindow>> {
    if {[set ::%W::_modal]} {
                vTcl:Toplevel:WidgetProc %W endmodal
            } else {
                destroy %W; if {$_topcount == 0} {exit}
            }
}
bind "_TopLevel" <Destroy> {
    if {[winfo toplevel %W] == "%W"} {incr _topcount -1}
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top42 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}
