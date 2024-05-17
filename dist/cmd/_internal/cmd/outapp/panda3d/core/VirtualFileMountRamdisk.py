# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .VirtualFileMount import VirtualFileMount

class VirtualFileMountRamdisk(VirtualFileMount):
    """
    /**
     * Simulates an actual directory on disk with in-memory storage.  This is
     * useful mainly for performing high level functions that expect disk I/O
     * without actually writing files to disk.  Naturally, there are significant
     * limits to the size of the files that may be written with this system; and
     * "files" written here are not automatically persistent between sessions.
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

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * Simulates an actual directory on disk with in-memory storage.  This is\n * useful mainly for performing high level functions that expect disk I/O\n * without actually writing files to disk.  Naturally, there are significant\n * limits to the size of the files that may be written with this system; and\n * "files" written here are not automatically persistent between sessions.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.VirtualFileMountRamdisk' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE279D90>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE279D90>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE279D90>)>'
    }


