# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class SparseArray(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This class records a set of integers, where each integer is either present
     * or not present in the set.
     *
     * It is similar in principle and in interface to a BitArray (which can be
     * thought of as a set of integers, one integer corresponding to each
     * different bit position), but the SparseArray is implemented as a list of
     * min/max subrange lists, rather than as a bitmask.
     *
     * This makes it particularly efficient for storing sets which consist of
     * large sections of consecutively included or consecutively excluded
     * elements, with arbitrarily large integers, but particularly inefficient for
     * doing boolean operations such as & or |.
     *
     * Also, unlike BitArray, the SparseArray can store negative integers.
     */
    """
    def allOff(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        all_off()
        
        /**
         * Returns a SparseArray whose bits are all off.
         */
        """
        pass

    def allOn(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        all_on()
        
        /**
         * Returns a SparseArray with an infinite array of bits, all on.
         */
        """
        pass

    def all_off(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        all_off()
        
        /**
         * Returns a SparseArray whose bits are all off.
         */
        """
        pass

    def all_on(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        all_on()
        
        /**
         * Returns a SparseArray with an infinite array of bits, all on.
         */
        """
        pass

    def bit(self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        bit(int index)
        
        /**
         * Returns a SparseArray with only the indicated bit on.
         */
        """
        pass

    def clear(self, const_SparseArray_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear(const SparseArray self)
        
        /**
         * Sets all the bits in the SparseArray off.
         */
        """
        pass

    def clearBit(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_bit(const SparseArray self, int index)
        
        /**
         * Sets the nth bit off.  If n >= get_num_bits(), this automatically extends
         * the array.
         */
        """
        pass

    def clearRange(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_range(const SparseArray self, int low_bit, int size)
        
        /**
         * Sets the indicated range of bits off.
         */
        """
        pass

    def clear_bit(self, const_SparseArray_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_bit(const SparseArray self, int index)
        
        /**
         * Sets the nth bit off.  If n >= get_num_bits(), this automatically extends
         * the array.
         */
        """
        pass

    def clear_range(self, const_SparseArray_self, int_low_bit, int_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_range(const SparseArray self, int low_bit, int size)
        
        /**
         * Sets the indicated range of bits off.
         */
        """
        pass

    def compareTo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        compare_to(SparseArray self, const SparseArray other)
        
        /**
         * Returns a number less than zero if this SparseArray sorts before the
         * indicated other SparseArray, greater than zero if it sorts after, or 0 if
         * they are equivalent.  This is based on the same ordering defined by
         * operator <.
         */
        """
        pass

    def compare_to(self, SparseArray_self, const_SparseArray_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        compare_to(SparseArray self, const SparseArray other)
        
        /**
         * Returns a number less than zero if this SparseArray sorts before the
         * indicated other SparseArray, greater than zero if it sorts after, or 0 if
         * they are equivalent.  This is based on the same ordering defined by
         * operator <.
         */
        """
        pass

    def getBit(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_bit(SparseArray self, int index)
        
        /**
         * Returns true if the nth bit is set, false if it is cleared.  It is valid
         * for n to increase beyond get_num_bits(), but the return value
         * get_num_bits() will always be the same.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getHighestBits(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_highest_bits(SparseArray self)
        
        /**
         * Returns true if the infinite set of bits beyond get_num_bits() are all on,
         * or false of they are all off.
         */
        """
        pass

    def getHighestOffBit(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_highest_off_bit(SparseArray self)
        
        /**
         * Returns the index of the highest 0 bit in the array.  Returns -1 if there
         * are no 0 bits or if there an infinite number of 1 bits.
         */
        """
        pass

    def getHighestOnBit(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_highest_on_bit(SparseArray self)
        
        /**
         * Returns the index of the highest 1 bit in the array.  Returns -1 if there
         * are no 1 bits or if there an infinite number of 1 bits.
         */
        """
        pass

    def getLowestOffBit(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_lowest_off_bit(SparseArray self)
        
        /**
         * Returns the index of the lowest 0 bit in the array.  Returns -1 if there
         * are no 0 bits or if there are an infinite number of 1 bits.
         */
        """
        pass

    def getLowestOnBit(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_lowest_on_bit(SparseArray self)
        
        /**
         * Returns the index of the lowest 1 bit in the array.  Returns -1 if there
         * are no 1 bits or if there are an infinite number of 1 bits.
         */
        """
        pass

    def getMaxNumBits(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_max_num_bits()
        
        /**
         * If get_max_num_bits() returned true, this method may be called to return
         * the maximum number of bits that may be stored in this structure.  It is an
         * error to call this if get_max_num_bits() return false.
         *
         * It is always an error to call this method.  The SparseArray has no maximum
         * number of bits.  This method is defined so generic programming algorithms
         * can use BitMask or SparseArray interchangeably.
         */
        """
        pass

    def getNextHigherDifferentBit(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_next_higher_different_bit(SparseArray self, int low_bit)
        
        /**
         * Returns the index of the next bit in the array, above low_bit, whose value
         * is different that the value of low_bit.  Returns low_bit again if all bits
         * higher than low_bit have the same value.
         *
         * This can be used to quickly iterate through all of the bits in the array.
         */
        """
        pass

    def getNumBits(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_bits(SparseArray self)
        
        /**
         * Returns the current number of possibly different bits in this array.  There
         * are actually an infinite number of bits, but every bit higher than this bit
         * will have the same value, either 0 or 1 (see get_highest_bits()).
         *
         * This number may grow and/or shrink automatically as needed.
         */
        """
        pass

    def getNumOffBits(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_off_bits(SparseArray self)
        
        /**
         * Returns the number of bits that are set to 0 in the array.  Returns -1 if
         * there are an infinite number of 0 bits.
         */
        """
        pass

    def getNumOnBits(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_on_bits(SparseArray self)
        
        /**
         * Returns the number of bits that are set to 1 in the array.  Returns -1 if
         * there are an infinite number of 1 bits.
         */
        """
        pass

    def getNumSubranges(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_subranges(SparseArray self)
        
        /**
         * Returns the number of separate subranges stored in the SparseArray.  You
         * can use this limit to iterate through the subranges, calling
         * get_subrange_begin() and get_subrange_end() for each one.
         *
         * Also see is_inverse().
         */
        """
        pass

    def getSubrangeBegin(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_subrange_begin(SparseArray self, int n)
        
        /**
         * Returns the first numeric element in the nth subrange.
         *
         * Also see is_inverse().
         */
        """
        pass

    def getSubrangeEnd(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_subrange_end(SparseArray self, int n)
        
        /**
         * Returns the last numeric element, plus one, in the nth subrange.
         *
         * Also see is_inverse().
         */
        """
        pass

    def get_bit(self, SparseArray_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_bit(SparseArray self, int index)
        
        /**
         * Returns true if the nth bit is set, false if it is cleared.  It is valid
         * for n to increase beyond get_num_bits(), but the return value
         * get_num_bits() will always be the same.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_highest_bits(self, SparseArray_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_highest_bits(SparseArray self)
        
        /**
         * Returns true if the infinite set of bits beyond get_num_bits() are all on,
         * or false of they are all off.
         */
        """
        pass

    def get_highest_off_bit(self, SparseArray_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_highest_off_bit(SparseArray self)
        
        /**
         * Returns the index of the highest 0 bit in the array.  Returns -1 if there
         * are no 0 bits or if there an infinite number of 1 bits.
         */
        """
        pass

    def get_highest_on_bit(self, SparseArray_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_highest_on_bit(SparseArray self)
        
        /**
         * Returns the index of the highest 1 bit in the array.  Returns -1 if there
         * are no 1 bits or if there an infinite number of 1 bits.
         */
        """
        pass

    def get_lowest_off_bit(self, SparseArray_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_lowest_off_bit(SparseArray self)
        
        /**
         * Returns the index of the lowest 0 bit in the array.  Returns -1 if there
         * are no 0 bits or if there are an infinite number of 1 bits.
         */
        """
        pass

    def get_lowest_on_bit(self, SparseArray_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_lowest_on_bit(SparseArray self)
        
        /**
         * Returns the index of the lowest 1 bit in the array.  Returns -1 if there
         * are no 1 bits or if there are an infinite number of 1 bits.
         */
        """
        pass

    def get_max_num_bits(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_max_num_bits()
        
        /**
         * If get_max_num_bits() returned true, this method may be called to return
         * the maximum number of bits that may be stored in this structure.  It is an
         * error to call this if get_max_num_bits() return false.
         *
         * It is always an error to call this method.  The SparseArray has no maximum
         * number of bits.  This method is defined so generic programming algorithms
         * can use BitMask or SparseArray interchangeably.
         */
        """
        pass

    def get_next_higher_different_bit(self, SparseArray_self, int_low_bit): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_next_higher_different_bit(SparseArray self, int low_bit)
        
        /**
         * Returns the index of the next bit in the array, above low_bit, whose value
         * is different that the value of low_bit.  Returns low_bit again if all bits
         * higher than low_bit have the same value.
         *
         * This can be used to quickly iterate through all of the bits in the array.
         */
        """
        pass

    def get_num_bits(self, SparseArray_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_bits(SparseArray self)
        
        /**
         * Returns the current number of possibly different bits in this array.  There
         * are actually an infinite number of bits, but every bit higher than this bit
         * will have the same value, either 0 or 1 (see get_highest_bits()).
         *
         * This number may grow and/or shrink automatically as needed.
         */
        """
        pass

    def get_num_off_bits(self, SparseArray_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_off_bits(SparseArray self)
        
        /**
         * Returns the number of bits that are set to 0 in the array.  Returns -1 if
         * there are an infinite number of 0 bits.
         */
        """
        pass

    def get_num_on_bits(self, SparseArray_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_on_bits(SparseArray self)
        
        /**
         * Returns the number of bits that are set to 1 in the array.  Returns -1 if
         * there are an infinite number of 1 bits.
         */
        """
        pass

    def get_num_subranges(self, SparseArray_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_subranges(SparseArray self)
        
        /**
         * Returns the number of separate subranges stored in the SparseArray.  You
         * can use this limit to iterate through the subranges, calling
         * get_subrange_begin() and get_subrange_end() for each one.
         *
         * Also see is_inverse().
         */
        """
        pass

    def get_subrange_begin(self, SparseArray_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_subrange_begin(SparseArray self, int n)
        
        /**
         * Returns the first numeric element in the nth subrange.
         *
         * Also see is_inverse().
         */
        """
        pass

    def get_subrange_end(self, SparseArray_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_subrange_end(SparseArray self, int n)
        
        /**
         * Returns the last numeric element, plus one, in the nth subrange.
         *
         * Also see is_inverse().
         */
        """
        pass

    def hasAllOf(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_all_of(SparseArray self, int low_bit, int size)
        
        /**
         * Returns true if all bits in the indicated range are set, false otherwise.
         */
        """
        pass

    def hasAnyOf(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_any_of(SparseArray self, int low_bit, int size)
        
        /**
         * Returns true if any bit in the indicated range is set, false otherwise.
         */
        """
        pass

    def hasBitsInCommon(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_bits_in_common(SparseArray self, const SparseArray other)
        
        /**
         * Returns true if this SparseArray has any "one" bits in common with the
         * other one, false otherwise.
         *
         * This is equivalent to (array & other) != 0, but may be faster.
         */
        """
        pass

    def hasMaxNumBits(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_max_num_bits()
        
        /**
         * Returns true if there is a maximum number of bits that may be stored in
         * this structure, false otherwise.  If this returns true, the number may be
         * queried in get_max_num_bits().
         *
         * This method always returns false.  The SparseArray has no maximum number of
         * bits.  This method is defined so generic programming algorithms can use
         * BitMask or SparseArray interchangeably.
         */
        """
        pass

    def has_all_of(self, SparseArray_self, int_low_bit, int_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_all_of(SparseArray self, int low_bit, int size)
        
        /**
         * Returns true if all bits in the indicated range are set, false otherwise.
         */
        """
        pass

    def has_any_of(self, SparseArray_self, int_low_bit, int_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_any_of(SparseArray self, int low_bit, int size)
        
        /**
         * Returns true if any bit in the indicated range is set, false otherwise.
         */
        """
        pass

    def has_bits_in_common(self, SparseArray_self, const_SparseArray_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_bits_in_common(SparseArray self, const SparseArray other)
        
        /**
         * Returns true if this SparseArray has any "one" bits in common with the
         * other one, false otherwise.
         *
         * This is equivalent to (array & other) != 0, but may be faster.
         */
        """
        pass

    def has_max_num_bits(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_max_num_bits()
        
        /**
         * Returns true if there is a maximum number of bits that may be stored in
         * this structure, false otherwise.  If this returns true, the number may be
         * queried in get_max_num_bits().
         *
         * This method always returns false.  The SparseArray has no maximum number of
         * bits.  This method is defined so generic programming algorithms can use
         * BitMask or SparseArray interchangeably.
         */
        """
        pass

    def invertInPlace(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        invert_in_place(const SparseArray self)
        
        /**
         * Inverts all the bits in the SparseArray.  This is equivalent to array =
         * ~array.
         */
        """
        pass

    def invert_in_place(self, const_SparseArray_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        invert_in_place(const SparseArray self)
        
        /**
         * Inverts all the bits in the SparseArray.  This is equivalent to array =
         * ~array.
         */
        """
        pass

    def isAllOn(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_all_on(SparseArray self)
        
        /**
         * Returns true if the entire bitmask is one, false otherwise.
         */
        """
        pass

    def isInverse(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_inverse(SparseArray self)
        
        /**
         * If this is true, the SparseArray is actually defined as a list of subranges
         * of integers that are *not* in the set.  If this is false (the default),
         * then the subranges define the integers that *are* in the set.  This affects
         * the interpretation of the values returned by iterating through
         * get_num_subranges().
         */
        """
        pass

    def isZero(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_zero(SparseArray self)
        
        /**
         * Returns true if the entire bitmask is zero, false otherwise.
         */
        """
        pass

    def is_all_on(self, SparseArray_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_all_on(SparseArray self)
        
        /**
         * Returns true if the entire bitmask is one, false otherwise.
         */
        """
        pass

    def is_inverse(self, SparseArray_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_inverse(SparseArray self)
        
        /**
         * If this is true, the SparseArray is actually defined as a list of subranges
         * of integers that are *not* in the set.  If this is false (the default),
         * then the subranges define the integers that *are* in the set.  This affects
         * the interpretation of the values returned by iterating through
         * get_num_subranges().
         */
        """
        pass

    def is_zero(self, SparseArray_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_zero(SparseArray self)
        
        /**
         * Returns true if the entire bitmask is zero, false otherwise.
         */
        """
        pass

    def lowerOn(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        lower_on(int on_bits)
        
        /**
         * Returns a SparseArray whose lower on_bits bits are on.
         */
        """
        pass

    def lower_on(self, int_on_bits): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        lower_on(int on_bits)
        
        /**
         * Returns a SparseArray whose lower on_bits bits are on.
         */
        """
        pass

    def output(self, SparseArray_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(SparseArray self, ostream out)
        
        /**
         *
         */
        """
        pass

    def range(self, int_low_bit, int_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        range(int low_bit, int size)
        
        /**
         * Returns a SparseArray whose size bits, beginning at low_bit, are on.
         */
        """
        pass

    def setBit(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_bit(const SparseArray self, int index)
        
        /**
         * Sets the nth bit on.  If n >= get_num_bits(), this automatically extends
         * the array.
         */
        """
        pass

    def setBitTo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_bit_to(const SparseArray self, int index, bool value)
        
        /**
         * Sets the nth bit either on or off, according to the indicated bool value.
         */
        """
        pass

    def setRange(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_range(const SparseArray self, int low_bit, int size)
        
        /**
         * Sets the indicated range of bits on.
         */
        """
        pass

    def setRangeTo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_range_to(const SparseArray self, bool value, int low_bit, int size)
        
        /**
         * Sets the indicated range of bits to either on or off.
         */
        """
        pass

    def set_bit(self, const_SparseArray_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_bit(const SparseArray self, int index)
        
        /**
         * Sets the nth bit on.  If n >= get_num_bits(), this automatically extends
         * the array.
         */
        """
        pass

    def set_bit_to(self, const_SparseArray_self, int_index, bool_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_bit_to(const SparseArray self, int index, bool value)
        
        /**
         * Sets the nth bit either on or off, according to the indicated bool value.
         */
        """
        pass

    def set_range(self, const_SparseArray_self, int_low_bit, int_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_range(const SparseArray self, int low_bit, int size)
        
        /**
         * Sets the indicated range of bits on.
         */
        """
        pass

    def set_range_to(self, const_SparseArray_self, bool_value, int_low_bit, int_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_range_to(const SparseArray self, bool value, int low_bit, int size)
        
        /**
         * Sets the indicated range of bits to either on or off.
         */
        """
        pass

    def __and__(self, *args, **kwargs): # real signature unknown
        """ Return self&value. """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getstate__(self, SparseArray_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        __getstate__(SparseArray self)
        """
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

    def __iand__(self, *args, **kwargs): # real signature unknown
        """ Return self&=value. """
        pass

    def __ilshift__(self, *args, **kwargs): # real signature unknown
        """ Return self<<=value. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __invert__(self, *args, **kwargs): # real signature unknown
        """ ~self """
        pass

    def __ior__(self, *args, **kwargs): # real signature unknown
        """ Return self|=value. """
        pass

    def __irshift__(self, *args, **kwargs): # real signature unknown
        """ Return self>>=value. """
        pass

    def __ixor__(self, *args, **kwargs): # real signature unknown
        """ Return self^=value. """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lshift__(self, *args, **kwargs): # real signature unknown
        """ Return self<<value. """
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

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __rand__(self, *args, **kwargs): # real signature unknown
        """ Return value&self. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, *args, **kwargs): # real signature unknown
        """ Return self>>value. """
        pass

    def __rxor__(self, *args, **kwargs): # real signature unknown
        """ Return value^self. """
        pass

    def __setstate__(self, const_SparseArray_self, object_state): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        __setstate__(const SparseArray self, object state)
        """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    def __xor__(self, *args, **kwargs): # real signature unknown
        """ Return self^value. """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__and__': None, # (!) real value is "<slot wrapper '__and__' of 'panda3d.core.SparseArray' objects>"
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.SparseArray' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.SparseArray' objects>"
        '__doc__': '/**\n * This class records a set of integers, where each integer is either present\n * or not present in the set.\n *\n * It is similar in principle and in interface to a BitArray (which can be\n * thought of as a set of integers, one integer corresponding to each\n * different bit position), but the SparseArray is implemented as a list of\n * min/max subrange lists, rather than as a bitmask.\n *\n * This makes it particularly efficient for storing sets which consist of\n * large sections of consecutively included or consecutively excluded\n * elements, with arbitrarily large integers, but particularly inefficient for\n * doing boolean operations such as & or |.\n *\n * Also, unlike BitArray, the SparseArray can store negative integers.\n */',
        '__eq__': None, # (!) real value is "<slot wrapper '__eq__' of 'panda3d.core.SparseArray' objects>"
        '__ge__': None, # (!) real value is "<slot wrapper '__ge__' of 'panda3d.core.SparseArray' objects>"
        '__getstate__': None, # (!) real value is "<method '__getstate__' of 'panda3d.core.SparseArray' objects>"
        '__gt__': None, # (!) real value is "<slot wrapper '__gt__' of 'panda3d.core.SparseArray' objects>"
        '__hash__': None, # (!) real value is "<slot wrapper '__hash__' of 'panda3d.core.SparseArray' objects>"
        '__iand__': None, # (!) real value is "<slot wrapper '__iand__' of 'panda3d.core.SparseArray' objects>"
        '__ilshift__': None, # (!) real value is "<slot wrapper '__ilshift__' of 'panda3d.core.SparseArray' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.SparseArray' objects>"
        '__invert__': None, # (!) real value is "<slot wrapper '__invert__' of 'panda3d.core.SparseArray' objects>"
        '__ior__': None, # (!) real value is "<slot wrapper '__ior__' of 'panda3d.core.SparseArray' objects>"
        '__irshift__': None, # (!) real value is "<slot wrapper '__irshift__' of 'panda3d.core.SparseArray' objects>"
        '__ixor__': None, # (!) real value is "<slot wrapper '__ixor__' of 'panda3d.core.SparseArray' objects>"
        '__le__': None, # (!) real value is "<slot wrapper '__le__' of 'panda3d.core.SparseArray' objects>"
        '__lshift__': None, # (!) real value is "<slot wrapper '__lshift__' of 'panda3d.core.SparseArray' objects>"
        '__lt__': None, # (!) real value is "<slot wrapper '__lt__' of 'panda3d.core.SparseArray' objects>"
        '__ne__': None, # (!) real value is "<slot wrapper '__ne__' of 'panda3d.core.SparseArray' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE373100>'
        '__or__': None, # (!) real value is "<slot wrapper '__or__' of 'panda3d.core.SparseArray' objects>"
        '__rand__': None, # (!) real value is "<slot wrapper '__rand__' of 'panda3d.core.SparseArray' objects>"
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.SparseArray' objects>"
        '__rlshift__': None, # (!) real value is "<slot wrapper '__rlshift__' of 'panda3d.core.SparseArray' objects>"
        '__ror__': None, # (!) real value is "<slot wrapper '__ror__' of 'panda3d.core.SparseArray' objects>"
        '__rrshift__': None, # (!) real value is "<slot wrapper '__rrshift__' of 'panda3d.core.SparseArray' objects>"
        '__rshift__': None, # (!) real value is "<slot wrapper '__rshift__' of 'panda3d.core.SparseArray' objects>"
        '__rxor__': None, # (!) real value is "<slot wrapper '__rxor__' of 'panda3d.core.SparseArray' objects>"
        '__setstate__': None, # (!) real value is "<method '__setstate__' of 'panda3d.core.SparseArray' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.SparseArray' objects>"
        '__xor__': None, # (!) real value is "<slot wrapper '__xor__' of 'panda3d.core.SparseArray' objects>"
        'allOff': None, # (!) real value is '<staticmethod(<built-in method allOff of type object at 0x00007FFCFE373100>)>'
        'allOn': None, # (!) real value is '<staticmethod(<built-in method allOn of type object at 0x00007FFCFE373100>)>'
        'all_off': None, # (!) real value is '<staticmethod(<built-in method all_off of type object at 0x00007FFCFE373100>)>'
        'all_on': None, # (!) real value is '<staticmethod(<built-in method all_on of type object at 0x00007FFCFE373100>)>'
        'bit': None, # (!) real value is '<staticmethod(<built-in method bit of type object at 0x00007FFCFE373100>)>'
        'clear': None, # (!) real value is "<method 'clear' of 'panda3d.core.SparseArray' objects>"
        'clearBit': None, # (!) real value is "<method 'clearBit' of 'panda3d.core.SparseArray' objects>"
        'clearRange': None, # (!) real value is "<method 'clearRange' of 'panda3d.core.SparseArray' objects>"
        'clear_bit': None, # (!) real value is "<method 'clear_bit' of 'panda3d.core.SparseArray' objects>"
        'clear_range': None, # (!) real value is "<method 'clear_range' of 'panda3d.core.SparseArray' objects>"
        'compareTo': None, # (!) real value is "<method 'compareTo' of 'panda3d.core.SparseArray' objects>"
        'compare_to': None, # (!) real value is "<method 'compare_to' of 'panda3d.core.SparseArray' objects>"
        'getBit': None, # (!) real value is "<method 'getBit' of 'panda3d.core.SparseArray' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE373100>)>'
        'getHighestBits': None, # (!) real value is "<method 'getHighestBits' of 'panda3d.core.SparseArray' objects>"
        'getHighestOffBit': None, # (!) real value is "<method 'getHighestOffBit' of 'panda3d.core.SparseArray' objects>"
        'getHighestOnBit': None, # (!) real value is "<method 'getHighestOnBit' of 'panda3d.core.SparseArray' objects>"
        'getLowestOffBit': None, # (!) real value is "<method 'getLowestOffBit' of 'panda3d.core.SparseArray' objects>"
        'getLowestOnBit': None, # (!) real value is "<method 'getLowestOnBit' of 'panda3d.core.SparseArray' objects>"
        'getMaxNumBits': None, # (!) real value is '<staticmethod(<built-in method getMaxNumBits of type object at 0x00007FFCFE373100>)>'
        'getNextHigherDifferentBit': None, # (!) real value is "<method 'getNextHigherDifferentBit' of 'panda3d.core.SparseArray' objects>"
        'getNumBits': None, # (!) real value is "<method 'getNumBits' of 'panda3d.core.SparseArray' objects>"
        'getNumOffBits': None, # (!) real value is "<method 'getNumOffBits' of 'panda3d.core.SparseArray' objects>"
        'getNumOnBits': None, # (!) real value is "<method 'getNumOnBits' of 'panda3d.core.SparseArray' objects>"
        'getNumSubranges': None, # (!) real value is "<method 'getNumSubranges' of 'panda3d.core.SparseArray' objects>"
        'getSubrangeBegin': None, # (!) real value is "<method 'getSubrangeBegin' of 'panda3d.core.SparseArray' objects>"
        'getSubrangeEnd': None, # (!) real value is "<method 'getSubrangeEnd' of 'panda3d.core.SparseArray' objects>"
        'get_bit': None, # (!) real value is "<method 'get_bit' of 'panda3d.core.SparseArray' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE373100>)>'
        'get_highest_bits': None, # (!) real value is "<method 'get_highest_bits' of 'panda3d.core.SparseArray' objects>"
        'get_highest_off_bit': None, # (!) real value is "<method 'get_highest_off_bit' of 'panda3d.core.SparseArray' objects>"
        'get_highest_on_bit': None, # (!) real value is "<method 'get_highest_on_bit' of 'panda3d.core.SparseArray' objects>"
        'get_lowest_off_bit': None, # (!) real value is "<method 'get_lowest_off_bit' of 'panda3d.core.SparseArray' objects>"
        'get_lowest_on_bit': None, # (!) real value is "<method 'get_lowest_on_bit' of 'panda3d.core.SparseArray' objects>"
        'get_max_num_bits': None, # (!) real value is '<staticmethod(<built-in method get_max_num_bits of type object at 0x00007FFCFE373100>)>'
        'get_next_higher_different_bit': None, # (!) real value is "<method 'get_next_higher_different_bit' of 'panda3d.core.SparseArray' objects>"
        'get_num_bits': None, # (!) real value is "<method 'get_num_bits' of 'panda3d.core.SparseArray' objects>"
        'get_num_off_bits': None, # (!) real value is "<method 'get_num_off_bits' of 'panda3d.core.SparseArray' objects>"
        'get_num_on_bits': None, # (!) real value is "<method 'get_num_on_bits' of 'panda3d.core.SparseArray' objects>"
        'get_num_subranges': None, # (!) real value is "<method 'get_num_subranges' of 'panda3d.core.SparseArray' objects>"
        'get_subrange_begin': None, # (!) real value is "<method 'get_subrange_begin' of 'panda3d.core.SparseArray' objects>"
        'get_subrange_end': None, # (!) real value is "<method 'get_subrange_end' of 'panda3d.core.SparseArray' objects>"
        'hasAllOf': None, # (!) real value is "<method 'hasAllOf' of 'panda3d.core.SparseArray' objects>"
        'hasAnyOf': None, # (!) real value is "<method 'hasAnyOf' of 'panda3d.core.SparseArray' objects>"
        'hasBitsInCommon': None, # (!) real value is "<method 'hasBitsInCommon' of 'panda3d.core.SparseArray' objects>"
        'hasMaxNumBits': None, # (!) real value is '<staticmethod(<built-in method hasMaxNumBits of type object at 0x00007FFCFE373100>)>'
        'has_all_of': None, # (!) real value is "<method 'has_all_of' of 'panda3d.core.SparseArray' objects>"
        'has_any_of': None, # (!) real value is "<method 'has_any_of' of 'panda3d.core.SparseArray' objects>"
        'has_bits_in_common': None, # (!) real value is "<method 'has_bits_in_common' of 'panda3d.core.SparseArray' objects>"
        'has_max_num_bits': None, # (!) real value is '<staticmethod(<built-in method has_max_num_bits of type object at 0x00007FFCFE373100>)>'
        'invertInPlace': None, # (!) real value is "<method 'invertInPlace' of 'panda3d.core.SparseArray' objects>"
        'invert_in_place': None, # (!) real value is "<method 'invert_in_place' of 'panda3d.core.SparseArray' objects>"
        'isAllOn': None, # (!) real value is "<method 'isAllOn' of 'panda3d.core.SparseArray' objects>"
        'isInverse': None, # (!) real value is "<method 'isInverse' of 'panda3d.core.SparseArray' objects>"
        'isZero': None, # (!) real value is "<method 'isZero' of 'panda3d.core.SparseArray' objects>"
        'is_all_on': None, # (!) real value is "<method 'is_all_on' of 'panda3d.core.SparseArray' objects>"
        'is_inverse': None, # (!) real value is "<method 'is_inverse' of 'panda3d.core.SparseArray' objects>"
        'is_zero': None, # (!) real value is "<method 'is_zero' of 'panda3d.core.SparseArray' objects>"
        'lowerOn': None, # (!) real value is '<staticmethod(<built-in method lowerOn of type object at 0x00007FFCFE373100>)>'
        'lower_on': None, # (!) real value is '<staticmethod(<built-in method lower_on of type object at 0x00007FFCFE373100>)>'
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.SparseArray' objects>"
        'range': None, # (!) real value is '<staticmethod(<built-in method range of type object at 0x00007FFCFE373100>)>'
        'setBit': None, # (!) real value is "<method 'setBit' of 'panda3d.core.SparseArray' objects>"
        'setBitTo': None, # (!) real value is "<method 'setBitTo' of 'panda3d.core.SparseArray' objects>"
        'setRange': None, # (!) real value is "<method 'setRange' of 'panda3d.core.SparseArray' objects>"
        'setRangeTo': None, # (!) real value is "<method 'setRangeTo' of 'panda3d.core.SparseArray' objects>"
        'set_bit': None, # (!) real value is "<method 'set_bit' of 'panda3d.core.SparseArray' objects>"
        'set_bit_to': None, # (!) real value is "<method 'set_bit_to' of 'panda3d.core.SparseArray' objects>"
        'set_range': None, # (!) real value is "<method 'set_range' of 'panda3d.core.SparseArray' objects>"
        'set_range_to': None, # (!) real value is "<method 'set_range_to' of 'panda3d.core.SparseArray' objects>"
    }


