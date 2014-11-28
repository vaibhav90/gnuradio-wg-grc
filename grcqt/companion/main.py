#! /usr/bin/env python3
import sys, os

from PyQt5 import QtCore, QtGui, QtWidgets

from . import views
from . import controllers
from . controllers import helpers

class MainController(object):
    def __init__(self):

        # Load the main view class and initialize QMainWindow
        self._window = views.MainView()
        self._platform = None

        # Need to setup the slots for the QtAction
        self._view_actions = self._window.getActions()
        helpers.Qt.connectSlots(self, self._view_actions)

        #self.flowgraph = views.FlowGraph(self._window, 'grcqt/companion/views/data/rx_logo.grc')
        #self._window.open(self.flowgraph)

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

        #self.reportDock.close()

        #load preferences and show the main window
        #Preferences.load(platform)
        # ToDo: use QSettings?
        #state = Preferences.main_window_state()
        # if state is not None: self.restoreState(state)
        #geometry = Preferences.main_window_geometry()
        # if geometry is not None: self.restoreGeometry(geometry)

    def start(self):
        self._window.show()

    def set_icon(self, path):
        icon = QtGui.QIcon(path)
        self._window.setWindowIcon(icon)


    ############################################################
    # Report Window
    ############################################################

    def add_report_line(self, line):
        pass

    ############################################################
    # Pages: create and close
    ############################################################

    def new_clicked(self):
        print ('new file')

    def open_clicked(self):
        print ('open')
        filename, filtr = QtWidgets.QFileDialog.getOpenFileName(self._window,
                            self._view_actions['open'].statusTip(),
                            filter='Flow Graph Files (*.grc);;All files (*.*)')
        if filename:
            self.flowgraph = FlowGraph(self, filename)

    def save_clicked(self):
        print ('save')

    def save_as_clicked(self):
        print ('save')

    def close_clicked(self):
        print ('close')

    def close_all_clicked(self):
        print ('close')

    def print_clicked(self):
        print ('print')

    def screen_capture_clicked(self):
        print ('screen capture')

    def undo_clicked(self):
        print ('undo')

    def redo_clicked(self):
        print ('redo')

    def cut_clicked(self):
        print ('cut')

    def copy_clicked(self):
        print ('copy')

    def paste_clicked(self):
        print ('paste')

    def delete_clicked(self):
        print ('delete')

    def rotate_ccw_clicked(self):
        print ('rotate ccw')

    def rotate_cw_clicked(self):
        print ('rotate cw')

    def errors_clicked(self):
        print ('errors')

    def find_clicked(self):
        print ('find block')

    def about_clicked(self):
        QtWidgets.QMessageBox.about(self._window, "GNU Radio Companion", "<b>GNU Radio Companion</b>")

    def notImplemented(self):
        print("Not yet implemented")
