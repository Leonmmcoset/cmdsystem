# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class LVecBase2i(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This is the base class for all two-component vectors and points.
     */
    """
    def addHash(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_hash(LVecBase2i self, int hash)
        
        /**
         * Adds the vector into the running hash.
         */
        """
        pass

    def addToCell(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_to_cell(const LVecBase2i self, int i, int value)
        
        // These next functions add to an existing value.  i.e.
        // foo.set_x(foo.get_x() + value) These are useful to reduce overhead in
        // scripting languages:
        
        /**
         *
         */
        """
        pass

    def addX(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_x(const LVecBase2i self, int value)
        
        /**
         *
         */
        """
        pass

    def addY(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_y(const LVecBase2i self, int value)
        
        /**
         *
         */
        """
        pass

    def add_hash(self, LVecBase2i_self, int_hash): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_hash(LVecBase2i self, int hash)
        
        /**
         * Adds the vector into the running hash.
         */
        """
        pass

    def add_to_cell(self, const_LVecBase2i_self, int_i, int_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_to_cell(const LVecBase2i self, int i, int value)
        
        // These next functions add to an existing value.  i.e.
        // foo.set_x(foo.get_x() + value) These are useful to reduce overhead in
        // scripting languages:
        
        /**
         *
         */
        """
        pass

    def add_x(self, const_LVecBase2i_self, int_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_x(const LVecBase2i self, int value)
        
        /**
         *
         */
        """
        pass

    def add_y(self, const_LVecBase2i_self, int_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_y(const LVecBase2i self, int value)
        
        /**
         *
         */
        """
        pass

    def almostEqual(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        almost_equal(LVecBase2i self, const LVecBase2i other)
        almost_equal(LVecBase2i self, const LVecBase2i other, int threshold)
        
        /**
         * Returns true if two vectors are memberwise equal within a specified
         * tolerance.
         */
        
        /**
         * Returns true if two vectors are memberwise equal within a default tolerance
         * based on the numeric type.
         */
        """
        pass

    def almost_equal(self, LVecBase2i_self, const_LVecBase2i_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        almost_equal(LVecBase2i self, const LVecBase2i other)
        almost_equal(LVecBase2i self, const LVecBase2i other, int threshold)
        
        /**
         * Returns true if two vectors are memberwise equal within a specified
         * tolerance.
         */
        
        /**
         * Returns true if two vectors are memberwise equal within a default tolerance
         * based on the numeric type.
         */
        """
        pass

    def assign(self, const_LVecBase2i_self, const_LVecBase2i_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const LVecBase2i self, const LVecBase2i copy)
        assign(const LVecBase2i self, int fill_value)
        """
        pass

    def Ceil(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        __ceil__(const LVecBase2i self)
        """
        pass

    def compareTo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        compare_to(LVecBase2i self, const LVecBase2i other)
        
        /**
         * This flavor of compare_to uses a default threshold value based on the
         * numeric type.
         */
        """
        pass

    def compare_to(self, LVecBase2i_self, const_LVecBase2i_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        compare_to(LVecBase2i self, const LVecBase2i other)
        
        /**
         * This flavor of compare_to uses a default threshold value based on the
         * numeric type.
         */
        """
        pass

    def componentwiseMult(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        componentwise_mult(const LVecBase2i self, const LVecBase2i other)
        
        /**
         *
         */
        """
        pass

    def componentwise_mult(self, const_LVecBase2i_self, const_LVecBase2i_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        componentwise_mult(const LVecBase2i self, const LVecBase2i other)
        
        /**
         *
         */
        """
        pass

    def dot(self, LVecBase2i_self, const_LVecBase2i_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        dot(LVecBase2i self, const LVecBase2i other)
        
        /**
         *
         */
        """
        pass

    def fill(self, const_LVecBase2i_self, int_fill_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        fill(const LVecBase2i self, int fill_value)
        
        /**
         * Sets each element of the vector to the indicated fill_value.  This is
         * particularly useful for initializing to zero.
         */
        """
        pass

    def Floor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        __floor__(const LVecBase2i self)
        """
        pass

    def fmax(self, LVecBase2i_self, const_LVecBase2i_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        fmax(LVecBase2i self, const LVecBase2i other)
        
        /**
         *
         */
        """
        pass

    def fmin(self, LVecBase2i_self, const_LVecBase2i_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        fmin(LVecBase2i self, const LVecBase2i other)
        
        /**
         *
         */
        """
        pass

    def getCell(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_cell(LVecBase2i self, int i)
        
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

    def getHash(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_hash(LVecBase2i self)
        
        /**
         * Returns a suitable hash for phash_map.
         */
        """
        pass

    def getNumComponents(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_components()
        """
        pass

    def getX(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_x(LVecBase2i self)
        
        /**
         *
         */
        """
        pass

    def getY(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_y(LVecBase2i self)
        
        /**
         *
         */
        """
        pass

    def get_cell(self, LVecBase2i_self, int_i): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_cell(LVecBase2i self, int i)
        
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

    def get_hash(self, LVecBase2i_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_hash(LVecBase2i self)
        
        /**
         * Returns a suitable hash for phash_map.
         */
        """
        pass

    def get_num_components(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_components()
        """
        pass

    def get_x(self, LVecBase2i_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_x(LVecBase2i self)
        
        /**
         *
         */
        """
        pass

    def get_y(self, LVecBase2i_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_y(LVecBase2i self)
        
        /**
         *
         */
        """
        pass

    def isNan(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_nan(LVecBase2i self)
        
        /**
         * Returns true if any component of the vector is not-a-number, false
         * otherwise.
         */
        """
        pass

    def is_nan(self, LVecBase2i_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_nan(LVecBase2i self)
        
        /**
         * Returns true if any component of the vector is not-a-number, false
         * otherwise.
         */
        """
        pass

    def lengthSquared(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        length_squared(LVecBase2i self)
        
        /**
         * Returns the square of the vector's length, cheap and easy.
         */
        """
        pass

    def length_squared(self, LVecBase2i_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        length_squared(LVecBase2i self)
        
        /**
         * Returns the square of the vector's length, cheap and easy.
         */
        """
        pass

    def output(self, LVecBase2i_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(LVecBase2i self, ostream out)
        
        /**
         *
         */
        """
        pass

    def readDatagram(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        read_datagram(const LVecBase2i self, DatagramIterator source)
        
        /**
         * Reads the vector from the Datagram using get_stdfloat().
         */
        """
        pass

    def readDatagramFixed(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        read_datagram_fixed(const LVecBase2i self, DatagramIterator source)
        
        /**
         * Reads the vector from the Datagram using get_float32() or get_float64().
         * See write_datagram_fixed().
         */
        """
        pass

    def read_datagram(self, const_LVecBase2i_self, DatagramIterator_source): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        read_datagram(const LVecBase2i self, DatagramIterator source)
        
        /**
         * Reads the vector from the Datagram using get_stdfloat().
         */
        """
        pass

    def read_datagram_fixed(self, const_LVecBase2i_self, DatagramIterator_source): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        read_datagram_fixed(const LVecBase2i self, DatagramIterator source)
        
        /**
         * Reads the vector from the Datagram using get_float32() or get_float64().
         * See write_datagram_fixed().
         */
        """
        pass

    def Round(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        __round__(const LVecBase2i self)
        """
        pass

    def set(self, const_LVecBase2i_self, int_x, int_y): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set(const LVecBase2i self, int x, int y)
        
        /**
         *
         */
        """
        pass

    def setCell(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_cell(const LVecBase2i self, int i, int value)
        
        /**
         *
         */
        """
        pass

    def setX(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_x(const LVecBase2i self, int value)
        
        /**
         *
         */
        """
        pass

    def setY(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_y(const LVecBase2i self, int value)
        
        /**
         *
         */
        """
        pass

    def set_cell(self, const_LVecBase2i_self, int_i, int_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_cell(const LVecBase2i self, int i, int value)
        
        /**
         *
         */
        """
        pass

    def set_x(self, const_LVecBase2i_self, int_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_x(const LVecBase2i self, int value)
        
        /**
         *
         */
        """
        pass

    def set_y(self, const_LVecBase2i_self, int_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_y(const LVecBase2i self, int value)
        
        /**
         *
         */
        """
        pass

    def unitX(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        unit_x()
        
        /**
         * Returns a unit X vector.
         */
        """
        pass

    def unitY(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        unit_y()
        
        /**
         * Returns a unit Y vector.
         */
        """
        pass

    def unit_x(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        unit_x()
        
        /**
         * Returns a unit X vector.
         */
        """
        pass

    def unit_y(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        unit_y()
        
        /**
         * Returns a unit Y vector.
         */
        """
        pass

    def writeDatagram(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        write_datagram(LVecBase2i self, Datagram destination)
        
        /**
         * Writes the vector to the Datagram using add_stdfloat().  This is
         * appropriate when you want to write the vector using the standard width
         * setting, especially when you are writing a bam file.
         */
        """
        pass

    def writeDatagramFixed(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        write_datagram_fixed(LVecBase2i self, Datagram destination)
        
        /**
         * Writes the vector to the Datagram using add_float32() or add_float64(),
         * depending on the type of floats in the vector, regardless of the setting of
         * Datagram::set_stdfloat_double().  This is appropriate when you want to
         * write a fixed-width value to the datagram, especially when you are not
         * writing a bam file.
         */
        """
        pass

    def write_datagram(self, LVecBase2i_self, Datagram_destination): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write_datagram(LVecBase2i self, Datagram destination)
        
        /**
         * Writes the vector to the Datagram using add_stdfloat().  This is
         * appropriate when you want to write the vector using the standard width
         * setting, especially when you are writing a bam file.
         */
        """
        pass

    def write_datagram_fixed(self, LVecBase2i_self, Datagram_destination): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write_datagram_fixed(LVecBase2i self, Datagram destination)
        
        /**
         * Writes the vector to the Datagram using add_float32() or add_float64(),
         * depending on the type of floats in the vector, regardless of the setting of
         * Datagram::set_stdfloat_double().  This is appropriate when you want to
         * write a fixed-width value to the datagram, especially when you are not
         * writing a bam file.
         */
        """
        pass

    def zero(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        zero()
        
        /**
         * Returns a zero-length vector.
         */
        """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __ceil__(self, const_LVecBase2i_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        __ceil__(const LVecBase2i self)
        """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __delitem__(self, *args, **kwargs): # real signature unknown
        """ Delete self[key]. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
        pass

    def __floor__(self, const_LVecBase2i_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        __floor__(const LVecBase2i self)
        """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
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

    def __iadd__(self, *args, **kwargs): # real signature unknown
        """ Return self+=value. """
        pass

    def __ifloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//=value. """
        pass

    def __imul__(self, *args, **kwargs): # real signature unknown
        """ Return self*=value. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __ipow__(self, *args, **kwargs): # real signature unknown
        """ Return self**=value. """
        pass

    def __isub__(self, *args, **kwargs): # real signature unknown
        """ Return self-=value. """
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __pow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(self, value, mod). """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __reduce__(self, LVecBase2i_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        __reduce__(LVecBase2i self)
        """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __round__(self, const_LVecBase2i_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        __round__(const LVecBase2i self)
        """
        pass

    def __rpow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(value, self, mod). """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """ Set self[key] to value. """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    x = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'Ceil': None, # (!) real value is "<method 'Ceil' of 'panda3d.core.LVecBase2i' objects>"
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'Floor': None, # (!) real value is "<method 'Floor' of 'panda3d.core.LVecBase2i' objects>"
        'Round': None, # (!) real value is "<method 'Round' of 'panda3d.core.LVecBase2i' objects>"
        '__add__': None, # (!) real value is "<slot wrapper '__add__' of 'panda3d.core.LVecBase2i' objects>"
        '__ceil__': None, # (!) real value is "<method '__ceil__' of 'panda3d.core.LVecBase2i' objects>"
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.LVecBase2i' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.LVecBase2i' objects>"
        '__delattr__': None, # (!) real value is "<slot wrapper '__delattr__' of 'panda3d.core.LVecBase2i' objects>"
        '__delitem__': None, # (!) real value is "<slot wrapper '__delitem__' of 'panda3d.core.LVecBase2i' objects>"
        '__doc__': '/**\n * This is the base class for all two-component vectors and points.\n */',
        '__eq__': None, # (!) real value is "<slot wrapper '__eq__' of 'panda3d.core.LVecBase2i' objects>"
        '__floor__': None, # (!) real value is "<method '__floor__' of 'panda3d.core.LVecBase2i' objects>"
        '__floordiv__': None, # (!) real value is "<slot wrapper '__floordiv__' of 'panda3d.core.LVecBase2i' objects>"
        '__ge__': None, # (!) real value is "<slot wrapper '__ge__' of 'panda3d.core.LVecBase2i' objects>"
        '__getattribute__': None, # (!) real value is "<slot wrapper '__getattribute__' of 'panda3d.core.LVecBase2i' objects>"
        '__getitem__': None, # (!) real value is "<slot wrapper '__getitem__' of 'panda3d.core.LVecBase2i' objects>"
        '__gt__': None, # (!) real value is "<slot wrapper '__gt__' of 'panda3d.core.LVecBase2i' objects>"
        '__hash__': None, # (!) real value is "<slot wrapper '__hash__' of 'panda3d.core.LVecBase2i' objects>"
        '__iadd__': None, # (!) real value is "<slot wrapper '__iadd__' of 'panda3d.core.LVecBase2i' objects>"
        '__ifloordiv__': None, # (!) real value is "<slot wrapper '__ifloordiv__' of 'panda3d.core.LVecBase2i' objects>"
        '__imul__': None, # (!) real value is "<slot wrapper '__imul__' of 'panda3d.core.LVecBase2i' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.LVecBase2i' objects>"
        '__ipow__': None, # (!) real value is "<slot wrapper '__ipow__' of 'panda3d.core.LVecBase2i' objects>"
        '__isub__': None, # (!) real value is "<slot wrapper '__isub__' of 'panda3d.core.LVecBase2i' objects>"
        '__le__': None, # (!) real value is "<slot wrapper '__le__' of 'panda3d.core.LVecBase2i' objects>"
        '__len__': None, # (!) real value is "<slot wrapper '__len__' of 'panda3d.core.LVecBase2i' objects>"
        '__lt__': None, # (!) real value is "<slot wrapper '__lt__' of 'panda3d.core.LVecBase2i' objects>"
        '__mul__': None, # (!) real value is "<slot wrapper '__mul__' of 'panda3d.core.LVecBase2i' objects>"
        '__ne__': None, # (!) real value is "<slot wrapper '__ne__' of 'panda3d.core.LVecBase2i' objects>"
        '__neg__': None, # (!) real value is "<slot wrapper '__neg__' of 'panda3d.core.LVecBase2i' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE320A70>'
        '__pow__': None, # (!) real value is "<slot wrapper '__pow__' of 'panda3d.core.LVecBase2i' objects>"
        '__radd__': None, # (!) real value is "<slot wrapper '__radd__' of 'panda3d.core.LVecBase2i' objects>"
        '__reduce__': None, # (!) real value is "<method '__reduce__' of 'panda3d.core.LVecBase2i' objects>"
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.LVecBase2i' objects>"
        '__rfloordiv__': None, # (!) real value is "<slot wrapper '__rfloordiv__' of 'panda3d.core.LVecBase2i' objects>"
        '__rmul__': None, # (!) real value is "<slot wrapper '__rmul__' of 'panda3d.core.LVecBase2i' objects>"
        '__round__': None, # (!) real value is "<method '__round__' of 'panda3d.core.LVecBase2i' objects>"
        '__rpow__': None, # (!) real value is "<slot wrapper '__rpow__' of 'panda3d.core.LVecBase2i' objects>"
        '__rsub__': None, # (!) real value is "<slot wrapper '__rsub__' of 'panda3d.core.LVecBase2i' objects>"
        '__setattr__': None, # (!) real value is "<slot wrapper '__setattr__' of 'panda3d.core.LVecBase2i' objects>"
        '__setitem__': None, # (!) real value is "<slot wrapper '__setitem__' of 'panda3d.core.LVecBase2i' objects>"
        '__sub__': None, # (!) real value is "<slot wrapper '__sub__' of 'panda3d.core.LVecBase2i' objects>"
        'addHash': None, # (!) real value is "<method 'addHash' of 'panda3d.core.LVecBase2i' objects>"
        'addToCell': None, # (!) real value is "<method 'addToCell' of 'panda3d.core.LVecBase2i' objects>"
        'addX': None, # (!) real value is "<method 'addX' of 'panda3d.core.LVecBase2i' objects>"
        'addY': None, # (!) real value is "<method 'addY' of 'panda3d.core.LVecBase2i' objects>"
        'add_hash': None, # (!) real value is "<method 'add_hash' of 'panda3d.core.LVecBase2i' objects>"
        'add_to_cell': None, # (!) real value is "<method 'add_to_cell' of 'panda3d.core.LVecBase2i' objects>"
        'add_x': None, # (!) real value is "<method 'add_x' of 'panda3d.core.LVecBase2i' objects>"
        'add_y': None, # (!) real value is "<method 'add_y' of 'panda3d.core.LVecBase2i' objects>"
        'almostEqual': None, # (!) real value is "<method 'almostEqual' of 'panda3d.core.LVecBase2i' objects>"
        'almost_equal': None, # (!) real value is "<method 'almost_equal' of 'panda3d.core.LVecBase2i' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.LVecBase2i' objects>"
        'compareTo': None, # (!) real value is "<method 'compareTo' of 'panda3d.core.LVecBase2i' objects>"
        'compare_to': None, # (!) real value is "<method 'compare_to' of 'panda3d.core.LVecBase2i' objects>"
        'componentwiseMult': None, # (!) real value is "<method 'componentwiseMult' of 'panda3d.core.LVecBase2i' objects>"
        'componentwise_mult': None, # (!) real value is "<method 'componentwise_mult' of 'panda3d.core.LVecBase2i' objects>"
        'dot': None, # (!) real value is "<method 'dot' of 'panda3d.core.LVecBase2i' objects>"
        'fill': None, # (!) real value is "<method 'fill' of 'panda3d.core.LVecBase2i' objects>"
        'fmax': None, # (!) real value is "<method 'fmax' of 'panda3d.core.LVecBase2i' objects>"
        'fmin': None, # (!) real value is "<method 'fmin' of 'panda3d.core.LVecBase2i' objects>"
        'getCell': None, # (!) real value is "<method 'getCell' of 'panda3d.core.LVecBase2i' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE320A70>)>'
        'getHash': None, # (!) real value is "<method 'getHash' of 'panda3d.core.LVecBase2i' objects>"
        'getNumComponents': None, # (!) real value is '<staticmethod(<built-in method getNumComponents of type object at 0x00007FFCFE320A70>)>'
        'getX': None, # (!) real value is "<method 'getX' of 'panda3d.core.LVecBase2i' objects>"
        'getY': None, # (!) real value is "<method 'getY' of 'panda3d.core.LVecBase2i' objects>"
        'get_cell': None, # (!) real value is "<method 'get_cell' of 'panda3d.core.LVecBase2i' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE320A70>)>'
        'get_hash': None, # (!) real value is "<method 'get_hash' of 'panda3d.core.LVecBase2i' objects>"
        'get_num_components': None, # (!) real value is '<staticmethod(<built-in method get_num_components of type object at 0x00007FFCFE320A70>)>'
        'get_x': None, # (!) real value is "<method 'get_x' of 'panda3d.core.LVecBase2i' objects>"
        'get_y': None, # (!) real value is "<method 'get_y' of 'panda3d.core.LVecBase2i' objects>"
        'isNan': None, # (!) real value is "<method 'isNan' of 'panda3d.core.LVecBase2i' objects>"
        'is_int': 1,
        'is_nan': None, # (!) real value is "<method 'is_nan' of 'panda3d.core.LVecBase2i' objects>"
        'lengthSquared': None, # (!) real value is "<method 'lengthSquared' of 'panda3d.core.LVecBase2i' objects>"
        'length_squared': None, # (!) real value is "<method 'length_squared' of 'panda3d.core.LVecBase2i' objects>"
        'num_components': 2,
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.LVecBase2i' objects>"
        'readDatagram': None, # (!) real value is "<method 'readDatagram' of 'panda3d.core.LVecBase2i' objects>"
        'readDatagramFixed': None, # (!) real value is "<method 'readDatagramFixed' of 'panda3d.core.LVecBase2i' objects>"
        'read_datagram': None, # (!) real value is "<method 'read_datagram' of 'panda3d.core.LVecBase2i' objects>"
        'read_datagram_fixed': None, # (!) real value is "<method 'read_datagram_fixed' of 'panda3d.core.LVecBase2i' objects>"
        'set': None, # (!) real value is "<method 'set' of 'panda3d.core.LVecBase2i' objects>"
        'setCell': None, # (!) real value is "<method 'setCell' of 'panda3d.core.LVecBase2i' objects>"
        'setX': None, # (!) real value is "<method 'setX' of 'panda3d.core.LVecBase2i' objects>"
        'setY': None, # (!) real value is "<method 'setY' of 'panda3d.core.LVecBase2i' objects>"
        'set_cell': None, # (!) real value is "<method 'set_cell' of 'panda3d.core.LVecBase2i' objects>"
        'set_x': None, # (!) real value is "<method 'set_x' of 'panda3d.core.LVecBase2i' objects>"
        'set_y': None, # (!) real value is "<method 'set_y' of 'panda3d.core.LVecBase2i' objects>"
        'unitX': None, # (!) real value is '<staticmethod(<built-in method unitX of type object at 0x00007FFCFE320A70>)>'
        'unitY': None, # (!) real value is '<staticmethod(<built-in method unitY of type object at 0x00007FFCFE320A70>)>'
        'unit_x': None, # (!) real value is '<staticmethod(<built-in method unit_x of type object at 0x00007FFCFE320A70>)>'
        'unit_y': None, # (!) real value is '<staticmethod(<built-in method unit_y of type object at 0x00007FFCFE320A70>)>'
        'writeDatagram': None, # (!) real value is "<method 'writeDatagram' of 'panda3d.core.LVecBase2i' objects>"
        'writeDatagramFixed': None, # (!) real value is "<method 'writeDatagramFixed' of 'panda3d.core.LVecBase2i' objects>"
        'write_datagram': None, # (!) real value is "<method 'write_datagram' of 'panda3d.core.LVecBase2i' objects>"
        'write_datagram_fixed': None, # (!) real value is "<method 'write_datagram_fixed' of 'panda3d.core.LVecBase2i' objects>"
        'x': None, # (!) real value is "<attribute 'x' of 'panda3d.core.LVecBase2i' objects>"
        'y': None, # (!) real value is "<attribute 'y' of 'panda3d.core.LVecBase2i' objects>"
        'zero': None, # (!) real value is '<staticmethod(<built-in method zero of type object at 0x00007FFCFE320A70>)>'
    }
    is_int = 1
    num_components = 2


