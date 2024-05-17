# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .GeometricBoundingVolume import GeometricBoundingVolume

class IntersectionBoundingVolume(GeometricBoundingVolume):
    """
    /**
     * This special bounding volume is the intersection of all of its constituent
     * bounding volumes.
     *
     * A point is defined to be within an IntersectionBoundingVolume if it is
     * within all of its component bounding volumes.
     */
    """
    def addComponent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_component(const IntersectionBoundingVolume self, const GeometricBoundingVolume component)
        
        /**
         * Adds a new component to the volume.  This does not necessarily increase the
         * total number of components by one, and you may or may not be able to find
         * this component in the volume by a subsequent call to get_component();
         * certain optimizations may prevent the component from being added, or have
         * other unexpected effects on the total set of components.
         */
        """
        pass

    def add_component(self, const_IntersectionBoundingVolume_self, const_GeometricBoundingVolume_component): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_component(const IntersectionBoundingVolume self, const GeometricBoundingVolume component)
        
        /**
         * Adds a new component to the volume.  This does not necessarily increase the
         * total number of components by one, and you may or may not be able to find
         * this component in the volume by a subsequent call to get_component();
         * certain optimizations may prevent the component from being added, or have
         * other unexpected effects on the total set of components.
         */
        """
        pass

    def clearComponents(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_components(const IntersectionBoundingVolume self)
        
        /**
         * Removes all components from the volume.
         */
        """
        pass

    def clear_components(self, const_IntersectionBoundingVolume_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_components(const IntersectionBoundingVolume self)
        
        /**
         * Removes all components from the volume.
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
        get_component(IntersectionBoundingVolume self, int n)
        
        /**
         * Returns the nth component in the intersection.
         */
        """
        pass

    def getComponents(self, *args, **kwargs): # real signature unknown
        pass

    def getNumComponents(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_components(IntersectionBoundingVolume self)
        
        /**
         * Returns the number of components in the intersection.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_component(self, IntersectionBoundingVolume_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_component(IntersectionBoundingVolume self, int n)
        
        /**
         * Returns the nth component in the intersection.
         */
        """
        pass

    def get_components(self, *args, **kwargs): # real signature unknown
        pass

    def get_num_components(self, IntersectionBoundingVolume_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_components(IntersectionBoundingVolume self)
        
        /**
         * Returns the number of components in the intersection.
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
        '__doc__': '/**\n * This special bounding volume is the intersection of all of its constituent\n * bounding volumes.\n *\n * A point is defined to be within an IntersectionBoundingVolume if it is\n * within all of its component bounding volumes.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.IntersectionBoundingVolume' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE342390>'
        'addComponent': None, # (!) real value is "<method 'addComponent' of 'panda3d.core.IntersectionBoundingVolume' objects>"
        'add_component': None, # (!) real value is "<method 'add_component' of 'panda3d.core.IntersectionBoundingVolume' objects>"
        'clearComponents': None, # (!) real value is "<method 'clearComponents' of 'panda3d.core.IntersectionBoundingVolume' objects>"
        'clear_components': None, # (!) real value is "<method 'clear_components' of 'panda3d.core.IntersectionBoundingVolume' objects>"
        'components': None, # (!) real value is "<attribute 'components' of 'panda3d.core.IntersectionBoundingVolume' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE342390>)>'
        'getComponent': None, # (!) real value is "<method 'getComponent' of 'panda3d.core.IntersectionBoundingVolume' objects>"
        'getComponents': None, # (!) real value is "<method 'getComponents' of 'panda3d.core.IntersectionBoundingVolume' objects>"
        'getNumComponents': None, # (!) real value is "<method 'getNumComponents' of 'panda3d.core.IntersectionBoundingVolume' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE342390>)>'
        'get_component': None, # (!) real value is "<method 'get_component' of 'panda3d.core.IntersectionBoundingVolume' objects>"
        'get_components': None, # (!) real value is "<method 'get_components' of 'panda3d.core.IntersectionBoundingVolume' objects>"
        'get_num_components': None, # (!) real value is "<method 'get_num_components' of 'panda3d.core.IntersectionBoundingVolume' objects>"
    }


