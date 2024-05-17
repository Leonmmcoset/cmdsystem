# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class BitArray(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * A dynamic array with an unlimited number of bits.
     *
     * This is similar to a BitMask, except it appears to contain an infinite
     * number of bits.  You can use it very much as you would use a BitMask.
     */
    """
    def allOff(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        all_off()
        
        /**
         * Returns a BitArray whose bits are all off.
         */
        """
        pass

    def allOn(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        all_on()
        
        /**
         * Returns a BitArray with an infinite array of bits, all on.
         */
        """
        pass

    def all_off(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        all_off()
        
        /**
         * Returns a BitArray whose bits are all off.
         */
        """
        pass

    def all_on(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        all_on()
        
        /**
         * Returns a BitArray with an infinite array of bits, all on.
         */
        """
        pass

    def bit(self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        bit(int index)
        
        /**
         * Returns a BitArray with only the indicated bit on.
         */
        """
        pass

    def clear(self, const_BitArray_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear(const BitArray self)
        
        /**
         * Sets all the bits in the BitArray off.
         */
        """
        pass

    def clearBit(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_bit(const BitArray self, int index)
        
        /**
         * Sets the nth bit off.  If n >= get_num_bits(), this automatically extends
         * the array.
         */
        """
        pass

    def clearRange(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_range(const BitArray self, int low_bit, int size)
        
        /**
         * Sets the indicated range of bits off.
         */
        """
        pass

    def clear_bit(self, const_BitArray_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_bit(const BitArray self, int index)
        
        /**
         * Sets the nth bit off.  If n >= get_num_bits(), this automatically extends
         * the array.
         */
        """
        pass

    def clear_range(self, const_BitArray_self, int_low_bit, int_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_range(const BitArray self, int low_bit, int size)
        
        /**
         * Sets the indicated range of bits off.
         */
        """
        pass

    def compareTo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        compare_to(BitArray self, const BitArray other)
        
        /**
         * Returns a number less than zero if this BitArray sorts before the indicated
         * other BitArray, greater than zero if it sorts after, or 0 if they are
         * equivalent.  This is based on the same ordering defined by operator <.
         */
        """
        pass

    def compare_to(self, BitArray_self, const_BitArray_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        compare_to(BitArray self, const BitArray other)
        
        /**
         * Returns a number less than zero if this BitArray sorts before the indicated
         * other BitArray, greater than zero if it sorts after, or 0 if they are
         * equivalent.  This is based on the same ordering defined by operator <.
         */
        """
        pass

    def extract(self, BitArray_self, int_low_bit, int_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        extract(BitArray self, int low_bit, int size)
        
        /**
         * Returns a word that represents only the indicated range of bits within this
         * BitArray, shifted to the least-significant position.  size must be <=
         * get_num_bits_per_word().
         */
        """
        pass

    def getBit(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_bit(BitArray self, int index)
        
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
        get_highest_bits(BitArray self)
        
        /**
         * Returns true if the infinite set of bits beyond get_num_bits() are all on,
         * or false of they are all off.
         */
        """
        pass

    def getHighestOffBit(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_highest_off_bit(BitArray self)
        
        /**
         * Returns the index of the highest 0 bit in the array.  Returns -1 if there
         * are no 0 bits or if there an infinite number of 1 bits.
         */
        """
        pass

    def getHighestOnBit(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_highest_on_bit(BitArray self)
        
        /**
         * Returns the index of the highest 1 bit in the array.  Returns -1 if there
         * are no 1 bits or if there an infinite number of 1 bits.
         */
        """
        pass

    def getLowestOffBit(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_lowest_off_bit(BitArray self)
        
        /**
         * Returns the index of the lowest 0 bit in the array.  Returns -1 if there
         * are no 0 bits.
         */
        """
        pass

    def getLowestOnBit(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_lowest_on_bit(BitArray self)
        
        /**
         * Returns the index of the lowest 1 bit in the array.  Returns -1 if there
         * are no 1 bits.
         */
        """
        pass

    def getMaxNumBits(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_max_num_bits()
        """
        pass

    def getNextHigherDifferentBit(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_next_higher_different_bit(BitArray self, int low_bit)
        
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
        get_num_bits(BitArray self)
        
        /**
         * Returns the current number of possibly different bits in this array.  There
         * are actually an infinite number of bits, but every bit higher than this bit
         * will have the same value, either 0 or 1 (see get_highest_bits()).
         *
         * This number may grow and/or shrink automatically as needed.
         */
        """
        pass

    def getNumBitsPerWord(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_bits_per_word()
        """
        pass

    def getNumOffBits(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_off_bits(BitArray self)
        
        /**
         * Returns the number of bits that are set to 0 in the array.  Returns -1 if
         * there are an infinite number of 0 bits.
         */
        """
        pass

    def getNumOnBits(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_on_bits(BitArray self)
        
        /**
         * Returns the number of bits that are set to 1 in the array.  Returns -1 if
         * there are an infinite number of 1 bits.
         */
        """
        pass

    def getNumWords(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_words(BitArray self)
        
        /**
         * Returns the number of possibly-unique words stored in the array.
         */
        """
        pass

    def getWord(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_word(BitArray self, int n)
        
        /**
         * Returns the nth word in the array.  It is valid for n to be greater than
         * get_num_words(), but the return value beyond get_num_words() will always be
         * the same.
         */
        """
        pass

    def get_bit(self, BitArray_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_bit(BitArray self, int index)
        
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

    def get_highest_bits(self, BitArray_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_highest_bits(BitArray self)
        
        /**
         * Returns true if the infinite set of bits beyond get_num_bits() are all on,
         * or false of they are all off.
         */
        """
        pass

    def get_highest_off_bit(self, BitArray_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_highest_off_bit(BitArray self)
        
        /**
         * Returns the index of the highest 0 bit in the array.  Returns -1 if there
         * are no 0 bits or if there an infinite number of 1 bits.
         */
        """
        pass

    def get_highest_on_bit(self, BitArray_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_highest_on_bit(BitArray self)
        
        /**
         * Returns the index of the highest 1 bit in the array.  Returns -1 if there
         * are no 1 bits or if there an infinite number of 1 bits.
         */
        """
        pass

    def get_lowest_off_bit(self, BitArray_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_lowest_off_bit(BitArray self)
        
        /**
         * Returns the index of the lowest 0 bit in the array.  Returns -1 if there
         * are no 0 bits.
         */
        """
        pass

    def get_lowest_on_bit(self, BitArray_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_lowest_on_bit(BitArray self)
        
        /**
         * Returns the index of the lowest 1 bit in the array.  Returns -1 if there
         * are no 1 bits.
         */
        """
        pass

    def get_max_num_bits(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_max_num_bits()
        """
        pass

    def get_next_higher_different_bit(self, BitArray_self, int_low_bit): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_next_higher_different_bit(BitArray self, int low_bit)
        
        /**
         * Returns the index of the next bit in the array, above low_bit, whose value
         * is different that the value of low_bit.  Returns low_bit again if all bits
         * higher than low_bit have the same value.
         *
         * This can be used to quickly iterate through all of the bits in the array.
         */
        """
        pass

    def get_num_bits(self, BitArray_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_bits(BitArray self)
        
        /**
         * Returns the current number of possibly different bits in this array.  There
         * are actually an infinite number of bits, but every bit higher than this bit
         * will have the same value, either 0 or 1 (see get_highest_bits()).
         *
         * This number may grow and/or shrink automatically as needed.
         */
        """
        pass

    def get_num_bits_per_word(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_bits_per_word()
        """
        pass

    def get_num_off_bits(self, BitArray_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_off_bits(BitArray self)
        
        /**
         * Returns the number of bits that are set to 0 in the array.  Returns -1 if
         * there are an infinite number of 0 bits.
         */
        """
        pass

    def get_num_on_bits(self, BitArray_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_on_bits(BitArray self)
        
        /**
         * Returns the number of bits that are set to 1 in the array.  Returns -1 if
         * there are an infinite number of 1 bits.
         */
        """
        pass

    def get_num_words(self, BitArray_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_words(BitArray self)
        
        /**
         * Returns the number of possibly-unique words stored in the array.
         */
        """
        pass

    def get_word(self, BitArray_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_word(BitArray self, int n)
        
        /**
         * Returns the nth word in the array.  It is valid for n to be greater than
         * get_num_words(), but the return value beyond get_num_words() will always be
         * the same.
         */
        """
        pass

    def hasAllOf(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_all_of(BitArray self, int low_bit, int size)
        
        /**
         * Returns true if all bits in the indicated range are set, false otherwise.
         */
        """
        pass

    def hasAnyOf(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_any_of(BitArray self, int low_bit, int size)
        
        /**
         * Returns true if any bit in the indicated range is set, false otherwise.
         */
        """
        pass

    def hasBitsInCommon(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_bits_in_common(BitArray self, const BitArray other)
        
        /**
         * Returns true if this BitArray has any "one" bits in common with the other
         * one, false otherwise.
         *
         * This is equivalent to (array & other) != 0, but may be faster.
         */
        """
        pass

    def hasMaxNumBits(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_max_num_bits()
        """
        pass

    def has_all_of(self, BitArray_self, int_low_bit, int_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_all_of(BitArray self, int low_bit, int size)
        
        /**
         * Returns true if all bits in the indicated range are set, false otherwise.
         */
        """
        pass

    def has_any_of(self, BitArray_self, int_low_bit, int_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_any_of(BitArray self, int low_bit, int size)
        
        /**
         * Returns true if any bit in the indicated range is set, false otherwise.
         */
        """
        pass

    def has_bits_in_common(self, BitArray_self, const_BitArray_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_bits_in_common(BitArray self, const BitArray other)
        
        /**
         * Returns true if this BitArray has any "one" bits in common with the other
         * one, false otherwise.
         *
         * This is equivalent to (array & other) != 0, but may be faster.
         */
        """
        pass

    def has_max_num_bits(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_max_num_bits()
        """
        pass

    def invertInPlace(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        invert_in_place(const BitArray self)
        
        /**
         * Inverts all the bits in the BitArray.  This is equivalent to array =
         * ~array.
         */
        """
        pass

    def invert_in_place(self, const_BitArray_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        invert_in_place(const BitArray self)
        
        /**
         * Inverts all the bits in the BitArray.  This is equivalent to array =
         * ~array.
         */
        """
        pass

    def isAllOn(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_all_on(BitArray self)
        
        /**
         * Returns true if the entire bitmask is one, false otherwise.
         */
        """
        pass

    def isZero(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_zero(BitArray self)
        
        /**
         * Returns true if the entire bitmask is zero, false otherwise.
         */
        """
        pass

    def is_all_on(self, BitArray_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_all_on(BitArray self)
        
        /**
         * Returns true if the entire bitmask is one, false otherwise.
         */
        """
        pass

    def is_zero(self, BitArray_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_zero(BitArray self)
        
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
         * Returns a BitArray whose lower on_bits bits are on.
         */
        """
        pass

    def lower_on(self, int_on_bits): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        lower_on(int on_bits)
        
        /**
         * Returns a BitArray whose lower on_bits bits are on.
         */
        """
        pass

    def output(self, BitArray_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(BitArray self, ostream out)
        
        /**
         * Writes the BitArray out as a hex number.  For a BitArray, this is always
         * the same as output_hex(); it's too confusing for the output format to
         * change back and forth at runtime.
         */
        """
        pass

    def outputBinary(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        output_binary(BitArray self, ostream out, int spaces_every)
        
        /**
         * Writes the BitArray out as a binary number, with spaces every four bits.
         */
        """
        pass

    def outputHex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        output_hex(BitArray self, ostream out, int spaces_every)
        
        /**
         * Writes the BitArray out as a hexadecimal number, with spaces every four
         * digits.
         */
        """
        pass

    def output_binary(self, BitArray_self, ostream_out, int_spaces_every): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output_binary(BitArray self, ostream out, int spaces_every)
        
        /**
         * Writes the BitArray out as a binary number, with spaces every four bits.
         */
        """
        pass

    def output_hex(self, BitArray_self, ostream_out, int_spaces_every): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output_hex(BitArray self, ostream out, int spaces_every)
        
        /**
         * Writes the BitArray out as a hexadecimal number, with spaces every four
         * digits.
         */
        """
        pass

    def range(self, int_low_bit, int_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        range(int low_bit, int size)
        
        /**
         * Returns a BitArray whose size bits, beginning at low_bit, are on.
         */
        """
        pass

    def setBit(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_bit(const BitArray self, int index)
        
        /**
         * Sets the nth bit on.  If n >= get_num_bits(), this automatically extends
         * the array.
         */
        """
        pass

    def setBitTo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_bit_to(const BitArray self, int index, bool value)
        
        /**
         * Sets the nth bit either on or off, according to the indicated bool value.
         */
        """
        pass

    def setRange(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_range(const BitArray self, int low_bit, int size)
        
        /**
         * Sets the indicated range of bits on.
         */
        """
        pass

    def setRangeTo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_range_to(const BitArray self, bool value, int low_bit, int size)
        
        /**
         * Sets the indicated range of bits to either on or off.
         */
        """
        pass

    def setWord(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_word(const BitArray self, int n, long value)
        
        /**
         * Replaces the nth word in the array.  If n >= get_num_words(), this
         * automatically extends the array.
         */
        """
        pass

    def set_bit(self, const_BitArray_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_bit(const BitArray self, int index)
        
        /**
         * Sets the nth bit on.  If n >= get_num_bits(), this automatically extends
         * the array.
         */
        """
        pass

    def set_bit_to(self, const_BitArray_self, int_index, bool_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_bit_to(const BitArray self, int index, bool value)
        
        /**
         * Sets the nth bit either on or off, according to the indicated bool value.
         */
        """
        pass

    def set_range(self, const_BitArray_self, int_low_bit, int_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_range(const BitArray self, int low_bit, int size)
        
        /**
         * Sets the indicated range of bits on.
         */
        """
        pass

    def set_range_to(self, const_BitArray_self, bool_value, int_low_bit, int_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_range_to(const BitArray self, bool value, int low_bit, int size)
        
        /**
         * Sets the indicated range of bits to either on or off.
         */
        """
        pass

    def set_word(self, const_BitArray_self, int_n, long_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_word(const BitArray self, int n, long value)
        
        /**
         * Replaces the nth word in the array.  If n >= get_num_words(), this
         * automatically extends the array.
         */
        """
        pass

    def store(self, const_BitArray_self, long_value, int_low_bit, int_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        store(const BitArray self, long value, int low_bit, int size)
        
        /**
         * Stores the indicated word into the indicated range of bits with this
         * BitArray.
         */
        """
        pass

    def write(self, BitArray_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(BitArray self, ostream out, int indent_level)
        
        /**
         * Writes the BitArray out as a binary or a hex number, according to the
         * number of bits.
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

    def __getstate__(self, BitArray_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        __getstate__(BitArray self)
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

    def __setstate__(self, const_BitArray_self, object_state): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        __setstate__(const BitArray self, object state)
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
        '__and__': None, # (!) real value is "<slot wrapper '__and__' of 'panda3d.core.BitArray' objects>"
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.BitArray' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.BitArray' objects>"
        '__doc__': '/**\n * A dynamic array with an unlimited number of bits.\n *\n * This is similar to a BitMask, except it appears to contain an infinite\n * number of bits.  You can use it very much as you would use a BitMask.\n */',
        '__eq__': None, # (!) real value is "<slot wrapper '__eq__' of 'panda3d.core.BitArray' objects>"
        '__ge__': None, # (!) real value is "<slot wrapper '__ge__' of 'panda3d.core.BitArray' objects>"
        '__getstate__': None, # (!) real value is "<method '__getstate__' of 'panda3d.core.BitArray' objects>"
        '__gt__': None, # (!) real value is "<slot wrapper '__gt__' of 'panda3d.core.BitArray' objects>"
        '__hash__': None, # (!) real value is "<slot wrapper '__hash__' of 'panda3d.core.BitArray' objects>"
        '__iand__': None, # (!) real value is "<slot wrapper '__iand__' of 'panda3d.core.BitArray' objects>"
        '__ilshift__': None, # (!) real value is "<slot wrapper '__ilshift__' of 'panda3d.core.BitArray' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.BitArray' objects>"
        '__invert__': None, # (!) real value is "<slot wrapper '__invert__' of 'panda3d.core.BitArray' objects>"
        '__ior__': None, # (!) real value is "<slot wrapper '__ior__' of 'panda3d.core.BitArray' objects>"
        '__irshift__': None, # (!) real value is "<slot wrapper '__irshift__' of 'panda3d.core.BitArray' objects>"
        '__ixor__': None, # (!) real value is "<slot wrapper '__ixor__' of 'panda3d.core.BitArray' objects>"
        '__le__': None, # (!) real value is "<slot wrapper '__le__' of 'panda3d.core.BitArray' objects>"
        '__lshift__': None, # (!) real value is "<slot wrapper '__lshift__' of 'panda3d.core.BitArray' objects>"
        '__lt__': None, # (!) real value is "<slot wrapper '__lt__' of 'panda3d.core.BitArray' objects>"
        '__ne__': None, # (!) real value is "<slot wrapper '__ne__' of 'panda3d.core.BitArray' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE370920>'
        '__or__': None, # (!) real value is "<slot wrapper '__or__' of 'panda3d.core.BitArray' objects>"
        '__rand__': None, # (!) real value is "<slot wrapper '__rand__' of 'panda3d.core.BitArray' objects>"
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.BitArray' objects>"
        '__rlshift__': None, # (!) real value is "<slot wrapper '__rlshift__' of 'panda3d.core.BitArray' objects>"
        '__ror__': None, # (!) real value is "<slot wrapper '__ror__' of 'panda3d.core.BitArray' objects>"
        '__rrshift__': None, # (!) real value is "<slot wrapper '__rrshift__' of 'panda3d.core.BitArray' objects>"
        '__rshift__': None, # (!) real value is "<slot wrapper '__rshift__' of 'panda3d.core.BitArray' objects>"
        '__rxor__': None, # (!) real value is "<slot wrapper '__rxor__' of 'panda3d.core.BitArray' objects>"
        '__setstate__': None, # (!) real value is "<method '__setstate__' of 'panda3d.core.BitArray' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.BitArray' objects>"
        '__xor__': None, # (!) real value is "<slot wrapper '__xor__' of 'panda3d.core.BitArray' objects>"
        'allOff': None, # (!) real value is '<staticmethod(<built-in method allOff of type object at 0x00007FFCFE370920>)>'
        'allOn': None, # (!) real value is '<staticmethod(<built-in method allOn of type object at 0x00007FFCFE370920>)>'
        'all_off': None, # (!) real value is '<staticmethod(<built-in method all_off of type object at 0x00007FFCFE370920>)>'
        'all_on': None, # (!) real value is '<staticmethod(<built-in method all_on of type object at 0x00007FFCFE370920>)>'
        'bit': None, # (!) real value is '<staticmethod(<built-in method bit of type object at 0x00007FFCFE370920>)>'
        'clear': None, # (!) real value is "<method 'clear' of 'panda3d.core.BitArray' objects>"
        'clearBit': None, # (!) real value is "<method 'clearBit' of 'panda3d.core.BitArray' objects>"
        'clearRange': None, # (!) real value is "<method 'clearRange' of 'panda3d.core.BitArray' objects>"
        'clear_bit': None, # (!) real value is "<method 'clear_bit' of 'panda3d.core.BitArray' objects>"
        'clear_range': None, # (!) real value is "<method 'clear_range' of 'panda3d.core.BitArray' objects>"
        'compareTo': None, # (!) real value is "<method 'compareTo' of 'panda3d.core.BitArray' objects>"
        'compare_to': None, # (!) real value is "<method 'compare_to' of 'panda3d.core.BitArray' objects>"
        'extract': None, # (!) real value is "<method 'extract' of 'panda3d.core.BitArray' objects>"
        'getBit': None, # (!) real value is "<method 'getBit' of 'panda3d.core.BitArray' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE370920>)>'
        'getHighestBits': None, # (!) real value is "<method 'getHighestBits' of 'panda3d.core.BitArray' objects>"
        'getHighestOffBit': None, # (!) real value is "<method 'getHighestOffBit' of 'panda3d.core.BitArray' objects>"
        'getHighestOnBit': None, # (!) real value is "<method 'getHighestOnBit' of 'panda3d.core.BitArray' objects>"
        'getLowestOffBit': None, # (!) real value is "<method 'getLowestOffBit' of 'panda3d.core.BitArray' objects>"
        'getLowestOnBit': None, # (!) real value is "<method 'getLowestOnBit' of 'panda3d.core.BitArray' objects>"
        'getMaxNumBits': None, # (!) real value is '<staticmethod(<built-in method getMaxNumBits of type object at 0x00007FFCFE370920>)>'
        'getNextHigherDifferentBit': None, # (!) real value is "<method 'getNextHigherDifferentBit' of 'panda3d.core.BitArray' objects>"
        'getNumBits': None, # (!) real value is "<method 'getNumBits' of 'panda3d.core.BitArray' objects>"
        'getNumBitsPerWord': None, # (!) real value is '<staticmethod(<built-in method getNumBitsPerWord of type object at 0x00007FFCFE370920>)>'
        'getNumOffBits': None, # (!) real value is "<method 'getNumOffBits' of 'panda3d.core.BitArray' objects>"
        'getNumOnBits': None, # (!) real value is "<method 'getNumOnBits' of 'panda3d.core.BitArray' objects>"
        'getNumWords': None, # (!) real value is "<method 'getNumWords' of 'panda3d.core.BitArray' objects>"
        'getWord': None, # (!) real value is "<method 'getWord' of 'panda3d.core.BitArray' objects>"
        'get_bit': None, # (!) real value is "<method 'get_bit' of 'panda3d.core.BitArray' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE370920>)>'
        'get_highest_bits': None, # (!) real value is "<method 'get_highest_bits' of 'panda3d.core.BitArray' objects>"
        'get_highest_off_bit': None, # (!) real value is "<method 'get_highest_off_bit' of 'panda3d.core.BitArray' objects>"
        'get_highest_on_bit': None, # (!) real value is "<method 'get_highest_on_bit' of 'panda3d.core.BitArray' objects>"
        'get_lowest_off_bit': None, # (!) real value is "<method 'get_lowest_off_bit' of 'panda3d.core.BitArray' objects>"
        'get_lowest_on_bit': None, # (!) real value is "<method 'get_lowest_on_bit' of 'panda3d.core.BitArray' objects>"
        'get_max_num_bits': None, # (!) real value is '<staticmethod(<built-in method get_max_num_bits of type object at 0x00007FFCFE370920>)>'
        'get_next_higher_different_bit': None, # (!) real value is "<method 'get_next_higher_different_bit' of 'panda3d.core.BitArray' objects>"
        'get_num_bits': None, # (!) real value is "<method 'get_num_bits' of 'panda3d.core.BitArray' objects>"
        'get_num_bits_per_word': None, # (!) real value is '<staticmethod(<built-in method get_num_bits_per_word of type object at 0x00007FFCFE370920>)>'
        'get_num_off_bits': None, # (!) real value is "<method 'get_num_off_bits' of 'panda3d.core.BitArray' objects>"
        'get_num_on_bits': None, # (!) real value is "<method 'get_num_on_bits' of 'panda3d.core.BitArray' objects>"
        'get_num_words': None, # (!) real value is "<method 'get_num_words' of 'panda3d.core.BitArray' objects>"
        'get_word': None, # (!) real value is "<method 'get_word' of 'panda3d.core.BitArray' objects>"
        'hasAllOf': None, # (!) real value is "<method 'hasAllOf' of 'panda3d.core.BitArray' objects>"
        'hasAnyOf': None, # (!) real value is "<method 'hasAnyOf' of 'panda3d.core.BitArray' objects>"
        'hasBitsInCommon': None, # (!) real value is "<method 'hasBitsInCommon' of 'panda3d.core.BitArray' objects>"
        'hasMaxNumBits': None, # (!) real value is '<staticmethod(<built-in method hasMaxNumBits of type object at 0x00007FFCFE370920>)>'
        'has_all_of': None, # (!) real value is "<method 'has_all_of' of 'panda3d.core.BitArray' objects>"
        'has_any_of': None, # (!) real value is "<method 'has_any_of' of 'panda3d.core.BitArray' objects>"
        'has_bits_in_common': None, # (!) real value is "<method 'has_bits_in_common' of 'panda3d.core.BitArray' objects>"
        'has_max_num_bits': None, # (!) real value is '<staticmethod(<built-in method has_max_num_bits of type object at 0x00007FFCFE370920>)>'
        'invertInPlace': None, # (!) real value is "<method 'invertInPlace' of 'panda3d.core.BitArray' objects>"
        'invert_in_place': None, # (!) real value is "<method 'invert_in_place' of 'panda3d.core.BitArray' objects>"
        'isAllOn': None, # (!) real value is "<method 'isAllOn' of 'panda3d.core.BitArray' objects>"
        'isZero': None, # (!) real value is "<method 'isZero' of 'panda3d.core.BitArray' objects>"
        'is_all_on': None, # (!) real value is "<method 'is_all_on' of 'panda3d.core.BitArray' objects>"
        'is_zero': None, # (!) real value is "<method 'is_zero' of 'panda3d.core.BitArray' objects>"
        'lowerOn': None, # (!) real value is '<staticmethod(<built-in method lowerOn of type object at 0x00007FFCFE370920>)>'
        'lower_on': None, # (!) real value is '<staticmethod(<built-in method lower_on of type object at 0x00007FFCFE370920>)>'
        'num_bits_per_word': 64,
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.BitArray' objects>"
        'outputBinary': None, # (!) real value is "<method 'outputBinary' of 'panda3d.core.BitArray' objects>"
        'outputHex': None, # (!) real value is "<method 'outputHex' of 'panda3d.core.BitArray' objects>"
        'output_binary': None, # (!) real value is "<method 'output_binary' of 'panda3d.core.BitArray' objects>"
        'output_hex': None, # (!) real value is "<method 'output_hex' of 'panda3d.core.BitArray' objects>"
        'range': None, # (!) real value is '<staticmethod(<built-in method range of type object at 0x00007FFCFE370920>)>'
        'setBit': None, # (!) real value is "<method 'setBit' of 'panda3d.core.BitArray' objects>"
        'setBitTo': None, # (!) real value is "<method 'setBitTo' of 'panda3d.core.BitArray' objects>"
        'setRange': None, # (!) real value is "<method 'setRange' of 'panda3d.core.BitArray' objects>"
        'setRangeTo': None, # (!) real value is "<method 'setRangeTo' of 'panda3d.core.BitArray' objects>"
        'setWord': None, # (!) real value is "<method 'setWord' of 'panda3d.core.BitArray' objects>"
        'set_bit': None, # (!) real value is "<method 'set_bit' of 'panda3d.core.BitArray' objects>"
        'set_bit_to': None, # (!) real value is "<method 'set_bit_to' of 'panda3d.core.BitArray' objects>"
        'set_range': None, # (!) real value is "<method 'set_range' of 'panda3d.core.BitArray' objects>"
        'set_range_to': None, # (!) real value is "<method 'set_range_to' of 'panda3d.core.BitArray' objects>"
        'set_word': None, # (!) real value is "<method 'set_word' of 'panda3d.core.BitArray' objects>"
        'store': None, # (!) real value is "<method 'store' of 'panda3d.core.BitArray' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.BitArray' objects>"
    }
    num_bits_per_word = 64


