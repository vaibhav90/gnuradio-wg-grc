import sys, os
import logging

# GRC imports
from .. import views
from .  import helpers

logger = logging.getLogger("grc.controllers.mainwindow")

'''
GRC.Controllers.MainWindow
---------------------------
Controller for the MainWindow view
'''
class MainWindow(object):
    def __init__(self, gp):

        logger.debug("__init__")

        # Load the main view class and initialize QMainWindow
        self._view = views.MainWindow(gp)

        # Need to setup the slots for the QtAction
        logger.debug("Connecting signals")
        self._view_actions = self._view.getActions()
        helpers.Qt.connectSlots(self, self._view_actions)

        logger.debug("Loading flowgraph model")
        test_flowgraph = os.path.join(gp.path.INSTALL, 'companion/views/data/rx_logo.grc')
        self.flowgraph = views.FlowGraph(self._view, test_flowgraph)
        logger.debug("Adding flowgraph view")
        self._view.open(self.flowgraph)

        # Also load and initialize child controllers
        #report_view = views.ReportsView()
        #self.report_controller = controllers.ReportsController(report_view)
        #self._window.addDockWidget(QtCore.Qt.DockWidgetArea(8), report_view)

        #self.projects_controller = controllers.ProjectsController()
        #self._window.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.projects_controller.get_view())

        #QtWidgets.QMessageBox.information(self._window, 'Message Title', 'The Bosy Text', QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.Cancel)
        #QtWidgets.QMessageBox.about(self._window, "Just dropped by to say hi!", "Welcome to this tutorial!")

        #self.report_controller.add_line("s")


        #block_view = blocktree.BlockTreeView()
        #self._window.addDockWidget(QtCore.Qt.RightDockWidgetArea, block_view)

        #project_view = projects.ProjectView()
        #self._window.addDockWidget(QtCore.Qt.RightDockWidgetArea, project_view)

        #self.actionLibrary.triggered.connect(self.blockLibrary.show)
        #self.actionNew.triggered.connect(self.new_page)
        #self.actionClose.triggered.connect(self.close_page)
        #self.editorTabs.tabCloseRequested.connect(self.close_page)


        # if state is not None: self.restoreState(state)
        #geometry = Preferences.main_window_geometry()
        # if geometry is not None: self.restoreGeometry(geometry)

    def show(self):
        logger.debug("Showing main window")
        self._view.show()


    ### Action Handlers ######################################

    def new_clicked(self):
        logger.debug ('new file')

    def open_clicked(self):
        logger.debug ('open')
        filename, filtr = QtWidgets.QFileDialog.getOpenFileName(self._window,
                            self._view_actions['open'].statusTip(),
                            filter='Flow Graph Files (*.grc);;All files (*.*)')
        if filename:
            logger.info("Opening flowgraph (%s) " % filename )
            self.flowgraph = FlowGraph(self, filename)

    def save_clicked(self):
        logger.debug ('save')

    def save_as_clicked(self):
        logger.debug ('save')

    def close_clicked(self):
        logger.debug ('close')

    def close_all_clicked(self):
        logger.debug ('close')

    def print_clicked(self):
        logger.debug ('print')

    def screen_capture_clicked(self):
        logger.debug ('screen capture')

    def undo_clicked(self):
        logger.debug ('undo')

    def redo_clicked(self):
        logger.debug ('redo')

    def cut_clicked(self):
        logger.debug ('cut')

    def copy_clicked(self):
        logger.debug ('copy')

    def paste_clicked(self):
        logger.debug ('paste')

    def delete_clicked(self):
        logger.debug ('delete')

    def rotate_ccw_clicked(self):
        logger.debug ('rotate ccw')

    def rotate_cw_clicked(self):
        logger.debug ('rotate cw')

    def errors_clicked(self):
        logger.debug ('errors')

    def find_clicked(self):
        logger.debug ('find block')

    def about_clicked(self):
        logger.debug ('about')
        QtWidgets.QMessageBox.about(self._window, "GNU Radio Companion", "<b>GNU Radio Companion</b>")

    def notImplemented(self):
        logger.debug ('Not implemented')
