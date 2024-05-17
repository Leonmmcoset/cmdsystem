# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .RenderEffect import RenderEffect

class ShowBoundsEffect(RenderEffect):
    """
    /**
     * Applied to a GeomNode to cause a visible bounding volume to be drawn for
     * this node.  This is generally used only during development to help identify
     * bounding volume issues.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getTight(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_tight(ShowBoundsEffect self)
        
        /**
         * Returns true if the "tight" flag was set, meaning the effect should compute
         * and draw the tight bounding-box of the node's vertices every frame.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_tight(self, ShowBoundsEffect_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_tight(ShowBoundsEffect self)
        
        /**
         * Returns true if the "tight" flag was set, meaning the effect should compute
         * and draw the tight bounding-box of the node's vertices every frame.
         */
        """
        pass

    def make(self, bool_tight): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make(bool tight)
        
        /**
         * Constructs a new ShowBoundsEffect object.
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
        '__doc__': '/**\n * Applied to a GeomNode to cause a visible bounding volume to be drawn for\n * this node.  This is generally used only during development to help identify\n * bounding volume issues.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.ShowBoundsEffect' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE29A390>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE29A390>)>'
        'getTight': None, # (!) real value is "<method 'getTight' of 'panda3d.core.ShowBoundsEffect' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE29A390>)>'
        'get_tight': None, # (!) real value is "<method 'get_tight' of 'panda3d.core.ShowBoundsEffect' objects>"
        'make': None, # (!) real value is '<staticmethod(<built-in method make of type object at 0x00007FFCFE29A390>)>'
    }


