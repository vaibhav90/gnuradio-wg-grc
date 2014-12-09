
'''
 Handles connecting signals from given actions to handlers
    self    - Calling class
    actions - Dictionary of a QAction and unique key

 Dynamically build the connections for the signals by finding the correct
 function to handle an action.

 Essentially the same as QMetaObject::connectSlotsByName, except the actions
  and slots can be separated into a view and controller class

'''

def connectSlots(self, actions):
    for key in actions:
        # Try and bind the 'triggered' signal to a handler.
        try:
            triggered_handler = key + "_triggered"
            actions[key].triggered.connect(getattr(self, triggered_handler))
            self.log.debug("<%s.triggered> connected to handler <%s>" % (key, triggered_handler))
        except:
            try:
                self.log.warning("Handler not implemented for <%s.triggered> in %s" % (key, type(self)))
                actions[key].triggered.connect(getattr(self, 'notImplemented'))
            except:
                # This should never happen because 'notImplemented' is defined in base.Controller
                self.log.error("Class cannot handle <%s.triggered>" % key)

        # Try and bind the 'toggled' signal to a handler
        # Just ignore an error if this handler does not exist
        try:
            toggled_handler = key + "_toggled"
            actions[key].toggled.connect(getattr(self, toggled_handler))
            self.log.debug("<%s.toggled> connected to handler <%s>" % (key, toggled_handler))
        except:
            pass
