# encoding: utf-8
# module panda3d.egg
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\egg.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


class EggAttributes(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * The set of attributes that may be applied to vertices as well as polygons,
     * such as surface normal and color.
     *
     * This class cannot inherit from EggObject, because it causes problems at the
     * EggPolygon level with multiple appearances of the EggObject base class.
     * And making EggObject a virtual base class is just no fun.
     */
    """
    def assign(self, const_EggAttributes_self, const_EggAttributes_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const EggAttributes self, const EggAttributes copy)
        
        /**
         *
         */
        """
        pass

    def clearColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_color(const EggAttributes self)
        
        /**
         *
         */
        """
        pass

    def clearNormal(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_normal(const EggAttributes self)
        
        /**
         *
         */
        """
        pass

    def clear_color(self, const_EggAttributes_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_color(const EggAttributes self)
        
        /**
         *
         */
        """
        pass

    def clear_normal(self, const_EggAttributes_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_normal(const EggAttributes self)
        
        /**
         *
         */
        """
        pass

    def compareTo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        compare_to(EggAttributes self, const EggAttributes other)
        
        /**
         * An ordering operator to compare two vertices for sorting order.  This
         * imposes an arbitrary ordering useful to identify unique vertices.
         */
        """
        pass

    def compare_to(self, EggAttributes_self, const_EggAttributes_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        compare_to(EggAttributes self, const EggAttributes other)
        
        /**
         * An ordering operator to compare two vertices for sorting order.  This
         * imposes an arbitrary ordering useful to identify unique vertices.
         */
        """
        pass

    def copyColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        copy_color(const EggAttributes self, const EggAttributes other)
        
        /**
         * Sets this color to be the same as the other's, include morphs.  If the
         * other has no color, this clears the color.
         */
        """
        pass

    def copyNormal(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        copy_normal(const EggAttributes self, const EggAttributes other)
        
        /**
         * Sets this normal to be the same as the other's, include morphs.  If the
         * other has no normal, this clears the normal.
         */
        """
        pass

    def copy_color(self, const_EggAttributes_self, const_EggAttributes_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        copy_color(const EggAttributes self, const EggAttributes other)
        
        /**
         * Sets this color to be the same as the other's, include morphs.  If the
         * other has no color, this clears the color.
         */
        """
        pass

    def copy_normal(self, const_EggAttributes_self, const_EggAttributes_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        copy_normal(const EggAttributes self, const EggAttributes other)
        
        /**
         * Sets this normal to be the same as the other's, include morphs.  If the
         * other has no normal, this clears the normal.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_color(EggAttributes self)
        
        /**
         * Returns the color set on this particular attribute.  If there is no color
         * set, returns white.
         */
        """
        pass

    def getNormal(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_normal(EggAttributes self)
        
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

    def get_color(self, EggAttributes_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_color(EggAttributes self)
        
        /**
         * Returns the color set on this particular attribute.  If there is no color
         * set, returns white.
         */
        """
        pass

    def get_normal(self, EggAttributes_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_normal(EggAttributes self)
        
        /**
         *
         */
        """
        pass

    def hasColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_color(EggAttributes self)
        
        /**
         *
         */
        """
        pass

    def hasNormal(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_normal(EggAttributes self)
        
        /**
         *
         */
        """
        pass

    def has_color(self, EggAttributes_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_color(EggAttributes self)
        
        /**
         *
         */
        """
        pass

    def has_normal(self, EggAttributes_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_normal(EggAttributes self)
        
        /**
         *
         */
        """
        pass

    def matchesColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        matches_color(EggAttributes self, const EggAttributes other)
        
        /**
         * Returns true if this color matches that of the other EggAttributes object,
         * include the morph list.
         */
        """
        pass

    def matchesNormal(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        matches_normal(EggAttributes self, const EggAttributes other)
        
        /**
         * Returns true if this normal matches that of the other EggAttributes object,
         * include the morph list.
         */
        """
        pass

    def matches_color(self, EggAttributes_self, const_EggAttributes_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        matches_color(EggAttributes self, const EggAttributes other)
        
        /**
         * Returns true if this color matches that of the other EggAttributes object,
         * include the morph list.
         */
        """
        pass

    def matches_normal(self, EggAttributes_self, const_EggAttributes_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        matches_normal(EggAttributes self, const EggAttributes other)
        
        /**
         * Returns true if this normal matches that of the other EggAttributes object,
         * include the morph list.
         */
        """
        pass

    def setColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_color(const EggAttributes self, const LVecBase4f Color)
        
        /**
         *
         */
        """
        pass

    def setNormal(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_normal(const EggAttributes self, const LVector3d normal)
        
        /**
         *
         */
        """
        pass

    def set_color(self, const_EggAttributes_self, const_LVecBase4f_Color): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_color(const EggAttributes self, const LVecBase4f Color)
        
        /**
         *
         */
        """
        pass

    def set_normal(self, const_EggAttributes_self, const_LVector3d_normal): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_normal(const EggAttributes self, const LVector3d normal)
        
        /**
         *
         */
        """
        pass

    def sortsLessThan(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        sorts_less_than(EggAttributes self, const EggAttributes other)
        
        /**
         * An ordering operator to compare two vertices for sorting order.  This
         * imposes an arbitrary ordering useful to identify unique vertices.
         */
        """
        pass

    def sorts_less_than(self, EggAttributes_self, const_EggAttributes_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        sorts_less_than(EggAttributes self, const EggAttributes other)
        
        /**
         * An ordering operator to compare two vertices for sorting order.  This
         * imposes an arbitrary ordering useful to identify unique vertices.
         */
        """
        pass

    def transform(self, const_EggAttributes_self, const_LMatrix4d_mat): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        transform(const EggAttributes self, const LMatrix4d mat)
        
        /**
         * Applies the indicated transformation matrix to the attributes.
         */
        """
        pass

    def write(self, EggAttributes_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(EggAttributes self, ostream out, int indent_level)
        
        /**
         * Writes the attributes to the indicated output stream in Egg format.
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
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.egg.EggAttributes' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.egg.EggAttributes' objects>"
        '__doc__': '/**\n * The set of attributes that may be applied to vertices as well as polygons,\n * such as surface normal and color.\n *\n * This class cannot inherit from EggObject, because it causes problems at the\n * EggPolygon level with multiple appearances of the EggObject base class.\n * And making EggObject a virtual base class is just no fun.\n */',
        '__eq__': None, # (!) real value is "<slot wrapper '__eq__' of 'panda3d.egg.EggAttributes' objects>"
        '__ge__': None, # (!) real value is "<slot wrapper '__ge__' of 'panda3d.egg.EggAttributes' objects>"
        '__gt__': None, # (!) real value is "<slot wrapper '__gt__' of 'panda3d.egg.EggAttributes' objects>"
        '__hash__': None, # (!) real value is "<slot wrapper '__hash__' of 'panda3d.egg.EggAttributes' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.egg.EggAttributes' objects>"
        '__le__': None, # (!) real value is "<slot wrapper '__le__' of 'panda3d.egg.EggAttributes' objects>"
        '__lt__': None, # (!) real value is "<slot wrapper '__lt__' of 'panda3d.egg.EggAttributes' objects>"
        '__ne__': None, # (!) real value is "<slot wrapper '__ne__' of 'panda3d.egg.EggAttributes' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC68CD260>'
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.egg.EggAttributes' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.egg.EggAttributes' objects>"
        'clearColor': None, # (!) real value is "<method 'clearColor' of 'panda3d.egg.EggAttributes' objects>"
        'clearNormal': None, # (!) real value is "<method 'clearNormal' of 'panda3d.egg.EggAttributes' objects>"
        'clear_color': None, # (!) real value is "<method 'clear_color' of 'panda3d.egg.EggAttributes' objects>"
        'clear_normal': None, # (!) real value is "<method 'clear_normal' of 'panda3d.egg.EggAttributes' objects>"
        'compareTo': None, # (!) real value is "<method 'compareTo' of 'panda3d.egg.EggAttributes' objects>"
        'compare_to': None, # (!) real value is "<method 'compare_to' of 'panda3d.egg.EggAttributes' objects>"
        'copyColor': None, # (!) real value is "<method 'copyColor' of 'panda3d.egg.EggAttributes' objects>"
        'copyNormal': None, # (!) real value is "<method 'copyNormal' of 'panda3d.egg.EggAttributes' objects>"
        'copy_color': None, # (!) real value is "<method 'copy_color' of 'panda3d.egg.EggAttributes' objects>"
        'copy_normal': None, # (!) real value is "<method 'copy_normal' of 'panda3d.egg.EggAttributes' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFDC68CD260>)>'
        'getColor': None, # (!) real value is "<method 'getColor' of 'panda3d.egg.EggAttributes' objects>"
        'getNormal': None, # (!) real value is "<method 'getNormal' of 'panda3d.egg.EggAttributes' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFDC68CD260>)>'
        'get_color': None, # (!) real value is "<method 'get_color' of 'panda3d.egg.EggAttributes' objects>"
        'get_normal': None, # (!) real value is "<method 'get_normal' of 'panda3d.egg.EggAttributes' objects>"
        'hasColor': None, # (!) real value is "<method 'hasColor' of 'panda3d.egg.EggAttributes' objects>"
        'hasNormal': None, # (!) real value is "<method 'hasNormal' of 'panda3d.egg.EggAttributes' objects>"
        'has_color': None, # (!) real value is "<method 'has_color' of 'panda3d.egg.EggAttributes' objects>"
        'has_normal': None, # (!) real value is "<method 'has_normal' of 'panda3d.egg.EggAttributes' objects>"
        'matchesColor': None, # (!) real value is "<method 'matchesColor' of 'panda3d.egg.EggAttributes' objects>"
        'matchesNormal': None, # (!) real value is "<method 'matchesNormal' of 'panda3d.egg.EggAttributes' objects>"
        'matches_color': None, # (!) real value is "<method 'matches_color' of 'panda3d.egg.EggAttributes' objects>"
        'matches_normal': None, # (!) real value is "<method 'matches_normal' of 'panda3d.egg.EggAttributes' objects>"
        'setColor': None, # (!) real value is "<method 'setColor' of 'panda3d.egg.EggAttributes' objects>"
        'setNormal': None, # (!) real value is "<method 'setNormal' of 'panda3d.egg.EggAttributes' objects>"
        'set_color': None, # (!) real value is "<method 'set_color' of 'panda3d.egg.EggAttributes' objects>"
        'set_normal': None, # (!) real value is "<method 'set_normal' of 'panda3d.egg.EggAttributes' objects>"
        'sortsLessThan': None, # (!) real value is "<method 'sortsLessThan' of 'panda3d.egg.EggAttributes' objects>"
        'sorts_less_than': None, # (!) real value is "<method 'sorts_less_than' of 'panda3d.egg.EggAttributes' objects>"
        'transform': None, # (!) real value is "<method 'transform' of 'panda3d.egg.EggAttributes' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.egg.EggAttributes' objects>"
    }


