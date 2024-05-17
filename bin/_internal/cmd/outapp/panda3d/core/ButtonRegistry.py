# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class ButtonRegistry(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * The ButtonRegistry class maintains all the assigned ButtonHandles in a
     * given system.  There should be only one ButtonRegistry class during the
     * lifetime of the application.
     */
    """
    def findAsciiButton(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        find_ascii_button(ButtonRegistry self, char ascii_equivalent)
        
        /**
         * Finds a ButtonHandle in the registry matching the indicated ASCII
         * equivalent character.  If there is no such ButtonHandle, returns
         * ButtonHandle::none().
         */
        """
        pass

    def findButton(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        find_button(const ButtonRegistry self, str name)
        
        /**
         * Finds a ButtonHandle in the registry matching the indicated name.  If there
         * is no such ButtonHandle, returns ButtonHandle::none().
         */
        """
        pass

    def find_ascii_button(self, ButtonRegistry_self, char_ascii_equivalent): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        find_ascii_button(ButtonRegistry self, char ascii_equivalent)
        
        /**
         * Finds a ButtonHandle in the registry matching the indicated ASCII
         * equivalent character.  If there is no such ButtonHandle, returns
         * ButtonHandle::none().
         */
        """
        pass

    def find_button(self, const_ButtonRegistry_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        find_button(const ButtonRegistry self, str name)
        
        /**
         * Finds a ButtonHandle in the registry matching the indicated name.  If there
         * is no such ButtonHandle, returns ButtonHandle::none().
         */
        """
        pass

    def getButton(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_button(const ButtonRegistry self, str name)
        
        /**
         * Finds a ButtonHandle in the registry matching the indicated name.  If there
         * is no such ButtonHandle, registers a new one and returns it.
         */
        """
        pass

    def get_button(self, const_ButtonRegistry_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_button(const ButtonRegistry self, str name)
        
        /**
         * Finds a ButtonHandle in the registry matching the indicated name.  If there
         * is no such ButtonHandle, registers a new one and returns it.
         */
        """
        pass

    def ptr(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        ptr()
        
        // ptr() returns the pointer to the global ButtonRegistry object.
        
        /**
         * Returns the pointer to the global ButtonRegistry object.
         */
        """
        pass

    def write(self, ButtonRegistry_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(ButtonRegistry self, ostream out)
        
        /**
         *
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

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.ButtonRegistry' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.ButtonRegistry' objects>"
        '__doc__': '/**\n * The ButtonRegistry class maintains all the assigned ButtonHandles in a\n * given system.  There should be only one ButtonRegistry class during the\n * lifetime of the application.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.ButtonRegistry' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE370CC0>'
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.ButtonRegistry' objects>"
        'findAsciiButton': None, # (!) real value is "<method 'findAsciiButton' of 'panda3d.core.ButtonRegistry' objects>"
        'findButton': None, # (!) real value is "<method 'findButton' of 'panda3d.core.ButtonRegistry' objects>"
        'find_ascii_button': None, # (!) real value is "<method 'find_ascii_button' of 'panda3d.core.ButtonRegistry' objects>"
        'find_button': None, # (!) real value is "<method 'find_button' of 'panda3d.core.ButtonRegistry' objects>"
        'getButton': None, # (!) real value is "<method 'getButton' of 'panda3d.core.ButtonRegistry' objects>"
        'get_button': None, # (!) real value is "<method 'get_button' of 'panda3d.core.ButtonRegistry' objects>"
        'ptr': None, # (!) real value is '<staticmethod(<built-in method ptr of type object at 0x00007FFCFE370CC0>)>'
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.ButtonRegistry' objects>"
    }


