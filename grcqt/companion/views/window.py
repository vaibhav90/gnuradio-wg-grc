import sys, os
from PyQt5 import QtCore, QtGui, QtWidgets

from .. import base

'''
GRC.Views.MainWindow
---------------------------
Class that handles the main view definition for the main grc window
'''
class MainWindow(base.View, QtWidgets.QMainWindow):

    '''
    Initialize the main window and call wrappers to initialize subviews
    '''
    @base.init_view("grc.views.mainwindow")
    def __init__(self):
        super().__init__() # For the QT Framework
        self.log.debug("__init__")

        # Internal dictionaries for menus, toolbars, etc.
        # - Actiona are in base class
        self.menus = {}
        self.toolbars = {}

        # Main window properties
        self.log.debug("Setting window properties")
        self.setWindowTitle(_('window-title'))
        self.setDockOptions(QtWidgets.QMainWindow.AllowNestedDocks | \
            QtWidgets.QMainWindow.AllowTabbedDocks | \
            QtWidgets.QMainWindow.AnimatedDocks)

        # Setup the window icon
        self.log.debug("Setting window icon (%s)" % self.gp.path.ICON )
        icon = QtGui.QIcon(self.gp.path.ICON)
        self.setWindowIcon(icon)

        self.log.debug("Setting window size")
        screen = QtWidgets.QDesktopWidget().availableGeometry()
        self.resize(screen.width() * 0.40, screen.height())

        self.menuBar().setNativeMenuBar(self.gp.window.NATIVE_MENUBAR)

        ### TODO: Not sure about document mode
        #self.setDocumentMode(True)

        ### TODO: Also need to pull from the saved preferences as what to show and where

        # Generate the rest of the window
        self.createActions()
        self.createMenus()
        self.createToolbars()
        self.createStatusBar()
        #self.init_other()

        #my['Quit.triggered.connect(self.close)
        #my['Report.triggered.connect(self.reportDock.show)
        #QtCore.QMetaObject.connectSlotsByName(self)


    # Any action for the window is defined here. Controller must
    # use getActions and setup signals and slots to its own handlers
    # Need to have translation capability here
    def createActions(self):
        self.log.debug("Creating actions")
        actions = QtWidgets.QAction
        icons = QtGui.QIcon.fromTheme
        keys = QtGui.QKeySequence

        my = self.actions
        ### File Actions ###
        my['new'] = actions(icons("document-new"),
                                _("new"), self,
                                shortcut = keys.New,
                                statusTip = _("new-tooltip"))

        my['open'] = actions(icons("document-open"),
                                _("open"), self,
                                shortcut = keys.Open,
                                statusTip = _("open-tooltip"))

        my['close'] = actions(icons("window-close"),
                                _("close"), self,
                                shortcut = keys.Close,
                                statusTip = _("close-tooltip"))

        my['close_all'] = actions(icons("window-close"),
                                _("close_all"), self,
                                #shortcut = QtGui.QKeySequence.Close,
                                statusTip = _("close_all-tooltip"))

        my['save'] = actions(icons("document-save"),
                                _("save"), self,
                                shortcut = keys.Save,
                                statusTip = _("save-tooltip"))

        my['save_as'] = actions(icons("document-save-as"),
                                _("save_as"), self,
                                shortcut = keys.SaveAs,
                                statusTip = _("save_as-tooltip"))

        my['print'] = actions(icons('document-print'),
                                _("print"), self,
                                shortcut = keys.Print,
                                statusTip = _("print-tooltip"))

        my['screen_capture'] = actions(icons('camera-photo'),
                                _("screen_capture"), self,
                                #shortcut = Qt,
                                statusTip = _("screen_capture-tooltip"))

        my['exit'] = actions(icons("application-exit"),
                                _("exit"), self,
                                shortcut = keys.Quit,
                                statusTip = _("exit-tooltip"))

        ### Edit Actions ###
        my['undo'] = actions(icons('edit-undo'),
                                _("undo"), self,
                                shortcut = keys.Undo,
                                statusTip = _("undo-tooltip"))

        my['redo'] = actions(icons('edit-redo'),
                                _("redo"), self,
                                shortcut = keys.Redo,
                                statusTip = _("redo-tooltip"))

        my['cut'] = actions(icons('edit-cut'),
                                _("cut"), self,
                                shortcut = keys.Cut,
                                statusTip = _("cut-tooltip"))

        my['copy'] = actions(icons('edit-copy'),
                                _("copy"), self,
                                shortcut = keys.Copy,
                                statusTip = _("copy-tooltip"))

        my['paste'] = actions(icons('edit-paste'),
                                _("paste"), self,
                                shortcut = keys.Paste,
                                statusTip = _("paste-tooltip"))

        my['delete'] = actions(icons('edit-delete'),
                                _("delete"), self,
                                shortcut = keys.Delete,
                                statusTip = _("delete-tooltip"))

        my['rotate_ccw'] = actions(icons('object-rotate-left'),
                                _("rotate_ccw"), self,
                                shortcut = keys.MoveToPreviousChar,
                                statusTip = _("rotate_ccw-tooltip"))

        my['rotate_cw'] = actions(icons('object-rotate-right'),
                                _("rotate_cw"), self,
                                shortcut = keys.MoveToNextChar,
                                statusTip = _("rotate_cw-tooltip"))

        ### View Actions ###
        my['errors'] = actions(icons('dialog-error'),
                                _("errors"), self,
                                shortcut = 'E',
                                statusTip = _("errors-tooltip"))

        my['find'] = actions(icons('edit-find'),
                                _("find"), self,
                                shortcut = keys.Find,
                                statusTip = _("find-tooltip"))

        ### Help Actions ###
        my['about'] = actions(icons('help-about'),
                                _("about"), self,
                                statusTip = _("about-tooltip"))

        my['about_qt'] = actions(icons('help-about'),
                                _("about-qt"), self,
                                statusTip = _("about-tooltip"))

        my['generate'] = actions(icons('system-run'),
                                _("process-generate"), self,
                                shortcut = 'F5',
                                statusTip = _("process-generate-tooltip"))

        my['execute'] = actions(icons('media-playback-start'),
                                _("process-execute"), self,
                                shortcut = 'F6',
                                statusTip = _("process-execute-tooltip"))

        my['kill'] =   actions(icons('process-stop'),
                                _("process-kill"), self,
                                shortcut = 'F7',
                                statusTip = _("process-kill-tooltip"))

        my['help'] = actions(icons('help-browser'),
                                _("help"), self,
                                shortcut = keys.HelpContents,
                                statusTip = _("help-tooltip"))

        my['types'] = actions("Types", self)

        my['library'] = actions("Library", self,
                                shortcut = "Ctrl+L",
                                statusTip = _("block-library-tooltip"),
                                checkable=True)

        my['report'] = actions("Reports", self,
                        checkable=True)
        my['enable'] = actions("Enable", self)
        my['disable'] = actions("Disable", self)

        my['properties'] = actions(icons('document-properties'),
                                _("flowgraph-properties"), self,
                                #shortcut = QtGui,
                                statusTip = _("flowgraph-properties-tooltip"))

        my['preferences'] = actions(icons('preferences-system'),
                                _("preferences"), self,
                                #shortcut,
                                statusTip = _("preferences-tooltip"))

        # Disable some actions, by default
        my['save'].setEnabled(False)
        my['undo'].setEnabled(False)
        my['redo'].setEnabled(False)
        my['cut'].setEnabled(False)
        my['copy'].setEnabled(False)
        my['paste'].setEnabled(False)
        my['delete'].setEnabled(False)
        my['rotate_ccw'].setEnabled(False)
        my['rotate_cw'].setEnabled(False)
        my['errors'].setEnabled(False)

    # Setup the main menubar for the application
    def createMenus(self):
        self.log.debug("Creating menus")
        my = self.actions
        menus = self.menus

        # Global menu options
        self.menuBar().setNativeMenuBar(True)

        # Setup the file menu
        file = self.menuBar().addMenu("&File")
        file.addAction(my['new'])
        file.addAction(my['open'])
        file.addAction(my['close'])
        file.addAction(my['close_all'])
        file.addSeparator();
        file.addAction(my['save'])
        file.addAction(my['save_as'])
        file.addSeparator();
        file.addAction(my['screen_capture'])
        file.addAction(my['print'])
        file.addSeparator();
        file.addAction(my['exit'])
        menus['file'] = file

        # Setup the edit menu
        edit = self.menuBar().addMenu("&Edit")
        edit.addAction(my['undo'])
        edit.addAction(my['redo'])
        edit.addSeparator()
        edit.addAction(my['cut'])
        edit.addAction(my['copy'])
        edit.addAction(my['paste'])
        edit.addAction(my['delete'])
        edit.addSeparator()
        edit.addAction(my['rotate_ccw'])
        edit.addAction(my['rotate_cw'])
        edit.addSeparator()
        edit.addAction(my['enable'])
        edit.addAction(my['disable'])
        edit.addAction(my['properties'])
        menus['edit'] = edit

        # Setup the view menu
        view = self.menuBar().addMenu("&View")
        view.addAction(my['errors'])
        view.addAction(my['find'])
        view.addSeparator()
        view.addAction(my['library'])
        view.addAction(my['report'])
        menus['view'] = view

        # Setup the build menu
        build = self.menuBar().addMenu("&Build")
        build.addAction(my['generate'])
        build.addAction(my['execute'])
        build.addAction(my['kill'])
        menus['build'] = build

        # Setup the help menu
        help = self.menuBar().addMenu("&Help")
        help.addAction(my['help'])
        help.addAction(my['types'])
        help.addSeparator()
        help.addAction(my['about'])
        help.addAction(my['about_qt'])
        menus['help'] = help

    def createToolbars(self):
        self.log.debug("Creating toolbars")
        toolbars = self.toolbars
        my = self.actions

        # Main toolbar
        file = self.addToolBar("file")
        file.addAction(my['new'])
        file.addAction(my['open'])
        file.addAction(my['save'])
        file.addAction(my['close'])
        file.addAction(my['print'])
        toolbars['file'] = file

        # Edit toolbar
        edit = self.addToolBar("edit")
        edit.addAction(my['cut'])
        edit.addAction(my['copy'])
        edit.addAction(my['paste'])
        edit.addAction(my['delete'])
        edit.addSeparator()
        edit.addAction(my['rotate_ccw'])
        edit.addAction(my['rotate_cw'])
        toolbars['edit'] = edit

        # Run Toolbar
        run = self.addToolBar("run")
        run.addAction(my['generate'])
        run.addAction(my['execute'])
        run.addAction(my['kill'])
        toolbars['run'] = run

    def createStatusBar(self):
        self.log.debug("Creating status bar")
        self.statusBar().showMessage(_("ready-message"))

    def init_other(self):
        self.log.debug("Creating other")
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

    def new_tab(self, flowgraph):
        self.setCentralWidget(flowgraph)

    def open(self):
        filename, filtr = QtWidgets.QFileDialog.getOpenFileName(self,
            self.my['open'].statusTip(),
            filter='Flow Graph Files (*.grc);;All files (*.*)')
        return filename


    ### TODO: Dynamic translation?
    def retranslateUi(self):
        self.log.debug("Translating")
