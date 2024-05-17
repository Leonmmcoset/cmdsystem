# encoding: utf-8
# module panda3d.egg
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\egg.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


from .EggNode import EggNode

class EggFilenameNode(EggNode):
    """
    /**
     * This is an egg node that contains a filename.  It references a physical
     * file relative to the directory the egg file was loaded in.  It is a base
     * class for EggTexture and EggExternalReference.
     */
    """
    def assign(self, const_EggFilenameNode_self, const_EggFilenameNode_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const EggFilenameNode self, const EggFilenameNode copy)
        
        /**
         *
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getDefaultExtension(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_default_extension(EggFilenameNode self)
        
        /**
         * Returns the default extension for this filename type.
         */
        """
        pass

    def getFilename(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_filename(EggFilenameNode self)
        
        /**
         * Returns a nonmodifiable reference to the filename.
         */
        """
        pass

    def getFullpath(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_fullpath(EggFilenameNode self)
        
        /**
         * Returns the full pathname to the file, if it is known; otherwise, returns
         * the same thing as get_filename().
         *
         * This function simply returns whatever was set by the last call to
         * set_fullpath().  This string is not written to the egg file; its main
         * purpose is to record the full path to a filename (for instance, a texture
         * filename) if it is known, for egg structures that are generated in-memory
         * and then immediately converted to a scene graph.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_default_extension(self, EggFilenameNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_default_extension(EggFilenameNode self)
        
        /**
         * Returns the default extension for this filename type.
         */
        """
        pass

    def get_filename(self, EggFilenameNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_filename(EggFilenameNode self)
        
        /**
         * Returns a nonmodifiable reference to the filename.
         */
        """
        pass

    def get_fullpath(self, EggFilenameNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_fullpath(EggFilenameNode self)
        
        /**
         * Returns the full pathname to the file, if it is known; otherwise, returns
         * the same thing as get_filename().
         *
         * This function simply returns whatever was set by the last call to
         * set_fullpath().  This string is not written to the egg file; its main
         * purpose is to record the full path to a filename (for instance, a texture
         * filename) if it is known, for egg structures that are generated in-memory
         * and then immediately converted to a scene graph.
         */
        """
        pass

    def setFilename(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_filename(const EggFilenameNode self, const Filename filename)
        
        /**
         *
         */
        """
        pass

    def setFullpath(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_fullpath(const EggFilenameNode self, const Filename fullpath)
        
        /**
         * Records the full pathname to the file, for the benefit of get_fullpath().
         */
        """
        pass

    def set_filename(self, const_EggFilenameNode_self, const_Filename_filename): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_filename(const EggFilenameNode self, const Filename filename)
        
        /**
         *
         */
        """
        pass

    def set_fullpath(self, const_EggFilenameNode_self, const_Filename_fullpath): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_fullpath(const EggFilenameNode self, const Filename fullpath)
        
        /**
         * Records the full pathname to the file, for the benefit of get_fullpath().
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
        '__doc__': '/**\n * This is an egg node that contains a filename.  It references a physical\n * file relative to the directory the egg file was loaded in.  It is a base\n * class for EggTexture and EggExternalReference.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.egg.EggFilenameNode' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC68CE9F0>'
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.egg.EggFilenameNode' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFDC68CE9F0>)>'
        'getDefaultExtension': None, # (!) real value is "<method 'getDefaultExtension' of 'panda3d.egg.EggFilenameNode' objects>"
        'getFilename': None, # (!) real value is "<method 'getFilename' of 'panda3d.egg.EggFilenameNode' objects>"
        'getFullpath': None, # (!) real value is "<method 'getFullpath' of 'panda3d.egg.EggFilenameNode' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFDC68CE9F0>)>'
        'get_default_extension': None, # (!) real value is "<method 'get_default_extension' of 'panda3d.egg.EggFilenameNode' objects>"
        'get_filename': None, # (!) real value is "<method 'get_filename' of 'panda3d.egg.EggFilenameNode' objects>"
        'get_fullpath': None, # (!) real value is "<method 'get_fullpath' of 'panda3d.egg.EggFilenameNode' objects>"
        'setFilename': None, # (!) real value is "<method 'setFilename' of 'panda3d.egg.EggFilenameNode' objects>"
        'setFullpath': None, # (!) real value is "<method 'setFullpath' of 'panda3d.egg.EggFilenameNode' objects>"
        'set_filename': None, # (!) real value is "<method 'set_filename' of 'panda3d.egg.EggFilenameNode' objects>"
        'set_fullpath': None, # (!) real value is "<method 'set_fullpath' of 'panda3d.egg.EggFilenameNode' objects>"
    }


