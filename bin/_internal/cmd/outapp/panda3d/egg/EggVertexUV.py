# encoding: utf-8
# module panda3d.egg
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\egg.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


from .EggNamedObject import EggNamedObject

class EggVertexUV(EggNamedObject):
    """
    /**
     * The set of UV's that may or may not be assigned to a vertex.  To support
     * multitexturing, there may be multiple sets of UV's on a particular vertex,
     * each with its own name.
     */
    """
    def assign(self, const_EggVertexUV_self, const_EggVertexUV_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const EggVertexUV self, const EggVertexUV copy)
        
        /**
         *
         */
        """
        pass

    def clearBinormal(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_binormal(const EggVertexUV self)
        
        /**
         *
         */
        """
        pass

    def clearTangent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_tangent(const EggVertexUV self)
        
        /**
         *
         */
        """
        pass

    def clear_binormal(self, const_EggVertexUV_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_binormal(const EggVertexUV self)
        
        /**
         *
         */
        """
        pass

    def clear_tangent(self, const_EggVertexUV_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_tangent(const EggVertexUV self)
        
        /**
         *
         */
        """
        pass

    def compareTo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        compare_to(EggVertexUV self, const EggVertexUV other)
        
        /**
         * An ordering operator to compare two vertices for sorting order.  This
         * imposes an arbitrary ordering useful to identify unique vertices.
         */
        """
        pass

    def compare_to(self, EggVertexUV_self, const_EggVertexUV_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        compare_to(EggVertexUV self, const EggVertexUV other)
        
        /**
         * An ordering operator to compare two vertices for sorting order.  This
         * imposes an arbitrary ordering useful to identify unique vertices.
         */
        """
        pass

    def filterName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        filter_name(str name)
        
        /**
         * Returns the actual name that should be set for a given name string.
         * Usually this is the same string that is input, but for historical reasons
         * the texture coordinate name "default" is mapped to the empty string.
         */
        """
        pass

    def filter_name(self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        filter_name(str name)
        
        /**
         * Returns the actual name that should be set for a given name string.
         * Usually this is the same string that is input, but for historical reasons
         * the texture coordinate name "default" is mapped to the empty string.
         */
        """
        pass

    def getBinormal(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_binormal(EggVertexUV self)
        
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

    def getNumDimensions(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_dimensions(EggVertexUV self)
        
        /**
         * Returns the number of components of the texture coordinate set.  This is
         * either 2 (the normal case) or 3 (for a 3-d texture coordinate).
         */
        """
        pass

    def getTangent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_tangent(EggVertexUV self)
        
        /**
         *
         */
        """
        pass

    def getTangent4(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_tangent4(EggVertexUV self)
        
        /**
         *
         */
        """
        pass

    def getUv(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_uv(EggVertexUV self)
        
        /**
         * Returns the texture coordinate pair, if get_num_dimensions() is 2.
         */
        """
        pass

    def getUvw(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_uvw(EggVertexUV self)
        
        /**
         * Returns the texture coordinate triple, if get_num_dimensions() is 3.  This
         * is also legal to call if get_num_dimensions() is 2 (but the last dimension
         * will be zero).
         */
        """
        pass

    def get_binormal(self, EggVertexUV_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_binormal(EggVertexUV self)
        
        /**
         *
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_num_dimensions(self, EggVertexUV_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_dimensions(EggVertexUV self)
        
        /**
         * Returns the number of components of the texture coordinate set.  This is
         * either 2 (the normal case) or 3 (for a 3-d texture coordinate).
         */
        """
        pass

    def get_tangent(self, EggVertexUV_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_tangent(EggVertexUV self)
        
        /**
         *
         */
        """
        pass

    def get_tangent4(self, EggVertexUV_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_tangent4(EggVertexUV self)
        
        /**
         *
         */
        """
        pass

    def get_uv(self, EggVertexUV_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_uv(EggVertexUV self)
        
        /**
         * Returns the texture coordinate pair, if get_num_dimensions() is 2.
         */
        """
        pass

    def get_uvw(self, EggVertexUV_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_uvw(EggVertexUV self)
        
        /**
         * Returns the texture coordinate triple, if get_num_dimensions() is 3.  This
         * is also legal to call if get_num_dimensions() is 2 (but the last dimension
         * will be zero).
         */
        """
        pass

    def hasBinormal(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_binormal(EggVertexUV self)
        
        /**
         *
         */
        """
        pass

    def hasTangent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_tangent(EggVertexUV self)
        
        /**
         *
         */
        """
        pass

    def hasTangent4(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_tangent4(EggVertexUV self)
        
        /**
         *
         */
        """
        pass

    def hasW(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_w(EggVertexUV self)
        
        /**
         * Returns true if the texture coordinate has a third, w component, false if
         * it is just a normal 2-d texture coordinate.
         */
        """
        pass

    def has_binormal(self, EggVertexUV_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_binormal(EggVertexUV self)
        
        /**
         *
         */
        """
        pass

    def has_tangent(self, EggVertexUV_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_tangent(EggVertexUV self)
        
        /**
         *
         */
        """
        pass

    def has_tangent4(self, EggVertexUV_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_tangent4(EggVertexUV self)
        
        /**
         *
         */
        """
        pass

    def has_w(self, EggVertexUV_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_w(EggVertexUV self)
        
        /**
         * Returns true if the texture coordinate has a third, w component, false if
         * it is just a normal 2-d texture coordinate.
         */
        """
        pass

    def makeAverage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_average(const EggVertexUV first, const EggVertexUV second)
        
        /**
         * Creates a new EggVertexUV that contains the averaged values of the two
         * given objects.  It is an error if they don't have the same name.
         */
        """
        pass

    def make_average(self, const_EggVertexUV_first, const_EggVertexUV_second): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_average(const EggVertexUV first, const EggVertexUV second)
        
        /**
         * Creates a new EggVertexUV that contains the averaged values of the two
         * given objects.  It is an error if they don't have the same name.
         */
        """
        pass

    def setBinormal(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_binormal(const EggVertexUV self, const LVector3d binormal)
        
        /**
         *
         */
        """
        pass

    def setName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_name(const EggVertexUV self, str name)
        
        /**
         *
         */
        """
        pass

    def setTangent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_tangent(const EggVertexUV self, const LVector3d tangent)
        
        /**
         *
         */
        """
        pass

    def setTangent4(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_tangent4(const EggVertexUV self, const LVecBase4d tangent)
        
        /**
         * Sets the tangent vector, along with a fourth parameter that is multiplied
         * with the result of cross(normal, tangent) when computing the binormal.
         */
        """
        pass

    def setUv(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_uv(const EggVertexUV self, const LPoint2d texCoord)
        
        /**
         * Sets the texture coordinate pair.  This makes the texture coordinate a 2-d
         * texture coordinate, which is the usual case.
         */
        """
        pass

    def setUvw(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_uvw(const EggVertexUV self, const LPoint3d texCoord)
        
        /**
         * Sets the texture coordinate triple.  This makes the texture coordinate a
         * 3-d texture coordinate.
         */
        """
        pass

    def set_binormal(self, const_EggVertexUV_self, const_LVector3d_binormal): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_binormal(const EggVertexUV self, const LVector3d binormal)
        
        /**
         *
         */
        """
        pass

    def set_name(self, const_EggVertexUV_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_name(const EggVertexUV self, str name)
        
        /**
         *
         */
        """
        pass

    def set_tangent(self, const_EggVertexUV_self, const_LVector3d_tangent): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_tangent(const EggVertexUV self, const LVector3d tangent)
        
        /**
         *
         */
        """
        pass

    def set_tangent4(self, const_EggVertexUV_self, const_LVecBase4d_tangent): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_tangent4(const EggVertexUV self, const LVecBase4d tangent)
        
        /**
         * Sets the tangent vector, along with a fourth parameter that is multiplied
         * with the result of cross(normal, tangent) when computing the binormal.
         */
        """
        pass

    def set_uv(self, const_EggVertexUV_self, const_LPoint2d_texCoord): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_uv(const EggVertexUV self, const LPoint2d texCoord)
        
        /**
         * Sets the texture coordinate pair.  This makes the texture coordinate a 2-d
         * texture coordinate, which is the usual case.
         */
        """
        pass

    def set_uvw(self, const_EggVertexUV_self, const_LPoint3d_texCoord): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_uvw(const EggVertexUV self, const LPoint3d texCoord)
        
        /**
         * Sets the texture coordinate triple.  This makes the texture coordinate a
         * 3-d texture coordinate.
         */
        """
        pass

    def transform(self, const_EggVertexUV_self, const_LMatrix4d_mat): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        transform(const EggVertexUV self, const LMatrix4d mat)
        
        /**
         * Applies the indicated transformation matrix to the UV's tangent and/or
         * binormal.  This does nothing if there is no tangent or binormal.
         */
        """
        pass

    def write(self, EggVertexUV_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(EggVertexUV self, ostream out, int indent_level)
        
        /**
         *
         */
        """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
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

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.egg.EggVertexUV' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.egg.EggVertexUV' objects>"
        '__doc__': "/**\n * The set of UV's that may or may not be assigned to a vertex.  To support\n * multitexturing, there may be multiple sets of UV's on a particular vertex,\n * each with its own name.\n */",
        '__eq__': None, # (!) real value is "<slot wrapper '__eq__' of 'panda3d.egg.EggVertexUV' objects>"
        '__ge__': None, # (!) real value is "<slot wrapper '__ge__' of 'panda3d.egg.EggVertexUV' objects>"
        '__gt__': None, # (!) real value is "<slot wrapper '__gt__' of 'panda3d.egg.EggVertexUV' objects>"
        '__hash__': None, # (!) real value is "<slot wrapper '__hash__' of 'panda3d.egg.EggVertexUV' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.egg.EggVertexUV' objects>"
        '__le__': None, # (!) real value is "<slot wrapper '__le__' of 'panda3d.egg.EggVertexUV' objects>"
        '__lt__': None, # (!) real value is "<slot wrapper '__lt__' of 'panda3d.egg.EggVertexUV' objects>"
        '__ne__': None, # (!) real value is "<slot wrapper '__ne__' of 'panda3d.egg.EggVertexUV' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC68CD430>'
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.egg.EggVertexUV' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.egg.EggVertexUV' objects>"
        'clearBinormal': None, # (!) real value is "<method 'clearBinormal' of 'panda3d.egg.EggVertexUV' objects>"
        'clearTangent': None, # (!) real value is "<method 'clearTangent' of 'panda3d.egg.EggVertexUV' objects>"
        'clear_binormal': None, # (!) real value is "<method 'clear_binormal' of 'panda3d.egg.EggVertexUV' objects>"
        'clear_tangent': None, # (!) real value is "<method 'clear_tangent' of 'panda3d.egg.EggVertexUV' objects>"
        'compareTo': None, # (!) real value is "<method 'compareTo' of 'panda3d.egg.EggVertexUV' objects>"
        'compare_to': None, # (!) real value is "<method 'compare_to' of 'panda3d.egg.EggVertexUV' objects>"
        'filterName': None, # (!) real value is '<staticmethod(<built-in method filterName of type object at 0x00007FFDC68CD430>)>'
        'filter_name': None, # (!) real value is '<staticmethod(<built-in method filter_name of type object at 0x00007FFDC68CD430>)>'
        'getBinormal': None, # (!) real value is "<method 'getBinormal' of 'panda3d.egg.EggVertexUV' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFDC68CD430>)>'
        'getNumDimensions': None, # (!) real value is "<method 'getNumDimensions' of 'panda3d.egg.EggVertexUV' objects>"
        'getTangent': None, # (!) real value is "<method 'getTangent' of 'panda3d.egg.EggVertexUV' objects>"
        'getTangent4': None, # (!) real value is "<method 'getTangent4' of 'panda3d.egg.EggVertexUV' objects>"
        'getUv': None, # (!) real value is "<method 'getUv' of 'panda3d.egg.EggVertexUV' objects>"
        'getUvw': None, # (!) real value is "<method 'getUvw' of 'panda3d.egg.EggVertexUV' objects>"
        'get_binormal': None, # (!) real value is "<method 'get_binormal' of 'panda3d.egg.EggVertexUV' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFDC68CD430>)>'
        'get_num_dimensions': None, # (!) real value is "<method 'get_num_dimensions' of 'panda3d.egg.EggVertexUV' objects>"
        'get_tangent': None, # (!) real value is "<method 'get_tangent' of 'panda3d.egg.EggVertexUV' objects>"
        'get_tangent4': None, # (!) real value is "<method 'get_tangent4' of 'panda3d.egg.EggVertexUV' objects>"
        'get_uv': None, # (!) real value is "<method 'get_uv' of 'panda3d.egg.EggVertexUV' objects>"
        'get_uvw': None, # (!) real value is "<method 'get_uvw' of 'panda3d.egg.EggVertexUV' objects>"
        'hasBinormal': None, # (!) real value is "<method 'hasBinormal' of 'panda3d.egg.EggVertexUV' objects>"
        'hasTangent': None, # (!) real value is "<method 'hasTangent' of 'panda3d.egg.EggVertexUV' objects>"
        'hasTangent4': None, # (!) real value is "<method 'hasTangent4' of 'panda3d.egg.EggVertexUV' objects>"
        'hasW': None, # (!) real value is "<method 'hasW' of 'panda3d.egg.EggVertexUV' objects>"
        'has_binormal': None, # (!) real value is "<method 'has_binormal' of 'panda3d.egg.EggVertexUV' objects>"
        'has_tangent': None, # (!) real value is "<method 'has_tangent' of 'panda3d.egg.EggVertexUV' objects>"
        'has_tangent4': None, # (!) real value is "<method 'has_tangent4' of 'panda3d.egg.EggVertexUV' objects>"
        'has_w': None, # (!) real value is "<method 'has_w' of 'panda3d.egg.EggVertexUV' objects>"
        'makeAverage': None, # (!) real value is '<staticmethod(<built-in method makeAverage of type object at 0x00007FFDC68CD430>)>'
        'make_average': None, # (!) real value is '<staticmethod(<built-in method make_average of type object at 0x00007FFDC68CD430>)>'
        'setBinormal': None, # (!) real value is "<method 'setBinormal' of 'panda3d.egg.EggVertexUV' objects>"
        'setName': None, # (!) real value is "<method 'setName' of 'panda3d.egg.EggVertexUV' objects>"
        'setTangent': None, # (!) real value is "<method 'setTangent' of 'panda3d.egg.EggVertexUV' objects>"
        'setTangent4': None, # (!) real value is "<method 'setTangent4' of 'panda3d.egg.EggVertexUV' objects>"
        'setUv': None, # (!) real value is "<method 'setUv' of 'panda3d.egg.EggVertexUV' objects>"
        'setUvw': None, # (!) real value is "<method 'setUvw' of 'panda3d.egg.EggVertexUV' objects>"
        'set_binormal': None, # (!) real value is "<method 'set_binormal' of 'panda3d.egg.EggVertexUV' objects>"
        'set_name': None, # (!) real value is "<method 'set_name' of 'panda3d.egg.EggVertexUV' objects>"
        'set_tangent': None, # (!) real value is "<method 'set_tangent' of 'panda3d.egg.EggVertexUV' objects>"
        'set_tangent4': None, # (!) real value is "<method 'set_tangent4' of 'panda3d.egg.EggVertexUV' objects>"
        'set_uv': None, # (!) real value is "<method 'set_uv' of 'panda3d.egg.EggVertexUV' objects>"
        'set_uvw': None, # (!) real value is "<method 'set_uvw' of 'panda3d.egg.EggVertexUV' objects>"
        'transform': None, # (!) real value is "<method 'transform' of 'panda3d.egg.EggVertexUV' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.egg.EggVertexUV' objects>"
    }


