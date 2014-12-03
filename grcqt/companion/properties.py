import os,  logging
logger = logging.getLogger("grc.properties")

'''
Stores global system and preference properties for GRC
'''
class Properties(object):

    def __init__(self, argv, file):
        self.argv = argv
        self.Constants()

        # Setup sub-categories
        self.path = self.Path(file) # Setup default path and file information
        self.system = self.System()
        self.window = self.Window()
        self.colors = self.Colors()

    # Initialize constants
    def Constants(self):
        self.APP_NAME = 'grc'
        self.DEFAULT_LANGUAGE = ['en_US']
        logger.debug("APP_NAME - %s" % self.APP_NAME)
        logger.debug("DEFAULT_LANGUAGE - %s" % self.DEFAULT_LANGUAGE)


    ''' Sub-category property classes '''
    # Initialize directories based on the path of the main script
    class Path(object):
        def __init__(self, file):
            ### GRC
            self.INSTALL = os.path.abspath(os.path.dirname(file))
            self.RESOURCES = os.path.join(self.INSTALL, 'companion/resources')
            self.LANGUAGE = os.path.join(self.INSTALL, 'companion/resources/language')
            self.LOGO = os.path.join(self.INSTALL, 'companion/resources/logo')
            self.ICON = os.path.join(self.LOGO, 'gnuradio_logo_icon-square-150x150-white.png')
            logger.debug("INSTALL - %s" % self.INSTALL)
            logger.debug("RESOURCES - %s" % self.RESOURCES)
            logger.debug("LANGUAGE - %s" % self.LANGUAGE)
            logger.debug("LOGO - %s" % self.LOGO)
            logger.debug("ICON - %s" % self.ICON)

            ### Flow graph
            self.DEFAULT_FILE = os.getcwd()
            self.IMAGE_FILE_EXTENSION = '.png'
            self.TEXT_FILE_EXTENSION = '.txt'
            self.NEW_FLOGRAPH_TITLE = 'untitled'
            logger.debug("DEFAULT_FILE - %s" % self.DEFAULT_FILE)
            logger.debug("IMAGE_FILE_EXTENSION - %s" % self.IMAGE_FILE_EXTENSION)
            logger.debug("TEXT_FILE_EXTENSION - %s" % self.TEXT_FILE_EXTENSION)
            logger.debug("NEW_FLOGRAPH_TITLE - %s" % self.NEW_FLOGRAPH_TITLE)


    class System(object):
        def __init__(self):
            self.OS = "Unknown"

    class Window(object):
        def __init__(self):
            # Default window properties
            self.MIN_WINDOW_WIDTH = 600
            self.MIN_WINDOW_HEIGHT = 400

            self.MIN_DIALOG_WIDTH = 500
            self.MIN_DIALOG_HEIGHT = 500

            # How close can the mouse get to the window border before mouse events are ignored.
            self.BORDER_PROXIMITY_SENSITIVITY = 50

            # How close the mouse can get to the edge of the visible window before scrolling is invoked.
            self.SCROLL_PROXIMITY_SENSITIVITY = 30

            # When the window has to be scrolled, move it this distance in the required direction.
            self.SCROLL_DISTANCE = 15

            # By default Always show the menubar
            self.NATIVE_MENUBAR = False

            # Default sizes
            self.DEFAULT_BLOCKS_WINDOW_WIDTH = 100
            self.DEFAULT_REPORTS_WINDOW_WIDTH = 100

    class FlowGraph(object):
        def __init__(self):
            # Fonts
            self.FONT_FAMILY = "Sans"
            self.FONT_SIZE = 8
            self.BLOCK_FONT = "%s %f" % (FONT_FAMILY, FONT_SIZE)
            self.PORT_FONT = BLOCK_FONT
            self.PARAM_FONT = "%s %f" % (FONT_FAMILY, FONT_SIZE - 0.5)

            # The size of the state saving cache in the flow graph (for undo/redo functionality)
            self.STATE_CACHE_SIZE = 42

            # Shared targets for drag and drop of blocks
            #DND_TARGETS = [('STRING', gtk.TARGET_SAME_APP, 0)]

            # Label constraints
            self.LABEL_SEPARATION = 3
            self.BLOCK_LABEL_PADDING = 7
            self.PORT_LABEL_PADDING = 2

            # Port constraints
            self.PORT_SEPARATION = 32
            self.PORT_BORDER_SEPARATION = 9
            self.PORT_MIN_WIDTH = 20
            self.PORT_LABEL_HIDDEN_WIDTH = 10

            # Connector lengths
            self.CONNECTOR_EXTENSION_MINIMAL = 11
            self.CONNECTOR_EXTENSION_INCREMENT = 11

            # Connection arrows
            self.CONNECTOR_ARROW_BASE = 13
            self.CONNECTOR_ARROW_HEIGHT = 17

            # Rotations
            self.POSSIBLE_ROTATIONS = (0, 90, 180, 270)

            # How close the mouse click can be to a line and register a connection select.
            self.LINE_SELECT_SENSITIVITY = 5

            # canvas grid size
            self.CANVAS_GRID_SIZE = 8

    class Colors(object):
        def __init__(self):
            from PyQt5 import QtGui
            color = QtGui.QColor

            self.HIGHLIGHT = color('#00FFFF')
            self.BORDER = color('black')
            self.MISSING_BLOCK_BACKGROUND = color('#FFF2F2')
            self.MISSING_BLOCK_BORDER = color('red')
            self.PARAM_ENTRY_TEXT = color('black')
            self.ENTRYENUM_CUSTOM = color('#EEEEEE')
            self.FLOWGRAPH_BACKGROUND = color('#FFF9FF')
            self.BLOCK_ENABLED = color('#F1ECFF')
            self.BLOCK_DISABLED = color('#CCCCCC')
            self.CONNECTION_ENABLED = color('black')
            self.CONNECTION_DISABLED = color('#999999')
            self.CONNECTION_ERROR = color('red')

# In case importing is a better method
# properties = Properties() # Use for import method?
