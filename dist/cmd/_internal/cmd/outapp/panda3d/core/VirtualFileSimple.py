# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .VirtualFile import VirtualFile

class VirtualFileSimple(VirtualFile):
    """
    /**
     * A simple file or directory within the VirtualFileSystem: this maps to
     * exactly one file on one mount point.  Most directories, and all regular
     * files, are of this kind.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getMount(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_mount(VirtualFileSimple self)
        
        /**
         * Returns the VirtualFileMount this file is associated with.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_mount(self, VirtualFileSimple_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_mount(VirtualFileSimple self)
        
        /**
         * Returns the VirtualFileMount this file is associated with.
         */
        """
        pass

    def isImplicitPzFile(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_implicit_pz_file(VirtualFileSimple self)
        
        /**
         * Returns true if this file is a .pz file that should be implicitly
         * decompressed on load, or false if it is not a .pz file or if it should not
         * be decompressed.
         */
        """
        pass

    def is_implicit_pz_file(self, VirtualFileSimple_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_implicit_pz_file(VirtualFileSimple self)
        
        /**
         * Returns true if this file is a .pz file that should be implicitly
         * decompressed on load, or false if it is not a .pz file or if it should not
         * be decompressed.
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
        '__doc__': '/**\n * A simple file or directory within the VirtualFileSystem: this maps to\n * exactly one file on one mount point.  Most directories, and all regular\n * files, are of this kind.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.VirtualFileSimple' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE27A130>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE27A130>)>'
        'getMount': None, # (!) real value is "<method 'getMount' of 'panda3d.core.VirtualFileSimple' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE27A130>)>'
        'get_mount': None, # (!) real value is "<method 'get_mount' of 'panda3d.core.VirtualFileSimple' objects>"
        'isImplicitPzFile': None, # (!) real value is "<method 'isImplicitPzFile' of 'panda3d.core.VirtualFileSimple' objects>"
        'is_implicit_pz_file': None, # (!) real value is "<method 'is_implicit_pz_file' of 'panda3d.core.VirtualFileSimple' objects>"
    }


