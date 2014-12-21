import logging


class GRCHandler(logging.Handler):  # Inherit from logging.Handler
    """ Custom log handler for GRC. Stores log entries to be viewed using the GRC debug window. """

    def __init__(self, maxLength=256):
        # run the regular Handler __init__
        logging.Handler.__init__(self)
        # Our custom argument
        self.log = collections.deque(maxlen=maxLength)

    def emit(self, record):
        self.log.append(record)

    def getLogs(self, level):
        pass


class ConsoleFormatter(logging.Formatter):
    """
     Custom log formatter that nicely truncates the log message and log levels
      - Verbose mode outputs: time, level, message, name, filename, and line number
      - Normal mode output varies based on terminal size:
            w < 80       - Level, Message (min length 40)
            80 < w < 120 - Level, Message, File, Line (25)
            120 < w      - Level, Message, Name, File, Line
      - Color mode ouptuts the same variable sizes and uses the blessings module
        to add color
    """

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
        width = max(40, size.columns - 15)
        if size.columns < 80:
            self.format = self.short
            self.width = width
        elif size.columns < 120:
            self.format = self.medium
            self.width = width - 30
        elif size.columns >= 120:
            self.format = self.long
            self.width = width - 45
        # Check if verbose mode. If so override other options
        if verbose:
            self.format = self.verbose

    # Normal log formmatters
    def short(self, record):
        message = self.formatMessage(record.msg, self.width)
        level = self.formatLevel(record.levelname)
        return "{0} -- {1}".format(level, message)

    def medium(self, record):
        message = self.formatMessage(record.msg, self.width)
        level = self.formatLevel(record.levelname)
        output = '{0} -- {1:<' + str(self.width) + '} ({2}:{3})'
        return output.format(level, message, record.filename, record.lineno)

    def long(self, record):
        message = self.formatMessage(record.msg, self.width)
        level = self.formatLevel(record.levelname)
        output = '{0} -- {1:<' + str(self.width) + '} {2} ({3}:{4})'
        return output.format(level, message, record.name, record.filename, record.lineno)

    ''' Verbose formatter '''
    def verbose(self, record):
        pass

    ''' Level and message formatters '''
    # Nicely format the levelname
    def formatLevelColor(self, levelname):
        term = self.terminal
        output = "{0}{1}{2:<10}{3}"
        if levelname == "DEBUG":
            return output.format(term.blue, "", "[Debug]", term.normal)
        elif levelname == "INFO":
            return output.format(term.green, "", "[Info]", term.normal)
        elif levelname == "WARNING":
            return output.format(term.yellow, "", "[Warning]", term.normal)
        elif levelname == "ERROR":
            return output.format(term.red, term.bold, "[ERROR]", term.normal)
        elif levelname == "CRITICAL":
            return output.format(term.red, term.bold, "[CRITICAL]", term.normal)
        else:
            return output.format(term.blue, "", "[NOTSET]", term.normal)

    def formatLevelPlain(self, levelname):
        output = "{0:<10}"
        if(levelname == "DEBUG"):
            return output.format("[Debug]")
        elif(levelname == "INFO"):
            return output.format("[Info]")
        elif(levelname == "WARNING"):
            return output.format("[Warning]")
        elif(levelname == "ERROR"):
            return output.format("[ERROR]")
        elif(levelname == "CRITICAL"):
            return output.format("[CRITICAL]")
        else:
            return output.format("[NOTSET]")

    def formatMessage(self, message, width):
        if len(message) > width:
            return (message[:(width - 3)] + "...")
        return message
