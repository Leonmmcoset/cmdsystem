# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .DataNode import DataNode

class MouseInterfaceNode(DataNode):
    """
    /**
     * This is the base class for some classes that monitor the mouse and keyboard
     * input and perform some action due to their state.
     *
     * It collects together some common interface; in particular, the
     * require_button() and related methods.
     */
    """
    def clearAllButtons(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_all_buttons(const MouseInterfaceNode self)
        
        /**
         * Removes all requirements on buttons set by an earlier call to
         * require_button().
         */
        """
        pass

    def clearButton(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_button(const MouseInterfaceNode self, const ButtonHandle button)
        
        /**
         * Removes any requirement on the indicated button set by an earlier call to
         * require_button().
         */
        """
        pass

    def clear_all_buttons(self, const_MouseInterfaceNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_all_buttons(const MouseInterfaceNode self)
        
        /**
         * Removes all requirements on buttons set by an earlier call to
         * require_button().
         */
        """
        pass

    def clear_button(self, const_MouseInterfaceNode_self, const_ButtonHandle_button): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_button(const MouseInterfaceNode self, const ButtonHandle button)
        
        /**
         * Removes any requirement on the indicated button set by an earlier call to
         * require_button().
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def requireButton(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        require_button(const MouseInterfaceNode self, const ButtonHandle button, bool is_down)
        
        /**
         * Indicates that the indicated button must be in the required state (either
         * up or down) in order for this particular MouseInterfaceNode to do anything.
         * For instance, this may be called to make a Trackball object respect mouse
         * input only when the control key is held down.
         */
        """
        pass

    def require_button(self, const_MouseInterfaceNode_self, const_ButtonHandle_button, bool_is_down): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        require_button(const MouseInterfaceNode self, const ButtonHandle button, bool is_down)
        
        /**
         * Indicates that the indicated button must be in the required state (either
         * up or down) in order for this particular MouseInterfaceNode to do anything.
         * For instance, this may be called to make a Trackball object respect mouse
         * input only when the control key is held down.
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
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.MouseInterfaceNode' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.MouseInterfaceNode' objects>"
        '__doc__': '/**\n * This is the base class for some classes that monitor the mouse and keyboard\n * input and perform some action due to their state.\n *\n * It collects together some common interface; in particular, the\n * require_button() and related methods.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.MouseInterfaceNode' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE3660D0>'
        'clearAllButtons': None, # (!) real value is "<method 'clearAllButtons' of 'panda3d.core.MouseInterfaceNode' objects>"
        'clearButton': None, # (!) real value is "<method 'clearButton' of 'panda3d.core.MouseInterfaceNode' objects>"
        'clear_all_buttons': None, # (!) real value is "<method 'clear_all_buttons' of 'panda3d.core.MouseInterfaceNode' objects>"
        'clear_button': None, # (!) real value is "<method 'clear_button' of 'panda3d.core.MouseInterfaceNode' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE3660D0>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE3660D0>)>'
        'requireButton': None, # (!) real value is "<method 'requireButton' of 'panda3d.core.MouseInterfaceNode' objects>"
        'require_button': None, # (!) real value is "<method 'require_button' of 'panda3d.core.MouseInterfaceNode' objects>"
    }


