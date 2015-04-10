#!/usr/bin/env python
#-*- coding: UTF-8 -*-

import wx

class MainWindow (wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(400,200))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        # A Statusbar in the bottom of the window
        self.CreateStatusBar()
        
         # Setting up the menu.
        filemenu = wx.Menu()
        
        # wx.ID_ABOUT and wx.ID_EXIT are standard IDs provided by wxWidgets.
        filemenu.Append(wx.ID_ABOUT, "&About", "Information about this program")
        filemenu.AppendSeparator()
        filemenu.Append(wx.ID_EXIT, "&Exit", "Terminate the program")
        
        # Creating the menubar.
        menuBar = wx.MenuBar()
        # Adding the "filemenu" to the MenuBar
        menuBar.Append(filemenu, "&File")
        
        # Adding the MenuBar to the Frame content.
        self.SetMenuBar(menuBar)
        self.Show(True)
        
app = wx.App(False)
frame = MainWindow(None, 'Sample editor')
app.MainLoop()
