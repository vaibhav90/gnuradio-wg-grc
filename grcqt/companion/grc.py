import logging
from PyQt5 import QtWidgets

# GRC imports
from . import controllers

# Note. Logger must have the correct naming convention to share
# handlers
logger = logging.getLogger("grc.app")


'''
Main controller for the whole application.
Handles setting up all the child controllers and views and also global actions.
'''
class AppController(object):
    def __init__(self, gp):

        logger.debug("__init__")
        # Load the main view class and initialize QMainWindow
        logger.debug("ARGV - %s" % gp.argv)
        logger.debug("INSTALL_DIR - %s" % gp.path.INSTALL)

        # Define a list for global actions
        self._global_actions = {}

        logger.debug("Creating QApplication instance")
        self._app = QtWidgets.QApplication(gp.argv)

        # Need to setup the slots for the QtAction
        logger.debug("Creating MainWindow controller")
        self.mainwindow = controllers.MainWindow(gp)

    def run(self):

        # Show the main window then launch the QT app
        self.mainwindow.show()

        # Launch the qt app
        return (self._app.exec_())
