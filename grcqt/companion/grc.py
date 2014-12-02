import sys, os
import logging
from PyQt5 import QtCore, QtGui, QtWidgets

# GRC imports
from . import controllers

# Note. Logger must have the correct naming convention to share
# handlers
logger = logging.getLogger("grc.main")


'''
Main controller for the whole application.
Handles setting up all the child controllers and views and also global actions.
'''
class AppController(object):
    def __init__(self, argv, INSTALL_DIR):

        # Load the main view class and initialize QMainWindow
        logger.debug("__init__")
        logger.debug("ARGV - %s" % argv)
        logger.debug("INSTALL_DIR - %s" % INSTALL_DIR)

        # Define a list for global actions
        self._global_actions = {}

        logger.debug("Creating QApplication instance")
        self._app = QtWidgets.QApplication(argv)

        # Need to setup the slots for the QtAction
        logger.debug("Creating MainWindow controller")
        self.mainwindow = controllers.MainWindow(INSTALL_DIR)

    def run(self):

        # Show the main window then launch the QT app
        self.mainwindow.show()

        # Launch the qt app
        return (self._app.exec_())
