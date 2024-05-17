# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TypedWritableReferenceCount import TypedWritableReferenceCount

class VertexSlider(TypedWritableReferenceCount):
    """
    /**
     * This is an abstract base class that retains some slider value, which is a
     * linear value that typically ranges from 0.0 to 1.0, and is used to control
     * the animation of morphs (blend shapes).
     *
     * It is similar to VertexTransform, which keeps a full 4x4 transform matrix,
     * but the VertexSlider only keeps a single float value.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getModified(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_modified(VertexSlider self, Thread current_thread)
        
        /**
         * Returns a sequence number that's guaranteed to change at least every time
         * the value reported by get_slider() changes.
         */
        """
        pass

    def getName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_name(VertexSlider self)
        
        /**
         * Returns the name of this particular slider.  Every unique blend shape
         * within a particular Geom must be identified with a different name, which is
         * shared by the slider that controls it.
         */
        """
        pass

    def getSlider(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_slider(VertexSlider self)
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_modified(self, VertexSlider_self, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_modified(VertexSlider self, Thread current_thread)
        
        /**
         * Returns a sequence number that's guaranteed to change at least every time
         * the value reported by get_slider() changes.
         */
        """
        pass

    def get_name(self, VertexSlider_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_name(VertexSlider self)
        
        /**
         * Returns the name of this particular slider.  Every unique blend shape
         * within a particular Geom must be identified with a different name, which is
         * shared by the slider that controls it.
         */
        """
        pass

    def get_slider(self, VertexSlider_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_slider(VertexSlider self)
        """
        pass

    def output(self, VertexSlider_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(VertexSlider self, ostream out)
        
        /**
         *
         */
        """
        pass

    def write(self, VertexSlider_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(VertexSlider self, ostream out, int indent_level)
        
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

    modified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    slider = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * This is an abstract base class that retains some slider value, which is a\n * linear value that typically ranges from 0.0 to 1.0, and is used to control\n * the animation of morphs (blend shapes).\n *\n * It is similar to VertexTransform, which keeps a full 4x4 transform matrix,\n * but the VertexSlider only keeps a single float value.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.VertexSlider' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2FBFF0>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.VertexSlider' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.VertexSlider' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2FBFF0>)>'
        'getModified': None, # (!) real value is "<method 'getModified' of 'panda3d.core.VertexSlider' objects>"
        'getName': None, # (!) real value is "<method 'getName' of 'panda3d.core.VertexSlider' objects>"
        'getSlider': None, # (!) real value is "<method 'getSlider' of 'panda3d.core.VertexSlider' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2FBFF0>)>'
        'get_modified': None, # (!) real value is "<method 'get_modified' of 'panda3d.core.VertexSlider' objects>"
        'get_name': None, # (!) real value is "<method 'get_name' of 'panda3d.core.VertexSlider' objects>"
        'get_slider': None, # (!) real value is "<method 'get_slider' of 'panda3d.core.VertexSlider' objects>"
        'modified': None, # (!) real value is "<attribute 'modified' of 'panda3d.core.VertexSlider' objects>"
        'name': None, # (!) real value is "<attribute 'name' of 'panda3d.core.VertexSlider' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.VertexSlider' objects>"
        'slider': None, # (!) real value is "<attribute 'slider' of 'panda3d.core.VertexSlider' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.VertexSlider' objects>"
    }


