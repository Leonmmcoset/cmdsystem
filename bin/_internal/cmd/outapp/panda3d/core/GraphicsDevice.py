# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TypedReferenceCount import TypedReferenceCount

class GraphicsDevice(TypedReferenceCount):
    """
    /**
     * An abstract device object that is part of Graphics Pipe.  This device is
     * set to NULL for OpenGL. But DirectX uses it to take control of multiple
     * windows under single device or multiple devices (i.e.  more than one
     * adapters in the machine).
     *
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getPipe(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_pipe(GraphicsDevice self)
        
        /**
         * Returns the GraphicsPipe that this device is associated with.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_pipe(self, GraphicsDevice_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_pipe(GraphicsDevice self)
        
        /**
         * Returns the GraphicsPipe that this device is associated with.
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
        '__doc__': '/**\n * An abstract device object that is part of Graphics Pipe.  This device is\n * set to NULL for OpenGL. But DirectX uses it to take control of multiple\n * windows under single device or multiple devices (i.e.  more than one\n * adapters in the machine).\n *\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.GraphicsDevice' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2DC880>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2DC880>)>'
        'getPipe': None, # (!) real value is "<method 'getPipe' of 'panda3d.core.GraphicsDevice' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2DC880>)>'
        'get_pipe': None, # (!) real value is "<method 'get_pipe' of 'panda3d.core.GraphicsDevice' objects>"
    }


