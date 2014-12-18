import logging

# Library used for formatting console output

'''
 Custom log handler for GRC. Handles storing logs in list that can be
  viewed using the GRC debug window.
'''
class GRCHandler(logging.Handler): # Inherit from logging.Handler
    def __init__(self, maxLength=256):
        # run the regular Handler __init__
        logging.Handler.__init__(self)
        # Our custom argument
        self.maxLength = maxLength  # Default to 256 log entries
        self.log = []

    def emit(self, record):
        self.log.append(record)
        if len(self.log) > self.maxLength:
            self.log.pop(0)    # List is too long. Remove the first item

    def getLogs(self, level):
        pass


'''
 Custom log formatter that nicely truncates the log message and log levels
  - Verbose mode outputs: time, level, message, name, filename, and line number
  - Normal mode output varies based on terminal size:
        w < 80       - Level, Message (min length 40)
        80 < w < 120 - Level, Message, File, Line (25)
        120 < w      - Level, Message, Name, File, Line
  - Color mode ouptuts the same variable sizes and uses the blessings module
    to add color
'''
class ConsoleFormatter(logging.Formatter):
    def __init__(self, verbose=False):
        # Test for blessings formatter
        try:
            from blessings import Terminal
            self.terminal = Terminal()
            self.formatLevel = self.formatLevelColor
        except:
            self.terminal = None
            self.formatLevel = self.formatLevelPlain

        # Setup the format function as a pointer to the correct formatting function
        # Determine size and mode
        import shutil
        size = shutil.get_terminal_size()
        self.width = size.columns
        if size.columns < 80:
            self.format = self.short
        elif size.columns < 120:
            self.format = self.medium
        elif size.columns >= 120:
            self.format = self.long

        # Check if verbose mode. If so override other options
        if verbose:
            self.format = self.verbose

    ''' Normal console formatters '''
    def short(self, record):
        message_width = max(40, self.width - 15) # Account for level width
        message = self.formatMessage(record.msg, message_width)
        level = self.formatLevel(record.levelname)
        return ('%s -- %s' % (level, message))

    def medium(self, record):
        # Show the file and line number (25)
        message_width = self.width - 45
        message = self.formatMessage(record.msg, message_width)
        level = self.formatLevel(record.levelname)
        format = '%s -- %-' + str(message_width) + 's (%s:%s)'
        return format % (level, message, record.filename, record.lineno)

    def long(self, record):
        # Show the logger name
        message_width = self.width - 60
        message = self.formatMessage(record.msg, message_width)
        level = self.formatLevel(record.levelname)
        format = '%s -- %-' + str(message_width) + 's %s (%s:%s)'
        return format % (level, message, record.name, record.filename, record.lineno)

    ''' Verbose formatter '''
    def verbose(self, record):
        pass

    ''' Level and message formatters '''
    # Nicely format the levelname
    def formatLevelColor(self, levelname):
        term = self.terminal
        if(levelname == "DEBUG"):
            return (term.blue + "[Debug]".ljust(10) + term.normal)
        elif(levelname == "INFO"):
            return (term.green + "[Info]".ljust(10) + term.normal)
        elif(levelname == "WARNING"):
            return (term.yellow + "[Warning]".ljust(10) + term.normal)
        elif(levelname == "ERROR"):
            return (term.red + term.bold + "[ERROR]".ljust(10) + term.normal)
        elif(levelname == "CRITICAL"):
            return (term.red + term.bold + "[CRITICAL]".ljust(10) + term.normal)
        else:
            return levelname

    def formatLevelPlain(self, levelname):
        if(levelname == "DEBUG"):
            return "[Debug]".ljust(10)
        elif(levelname == "INFO"):
            return "[Info]".ljust(10)
        elif(levelname == "WARNING"):
            return "[Warning]".ljust(10)
        elif(levelname == "ERROR"):
            return "[ERROR]".ljust(10)
        elif(levelname == "CRITICAL"):
            return "[CRITICAL]".ljust(10)
        else:
            return levelname

    def formatMessage(self, message, width):
        if len(message) > width:
            return (message[:(width - 3)] + "...")
        return message
