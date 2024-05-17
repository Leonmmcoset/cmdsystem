# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .DataNode import DataNode

class VirtualMouse(DataNode):
    """
    /**
     * Poses as a MouseAndKeyboard object in the datagraph, but accepts input from
     * user calls, rather than reading the actual mouse and keyboard from an input
     * device.  The user can write high-level code to put the mouse wherever
     * he/she wants, and to insert keypresses on demand.
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

    def pressButton(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        press_button(const VirtualMouse self, ButtonHandle button)
        
        /**
         * Simulates a mouse or keyboard button being depressed.  This should be
         * followed up by a call to release_button() sometime later (possibly
         * immediately).
         */
        """
        pass

    def press_button(self, const_VirtualMouse_self, ButtonHandle_button): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        press_button(const VirtualMouse self, ButtonHandle button)
        
        /**
         * Simulates a mouse or keyboard button being depressed.  This should be
         * followed up by a call to release_button() sometime later (possibly
         * immediately).
         */
        """
        pass

    def releaseButton(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        release_button(const VirtualMouse self, ButtonHandle button)
        
        /**
         * Simulates the button being released.  This should follow a previous call to
         * press_button().
         */
        """
        pass

    def release_button(self, const_VirtualMouse_self, ButtonHandle_button): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        release_button(const VirtualMouse self, ButtonHandle button)
        
        /**
         * Simulates the button being released.  This should follow a previous call to
         * press_button().
         */
        """
        pass

    def setMouseOn(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_mouse_on(const VirtualMouse self, bool flag)
        
        /**
         * Sets whether the mouse should appear to be within the window or not.  If
         * this is true, the mouse is within the window; if false, the mouse is not
         * within the window (and set_mouse_pos() means nothing).
         */
        """
        pass

    def setMousePos(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_mouse_pos(const VirtualMouse self, int x, int y)
        
        /**
         * Sets the current mouse pixel location, where (0,0) is the upper left, and
         * (width-1, height-1) is the lower right pixel of the virtual window.
         */
        """
        pass

    def setWindowSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_window_size(const VirtualMouse self, int width, int height)
        
        /**
         * Sets the size of the "window" in which the mouse rolls.  This changes the
         * meaning of the values passed to set_mouse_pos().
         */
        """
        pass

    def set_mouse_on(self, const_VirtualMouse_self, bool_flag): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_mouse_on(const VirtualMouse self, bool flag)
        
        /**
         * Sets whether the mouse should appear to be within the window or not.  If
         * this is true, the mouse is within the window; if false, the mouse is not
         * within the window (and set_mouse_pos() means nothing).
         */
        """
        pass

    def set_mouse_pos(self, const_VirtualMouse_self, int_x, int_y): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_mouse_pos(const VirtualMouse self, int x, int y)
        
        /**
         * Sets the current mouse pixel location, where (0,0) is the upper left, and
         * (width-1, height-1) is the lower right pixel of the virtual window.
         */
        """
        pass

    def set_window_size(self, const_VirtualMouse_self, int_width, int_height): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_window_size(const VirtualMouse self, int width, int height)
        
        /**
         * Sets the size of the "window" in which the mouse rolls.  This changes the
         * meaning of the values passed to set_mouse_pos().
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
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.VirtualMouse' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.VirtualMouse' objects>"
        '__doc__': '/**\n * Poses as a MouseAndKeyboard object in the datagraph, but accepts input from\n * user calls, rather than reading the actual mouse and keyboard from an input\n * device.  The user can write high-level code to put the mouse wherever\n * he/she wants, and to insert keypresses on demand.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.VirtualMouse' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2D76C0>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2D76C0>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2D76C0>)>'
        'pressButton': None, # (!) real value is "<method 'pressButton' of 'panda3d.core.VirtualMouse' objects>"
        'press_button': None, # (!) real value is "<method 'press_button' of 'panda3d.core.VirtualMouse' objects>"
        'releaseButton': None, # (!) real value is "<method 'releaseButton' of 'panda3d.core.VirtualMouse' objects>"
        'release_button': None, # (!) real value is "<method 'release_button' of 'panda3d.core.VirtualMouse' objects>"
        'setMouseOn': None, # (!) real value is "<method 'setMouseOn' of 'panda3d.core.VirtualMouse' objects>"
        'setMousePos': None, # (!) real value is "<method 'setMousePos' of 'panda3d.core.VirtualMouse' objects>"
        'setWindowSize': None, # (!) real value is "<method 'setWindowSize' of 'panda3d.core.VirtualMouse' objects>"
        'set_mouse_on': None, # (!) real value is "<method 'set_mouse_on' of 'panda3d.core.VirtualMouse' objects>"
        'set_mouse_pos': None, # (!) real value is "<method 'set_mouse_pos' of 'panda3d.core.VirtualMouse' objects>"
        'set_window_size': None, # (!) real value is "<method 'set_window_size' of 'panda3d.core.VirtualMouse' objects>"
    }


