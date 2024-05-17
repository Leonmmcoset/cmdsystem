# encoding: utf-8
# module panda3d.egg
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\egg.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


from .EggNamedObject import EggNamedObject

class EggVertexAux(EggNamedObject):
    """
    /**
     * The set of named auxiliary data that may or may not be assigned to a
     * vertex.  Panda will import this data and create a custom column for it in
     * the vertex data, but will not otherwise interpret it.  Presumably, a shader
     * will process the data later.
     */
    """
    def assign(self, const_EggVertexAux_self, const_EggVertexAux_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const EggVertexAux self, const EggVertexAux copy)
        
        /**
         *
         */
        """
        pass

    def compareTo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        compare_to(EggVertexAux self, const EggVertexAux other)
        
        /**
         * An ordering operator to compare two vertices for sorting order.  This
         * imposes an arbitrary ordering useful to identify unique vertices.
         */
        """
        pass

    def compare_to(self, EggVertexAux_self, const_EggVertexAux_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        compare_to(EggVertexAux self, const EggVertexAux other)
        
        /**
         * An ordering operator to compare two vertices for sorting order.  This
         * imposes an arbitrary ordering useful to identify unique vertices.
         */
        """
        pass

    def getAux(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_aux(EggVertexAux self)
        
        /**
         * Returns the auxiliary data quadruple.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_aux(self, EggVertexAux_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_aux(EggVertexAux self)
        
        /**
         * Returns the auxiliary data quadruple.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def makeAverage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_average(const EggVertexAux first, const EggVertexAux second)
        
        /**
         * Creates a new EggVertexAux that contains the averaged values of the two
         * given objects.  It is an error if they don't have the same name.
         */
        """
        pass

    def make_average(self, const_EggVertexAux_first, const_EggVertexAux_second): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_average(const EggVertexAux first, const EggVertexAux second)
        
        /**
         * Creates a new EggVertexAux that contains the averaged values of the two
         * given objects.  It is an error if they don't have the same name.
         */
        """
        pass

    def setAux(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_aux(const EggVertexAux self, const LVecBase4d aux)
        
        /**
         * Sets the auxiliary data quadruple.
         */
        """
        pass

    def setName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_name(const EggVertexAux self, str name)
        
        /**
         *
         */
        """
        pass

    def set_aux(self, const_EggVertexAux_self, const_LVecBase4d_aux): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_aux(const EggVertexAux self, const LVecBase4d aux)
        
        /**
         * Sets the auxiliary data quadruple.
         */
        """
        pass

    def set_name(self, const_EggVertexAux_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_name(const EggVertexAux self, str name)
        
        /**
         *
         */
        """
        pass

    def write(self, EggVertexAux_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(EggVertexAux self, ostream out, int indent_level)
        
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
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.egg.EggVertexAux' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.egg.EggVertexAux' objects>"
        '__doc__': '/**\n * The set of named auxiliary data that may or may not be assigned to a\n * vertex.  Panda will import this data and create a custom column for it in\n * the vertex data, but will not otherwise interpret it.  Presumably, a shader\n * will process the data later.\n */',
        '__eq__': None, # (!) real value is "<slot wrapper '__eq__' of 'panda3d.egg.EggVertexAux' objects>"
        '__ge__': None, # (!) real value is "<slot wrapper '__ge__' of 'panda3d.egg.EggVertexAux' objects>"
        '__gt__': None, # (!) real value is "<slot wrapper '__gt__' of 'panda3d.egg.EggVertexAux' objects>"
        '__hash__': None, # (!) real value is "<slot wrapper '__hash__' of 'panda3d.egg.EggVertexAux' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.egg.EggVertexAux' objects>"
        '__le__': None, # (!) real value is "<slot wrapper '__le__' of 'panda3d.egg.EggVertexAux' objects>"
        '__lt__': None, # (!) real value is "<slot wrapper '__lt__' of 'panda3d.egg.EggVertexAux' objects>"
        '__ne__': None, # (!) real value is "<slot wrapper '__ne__' of 'panda3d.egg.EggVertexAux' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC68CD600>'
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.egg.EggVertexAux' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.egg.EggVertexAux' objects>"
        'compareTo': None, # (!) real value is "<method 'compareTo' of 'panda3d.egg.EggVertexAux' objects>"
        'compare_to': None, # (!) real value is "<method 'compare_to' of 'panda3d.egg.EggVertexAux' objects>"
        'getAux': None, # (!) real value is "<method 'getAux' of 'panda3d.egg.EggVertexAux' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFDC68CD600>)>'
        'get_aux': None, # (!) real value is "<method 'get_aux' of 'panda3d.egg.EggVertexAux' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFDC68CD600>)>'
        'makeAverage': None, # (!) real value is '<staticmethod(<built-in method makeAverage of type object at 0x00007FFDC68CD600>)>'
        'make_average': None, # (!) real value is '<staticmethod(<built-in method make_average of type object at 0x00007FFDC68CD600>)>'
        'setAux': None, # (!) real value is "<method 'setAux' of 'panda3d.egg.EggVertexAux' objects>"
        'setName': None, # (!) real value is "<method 'setName' of 'panda3d.egg.EggVertexAux' objects>"
        'set_aux': None, # (!) real value is "<method 'set_aux' of 'panda3d.egg.EggVertexAux' objects>"
        'set_name': None, # (!) real value is "<method 'set_name' of 'panda3d.egg.EggVertexAux' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.egg.EggVertexAux' objects>"
    }


