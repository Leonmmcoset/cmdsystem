# encoding: utf-8
# module panda3d.egg
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\egg.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


from .EggPrimitive import EggPrimitive

class EggCompositePrimitive(EggPrimitive):
    """
    /**
     * The base class for primitives such as triangle strips and triangle fans,
     * which include several component triangles, each of which might have its own
     * color and/or normal.
     */
    """
    def assign(self, const_EggCompositePrimitive_self, const_EggCompositePrimitive_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const EggCompositePrimitive self, const EggCompositePrimitive copy)
        
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

    def getComponent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_component(const EggCompositePrimitive self, int i)
        get_component(EggCompositePrimitive self, int i)
        
        /**
         * Returns the attributes for the nth component triangle.
         */
        
        /**
         * Returns the attributes for the nth component triangle.
         */
        """
        pass

    def getComponents(self, *args, **kwargs): # real signature unknown
        pass

    def getNumComponents(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_components(EggCompositePrimitive self)
        
        /**
         * Returns the number of individual component triangles within the composite.
         * Each one of these might have a different set of attributes.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_component(self, const_EggCompositePrimitive_self, int_i): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_component(const EggCompositePrimitive self, int i)
        get_component(EggCompositePrimitive self, int i)
        
        /**
         * Returns the attributes for the nth component triangle.
         */
        
        /**
         * Returns the attributes for the nth component triangle.
         */
        """
        pass

    def get_components(self, *args, **kwargs): # real signature unknown
        pass

    def get_num_components(self, EggCompositePrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_components(EggCompositePrimitive self)
        
        /**
         * Returns the number of individual component triangles within the composite.
         * Each one of these might have a different set of attributes.
         */
        """
        pass

    def setComponent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_component(const EggCompositePrimitive self, int i, const EggAttributes attrib)
        
        /**
         * Changes the attributes for the nth component triangle.
         */
        """
        pass

    def set_component(self, const_EggCompositePrimitive_self, int_i, const_EggAttributes_attrib): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_component(const EggCompositePrimitive self, int i, const EggAttributes attrib)
        
        /**
         * Changes the attributes for the nth component triangle.
         */
        """
        pass

    def triangulateInPlace(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        triangulate_in_place(const EggCompositePrimitive self)
        
        /**
         * Subdivides the composite primitive into triangles and adds those triangles
         * to the parent group node in place of the original primitive.  Returns a
         * pointer to the original primitive, which is likely about to be destructed.
         *
         * If convex_also is true, both concave and convex polygons will be subdivided
         * into triangles; otherwise, only concave polygons will be subdivided, and
         * convex polygons will be copied unchanged into the container.
         */
        """
        pass

    def triangulateInto(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        triangulate_into(EggCompositePrimitive self, EggGroupNode container)
        
        /**
         * Subdivides the composite primitive into triangles and adds those triangles
         * to the indicated container.  Does not remove the primitive from its
         * existing parent or modify it in any way.
         *
         * Returns true if the triangulation is successful, or false if there was some
         * error (in which case the container may contain some partial triangulation).
         */
        """
        pass

    def triangulate_into(self, EggCompositePrimitive_self, EggGroupNode_container): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        triangulate_into(EggCompositePrimitive self, EggGroupNode container)
        
        /**
         * Subdivides the composite primitive into triangles and adds those triangles
         * to the indicated container.  Does not remove the primitive from its
         * existing parent or modify it in any way.
         *
         * Returns true if the triangulation is successful, or false if there was some
         * error (in which case the container may contain some partial triangulation).
         */
        """
        pass

    def triangulate_in_place(self, const_EggCompositePrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        triangulate_in_place(const EggCompositePrimitive self)
        
        /**
         * Subdivides the composite primitive into triangles and adds those triangles
         * to the parent group node in place of the original primitive.  Returns a
         * pointer to the original primitive, which is likely about to be destructed.
         *
         * If convex_also is true, both concave and convex polygons will be subdivided
         * into triangles; otherwise, only concave polygons will be subdivided, and
         * convex polygons will be copied unchanged into the container.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    components = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * The base class for primitives such as triangle strips and triangle fans,\n * which include several component triangles, each of which might have its own\n * color and/or normal.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.egg.EggCompositePrimitive' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC68CF130>'
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.egg.EggCompositePrimitive' objects>"
        'components': None, # (!) real value is "<attribute 'components' of 'panda3d.egg.EggCompositePrimitive' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFDC68CF130>)>'
        'getComponent': None, # (!) real value is "<method 'getComponent' of 'panda3d.egg.EggCompositePrimitive' objects>"
        'getComponents': None, # (!) real value is "<method 'getComponents' of 'panda3d.egg.EggCompositePrimitive' objects>"
        'getNumComponents': None, # (!) real value is "<method 'getNumComponents' of 'panda3d.egg.EggCompositePrimitive' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFDC68CF130>)>'
        'get_component': None, # (!) real value is "<method 'get_component' of 'panda3d.egg.EggCompositePrimitive' objects>"
        'get_components': None, # (!) real value is "<method 'get_components' of 'panda3d.egg.EggCompositePrimitive' objects>"
        'get_num_components': None, # (!) real value is "<method 'get_num_components' of 'panda3d.egg.EggCompositePrimitive' objects>"
        'setComponent': None, # (!) real value is "<method 'setComponent' of 'panda3d.egg.EggCompositePrimitive' objects>"
        'set_component': None, # (!) real value is "<method 'set_component' of 'panda3d.egg.EggCompositePrimitive' objects>"
        'triangulateInPlace': None, # (!) real value is "<method 'triangulateInPlace' of 'panda3d.egg.EggCompositePrimitive' objects>"
        'triangulateInto': None, # (!) real value is "<method 'triangulateInto' of 'panda3d.egg.EggCompositePrimitive' objects>"
        'triangulate_in_place': None, # (!) real value is "<method 'triangulate_in_place' of 'panda3d.egg.EggCompositePrimitive' objects>"
        'triangulate_into': None, # (!) real value is "<method 'triangulate_into' of 'panda3d.egg.EggCompositePrimitive' objects>"
    }


