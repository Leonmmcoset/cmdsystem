# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .CallbackData import CallbackData

class GraphicsWindowProcCallbackData(CallbackData):
    """
    /**
     * This specialization on CallbackData is passed when the callback is
     * initiated from from an implementation of the GraphicsWindowProc class, such
     * as PythonGraphicsWindowProc.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getHwnd(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_hwnd(GraphicsWindowProcCallbackData self)
        
        /**
         * Returns the Windows proc hwnd parameter.
         */
        """
        pass

    def getLparam(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_lparam(GraphicsWindowProcCallbackData self)
        
        /**
         * Returns the Windows proc lparam parameter.
         */
        """
        pass

    def getMsg(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_msg(GraphicsWindowProcCallbackData self)
        
        /**
         * Returns the Windows proc msg parameter.
         */
        """
        pass

    def getNumTouches(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_touches(const GraphicsWindowProcCallbackData self)
        
        /**
         * Returns the current number of touches on the window.
         *
         */
        """
        pass

    def getTouchInfo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_touch_info(const GraphicsWindowProcCallbackData self, int index)
        
        /**
         * Returns the TouchInfo object describing the specified touch.
         *
         */
        """
        pass

    def getWparam(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_wparam(GraphicsWindowProcCallbackData self)
        
        /**
         * Returns the Windows proc wparam parameter.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_hwnd(self, GraphicsWindowProcCallbackData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_hwnd(GraphicsWindowProcCallbackData self)
        
        /**
         * Returns the Windows proc hwnd parameter.
         */
        """
        pass

    def get_lparam(self, GraphicsWindowProcCallbackData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_lparam(GraphicsWindowProcCallbackData self)
        
        /**
         * Returns the Windows proc lparam parameter.
         */
        """
        pass

    def get_msg(self, GraphicsWindowProcCallbackData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_msg(GraphicsWindowProcCallbackData self)
        
        /**
         * Returns the Windows proc msg parameter.
         */
        """
        pass

    def get_num_touches(self, const_GraphicsWindowProcCallbackData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_touches(const GraphicsWindowProcCallbackData self)
        
        /**
         * Returns the current number of touches on the window.
         *
         */
        """
        pass

    def get_touch_info(self, const_GraphicsWindowProcCallbackData_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_touch_info(const GraphicsWindowProcCallbackData self, int index)
        
        /**
         * Returns the TouchInfo object describing the specified touch.
         *
         */
        """
        pass

    def get_wparam(self, GraphicsWindowProcCallbackData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_wparam(GraphicsWindowProcCallbackData self)
        
        /**
         * Returns the Windows proc wparam parameter.
         */
        """
        pass

    def isTouchEvent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_touch_event(const GraphicsWindowProcCallbackData self)
        
        /**
         * Returns whether the event is a touch event.
         *
         */
        """
        pass

    def is_touch_event(self, const_GraphicsWindowProcCallbackData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_touch_event(const GraphicsWindowProcCallbackData self)
        
        /**
         * Returns whether the event is a touch event.
         *
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
        '__doc__': '/**\n * This specialization on CallbackData is passed when the callback is\n * initiated from from an implementation of the GraphicsWindowProc class, such\n * as PythonGraphicsWindowProc.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.GraphicsWindowProcCallbackData' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2DE580>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2DE580>)>'
        'getHwnd': None, # (!) real value is "<method 'getHwnd' of 'panda3d.core.GraphicsWindowProcCallbackData' objects>"
        'getLparam': None, # (!) real value is "<method 'getLparam' of 'panda3d.core.GraphicsWindowProcCallbackData' objects>"
        'getMsg': None, # (!) real value is "<method 'getMsg' of 'panda3d.core.GraphicsWindowProcCallbackData' objects>"
        'getNumTouches': None, # (!) real value is "<method 'getNumTouches' of 'panda3d.core.GraphicsWindowProcCallbackData' objects>"
        'getTouchInfo': None, # (!) real value is "<method 'getTouchInfo' of 'panda3d.core.GraphicsWindowProcCallbackData' objects>"
        'getWparam': None, # (!) real value is "<method 'getWparam' of 'panda3d.core.GraphicsWindowProcCallbackData' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2DE580>)>'
        'get_hwnd': None, # (!) real value is "<method 'get_hwnd' of 'panda3d.core.GraphicsWindowProcCallbackData' objects>"
        'get_lparam': None, # (!) real value is "<method 'get_lparam' of 'panda3d.core.GraphicsWindowProcCallbackData' objects>"
        'get_msg': None, # (!) real value is "<method 'get_msg' of 'panda3d.core.GraphicsWindowProcCallbackData' objects>"
        'get_num_touches': None, # (!) real value is "<method 'get_num_touches' of 'panda3d.core.GraphicsWindowProcCallbackData' objects>"
        'get_touch_info': None, # (!) real value is "<method 'get_touch_info' of 'panda3d.core.GraphicsWindowProcCallbackData' objects>"
        'get_wparam': None, # (!) real value is "<method 'get_wparam' of 'panda3d.core.GraphicsWindowProcCallbackData' objects>"
        'isTouchEvent': None, # (!) real value is "<method 'isTouchEvent' of 'panda3d.core.GraphicsWindowProcCallbackData' objects>"
        'is_touch_event': None, # (!) real value is "<method 'is_touch_event' of 'panda3d.core.GraphicsWindowProcCallbackData' objects>"
    }


