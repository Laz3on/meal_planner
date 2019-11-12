import wx

class windowClass(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(windowClass, self).__init__(*args, **kwargs)

        self.basicGUI()

    def basicGUI(self):

        panel = wx.Panel(self)

        menuBar = wx.MenuBar()

        fileButton = wx.Menu()
        editButton = wx.Menu()
        importItem = wx.Menu()

        importItem.Append(wx.ID_ANY, 'Import Document...')
        importItem.Append(wx.ID_ANY, 'Import Picture...')
        importItem.Append(wx.ID_ANY, 'Import Video...')
        fileButton.AppendSubMenu(importItem, 'I&mport')

        toolBar = self.CreateToolBar()
        quitToolButton = toolBar.AddTool(wx.ID_ANY, 'Quit', wx.Bitmap('exit.png'))

        toolBar.Realize()
        self.Bind(wx.EVT_TOOL, self.Quit, quitToolButton)


        exitItem = wx.MenuItem(fileButton, wx.ID_EXIT, 'Quit\tCtrl+Q')
        exitItem.SetBitmap(wx.Bitmap('exit.png'))
        fileButton.Append(exitItem)





        menuBar.Append(fileButton, '&File')
        menuBar.Append(editButton, '&Edit')

        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU, self.Quit, exitItem)


        nameBox = wx.TextEntryDialog(None, 'What is your name?', 'Welcome', 'name')

        if nameBox.ShowModal()==wx.ID_OK:
            userName = nameBox.GetValue()


        yesNoBox = wx.MessageDialog(None, 'Do you enjoy wxPython?', 'Question', wx.YES_NO)
        yesNoAnswer = yesNoBox.ShowModal()
        yesNoBox.Destroy()




        

        if yesNoAnswer == wx.ID_NO:
            userName = 'Loser!'

        chooseOneBox = wx.SingleChoiceDialog(None, 'What is your faorite color?',
                                                'Color Question',
                                                ['Green', 'Red', 'Blue', 'Yellow'])

        if chooseOneBox.ShowModal() == wx.ID_OK:
            favColor = chooseOneBox.GetStringSelection()

        wx.TextCtrl(panel, pos=(3,100), size=(150,50))

        aweText = wx.StaticText(panel, -1, "Awesome Text", (3,3))
        aweText.SetForegroundColour('#67cddc')
        aweText.SetBackgroundColour('black')

        rlyAweText = wx.StaticText(panel, -1, "Custom Awesomeness", (3,30))
        rlyAweText.SetForegroundColour(favColor)
        rlyAweText.SetBackgroundColour('black')

        self.SetTitle('Welcome ' +userName)
        self.Show(True)

    def Quit(self, e):
        self.Close()


def main():
    app = wx.App()
    windowClass(None)

    app.MainLoop()


main()
