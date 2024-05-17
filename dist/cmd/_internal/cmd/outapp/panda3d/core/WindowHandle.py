# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TypedReferenceCount import TypedReferenceCount

class WindowHandle(TypedReferenceCount):
    """
    /**
     * This object represents a window on the desktop, not necessarily a Panda
     * window.  This structure can be assigned to a WindowProperties to indicate a
     * parent window.
     *
     * It also has callbacks so the Panda window can communicate with its parent
     * window, which is particularly important when running embedded in a browser.
     *
     * To create a WindowHandle, you would usually call one of the
     * NativeWindowHandle::make_*() methods, depending on the kind of native
     * window handle object you already have.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getIntHandle(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_int_handle(WindowHandle self)
        
        /**
         * Returns the OS-specific handle converted to an integer, if this is possible
         * for the particular representation.  Returns 0 if it is not.
         */
        """
        pass

    def getOsHandle(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_os_handle(WindowHandle self)
        
        /**
         * Returns the OS-specific handle stored internally to the WindowHandle
         * wrapper.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_int_handle(self, WindowHandle_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_int_handle(WindowHandle self)
        
        /**
         * Returns the OS-specific handle converted to an integer, if this is possible
         * for the particular representation.  Returns 0 if it is not.
         */
        """
        pass

    def get_os_handle(self, WindowHandle_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_os_handle(WindowHandle self)
        
        /**
         * Returns the OS-specific handle stored internally to the WindowHandle
         * wrapper.
         */
        """
        pass

    def output(self, WindowHandle_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(WindowHandle self, ostream out)
        
        /**
         *
         */
        """
        pass

    def sendWindowsMessage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        send_windows_message(const WindowHandle self, int msg, int wparam, int lparam)
        
        /**
         * Call this method on a parent WindowHandle to deliver a Windows message to
         * the current child window, if any.  This is used in the web plugin system to
         * deliver button events detected directly by the browser system into Panda,
         * which is particularly necessary on Vista.
         */
        """
        pass

    def send_windows_message(self, const_WindowHandle_self, int_msg, int_wparam, int_lparam): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        send_windows_message(const WindowHandle self, int msg, int wparam, int lparam)
        
        /**
         * Call this method on a parent WindowHandle to deliver a Windows message to
         * the current child window, if any.  This is used in the web plugin system to
         * deliver button events detected directly by the browser system into Panda,
         * which is particularly necessary on Vista.
         */
        """
        pass

    def setOsHandle(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_os_handle(const WindowHandle self, OSHandle os_handle)
        
        /**
         * Changes the OS-specific handle stored internally to the WindowHandle
         * wrapper.
         */
        """
        pass

    def set_os_handle(self, const_WindowHandle_self, OSHandle_os_handle): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_os_handle(const WindowHandle self, OSHandle os_handle)
        
        /**
         * Changes the OS-specific handle stored internally to the WindowHandle
         * wrapper.
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

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    os_handle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'OSHandle': None, # (!) real value is "<class 'panda3d.core.OSHandle'>"
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.WindowHandle' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.WindowHandle' objects>"
        '__doc__': '/**\n * This object represents a window on the desktop, not necessarily a Panda\n * window.  This structure can be assigned to a WindowProperties to indicate a\n * parent window.\n *\n * It also has callbacks so the Panda window can communicate with its parent\n * window, which is particularly important when running embedded in a browser.\n *\n * To create a WindowHandle, you would usually call one of the\n * NativeWindowHandle::make_*() methods, depending on the kind of native\n * window handle object you already have.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.WindowHandle' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2DCFC0>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.WindowHandle' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.WindowHandle' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2DCFC0>)>'
        'getIntHandle': None, # (!) real value is "<method 'getIntHandle' of 'panda3d.core.WindowHandle' objects>"
        'getOsHandle': None, # (!) real value is "<method 'getOsHandle' of 'panda3d.core.WindowHandle' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2DCFC0>)>'
        'get_int_handle': None, # (!) real value is "<method 'get_int_handle' of 'panda3d.core.WindowHandle' objects>"
        'get_os_handle': None, # (!) real value is "<method 'get_os_handle' of 'panda3d.core.WindowHandle' objects>"
        'os_handle': None, # (!) real value is "<attribute 'os_handle' of 'panda3d.core.WindowHandle' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.WindowHandle' objects>"
        'sendWindowsMessage': None, # (!) real value is "<method 'sendWindowsMessage' of 'panda3d.core.WindowHandle' objects>"
        'send_windows_message': None, # (!) real value is "<method 'send_windows_message' of 'panda3d.core.WindowHandle' objects>"
        'setOsHandle': None, # (!) real value is "<method 'setOsHandle' of 'panda3d.core.WindowHandle' objects>"
        'set_os_handle': None, # (!) real value is "<method 'set_os_handle' of 'panda3d.core.WindowHandle' objects>"
    }
    OSHandle = None # (!) real value is "<class 'panda3d.core.OSHandle'>"


