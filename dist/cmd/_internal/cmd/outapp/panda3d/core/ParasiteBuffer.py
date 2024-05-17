# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .GraphicsOutput import GraphicsOutput

class ParasiteBuffer(GraphicsOutput):
    """
    /**
     * This is a special GraphicsOutput type that acts a lot like a
     * GraphicsBuffer, effectively allowing rendering to an offscreen buffer,
     * except it does not create any framebuffer space for itself.  Instead, it
     * renders into the framebuffer owned by some other GraphicsOutput.
     *
     * The x_size and y_size must therefore fit within the bounds of the source
     * GraphicsOutput.
     *
     * Since the framebuffer will be subsequently cleared when the actual owner
     * draws in it later, this only makes sense if we are going to copy the
     * contents of the framebuffer to a texture immediately after we draw it.
     * Thus, has_texture() is implicitly true for a ParasiteBuffer.
     *
     * This class is useful to render offscreen to a texture while preventing the
     * waste of framebuffer memory for API's that are unable to render directly
     * into a texture (and must render into a separate framebuffer first and then
     * copy to texture).  It is also the only way to render to a texture on API's
     * that do not support offscreen rendering.
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

    def setSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_size(const ParasiteBuffer self, int x, int y)
        
        /**
         * This is called by the GraphicsEngine to request that the buffer resize
         * itself.  Although calls to get the size will return the new value, much of
         * the actual resizing work doesn't take place until the next begin_frame.
         * Not all buffers are resizeable.
         */
        """
        pass

    def set_size(self, const_ParasiteBuffer_self, int_x, int_y): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_size(const ParasiteBuffer self, int x, int y)
        
        /**
         * This is called by the GraphicsEngine to request that the buffer resize
         * itself.  Although calls to get the size will return the new value, much of
         * the actual resizing work doesn't take place until the next begin_frame.
         * Not all buffers are resizeable.
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
        '__doc__': "/**\n * This is a special GraphicsOutput type that acts a lot like a\n * GraphicsBuffer, effectively allowing rendering to an offscreen buffer,\n * except it does not create any framebuffer space for itself.  Instead, it\n * renders into the framebuffer owned by some other GraphicsOutput.\n *\n * The x_size and y_size must therefore fit within the bounds of the source\n * GraphicsOutput.\n *\n * Since the framebuffer will be subsequently cleared when the actual owner\n * draws in it later, this only makes sense if we are going to copy the\n * contents of the framebuffer to a texture immediately after we draw it.\n * Thus, has_texture() is implicitly true for a ParasiteBuffer.\n *\n * This class is useful to render offscreen to a texture while preventing the\n * waste of framebuffer memory for API's that are unable to render directly\n * into a texture (and must render into a separate framebuffer first and then\n * copy to texture).  It is also the only way to render to a texture on API's\n * that do not support offscreen rendering.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.ParasiteBuffer' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2E00B0>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2E00B0>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2E00B0>)>'
        'setSize': None, # (!) real value is "<method 'setSize' of 'panda3d.core.ParasiteBuffer' objects>"
        'set_size': None, # (!) real value is "<method 'set_size' of 'panda3d.core.ParasiteBuffer' objects>"
    }


