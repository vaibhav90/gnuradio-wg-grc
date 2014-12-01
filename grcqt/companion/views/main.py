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
        self.setWindowTitle(_('window-title'))
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
                                _("new"), self,
                                shortcut = keys.New,
                                statusTip = _("new-tooltip"))

        actions['open'] = QtWidgets.QAction(icons("document-open"),
                                _("open"), self,
                                shortcut = keys.Open,
                                statusTip = _("open-tooltip"))

        actions['close'] = QtWidgets.QAction(icons("window-close"),
                                _("close"), self,
                                shortcut = keys.Close,
                                statusTip = _("close-tooltip"))

        actions['close_all'] = QtWidgets.QAction(icons("window-close"),
                                _("close_all"), self,
                                #shortcut = QtGui.QKeySequence.Close,
                                statusTip = _("close_all-tooltip"))

        actions['save'] = QtWidgets.QAction(icons("document-save"),
                                _("save"), self,
                                shortcut = keys.Save,
                                statusTip = _("save-tooltip"))

        actions['save_as'] = QtWidgets.QAction(icons("document-save-as"),
                                _("save_as"), self,
                                shortcut = keys.SaveAs,
                                statusTip = _("save_as-tooltip"))

        actions['print'] = QtWidgets.QAction(icons('document-print'),
                                _("print"), self,
                                shortcut = keys.Print,
                                statusTip = _("print-tooltip"))

        actions['screen_capture'] = QtWidgets.QAction(icons('camera-photo'),
                                _("screen_capture"), self,
                                #shortcut = Qt,
                                statusTip = _("screen_capture-tooltip"))

        actions['exit'] = QtWidgets.QAction(icons("application-exit"),
                                _("exit"), self,
                                shortcut = keys.Quit,
                                statusTip = _("exit-tooltip"))

        ### Edit Actions ###
        actions['undo'] = QtWidgets.QAction(icons('edit-undo'),
                                _("undo"), self,
                                shortcut = keys.Undo,
                                statusTip = _("undo-tooltip"))

        actions['redo'] = QtWidgets.QAction(icons('edit-redo'),
                                _("redo"), self,
                                shortcut = keys.Redo,
                                statusTip = _("redo-tooltip"))

        actions['cut'] = QtWidgets.QAction(icons('edit-cut'),
                                _("cut"), self,
                                shortcut = keys.Cut,
                                statusTip = _("cut-tooltip"))

        actions['copy'] = QtWidgets.QAction(icons('edit-copy'),
                                _("copy"), self,
                                shortcut = keys.Copy,
                                statusTip = _("copy-tooltip"))

        actions['paste'] = QtWidgets.QAction(icons('edit-paste'),
                                _("paste"), self,
                                shortcut = keys.Paste,
                                statusTip = _("paste-tooltip"))

        actions['delete'] = QtWidgets.QAction(icons('edit-delete'),
                                _("delete"), self,
                                shortcut = keys.Delete,
                                statusTip = _("delete-tooltip"))

        actions['rotate_ccw'] = QtWidgets.QAction(icons('object-rotate-left'),
                                _("rotate_ccw"), self,
                                shortcut = keys.MoveToPreviousChar,
                                statusTip = _("rotate_ccw-tooltip"))

        actions['rotate_cw'] = QtWidgets.QAction(icons('object-rotate-right'),
                                _("rotate_cw"), self,
                                shortcut = keys.MoveToNextChar,
                                statusTip = _("rotate_cw-tooltip"))

        ### View Actions ###
        actions['errors'] = QtWidgets.QAction(icons('dialog-error'),
                                _("errors"), self,
                                shortcut = 'E',
                                statusTip = _("errors-tooltip"))

        actions['find'] = QtWidgets.QAction(icons('edit-find'),
                                _("find"), self,
                                shortcut = keys.Find,
                                statusTip = _("find-tooltip"))

        ### Help Actions ###
        actions['about'] = QtWidgets.QAction(icons('help-about'),
                                _("about"), self,
                                statusTip = _("about-tooltip"))

        actions['generate'] = QtWidgets.QAction(icons('system-run'),
                                _("process-generate"), self,
                                shortcut = 'F5',
                                statusTip = _("process-generate-tooltip"))

        actions['execute'] = QtWidgets.QAction(icons('media-playback-start'),
                                _("process-execute"), self,
                                shortcut = 'F6',
                                statusTip = _("process-execute-tooltip"))

        actions['kill'] =   QtWidgets.QAction(icons('process-stop'),
                                _("process-kill"), self,
                                shortcut = 'F7',
                                statusTip = _("process-kill-tooltip"))

        actions['help'] = QtWidgets.QAction(icons('help-browser'),
                                _("help"), self,
                                shortcut = keys.HelpContents,
                                statusTip = _("help-tooltip"))

        actions['types'] = QtWidgets.QAction("Types", self)

        actions['library'] = QtWidgets.QAction("Library", self,
                                shortcut = "Ctrl+L",
                                statusTip = _("block-library-tooltip"))

        actions['report'] = QtWidgets.QAction("Reports", self)
        actions['enable'] = QtWidgets.QAction("Enable", self)
        actions['disable'] = QtWidgets.QAction("Disable", self)

        actions['properties'] = QtWidgets.QAction(icons('document-properties'),
                                _("properties"), self,
                                #shortcut = QtGui,
                                statusTip = _("flowgraph-properties-tooltip"))

        actions['preferences'] = QtWidgets.QAction(icons('preferences-system'),
                                _("preferences"), self,
                                #shortcut,
                                statusTip = _("preferences-tooltip"))

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
        self.statusBar().showMessage(_("ready-message"))

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

    ### TODO: Dynamic translation?
    def retranslateUi(self):
        logger.debug("Translating")
