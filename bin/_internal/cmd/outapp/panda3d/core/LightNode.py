# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .Light import Light

from .PandaNode import PandaNode

class LightNode(Light, PandaNode):
    """
    /**
     * A derivative of Light and of PandaNode.  All kinds of Light except
     * Spotlight (which must inherit from LensNode instead) inherit from this
     * class.
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

    def output(self, LightNode_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(LightNode self, ostream out)
        
        // We have to explicitly publish these because they resolve the multiple
        // inheritance.
        
        /**
         *
         */
        """
        pass

    def upcastToLight(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_Light(const LightNode self)
        
        upcast from LightNode to Light
        """
        pass

    def upcastToPandaNode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_PandaNode(const LightNode self)
        
        upcast from LightNode to PandaNode
        """
        pass

    def upcast_to_Light(self, const_LightNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_Light(const LightNode self)
        
        upcast from LightNode to Light
        """
        pass

    def upcast_to_PandaNode(self, const_LightNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_PandaNode(const LightNode self)
        
        upcast from LightNode to PandaNode
        """
        pass

    def write(self, LightNode_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(LightNode self, ostream out, int indent_level)
        
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
        '__doc__': '/**\n * A derivative of Light and of PandaNode.  All kinds of Light except\n * Spotlight (which must inherit from LensNode instead) inherit from this\n * class.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.LightNode' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE286DF0>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.LightNode' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.LightNode' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE286DF0>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE286DF0>)>'
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.LightNode' objects>"
        'upcastToLight': None, # (!) real value is "<method 'upcastToLight' of 'panda3d.core.LightNode' objects>"
        'upcastToPandaNode': None, # (!) real value is "<method 'upcastToPandaNode' of 'panda3d.core.LightNode' objects>"
        'upcast_to_Light': None, # (!) real value is "<method 'upcast_to_Light' of 'panda3d.core.LightNode' objects>"
        'upcast_to_PandaNode': None, # (!) real value is "<method 'upcast_to_PandaNode' of 'panda3d.core.LightNode' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.LightNode' objects>"
    }


