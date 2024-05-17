# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .DataNode import DataNode

class MouseAndKeyboard(DataNode):
    """
    /**
     * Reads the mouse and/or keyboard data sent from a GraphicsWindow, and
     * transmits it down the data graph.
     *
     * The mouse and keyboard devices are bundled together into one device here,
     * because they interrelate so much.  A mouse might be constrained by the
     * holding down of the shift key, for instance, or the clicking of the mouse
     * button might be handled in much the same way as a keyboard key.
     *
     * Mouse data is sent down the data graph as an x,y position as well as the
     * set of buttons currently being held down; keyboard data is sent down as a
     * set of keypress events in an EventDataTransition.  To throw these events to
     * the system, you must attach an EventThrower to the MouseAndKeyboard object;
     * otherwise, the events will be discarded.
     */
    """
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

    def setSource(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_source(const MouseAndKeyboard self, GraphicsWindow window, int device)
        
        /**
         * Redirects the class to get the data from the mouse and keyboard associated
         * with a different window and/or device number.
         */
        """
        pass

    def set_source(self, const_MouseAndKeyboard_self, GraphicsWindow_window, int_device): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_source(const MouseAndKeyboard self, GraphicsWindow window, int device)
        
        /**
         * Redirects the class to get the data from the mouse and keyboard associated
         * with a different window and/or device number.
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
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.MouseAndKeyboard' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.MouseAndKeyboard' objects>"
        '__doc__': '/**\n * Reads the mouse and/or keyboard data sent from a GraphicsWindow, and\n * transmits it down the data graph.\n *\n * The mouse and keyboard devices are bundled together into one device here,\n * because they interrelate so much.  A mouse might be constrained by the\n * holding down of the shift key, for instance, or the clicking of the mouse\n * button might be handled in much the same way as a keyboard key.\n *\n * Mouse data is sent down the data graph as an x,y position as well as the\n * set of buttons currently being held down; keyboard data is sent down as a\n * set of keypress events in an EventDataTransition.  To throw these events to\n * the system, you must attach an EventThrower to the MouseAndKeyboard object;\n * otherwise, the events will be discarded.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.MouseAndKeyboard' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2DFD10>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2DFD10>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2DFD10>)>'
        'setSource': None, # (!) real value is "<method 'setSource' of 'panda3d.core.MouseAndKeyboard' objects>"
        'set_source': None, # (!) real value is "<method 'set_source' of 'panda3d.core.MouseAndKeyboard' objects>"
    }


