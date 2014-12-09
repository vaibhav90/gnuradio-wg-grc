import os

'''
Stores global system and preference properties for GRC.
 - Setup default values during initialization
'''
class Properties(object):

    def __init__(self, argv, file):
        self.argv = argv
        self.Constants()

        # Setup sub-categories
        self.path = self.Paths(file) # Setup default path and file information
        self.system = self.System()
        self.window = self.Window()
        self.colors = self.Colors()
        self.types = self.Types(self.colors)


    # Initialize constants
    def Constants(self):
        self.APP_NAME = 'grc'
        self.DEFAULT_LANGUAGE = ['en_US']


    ''' Sub-category property classes '''
    # Initialize directories based on the path of the main script
    class Paths(object):
        def __init__(self, file):
            ### GRC Specific Paths
            self.INSTALL = os.path.abspath(os.path.dirname(file))
            self.RESOURCES = os.path.join(self.INSTALL, 'companion/resources')
            self.LANGUAGE = os.path.join(self.INSTALL, 'companion/resources/language')
            self.LOGO = os.path.join(self.INSTALL, 'companion/resources/logo')
            self.ICON = os.path.join(self.LOGO, 'gnuradio_logo_icon-square-150x150-white.png')
            self.PREFERENCES = os.path.expanduser('~/.grc')

            # Model Paths
            self.MODEL = os.path.join(self.INSTALL, 'model')
            self.BLOCK_TREE_DTD = os.path.join(self.MODEL, 'block_tree.dtd')
            self.FLOW_GRAPH_DTD = os.path.join(self.MODEL, 'flow_graph.dtd')
            self.FLOW_GRAPH_TEMPLATE = os.path.join(self.MODEL, 'flow_graph.tmpl')

            ### Flow graph
            self.DEFAULT_FILE = os.getcwd()
            self.IMAGE_FILE_EXTENSION = '.png'
            self.TEXT_FILE_EXTENSION = '.txt'
            self.NEW_FLOGRAPH_TITLE = 'untitled'


    class System(object):
        def __init__(self):
            self.OS = 'Unknown'


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

            self.DEFAULT_PARAM_TAB = 'General'
            self.ADVANCED_PARAM_TAB = 'Advanced'


    class FlowGraph(object):
        def __init__(self):
            # File format
            self.FILE_FORMAT_VERSION = 1

            # Fonts
            self.FONT_FAMILY = 'Sans'
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
            # Some colors may be duplicated between different categories.
            # TODO: Should color actually be setup as a PyQT Object here?
            #       Maybe it's better to just return the string and have
            #       A view actually setup a color instance.
            #from PyQt5 import QtGui
            #color = QtGui.QColor

            # Graphics stuff
            self.HIGHLIGHT                  = '#00FFFF'      # = color('#00FFFF')
            self.BORDER                     = 'black'        # = color('black')
            self.MISSING_BLOCK_BACKGROUND   = '#FFF2F2'      # = color('#FFF2F2')
            self.MISSING_BLOCK_BORDER       = 'red'          # = color('red')
            self.PARAM_ENTRY_TEXT           = 'black'        # = color('black')
            self.ENTRYENUM_CUSTOM           = '#EEEEEE'      # = color('#EEEEEE')
            self.FLOWGRAPH_BACKGROUND       = '#FFF9FF'      # = color('#FFF9FF')
            self.BLOCK_ENABLED              = '#F1ECFF'      # = color('#F1ECFF')
            self.BLOCK_DISABLED             = '#CCCCCC'      # = color('#CCCCCC')
            self.CONNECTION_ENABLED         = 'black'        # = color('black')
            self.CONNECTION_DISABLED        = '#999999'      # = color('#999999')
            self.CONNECTION_ERROR           = 'red'          # = color('red')

            # Alias Colors
            self.COMPLEX                    = '#3399FF'      # = color('#3399FF')
            self.FLOAT                      = '#FF8C69'      # = color('#FF8C69')
            self.INT                        = '#00FF99'      # = color('#00FF99')
            self.SHORT                      = '#FFFF66'      # = color('#FFFF66')
            self.BYTE                       = '#FF66FF'      # = color('#FF66FF')

            # Type Colors
            self.COMPLEX_FLOAT_64           = '#CC8C69'      # = color('#CC8C69')
            self.COMPLEX_FLOAT_32           = '#3399FF'      # = color('#3399FF')
            self.COMPLEX_INTEGER_64         = '#66CC00'      # = color('#66CC00')
            self.COMPLEX_INTEGER_32         = '#33cc66'      # = color('#33cc66')
            self.COMPLEX_INTEGER_16         = '#cccc00'      # = color('#cccc00')
            self.COMPLEX_INTEGER_8          = '#cc00cc'      # = color('#cc00cc')
            self.FLOAT_64                   = '#66CCCC'      # = color('#66CCCC')
            self.FLOAT_32                   = '#FF8C69'      # = color('#FF8C69')
            self.INTEGER_64                 = '#99FF33'      # = color('#99FF33')
            self.INTEGER_32                 = '#00FF99'      # = color('#00FF99')
            self.INTEGER_16                 = '#FFFF66'      # = color('#FFFF66')
            self.INTEGER_8                  = '#FF66FF'      # = color('#FF66FF')
            self.MESSAGE_QUEUE              = '#777777'      # = color('#777777')
            self.ASYNC_MESSAGE              = '#C0C0C0'      # = color('#C0C0C0')
            self.BUS_CONNECTION             = '#FFFFFF'      # = color('#FFFFFF')
            self.WILDCARD                   = '#FFFFFF'      # = color('#FFFFFF')

            self.COMPLEX_VECTOR             = '#3399AA'      # = color('#3399AA')
            self.FLOAT_VECTOR               = '#CC8C69'      # = color('#CC8C69')
            self.INT_VECTOR                 = '#00CC99'      # = color('#00CC99')
            self.SHORT_VECTOR               = '#CCCC33'      # = color('#CCCC33')
            self.BYTE_VECTOR                = '#CC66CC'      # = color('#CC66CC')
            self.ID                         = '#DDDDDD'      # = color('#DDDDDD')
            self.WILDCARD                   = '#FFFFFF'      # = color('#FFFFFF')
            self.MSG                        = '#777777'      # = color('#777777')


    # Class is dependant on the color class.
    class Types(object):
        def __init__(self, colors):
            # Setup types then map them to the conversion dictionaries
            self.CORE_TYPES = {# key, size, color, name
                 'fc64':    (16, colors.COMPLEX_FLOAT_64,   'Complex Float 64'),
                 'fc32':    (8,  colors.COMPLEX_FLOAT_32,   'Complex Float 32'),
                 'sc64':    (16, colors.COMPLEX_INTEGER_64, 'Complex Integer 64'),
                 'sc32':    (8,  colors.COMPLEX_INTEGER_32, 'Complex Integer 32'),
                 'sc16':    (4,  colors.COMPLEX_INTEGER_16, 'Complex Integer 16'),
                 'sc8':     (2,  colors.COMPLEX_INTEGER_8,  'Complex Integer 8',),
                 'f64':     (8,  colors.FLOAT_64,           'Float 64'),
                 'f32':     (4,  colors.FLOAT_32,           'Float 32'),
                 's64':     (8,  colors.INTEGER_64,         'Integer 64'),
                 's32':     (4,  colors.INTEGER_32,         'Integer 32'),
                 's16':     (2,  colors.INTEGER_16,         'Integer 16'),
                 's8':      (1,  colors.INTEGER_8,          'Integer 8'),
                 'msg':     (0,  colors.MESSAGE_QUEUE,      'Message Queue'),
                 'message': (0,  colors.ASYNC_MESSAGE,      'Async Message'),
                 'bus':     (0,  colors.BUS_CONNECTION,     'Bus Connection'),
                 '':        (0,  colors.WILDCARD,           'Wildcard')
            }

            self.ALIAS_TYPES = {
                'complex' : (8, colors.COMPLEX),
                'float'   : (4, colors.FLOAT),
                'int'     : (4, colors.INT),
                'short'   : (2, colors.SHORT),
                'byte'    : (1, colors.BYTE),
            }

            # Setup conversion dictionaries
            self.TYPE_TO_COLOR = {}
            self.TYPE_TO_SIZEOF = {}
            for key, (size, color, name) in self.CORE_TYPES.items():
                self.TYPE_TO_COLOR[key]  = color
                self.TYPE_TO_SIZEOF[key] = size
            for key, (sizeof, color) in self.ALIAS_TYPES.items():
                self.TYPE_TO_COLOR[key]  = color
                self.TYPE_TO_SIZEOF[key] = size

# In case importing is a better method
# properties = Properties() # Use for import method?
