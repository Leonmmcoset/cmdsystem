# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .DataNode import DataNode

class ButtonNode(DataNode):
    """
    /**
     * This is the primary interface to on/off button devices associated with a
     * ClientBase.  This creates a node that connects to the named button device,
     * if it exists, and provides hooks to the user to read the state of any of
     * the sequentially numbered buttons associated with that device.
     *
     * It also can associate an arbitrary ButtonHandle with each button; when
     * buttons are associated with ButtonHandles, this node will put appropriate
     * up and down events on the data graph for each button state change.
     */
    """
    def getButtonMap(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_button_map(ButtonNode self, int index)
        
        /**
         * Returns the ButtonHandle that was previously associated with the given
         * index number by a call to set_button_map(), or ButtonHandle::none() if no
         * button was associated.
         */
        """
        pass

    def getButtonState(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_button_state(ButtonNode self, int index)
        
        /**
         * Returns true if the indicated button (identified by its index number) is
         * currently known to be down, or false if it is up or unknown.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getNumButtons(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_buttons(ButtonNode self)
        
        /**
         * Returns the number of buttons known to the ButtonNode.  This includes those
         * buttons whose state has been seen, as well as buttons that have been
         * associated with a ButtonHandle even if their state is unknown.  This number
         * may change as more buttons are discovered.
         */
        """
        pass

    def get_button_map(self, ButtonNode_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_button_map(ButtonNode self, int index)
        
        /**
         * Returns the ButtonHandle that was previously associated with the given
         * index number by a call to set_button_map(), or ButtonHandle::none() if no
         * button was associated.
         */
        """
        pass

    def get_button_state(self, ButtonNode_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_button_state(ButtonNode self, int index)
        
        /**
         * Returns true if the indicated button (identified by its index number) is
         * currently known to be down, or false if it is up or unknown.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_num_buttons(self, ButtonNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_buttons(ButtonNode self)
        
        /**
         * Returns the number of buttons known to the ButtonNode.  This includes those
         * buttons whose state has been seen, as well as buttons that have been
         * associated with a ButtonHandle even if their state is unknown.  This number
         * may change as more buttons are discovered.
         */
        """
        pass

    def isButtonKnown(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_button_known(ButtonNode self, int index)
        
        /**
         * Returns true if the state of the indicated button is known, or false if we
         * have never heard anything about this particular button.
         */
        """
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_valid(ButtonNode self)
        
        /**
         * Returns true if the ButtonNode is valid and connected to a server, false
         * otherwise.
         */
        """
        pass

    def is_button_known(self, ButtonNode_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_button_known(ButtonNode self, int index)
        
        /**
         * Returns true if the state of the indicated button is known, or false if we
         * have never heard anything about this particular button.
         */
        """
        pass

    def is_valid(self, ButtonNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_valid(ButtonNode self)
        
        /**
         * Returns true if the ButtonNode is valid and connected to a server, false
         * otherwise.
         */
        """
        pass

    def setButtonMap(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_button_map(const ButtonNode self, int index, ButtonHandle button)
        
        /**
         * Associates the indicated ButtonHandle with the button of the indicated
         * index number.  When the given button index changes state, a corresponding
         * ButtonEvent will be generated with the given ButtonHandle.  Pass
         * ButtonHandle::none() to turn off any association.
         *
         * It is not necessary to call this if you simply want to query the state of
         * the various buttons by index number; this is only necessary in order to
         * generate ButtonEvents when the buttons change state.
         */
        """
        pass

    def set_button_map(self, const_ButtonNode_self, int_index, ButtonHandle_button): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_button_map(const ButtonNode self, int index, ButtonHandle button)
        
        /**
         * Associates the indicated ButtonHandle with the button of the indicated
         * index number.  When the given button index changes state, a corresponding
         * ButtonEvent will be generated with the given ButtonHandle.  Pass
         * ButtonHandle::none() to turn off any association.
         *
         * It is not necessary to call this if you simply want to query the state of
         * the various buttons by index number; this is only necessary in order to
         * generate ButtonEvents when the buttons change state.
         */
        """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.ButtonNode' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.ButtonNode' objects>"
        '__doc__': '/**\n * This is the primary interface to on/off button devices associated with a\n * ClientBase.  This creates a node that connects to the named button device,\n * if it exists, and provides hooks to the user to read the state of any of\n * the sequentially numbered buttons associated with that device.\n *\n * It also can associate an arbitrary ButtonHandle with each button; when\n * buttons are associated with ButtonHandles, this node will put appropriate\n * up and down events on the data graph for each button state change.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.ButtonNode' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2D6BE0>'
        'getButtonMap': None, # (!) real value is "<method 'getButtonMap' of 'panda3d.core.ButtonNode' objects>"
        'getButtonState': None, # (!) real value is "<method 'getButtonState' of 'panda3d.core.ButtonNode' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2D6BE0>)>'
        'getNumButtons': None, # (!) real value is "<method 'getNumButtons' of 'panda3d.core.ButtonNode' objects>"
        'get_button_map': None, # (!) real value is "<method 'get_button_map' of 'panda3d.core.ButtonNode' objects>"
        'get_button_state': None, # (!) real value is "<method 'get_button_state' of 'panda3d.core.ButtonNode' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2D6BE0>)>'
        'get_num_buttons': None, # (!) real value is "<method 'get_num_buttons' of 'panda3d.core.ButtonNode' objects>"
        'isButtonKnown': None, # (!) real value is "<method 'isButtonKnown' of 'panda3d.core.ButtonNode' objects>"
        'isValid': None, # (!) real value is "<method 'isValid' of 'panda3d.core.ButtonNode' objects>"
        'is_button_known': None, # (!) real value is "<method 'is_button_known' of 'panda3d.core.ButtonNode' objects>"
        'is_valid': None, # (!) real value is "<method 'is_valid' of 'panda3d.core.ButtonNode' objects>"
        'setButtonMap': None, # (!) real value is "<method 'setButtonMap' of 'panda3d.core.ButtonNode' objects>"
        'set_button_map': None, # (!) real value is "<method 'set_button_map' of 'panda3d.core.ButtonNode' objects>"
    }


