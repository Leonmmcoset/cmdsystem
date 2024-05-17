# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TypedWritableReferenceCount import TypedWritableReferenceCount

class RenderEffect(TypedWritableReferenceCount):
    """
    /**
     * This is the base class for a number of special render effects that may be
     * set on scene graph nodes to change the way they render.  This includes
     * BillboardEffect, DecalEffect, etc.
     *
     * RenderEffect represents render properties that must be applied as soon as
     * they are encountered in the scene graph, rather than propagating down to
     * the leaves.  This is different from RenderAttrib, which represents
     * properties like color and texture that don't do anything until they
     * propagate down to a GeomNode.
     *
     * You should not attempt to create or modify a RenderEffect directly;
     * instead, use the make() method of the appropriate kind of effect you want.
     * This will allocate and return a new RenderEffect of the appropriate type,
     * and it may share pointers if possible.  Do not modify the new RenderEffect
     * if you wish to change its properties; instead, create a new one.
     */
    """
    def compareTo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        compare_to(RenderEffect self, const RenderEffect other)
        
        /**
         * Provides an arbitrary ordering among all unique RenderEffects, so we can
         * store the essentially different ones in a big set and throw away the rest.
         *
         * This method is not needed outside of the RenderEffect class because all
         * equivalent RenderEffect objects are guaranteed to share the same pointer;
         * thus, a pointer comparison is always sufficient.
         */
        """
        pass

    def compare_to(self, RenderEffect_self, const_RenderEffect_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        compare_to(RenderEffect self, const RenderEffect other)
        
        /**
         * Provides an arbitrary ordering among all unique RenderEffects, so we can
         * store the essentially different ones in a big set and throw away the rest.
         *
         * This method is not needed outside of the RenderEffect class because all
         * equivalent RenderEffect objects are guaranteed to share the same pointer;
         * thus, a pointer comparison is always sufficient.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getNumEffects(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_effects()
        
        /**
         * Returns the total number of unique RenderEffect objects allocated in the
         * world.  This will go up and down during normal operations.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_num_effects(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_effects()
        
        /**
         * Returns the total number of unique RenderEffect objects allocated in the
         * world.  This will go up and down during normal operations.
         */
        """
        pass

    def listEffects(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        list_effects(ostream out)
        
        /**
         * Lists all of the RenderEffects in the cache to the output stream, one per
         * line.  This can be quite a lot of output if the cache is large, so be
         * prepared.
         */
        """
        pass

    def list_effects(self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        list_effects(ostream out)
        
        /**
         * Lists all of the RenderEffects in the cache to the output stream, one per
         * line.  This can be quite a lot of output if the cache is large, so be
         * prepared.
         */
        """
        pass

    def output(self, RenderEffect_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(RenderEffect self, ostream out)
        
        /**
         *
         */
        """
        pass

    def validateEffects(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        validate_effects()
        
        /**
         * Ensures that the cache is still stored in sorted order.  Returns true if
         * so, false if there is a problem (which implies someone has modified one of
         * the supposedly-const RenderEffect objects).
         */
        """
        pass

    def validate_effects(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        validate_effects()
        
        /**
         * Ensures that the cache is still stored in sorted order.  Returns true if
         * so, false if there is a problem (which implies someone has modified one of
         * the supposedly-const RenderEffect objects).
         */
        """
        pass

    def write(self, RenderEffect_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(RenderEffect self, ostream out, int indent_level)
        
        /**
         *
         */
        """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': "/**\n * This is the base class for a number of special render effects that may be\n * set on scene graph nodes to change the way they render.  This includes\n * BillboardEffect, DecalEffect, etc.\n *\n * RenderEffect represents render properties that must be applied as soon as\n * they are encountered in the scene graph, rather than propagating down to\n * the leaves.  This is different from RenderAttrib, which represents\n * properties like color and texture that don't do anything until they\n * propagate down to a GeomNode.\n *\n * You should not attempt to create or modify a RenderEffect directly;\n * instead, use the make() method of the appropriate kind of effect you want.\n * This will allocate and return a new RenderEffect of the appropriate type,\n * and it may share pointers if possible.  Do not modify the new RenderEffect\n * if you wish to change its properties; instead, create a new one.\n */",
        '__eq__': None, # (!) real value is "<slot wrapper '__eq__' of 'panda3d.core.RenderEffect' objects>"
        '__ge__': None, # (!) real value is "<slot wrapper '__ge__' of 'panda3d.core.RenderEffect' objects>"
        '__gt__': None, # (!) real value is "<slot wrapper '__gt__' of 'panda3d.core.RenderEffect' objects>"
        '__hash__': None, # (!) real value is "<slot wrapper '__hash__' of 'panda3d.core.RenderEffect' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.RenderEffect' objects>"
        '__le__': None, # (!) real value is "<slot wrapper '__le__' of 'panda3d.core.RenderEffect' objects>"
        '__lt__': None, # (!) real value is "<slot wrapper '__lt__' of 'panda3d.core.RenderEffect' objects>"
        '__ne__': None, # (!) real value is "<slot wrapper '__ne__' of 'panda3d.core.RenderEffect' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2924B0>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.RenderEffect' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.RenderEffect' objects>"
        'compareTo': None, # (!) real value is "<method 'compareTo' of 'panda3d.core.RenderEffect' objects>"
        'compare_to': None, # (!) real value is "<method 'compare_to' of 'panda3d.core.RenderEffect' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2924B0>)>'
        'getNumEffects': None, # (!) real value is '<staticmethod(<built-in method getNumEffects of type object at 0x00007FFCFE2924B0>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2924B0>)>'
        'get_num_effects': None, # (!) real value is '<staticmethod(<built-in method get_num_effects of type object at 0x00007FFCFE2924B0>)>'
        'listEffects': None, # (!) real value is '<staticmethod(<built-in method listEffects of type object at 0x00007FFCFE2924B0>)>'
        'list_effects': None, # (!) real value is '<staticmethod(<built-in method list_effects of type object at 0x00007FFCFE2924B0>)>'
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.RenderEffect' objects>"
        'validateEffects': None, # (!) real value is '<staticmethod(<built-in method validateEffects of type object at 0x00007FFCFE2924B0>)>'
        'validate_effects': None, # (!) real value is '<staticmethod(<built-in method validate_effects of type object at 0x00007FFCFE2924B0>)>'
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.RenderEffect' objects>"
    }


