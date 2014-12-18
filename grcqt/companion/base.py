import sys, os
import logging, weakref
import functools

# GRC imports
from . import helpers

# Init decorator that handles setting common parameters.
# This method does not require the developer to handle passing multiple arguments
#  from the controller class to the base class.
def init_controller(view, logger_name=None):
    def decorator(init_func):
        '''
        Replacement __init__ for a Controller class:
         - Logging (self.log)
         - App Controller refereence (self.app)
         - Global properties
         - Auto connecting slots
        '''
        # Replacement init for the class
        @functools.wraps(init_func)
        def replacement(self, app, gp):

            # Setup the logger
            if (logger_name):
                self.log = logging.getLogger(logger_name)
            else:
                self.log = logging.getLogger("grc." + self.__class__.__name__)
                self.log.debug("Using default logger - %s" % ("grc." + self.__class__.__name__))
            self.log.debug("__init__")

            # Setup a reference to the AppController
            # Need to use a weak references due to circular references,
            #  otherwise the python gc will not correctly recover objects
            self.app = weakref.ref(app)
            self.gp = gp

            # Allocate the view (Should build actions and all)
            self.view = view(self, self.gp)

            # Dynamically build connection for the available signals
            self.log.debug("Connecting signals")
            helpers.qt.connectSlots(self, self.view.actions)

            # Call the original init
            init_func(self)

        return replacement
    return decorator

def init_view(logger_name=None):
    def decorator(init_func):
        '''
        Replacement __init__ for a View class:
         - Logging (self.log)
         - App Controller refereence (self.app)
         - Global properties
        '''

        @functools.wraps(init_func)
        def replacement(self, controller, gp):

            # Setup the logger
            if logger_name:
                self.log = logging.getLogger(logger_name)
            else:
                self.log = logging.getLogger("grc." + self.__class__.__name__)
                self.log.debug("Using default logger - %s", ("grc." + self.__class__.__name__))
            self.log.debug("__init__")

            # Setup a reference to the AppController
            # Need to use a weak references due to circular references,
            #  otherwise the python gc will not correctly recover objects
            self.controller = weakref.ref(controller)
            self.gp = gp

            # Call the original init function
            init_func(self)
        return replacement
    return decorator



class Controller(object):
    """
    GRC.Base.Controller
    ---------------------------
    Base class for all grc controllers and plugins.
    May need to convert these to class decorators?
     - Might help future development
    """

    def notImplemented(self):
        self.log.debug ('Not implemented')


class View(object):
    """
    GRC.Base.View
    ---------------------------
    Base class for all grc view and plugins.
    May need to convert these to class decorators?
     - Might help future development
    """

    def __init__(self):
        self.actions = {}

    def notImplemented(self):
        self.log.debug ('Not implemented')
