# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TypedReferenceCount import TypedReferenceCount

class BoundingVolume(TypedReferenceCount):
    """
    /**
     * This is an abstract class for any volume in any sense which can be said to
     * define the locality of reference of a node in a graph, along with all of
     * its descendants.  It is not necessarily a geometric volume (although see
     * GeometricBoundingVolume); this is simply an abstract interface for bounds
     * of any sort.
     */
    """
    def contains(self, BoundingVolume_self, const_BoundingVolume_vol): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        contains(BoundingVolume self, const BoundingVolume vol)
        
        /**
         * Returns the appropriate set of IntersectionFlags to indicate the amount of
         * intersection with the indicated volume.
         */
        """
        pass

    def extendBy(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        extend_by(const BoundingVolume self, const BoundingVolume vol)
        
        /**
         * Increases the size of the volume to include the given volume.
         */
        """
        pass

    def extend_by(self, const_BoundingVolume_self, const_BoundingVolume_vol): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        extend_by(const BoundingVolume self, const BoundingVolume vol)
        
        /**
         * Increases the size of the volume to include the given volume.
         */
        """
        pass

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

    def isEmpty(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_empty(BoundingVolume self)
        
        /**
         * Any kind of volume might be empty.  This is a degenerate volume that
         * contains no points; it's not the same as, for instance, a sphere with
         * radius zero, since that contains one point (the center).  It intersects
         * with no other volumes.
         */
        """
        pass

    def isInfinite(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_infinite(BoundingVolume self)
        
        /**
         * The other side of the empty coin is an infinite volume.  This is a
         * degenerate state of a normally finite volume that contains all points.
         * (Note that some kinds of infinite bounding volumes, like binary separating
         * planes, do not contain all points and thus correctly return is_infinite()
         * == false, even though they are technically infinite.  This is a special
         * case of the word 'infinite' meaning the volume covers all points in space.)
         *
         * It completely intersects with all other volumes except empty volumes.
         */
        """
        pass

    def is_empty(self, BoundingVolume_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_empty(BoundingVolume self)
        
        /**
         * Any kind of volume might be empty.  This is a degenerate volume that
         * contains no points; it's not the same as, for instance, a sphere with
         * radius zero, since that contains one point (the center).  It intersects
         * with no other volumes.
         */
        """
        pass

    def is_infinite(self, BoundingVolume_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_infinite(BoundingVolume self)
        
        /**
         * The other side of the empty coin is an infinite volume.  This is a
         * degenerate state of a normally finite volume that contains all points.
         * (Note that some kinds of infinite bounding volumes, like binary separating
         * planes, do not contain all points and thus correctly return is_infinite()
         * == false, even though they are technically infinite.  This is a special
         * case of the word 'infinite' meaning the volume covers all points in space.)
         *
         * It completely intersects with all other volumes except empty volumes.
         */
        """
        pass

    def makeCopy(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_copy(BoundingVolume self)
        """
        pass

    def make_copy(self, BoundingVolume_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_copy(BoundingVolume self)
        """
        pass

    def output(self, BoundingVolume_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(BoundingVolume self, ostream out)
        """
        pass

    def setInfinite(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_infinite(const BoundingVolume self)
        
        /**
         * Marks the volume as infinite, even if it is normally finite.  You can think
         * of this as an infinite extend_by() operation.
         */
        """
        pass

    def set_infinite(self, const_BoundingVolume_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_infinite(const BoundingVolume self)
        
        /**
         * Marks the volume as infinite, even if it is normally finite.  You can think
         * of this as an infinite extend_by() operation.
         */
        """
        pass

    def write(self, BoundingVolume_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(BoundingVolume self, ostream out, int indent_level)
        
        /**
         *
         */
        """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
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

    BTBest = 1
    BTBox = 3
    BTDefault = 0
    BTFastest = 4
    BTSphere = 2
    BT_best = 1
    BT_box = 3
    BT_default = 0
    BT_fastest = 4
    BT_sphere = 2
    DtoolClassDict = {
        'BTBest': 1,
        'BTBox': 3,
        'BTDefault': 0,
        'BTFastest': 4,
        'BTSphere': 2,
        'BT_best': 1,
        'BT_box': 3,
        'BT_default': 0,
        'BT_fastest': 4,
        'BT_sphere': 2,
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'IFAll': 4,
        'IFDontUnderstand': 8,
        'IFNoIntersection': 0,
        'IFPossible': 1,
        'IFSome': 2,
        'IF_all': 4,
        'IF_dont_understand': 8,
        'IF_no_intersection': 0,
        'IF_possible': 1,
        'IF_some': 2,
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.BoundingVolume' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.BoundingVolume' objects>"
        '__doc__': '/**\n * This is an abstract class for any volume in any sense which can be said to\n * define the locality of reference of a node in a graph, along with all of\n * its descendants.  It is not necessarily a geometric volume (although see\n * GeometricBoundingVolume); this is simply an abstract interface for bounds\n * of any sort.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.BoundingVolume' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE340A30>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.BoundingVolume' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.BoundingVolume' objects>"
        'contains': None, # (!) real value is "<method 'contains' of 'panda3d.core.BoundingVolume' objects>"
        'extendBy': None, # (!) real value is "<method 'extendBy' of 'panda3d.core.BoundingVolume' objects>"
        'extend_by': None, # (!) real value is "<method 'extend_by' of 'panda3d.core.BoundingVolume' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE340A30>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE340A30>)>'
        'isEmpty': None, # (!) real value is "<method 'isEmpty' of 'panda3d.core.BoundingVolume' objects>"
        'isInfinite': None, # (!) real value is "<method 'isInfinite' of 'panda3d.core.BoundingVolume' objects>"
        'is_empty': None, # (!) real value is "<method 'is_empty' of 'panda3d.core.BoundingVolume' objects>"
        'is_infinite': None, # (!) real value is "<method 'is_infinite' of 'panda3d.core.BoundingVolume' objects>"
        'makeCopy': None, # (!) real value is "<method 'makeCopy' of 'panda3d.core.BoundingVolume' objects>"
        'make_copy': None, # (!) real value is "<method 'make_copy' of 'panda3d.core.BoundingVolume' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.BoundingVolume' objects>"
        'setInfinite': None, # (!) real value is "<method 'setInfinite' of 'panda3d.core.BoundingVolume' objects>"
        'set_infinite': None, # (!) real value is "<method 'set_infinite' of 'panda3d.core.BoundingVolume' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.BoundingVolume' objects>"
    }
    IFAll = 4
    IFDontUnderstand = 8
    IFNoIntersection = 0
    IFPossible = 1
    IFSome = 2
    IF_all = 4
    IF_dont_understand = 8
    IF_no_intersection = 0
    IF_possible = 1
    IF_some = 2


