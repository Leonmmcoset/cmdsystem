# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .WindowHandle import WindowHandle

class NativeWindowHandle(WindowHandle):
    """
    /**
     * This subclass of WindowHandle exists to allow simple creation of a
     * WindowHandle of the appropriate type to the current OS.
     *
     * This class exists for name scoping only.  Don't use the constructor
     * directly; use one of the make_* methods.
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

    def makeInt(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_int(int window)
        
        /**
         * Constructs a new WindowHandle with an int value, which is understood to be
         * either an HWND or a Window, cast to int.  This method exists for the
         * convenience of Python, which likes to deal with ints; C++ code should use
         * one of the more specific make_x11() or make_win32() methods instead.
         */
        """
        pass

    def makeSubprocess(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_subprocess(const Filename filename)
        
        /**
         * Constructs a new WindowHandle that references a SubprocessWindowBuffer read
         * in another process, with the named pipe filename that it uses for
         * communication.
         *
         * This is (at present, and maybe always) useful only on the OS X platform,
         * where parenting child windows is particularly problematic.
         */
        """
        pass

    def make_int(self, int_window): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_int(int window)
        
        /**
         * Constructs a new WindowHandle with an int value, which is understood to be
         * either an HWND or a Window, cast to int.  This method exists for the
         * convenience of Python, which likes to deal with ints; C++ code should use
         * one of the more specific make_x11() or make_win32() methods instead.
         */
        """
        pass

    def make_subprocess(self, const_Filename_filename): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_subprocess(const Filename filename)
        
        /**
         * Constructs a new WindowHandle that references a SubprocessWindowBuffer read
         * in another process, with the named pipe filename that it uses for
         * communication.
         *
         * This is (at present, and maybe always) useful only on the OS X platform,
         * where parenting child windows is particularly problematic.
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
        '__doc__': "/**\n * This subclass of WindowHandle exists to allow simple creation of a\n * WindowHandle of the appropriate type to the current OS.\n *\n * This class exists for name scoping only.  Don't use the constructor\n * directly; use one of the make_* methods.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.NativeWindowHandle' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2DFEE0>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2DFEE0>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2DFEE0>)>'
        'makeInt': None, # (!) real value is '<staticmethod(<built-in method makeInt of type object at 0x00007FFCFE2DFEE0>)>'
        'makeSubprocess': None, # (!) real value is '<staticmethod(<built-in method makeSubprocess of type object at 0x00007FFCFE2DFEE0>)>'
        'make_int': None, # (!) real value is '<staticmethod(<built-in method make_int of type object at 0x00007FFCFE2DFEE0>)>'
        'make_subprocess': None, # (!) real value is '<staticmethod(<built-in method make_subprocess of type object at 0x00007FFCFE2DFEE0>)>'
    }


