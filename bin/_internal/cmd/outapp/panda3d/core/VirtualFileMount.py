# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TypedReferenceCount import TypedReferenceCount

class VirtualFileMount(TypedReferenceCount):
    """
    /**
     * The abstract base class for a mount definition used within a
     * VirtualFileSystem.  Normally users don't need to monkey with this class
     * directly.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getFileSystem(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_file_system(VirtualFileMount self)
        
        /**
         * Returns the file system this mount object is attached to.
         */
        """
        pass

    def getMountFlags(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_mount_flags(VirtualFileMount self)
        
        /**
         * Returns the set of flags passed by the user to the
         * VirtualFileSystem::mount() command.
         */
        """
        pass

    def getMountPoint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_mount_point(VirtualFileMount self)
        
        /**
         * Returns the name of the directory within the virtual file system that this
         * mount object is attached to.  This directory name will end with a slash.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_file_system(self, VirtualFileMount_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_file_system(VirtualFileMount self)
        
        /**
         * Returns the file system this mount object is attached to.
         */
        """
        pass

    def get_mount_flags(self, VirtualFileMount_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_mount_flags(VirtualFileMount self)
        
        /**
         * Returns the set of flags passed by the user to the
         * VirtualFileSystem::mount() command.
         */
        """
        pass

    def get_mount_point(self, VirtualFileMount_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_mount_point(VirtualFileMount self)
        
        /**
         * Returns the name of the directory within the virtual file system that this
         * mount object is attached to.  This directory name will end with a slash.
         */
        """
        pass

    def output(self, VirtualFileMount_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(VirtualFileMount self, ostream out)
        
        /**
         *
         */
        """
        pass

    def write(self, VirtualFileMount_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(VirtualFileMount self, ostream out)
        
        /**
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

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': "/**\n * The abstract base class for a mount definition used within a\n * VirtualFileSystem.  Normally users don't need to monkey with this class\n * directly.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.VirtualFileMount' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2799F0>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.VirtualFileMount' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.VirtualFileMount' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2799F0>)>'
        'getFileSystem': None, # (!) real value is "<method 'getFileSystem' of 'panda3d.core.VirtualFileMount' objects>"
        'getMountFlags': None, # (!) real value is "<method 'getMountFlags' of 'panda3d.core.VirtualFileMount' objects>"
        'getMountPoint': None, # (!) real value is "<method 'getMountPoint' of 'panda3d.core.VirtualFileMount' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2799F0>)>'
        'get_file_system': None, # (!) real value is "<method 'get_file_system' of 'panda3d.core.VirtualFileMount' objects>"
        'get_mount_flags': None, # (!) real value is "<method 'get_mount_flags' of 'panda3d.core.VirtualFileMount' objects>"
        'get_mount_point': None, # (!) real value is "<method 'get_mount_point' of 'panda3d.core.VirtualFileMount' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.VirtualFileMount' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.VirtualFileMount' objects>"
    }


