# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .InputDevice import InputDevice

class GraphicsWindowInputDevice(InputDevice):
    """
    /**
     * This is a virtual input device that represents the keyboard and mouse pair
     * that is associated with a particular window.  It collects mouse and
     * keyboard events from the windowing system while the window is in focus.
     */
    """
    def buttonDown(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        button_down(const GraphicsWindowInputDevice self, ButtonHandle button, double time)
        
        // The following interface is for the various kinds of GraphicsWindows to
        // record the data incoming on the device.
        
        /**
         * Records that the indicated button has been depressed.
         */
        """
        pass

    def buttonResumeDown(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        button_resume_down(const GraphicsWindowInputDevice self, ButtonHandle button, double time)
        
        /**
         * Records that the indicated button was depressed earlier, and we only just
         * detected the event after the fact.  This is mainly useful for tracking the
         * state of modifier keys.
         */
        """
        pass

    def buttonUp(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        button_up(const GraphicsWindowInputDevice self, ButtonHandle button, double time)
        
        /**
         * Records that the indicated button has been released.
         */
        """
        pass

    def button_down(self, const_GraphicsWindowInputDevice_self, ButtonHandle_button, double_time): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        button_down(const GraphicsWindowInputDevice self, ButtonHandle button, double time)
        
        // The following interface is for the various kinds of GraphicsWindows to
        // record the data incoming on the device.
        
        /**
         * Records that the indicated button has been depressed.
         */
        """
        pass

    def button_resume_down(self, const_GraphicsWindowInputDevice_self, ButtonHandle_button, double_time): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        button_resume_down(const GraphicsWindowInputDevice self, ButtonHandle button, double time)
        
        /**
         * Records that the indicated button was depressed earlier, and we only just
         * detected the event after the fact.  This is mainly useful for tracking the
         * state of modifier keys.
         */
        """
        pass

    def button_up(self, const_GraphicsWindowInputDevice_self, ButtonHandle_button, double_time): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        button_up(const GraphicsWindowInputDevice self, ButtonHandle button, double time)
        
        /**
         * Records that the indicated button has been released.
         */
        """
        pass

    def candidate(self, const_GraphicsWindowInputDevice_self, unicode_candidate_string, int_highlight_start, int_highlight_end, int_cursor_pos): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        candidate(const GraphicsWindowInputDevice self, unicode candidate_string, int highlight_start, int highlight_end, int cursor_pos)
        
        /**
         * Records that the indicated candidate string has been highlighted.  This is
         * used to implement IME support for typing in international languages,
         * especially Chinese/Japanese/Korean.
         */
        """
        pass

    def focusLost(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        focus_lost(const GraphicsWindowInputDevice self, double time)
        
        /**
         * This should be called when the window focus is lost, so that we may miss
         * upcoming button events (especially "up" events) for the next period of
         * time.  It generates keyboard and mouse "up" events for those buttons that
         * we previously sent unpaired "down" events, so that the Panda application
         * will believe all buttons are now released.
         */
        """
        pass

    def focus_lost(self, const_GraphicsWindowInputDevice_self, double_time): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        focus_lost(const GraphicsWindowInputDevice self, double time)
        
        /**
         * This should be called when the window focus is lost, so that we may miss
         * upcoming button events (especially "up" events) for the next period of
         * time.  It generates keyboard and mouse "up" events for those buttons that
         * we previously sent unpaired "down" events, so that the Panda application
         * will believe all buttons are now released.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getPointer(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_pointer(GraphicsWindowInputDevice self)
        
        /**
         * Returns the PointerData associated with the input device's pointer.  This
         * only makes sense if has_pointer() also returns true.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_pointer(self, GraphicsWindowInputDevice_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_pointer(GraphicsWindowInputDevice self)
        
        /**
         * Returns the PointerData associated with the input device's pointer.  This
         * only makes sense if has_pointer() also returns true.
         */
        """
        pass

    def keystroke(self, const_GraphicsWindowInputDevice_self, int_keycode, double_time): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        keystroke(const GraphicsWindowInputDevice self, int keycode, double time)
        
        /**
         * Records that the indicated keystroke has been generated.
         */
        """
        pass

    def pointerMoved(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        pointer_moved(const GraphicsWindowInputDevice self, double x, double y, double time)
        
        /**
         * To be called by a particular kind of GraphicsWindow to indicate that the
         * pointer has moved by the given relative amount.
         */
        """
        pass

    def pointer_moved(self, const_GraphicsWindowInputDevice_self, double_x, double_y, double_time): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        pointer_moved(const GraphicsWindowInputDevice self, double x, double y, double time)
        
        /**
         * To be called by a particular kind of GraphicsWindow to indicate that the
         * pointer has moved by the given relative amount.
         */
        """
        pass

    def rawButtonDown(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        raw_button_down(const GraphicsWindowInputDevice self, ButtonHandle button, double time)
        
        /**
         * Records that the indicated button has been depressed.
         */
        """
        pass

    def rawButtonUp(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        raw_button_up(const GraphicsWindowInputDevice self, ButtonHandle button, double time)
        
        /**
         * Records that the indicated button has been released.
         */
        """
        pass

    def raw_button_down(self, const_GraphicsWindowInputDevice_self, ButtonHandle_button, double_time): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        raw_button_down(const GraphicsWindowInputDevice self, ButtonHandle button, double time)
        
        /**
         * Records that the indicated button has been depressed.
         */
        """
        pass

    def raw_button_up(self, const_GraphicsWindowInputDevice_self, ButtonHandle_button, double_time): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        raw_button_up(const GraphicsWindowInputDevice self, ButtonHandle button, double time)
        
        /**
         * Records that the indicated button has been released.
         */
        """
        pass

    def removePointer(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_pointer(const GraphicsWindowInputDevice self, int id)
        
        /**
         * To be called by a particular kind of GraphicsWindow to indicate that the
         * pointer no longer exists.
         */
        """
        pass

    def remove_pointer(self, const_GraphicsWindowInputDevice_self, int_id): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_pointer(const GraphicsWindowInputDevice self, int id)
        
        /**
         * To be called by a particular kind of GraphicsWindow to indicate that the
         * pointer no longer exists.
         */
        """
        pass

    def setPointerInWindow(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_pointer_in_window(const GraphicsWindowInputDevice self, double x, double y, double time)
        
        /**
         * To be called by a particular kind of GraphicsWindow to indicate that the
         * pointer is within the window, at the given pixel coordinates.
         */
        """
        pass

    def setPointerOutOfWindow(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_pointer_out_of_window(const GraphicsWindowInputDevice self, double time)
        
        /**
         * To be called by a particular kind of GraphicsWindow to indicate that the
         * pointer is no longer within the window.
         */
        """
        pass

    def set_pointer_in_window(self, const_GraphicsWindowInputDevice_self, double_x, double_y, double_time): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_pointer_in_window(const GraphicsWindowInputDevice self, double x, double y, double time)
        
        /**
         * To be called by a particular kind of GraphicsWindow to indicate that the
         * pointer is within the window, at the given pixel coordinates.
         */
        """
        pass

    def set_pointer_out_of_window(self, const_GraphicsWindowInputDevice_self, double_time): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_pointer_out_of_window(const GraphicsWindowInputDevice self, double time)
        
        /**
         * To be called by a particular kind of GraphicsWindow to indicate that the
         * pointer is no longer within the window.
         */
        """
        pass

    def updatePointer(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        update_pointer(const GraphicsWindowInputDevice self, PointerData data, double time)
        
        /**
         * To be called by a particular kind of GraphicsWindow to indicate that the
         * pointer data has changed.
         */
        """
        pass

    def update_pointer(self, const_GraphicsWindowInputDevice_self, PointerData_data, double_time): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        update_pointer(const GraphicsWindowInputDevice self, PointerData data, double time)
        
        /**
         * To be called by a particular kind of GraphicsWindow to indicate that the
         * pointer data has changed.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * This is a virtual input device that represents the keyboard and mouse pair\n * that is associated with a particular window.  It collects mouse and\n * keyboard events from the windowing system while the window is in focus.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.GraphicsWindowInputDevice' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2DE1E0>'
        'buttonDown': None, # (!) real value is "<method 'buttonDown' of 'panda3d.core.GraphicsWindowInputDevice' objects>"
        'buttonResumeDown': None, # (!) real value is "<method 'buttonResumeDown' of 'panda3d.core.GraphicsWindowInputDevice' objects>"
        'buttonUp': None, # (!) real value is "<method 'buttonUp' of 'panda3d.core.GraphicsWindowInputDevice' objects>"
        'button_down': None, # (!) real value is "<method 'button_down' of 'panda3d.core.GraphicsWindowInputDevice' objects>"
        'button_resume_down': None, # (!) real value is "<method 'button_resume_down' of 'panda3d.core.GraphicsWindowInputDevice' objects>"
        'button_up': None, # (!) real value is "<method 'button_up' of 'panda3d.core.GraphicsWindowInputDevice' objects>"
        'candidate': None, # (!) real value is "<method 'candidate' of 'panda3d.core.GraphicsWindowInputDevice' objects>"
        'focusLost': None, # (!) real value is "<method 'focusLost' of 'panda3d.core.GraphicsWindowInputDevice' objects>"
        'focus_lost': None, # (!) real value is "<method 'focus_lost' of 'panda3d.core.GraphicsWindowInputDevice' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2DE1E0>)>'
        'getPointer': None, # (!) real value is "<method 'getPointer' of 'panda3d.core.GraphicsWindowInputDevice' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2DE1E0>)>'
        'get_pointer': None, # (!) real value is "<method 'get_pointer' of 'panda3d.core.GraphicsWindowInputDevice' objects>"
        'keystroke': None, # (!) real value is "<method 'keystroke' of 'panda3d.core.GraphicsWindowInputDevice' objects>"
        'pointerMoved': None, # (!) real value is "<method 'pointerMoved' of 'panda3d.core.GraphicsWindowInputDevice' objects>"
        'pointer_moved': None, # (!) real value is "<method 'pointer_moved' of 'panda3d.core.GraphicsWindowInputDevice' objects>"
        'rawButtonDown': None, # (!) real value is "<method 'rawButtonDown' of 'panda3d.core.GraphicsWindowInputDevice' objects>"
        'rawButtonUp': None, # (!) real value is "<method 'rawButtonUp' of 'panda3d.core.GraphicsWindowInputDevice' objects>"
        'raw_button_down': None, # (!) real value is "<method 'raw_button_down' of 'panda3d.core.GraphicsWindowInputDevice' objects>"
        'raw_button_up': None, # (!) real value is "<method 'raw_button_up' of 'panda3d.core.GraphicsWindowInputDevice' objects>"
        'removePointer': None, # (!) real value is "<method 'removePointer' of 'panda3d.core.GraphicsWindowInputDevice' objects>"
        'remove_pointer': None, # (!) real value is "<method 'remove_pointer' of 'panda3d.core.GraphicsWindowInputDevice' objects>"
        'setPointerInWindow': None, # (!) real value is "<method 'setPointerInWindow' of 'panda3d.core.GraphicsWindowInputDevice' objects>"
        'setPointerOutOfWindow': None, # (!) real value is "<method 'setPointerOutOfWindow' of 'panda3d.core.GraphicsWindowInputDevice' objects>"
        'set_pointer_in_window': None, # (!) real value is "<method 'set_pointer_in_window' of 'panda3d.core.GraphicsWindowInputDevice' objects>"
        'set_pointer_out_of_window': None, # (!) real value is "<method 'set_pointer_out_of_window' of 'panda3d.core.GraphicsWindowInputDevice' objects>"
        'updatePointer': None, # (!) real value is "<method 'updatePointer' of 'panda3d.core.GraphicsWindowInputDevice' objects>"
        'update_pointer': None, # (!) real value is "<method 'update_pointer' of 'panda3d.core.GraphicsWindowInputDevice' objects>"
    }


