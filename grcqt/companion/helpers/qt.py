
'''
 Handles connecting signals from given actions to handlers
    self    - Calling class
    actions - Dictionary of a QAction and unique key

 Dynamically build the connections for the signals by finding the correct
 function to handle an action. Default behavior is to connect checkable actions to
 the 'toggled' signal and normal actions to the 'triggered' signal. If 'toggled' is
 not avaliable or useToggled is set to False then try to connect it to triggered.
 Both toggled and triggered are called for checkable items, so there is no need for
 both to be connected.

    void QAction::toggled ( bool checked ) [signal]
    void QAction::triggered ( bool checked = false ) [signal]
      - Checked is set for checkable actions

 Essentially the same as QMetaObject::connectSlotsByName, except the actions
  and slots can be separated into a view and controller class

'''

def connectSlots(self, actions, useToggled=True,
                 toggledHander="_toggled", triggeredHandler="_triggered"):
    for key in actions:
        if useToggled == True and actions[key].isCheckable():
            # Try to use toggled rather than triggered
            try:
                handler = key + toggledHander
                actions[key].toggled.connect(getattr(self, handler))
                self.log.debug("<%s.toggled> connected to handler <%s>" % (key, handler))
                # Successful connection. Jump to the next action.
                continue
            except:
                # Default to the triggered handler
                self.log.warning("Could not connect <%s.toggled> to handler <%s>" % (key, handler))

        # Try and bind the 'triggered' signal to a handler.
        try:
            handler = key + triggeredHandler
            actions[key].triggered.connect(getattr(self, handler))
            self.log.debug("<%s.triggered> connected to handler <%s>" % (key, handler))
        except:
            try:
                self.log.warning("Handler not implemented for <%s.triggered> in %s" % (key, type(self).__name__))
                actions[key].triggered.connect(getattr(self, 'notImplemented'))
            except:
                # This should never happen because 'notImplemented' is defined in base.Controller
                self.log.error("Class cannot handle <%s.triggered>" % key)
