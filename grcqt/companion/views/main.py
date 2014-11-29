import logging
from PyQt5 import QtCore, QtGui, QtWidgets

logger = logging.getLogger("grc.views.main")

'''
Class that handles the main view definition for the main grc window
'''
class MainView(QtWidgets.QMainWindow):

    '''
    Initialize the main window and call wrappers to initialize subviews
    '''
    def __init__(self):
        super().__init__()
        logger.debug("__init__")

        # Internal dictionaries for actions and menus
        self._actions = {}
        self._menus = {}
        self._toolbars = {}

        # Main window properties
        logger.debug("Setting window properties")
        self.setWindowTitle('GNU Radio Companion')
        self.setDockOptions(QtWidgets.QMainWindow.AllowNestedDocks | \
            QtWidgets.QMainWindow.AllowTabbedDocks | \
            QtWidgets.QMainWindow.AnimatedDocks)

        screen = QtWidgets.QDesktopWidget().availableGeometry()
        self.resize(screen.width() * 0.40, screen.height())

        ### TODO: Not sure about document mode
        #self.setDocumentMode(True)

        ### TODO: Also need to pull from the saved preferences as what to show and where

        # Generate the rest of the window
        self.createActions()
        self.createMenus()
        self.createToolbars()
        self.createStatusBar()
        #self.init_other()

        #self.translateUI(language)

        #self.retranslateUi()
        #actions['Quit.triggered.connect(self.close)
        #actions['Report.triggered.connect(self.reportDock.show)
        #QtCore.QMetaObject.connectSlotsByName(self)


    # Any action for the window is defined here. Controller must
    # use getActions and setup signals and slots to its own handlers
    # Need to have translation capability here
    def createActions(self):
        logger.debug("Creating actions")
        icons = QtGui.QIcon.fromTheme
        keys = QtGui.QKeySequence

        actions = self._actions
        ### File Actions ###
        actions['new'] = QtWidgets.QAction(icons("document-new"),
                                "&New", self,
                                shortcut = keys.New,
                                statusTip = "Create a new flow graph")

        actions['open'] = QtWidgets.QAction(icons("document-open"),
                                "&Open...", self,
                                shortcut = keys.Open,
                                statusTip = "Open an existing flow graph")

        actions['close'] = QtWidgets.QAction(icons("window-close"),
                                "Close", self,
                                shortcut = keys.Close,
                                statusTip = "Close the current flow graph")

        actions['close_all'] = QtWidgets.QAction(icons("window-close"),
                                "Close All", self,
                                #shortcut = QtGui.QKeySequence.Close,
                                statusTip = "Close all flow graphs")

        actions['save'] = QtWidgets.QAction(icons("document-save"),
                                "&Save", self,
                                shortcut = keys.Save,
                                statusTip = "Save the current flow graph")

        actions['save_as'] = QtWidgets.QAction(icons("document-save-as"),
                                "Save &As...", self,
                                shortcut = keys.SaveAs,
                                statusTip = "Save the flow graph under a new name")

        actions['print'] = QtWidgets.QAction(icons('document-print'),
                                "&Print...", self,
                                shortcut = keys.Print,
                                statusTip = "Print the current flow graph")

        actions['screen_capture'] = QtWidgets.QAction(icons('camera-photo'),
                                "Screen Capture", self,
                                #shortcut = Qt,
                                statusTip = "Create a screen capture of the current flow graph")

        actions['exit'] = QtWidgets.QAction(icons("application-exit"),
                                "E&xit", self,
                                shortcut = keys.Quit,
                                statusTip = "Exit the application")

        ### Edit Actions ###
        actions['undo'] = QtWidgets.QAction(icons('edit-undo'),
                                "Undo", self,
                                shortcut = keys.Undo,
                                statusTip = "Undo last change")

        actions['redo'] = QtWidgets.QAction(icons('edit-redo'),
                                "Redo", self,
                                shortcut = keys.Redo,
                                statusTip = "Redo last change")

        actions['cut'] = QtWidgets.QAction(icons('edit-cut'),
                                "Cu&t", self,
                                shortcut = keys.Cut,
                                statusTip = "Cut the current selection's contents to the clipboard")

        actions['copy'] = QtWidgets.QAction(icons('edit-copy'),
                                "&Copy", self,
                                shortcut = keys.Copy,
                                statusTip = "Copy the current selection's contents to the clipboard")

        actions['paste'] = QtWidgets.QAction(icons('edit-paste'),
                                "&Paste", self,
                                shortcut = keys.Paste,
                                statusTip = "Paste the clipboard's contents into the current selection")

        actions['delete'] = QtWidgets.QAction(icons('edit-delete'),
                                "&Delete", self,
                                shortcut = keys.Delete,
                                statusTip = "Delete the selected blocks")

        actions['rotate_ccw'] = QtWidgets.QAction(icons('object-rotate-left'),
                                "Rotate Counterclockwise", self,
                                shortcut = keys.MoveToPreviousChar,
                                statusTip = "Rotate the selected block 90 degress counterclockwise")

        actions['rotate_cw'] = QtWidgets.QAction(icons('object-rotate-right'),
                                "Rotate Counterclockwise", self,
                                shortcut = keys.MoveToNextChar,
                                statusTip = "Rotate the selected block 90 degress clockwise")

        ### View Actions ###
        actions['errors'] = QtWidgets.QAction(icons('dialog-error'),
                                "&Errors", self,
                                shortcut = 'E',
                                statusTip = "View the flowgraph errors")

        actions['find'] = QtWidgets.QAction(icons('edit-find'),
                                "&Find Block", self,
                                shortcut = keys.Find,
                                statusTip = "Search for a block by name (and key)")

        ### Help Actions ###
        actions['about'] = QtWidgets.QAction(icons('help-about'),
                                "&About", self,
                                statusTip = "Show the application's About box")

        actions['generate'] = QtWidgets.QAction(icons('system-run'),
                                "&Generate", self,
                                shortcut = 'F5',
                                statusTip = "Generate a python flowgraph")

        actions['execute'] = QtWidgets.QAction(icons('media-playback-start'),
                                "Execute", self,
                                shortcut = 'F6',
                                statusTip = "Execute a python flowgraph")

        actions['kill'] =   QtWidgets.QAction(icons('process-stop'),
                                "Kill", self,
                                shortcut = 'F7',
                                statusTip = "Kill current flowgraph")

        actions['help'] = QtWidgets.QAction(icons('help-browser'),
                                "Help", self,
                                shortcut = keys.HelpContents,
                                statusTip = "Show help")

        actions['types'] = QtWidgets.QAction("Types", self)

        actions['library'] = QtWidgets.QAction("Library", self,
                                shortcut = "Ctrl+L",
                                statusTip = "Show the block library")

        actions['report'] = QtWidgets.QAction("Reports", self)
        actions['enable'] = QtWidgets.QAction("Enable", self)
        actions['disable'] = QtWidgets.QAction("Disable", self)
        actions['properties'] = QtWidgets.QAction(icons('document-properties'),
                                "Properties", self,
                                #shortcut = QtGui,
                                statusTip = "Show properties for flowgraph")

        actions['preferences'] = QtWidgets.QAction(icons('preferences-system'),
                                "Preferences", self,
                                #shortcut,
                                statusTip = "Show GRC preferences")

        # Disable some actions, by default
        actions['save'].setEnabled(False)
        actions['undo'].setEnabled(False)
        actions['redo'].setEnabled(False)
        actions['cut'].setEnabled(False)
        actions['copy'].setEnabled(False)
        actions['paste'].setEnabled(False)
        actions['delete'].setEnabled(False)
        actions['rotate_ccw'].setEnabled(False)
        actions['rotate_cw'].setEnabled(False)
        actions['errors'].setEnabled(False)

    def getActions(self):
        return self._actions

    # Setup the main menubar for the application
    def createMenus(self):
        logger.debug("Creating menus")
        actions = self._actions
        menus = self._menus

        # Global menu options
        self.menuBar().setNativeMenuBar(True)

        # Setup the file menu
        file = self.menuBar().addMenu("&File")
        file.addAction(actions['new'])
        file.addAction(actions['open'])
        file.addAction(actions['close'])
        file.addAction(actions['close_all'])
        file.addSeparator();
        file.addAction(actions['save'])
        file.addAction(actions['save_as'])
        file.addSeparator();
        file.addAction(actions['screen_capture'])
        file.addAction(actions['print'])
        file.addSeparator();
        file.addAction(actions['exit'])
        menus['file'] = file

        # Setup the edit menu
        edit = self.menuBar().addMenu("&Edit")
        edit.addAction(actions['undo'])
        edit.addAction(actions['redo'])
        edit.addSeparator()
        edit.addAction(actions['cut'])
        edit.addAction(actions['copy'])
        edit.addAction(actions['paste'])
        edit.addAction(actions['delete'])
        edit.addSeparator()
        edit.addAction(actions['rotate_ccw'])
        edit.addAction(actions['rotate_cw'])
        edit.addSeparator()
        edit.addAction(actions['enable'])
        edit.addAction(actions['disable'])
        edit.addAction(actions['properties'])
        menus['edit'] = edit

        # Setup the view menu
        view = self.menuBar().addMenu("&View")
        view.addAction(actions['errors'])
        view.addAction(actions['find'])
        view.addSeparator()
        view.addAction(actions['library'])
        view.addAction(actions['report'])
        menus['view'] = view

        # Setup the build menu
        build = self.menuBar().addMenu("&Build")
        build.addAction(actions['generate'])
        build.addAction(actions['execute'])
        build.addAction(actions['kill'])
        menus['build'] = build

        # Setup the help menu
        help = self.menuBar().addMenu("&Help")
        help.addAction(actions['help'])
        help.addSeparator()
        help.addAction(actions['about'])
        menus['help'] = help

    def createToolbars(self):
        logger.debug("Creating toolbars")
        toolbars = self._toolbars
        actions = self._actions

        # Main toolbar
        file = self.addToolBar("file")
        file.addAction(actions['new'])
        file.addAction(actions['open'])
        file.addAction(actions['save'])
        file.addAction(actions['close'])
        file.addAction(actions['print'])
        toolbars['file'] = file

        # Edit toolbar
        edit = self.addToolBar("edit")
        edit.addAction(actions['cut'])
        edit.addAction(actions['copy'])
        edit.addAction(actions['paste'])
        edit.addAction(actions['delete'])
        edit.addSeparator()
        edit.addAction(actions['rotate_ccw'])
        edit.addAction(actions['rotate_cw'])
        toolbars['edit'] = edit

        # Run Toolbar
        run = self.addToolBar("run")
        run.addAction(actions['generate'])
        run.addAction(actions['execute'])
        run.addAction(actions['kill'])
        toolbars['run'] = run

    def createStatusBar(self):
        logger.debug("Creating status bar")
        self.statusBar().showMessage("Ready")

    def init_other(self):
        logger.debug("Creating other")
        centralwidget = QtWidgets.QWidget(self)
        centralwidget.setObjectName("main::central")

        layout = QtWidgets.QHBoxLayout(centralwidget)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setObjectName("main::central::layout")

        tabs = QtWidgets.QTabWidget(centralwidget)
        tabs.setObjectName("main::central::layout::tabs")

        #tab_1 = QtWidgets.QWidget()
        #tab_1.setObjectName("tab_3")

        #tab_2'= QtWidgets.QWidget()
        #tab_2.setObjectName("tab_4")

        #tab_layout = QtWidgets.QHBoxLayout()
        #layout.setSpacing(0)
        #layout.setContentsMargins(0, 0, 0, 0)
        #layout.setObjectName("main::central::layout")

        #tabs.addTab(tab_1, "")
        #tabs.addTab(tab_2, "")

        #layout_5 = QtWidgets.QHBoxLayout()
        #layout_5.setObjectName("horizontalLayout_5"

        #self.horizontalLayout_5.addWidget(self.editorTabs)
        #self.horizontalLayout.addLayout(self.horizontalLayout_5)


    def open(self, flowgraph):
        self.setCentralWidget(flowgraph)

    ### TODO: Move action list and translations out of view
    def retranslateUi(self):
        logger.debug("Translating")
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "GNU Radio Companion"))
        #self.editorTabs.setTabText(self.editorTabs.indexOf(self.tab_3), _translate("self", "Tab 1"))
        #self.editorTabs.setTabText(self.editorTabs.indexOf(self.tab_4), _translate("self", "Tab 2"))
        self.menuFile.setTitle(_translate("self", "File"))
        self.menuEdit.setTitle(_translate("self", "Edit"))
        self.menuView.setTitle(_translate("self", "View"))
        self.menuBuild.setTitle(_translate("self", "Build"))
        self.menuHelp.setTitle(_translate("self", "Help"))
        self.fileToolbar.setWindowTitle(_translate("self", "File Toolbar"))
        #self.reportDock.setWindowTitle(_translate("self", "Console"))
        self.editToolbar.setWindowTitle(_translate("self", "Edit Toolbar"))
        self.runToolbar.setWindowTitle(_translate("self", "Run Toolbar"))
        #self.dockWidget.setWindowTitle(_translate("self", "Project"))
        '''actions['New.setText(_translate("self", "New"))
        actions['New.setToolTip(_translate("self", "New Flowgraph"))'''
