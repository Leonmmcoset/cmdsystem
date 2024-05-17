# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .VirtualFileMount import VirtualFileMount

class VirtualFileMountSystem(VirtualFileMount):
    """
    /**
     * Maps an actual OS directory into the VirtualFileSystem.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getPhysicalFilename(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_physical_filename(VirtualFileMountSystem self)
        
        /**
         * Returns the name of the source file on the OS filesystem of the directory
         * or file that is mounted.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_physical_filename(self, VirtualFileMountSystem_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_physical_filename(VirtualFileMountSystem self)
        
        /**
         * Returns the name of the source file on the OS filesystem of the directory
         * or file that is mounted.
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
        '__doc__': '/**\n * Maps an actual OS directory into the VirtualFileSystem.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.VirtualFileMountSystem' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE279F60>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE279F60>)>'
        'getPhysicalFilename': None, # (!) real value is "<method 'getPhysicalFilename' of 'panda3d.core.VirtualFileMountSystem' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE279F60>)>'
        'get_physical_filename': None, # (!) real value is "<method 'get_physical_filename' of 'panda3d.core.VirtualFileMountSystem' objects>"
    }


