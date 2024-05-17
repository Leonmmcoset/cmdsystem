# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class PortalMask(__dtoolconfig.DTOOL_SUPER_BASE):
    # no doc
    def allOff(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        all_off()
        """
        pass

    def allOn(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        all_on()
        """
        pass

    def all_off(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        all_off()
        """
        pass

    def all_on(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        all_on()
        """
        pass

    def bit(self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        bit(int index)
        """
        pass

    def clear(self, const_BitMask_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear(const BitMask self)
        """
        pass

    def clearBit(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_bit(const BitMask self, int index)
        """
        pass

    def clearRange(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_range(const BitMask self, int low_bit, int size)
        """
        pass

    def clear_bit(self, const_BitMask_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_bit(const BitMask self, int index)
        """
        pass

    def clear_range(self, const_BitMask_self, int_low_bit, int_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_range(const BitMask self, int low_bit, int size)
        """
        pass

    def compareTo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        compare_to(BitMask self, const BitMask other)
        """
        pass

    def compare_to(self, BitMask_self, const_BitMask_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        compare_to(BitMask self, const BitMask other)
        """
        pass

    def extract(self, BitMask_self, int_low_bit, int_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        extract(BitMask self, int low_bit, int size)
        """
        pass

    def floodBitsDown(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        flood_bits_down(BitMask self)
        """
        pass

    def floodBitsUp(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        flood_bits_up(BitMask self)
        """
        pass

    def floodDownInPlace(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        flood_down_in_place(const BitMask self)
        """
        pass

    def floodUpInPlace(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        flood_up_in_place(const BitMask self)
        """
        pass

    def flood_bits_down(self, BitMask_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        flood_bits_down(BitMask self)
        """
        pass

    def flood_bits_up(self, BitMask_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        flood_bits_up(BitMask self)
        """
        pass

    def flood_down_in_place(self, const_BitMask_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        flood_down_in_place(const BitMask self)
        """
        pass

    def flood_up_in_place(self, const_BitMask_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        flood_up_in_place(const BitMask self)
        """
        pass

    def getBit(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_bit(BitMask self, int index)
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getHighestOffBit(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_highest_off_bit(BitMask self)
        """
        pass

    def getHighestOnBit(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_highest_on_bit(BitMask self)
        """
        pass

    def getKey(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_key(BitMask self)
        """
        pass

    def getLowestOffBit(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_lowest_off_bit(BitMask self)
        """
        pass

    def getLowestOnBit(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_lowest_on_bit(BitMask self)
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
        get_next_higher_different_bit(BitMask self, int low_bit)
        """
        pass

    def getNumBits(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_bits(BitMask self)
        """
        pass

    def getNumOffBits(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_off_bits(BitMask self)
        """
        pass

    def getNumOnBits(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_on_bits(BitMask self)
        """
        pass

    def getWord(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_word(BitMask self)
        """
        pass

    def get_bit(self, BitMask_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_bit(BitMask self, int index)
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_highest_off_bit(self, BitMask_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_highest_off_bit(BitMask self)
        """
        pass

    def get_highest_on_bit(self, BitMask_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_highest_on_bit(BitMask self)
        """
        pass

    def get_key(self, BitMask_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_key(BitMask self)
        """
        pass

    def get_lowest_off_bit(self, BitMask_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_lowest_off_bit(BitMask self)
        """
        pass

    def get_lowest_on_bit(self, BitMask_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_lowest_on_bit(BitMask self)
        """
        pass

    def get_max_num_bits(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_max_num_bits()
        """
        pass

    def get_next_higher_different_bit(self, BitMask_self, int_low_bit): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_next_higher_different_bit(BitMask self, int low_bit)
        """
        pass

    def get_num_bits(self, BitMask_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_bits(BitMask self)
        """
        pass

    def get_num_off_bits(self, BitMask_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_off_bits(BitMask self)
        """
        pass

    def get_num_on_bits(self, BitMask_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_on_bits(BitMask self)
        """
        pass

    def get_word(self, BitMask_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_word(BitMask self)
        """
        pass

    def hasAllOf(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_all_of(BitMask self, int low_bit, int size)
        """
        pass

    def hasAnyOf(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_any_of(BitMask self, int low_bit, int size)
        """
        pass

    def hasBitsInCommon(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_bits_in_common(BitMask self, const BitMask other)
        """
        pass

    def hasMaxNumBits(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_max_num_bits()
        """
        pass

    def has_all_of(self, BitMask_self, int_low_bit, int_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_all_of(BitMask self, int low_bit, int size)
        """
        pass

    def has_any_of(self, BitMask_self, int_low_bit, int_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_any_of(BitMask self, int low_bit, int size)
        """
        pass

    def has_bits_in_common(self, BitMask_self, const_BitMask_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_bits_in_common(BitMask self, const BitMask other)
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
        invert_in_place(const BitMask self)
        """
        pass

    def invert_in_place(self, const_BitMask_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        invert_in_place(const BitMask self)
        """
        pass

    def isAllOn(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_all_on(BitMask self)
        """
        pass

    def isZero(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_zero(BitMask self)
        """
        pass

    def is_all_on(self, BitMask_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_all_on(BitMask self)
        """
        pass

    def is_zero(self, BitMask_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_zero(BitMask self)
        """
        pass

    def keepNextHighestBit(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        keep_next_highest_bit(BitMask self)
        keep_next_highest_bit(BitMask self, const BitMask other)
        keep_next_highest_bit(BitMask self, int index)
        """
        pass

    def keepNextLowestBit(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        keep_next_lowest_bit(BitMask self)
        keep_next_lowest_bit(BitMask self, const BitMask other)
        keep_next_lowest_bit(BitMask self, int index)
        """
        pass

    def keep_next_highest_bit(self, BitMask_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        keep_next_highest_bit(BitMask self)
        keep_next_highest_bit(BitMask self, const BitMask other)
        keep_next_highest_bit(BitMask self, int index)
        """
        pass

    def keep_next_lowest_bit(self, BitMask_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        keep_next_lowest_bit(BitMask self)
        keep_next_lowest_bit(BitMask self, const BitMask other)
        keep_next_lowest_bit(BitMask self, int index)
        """
        pass

    def lowerOn(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        lower_on(int on_bits)
        """
        pass

    def lower_on(self, int_on_bits): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        lower_on(int on_bits)
        """
        pass

    def output(self, BitMask_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(BitMask self, ostream out)
        """
        pass

    def outputBinary(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        output_binary(BitMask self, ostream out, int spaces_every)
        """
        pass

    def outputHex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        output_hex(BitMask self, ostream out, int spaces_every)
        """
        pass

    def output_binary(self, BitMask_self, ostream_out, int_spaces_every): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output_binary(BitMask self, ostream out, int spaces_every)
        """
        pass

    def output_hex(self, BitMask_self, ostream_out, int_spaces_every): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output_hex(BitMask self, ostream out, int spaces_every)
        """
        pass

    def range(self, int_low_bit, int_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        range(int low_bit, int size)
        """
        pass

    def setBit(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_bit(const BitMask self, int index)
        """
        pass

    def setBitTo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_bit_to(const BitMask self, int index, bool value)
        """
        pass

    def setRange(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_range(const BitMask self, int low_bit, int size)
        """
        pass

    def setRangeTo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_range_to(const BitMask self, bool value, int low_bit, int size)
        """
        pass

    def setWord(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_word(const BitMask self, int value)
        """
        pass

    def set_bit(self, const_BitMask_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_bit(const BitMask self, int index)
        """
        pass

    def set_bit_to(self, const_BitMask_self, int_index, bool_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_bit_to(const BitMask self, int index, bool value)
        """
        pass

    def set_range(self, const_BitMask_self, int_low_bit, int_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_range(const BitMask self, int low_bit, int size)
        """
        pass

    def set_range_to(self, const_BitMask_self, bool_value, int_low_bit, int_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_range_to(const BitMask self, bool value, int low_bit, int size)
        """
        pass

    def set_word(self, const_BitMask_self, int_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_word(const BitMask self, int value)
        """
        pass

    def store(self, const_BitMask_self, int_value, int_low_bit, int_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        store(const BitMask self, int value, int low_bit, int size)
        """
        pass

    def write(self, BitMask_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(BitMask self, ostream out, int indent_level)
        """
        pass

    def __and__(self, *args, **kwargs): # real signature unknown
        """ Return self&value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ True if self else False """
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

    def __reduce__(self, BitMask_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        __reduce__(BitMask self)
        """
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

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    def __xor__(self, *args, **kwargs): # real signature unknown
        """ Return self^value. """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__and__': None, # (!) real value is "<slot wrapper '__and__' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        '__bool__': None, # (!) real value is "<slot wrapper '__bool__' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        '__doc__': None,
        '__eq__': None, # (!) real value is "<slot wrapper '__eq__' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        '__ge__': None, # (!) real value is "<slot wrapper '__ge__' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        '__gt__': None, # (!) real value is "<slot wrapper '__gt__' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        '__hash__': None, # (!) real value is "<slot wrapper '__hash__' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        '__iand__': None, # (!) real value is "<slot wrapper '__iand__' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        '__ilshift__': None, # (!) real value is "<slot wrapper '__ilshift__' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        '__invert__': None, # (!) real value is "<slot wrapper '__invert__' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        '__ior__': None, # (!) real value is "<slot wrapper '__ior__' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        '__irshift__': None, # (!) real value is "<slot wrapper '__irshift__' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        '__ixor__': None, # (!) real value is "<slot wrapper '__ixor__' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        '__le__': None, # (!) real value is "<slot wrapper '__le__' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        '__lshift__': None, # (!) real value is "<slot wrapper '__lshift__' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        '__lt__': None, # (!) real value is "<slot wrapper '__lt__' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        '__ne__': None, # (!) real value is "<slot wrapper '__ne__' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE370580>'
        '__or__': None, # (!) real value is "<slot wrapper '__or__' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        '__rand__': None, # (!) real value is "<slot wrapper '__rand__' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        '__reduce__': None, # (!) real value is "<method '__reduce__' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        '__rlshift__': None, # (!) real value is "<slot wrapper '__rlshift__' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        '__ror__': None, # (!) real value is "<slot wrapper '__ror__' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        '__rrshift__': None, # (!) real value is "<slot wrapper '__rrshift__' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        '__rshift__': None, # (!) real value is "<slot wrapper '__rshift__' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        '__rxor__': None, # (!) real value is "<slot wrapper '__rxor__' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        '__xor__': None, # (!) real value is "<slot wrapper '__xor__' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        'allOff': None, # (!) real value is '<staticmethod(<built-in method allOff of type object at 0x00007FFCFE370580>)>'
        'allOn': None, # (!) real value is '<staticmethod(<built-in method allOn of type object at 0x00007FFCFE370580>)>'
        'all_off': None, # (!) real value is '<staticmethod(<built-in method all_off of type object at 0x00007FFCFE370580>)>'
        'all_on': None, # (!) real value is '<staticmethod(<built-in method all_on of type object at 0x00007FFCFE370580>)>'
        'bit': None, # (!) real value is '<staticmethod(<built-in method bit of type object at 0x00007FFCFE370580>)>'
        'clear': None, # (!) real value is "<method 'clear' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        'clearBit': None, # (!) real value is "<method 'clearBit' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        'clearRange': None, # (!) real value is "<method 'clearRange' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        'clear_bit': None, # (!) real value is "<method 'clear_bit' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        'clear_range': None, # (!) real value is "<method 'clear_range' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        'compareTo': None, # (!) real value is "<method 'compareTo' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        'compare_to': None, # (!) real value is "<method 'compare_to' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        'extract': None, # (!) real value is "<method 'extract' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        'floodBitsDown': None, # (!) real value is "<method 'floodBitsDown' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        'floodBitsUp': None, # (!) real value is "<method 'floodBitsUp' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        'floodDownInPlace': None, # (!) real value is "<method 'floodDownInPlace' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        'floodUpInPlace': None, # (!) real value is "<method 'floodUpInPlace' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        'flood_bits_down': None, # (!) real value is "<method 'flood_bits_down' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        'flood_bits_up': None, # (!) real value is "<method 'flood_bits_up' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        'flood_down_in_place': None, # (!) real value is "<method 'flood_down_in_place' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        'flood_up_in_place': None, # (!) real value is "<method 'flood_up_in_place' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        'getBit': None, # (!) real value is "<method 'getBit' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE370580>)>'
        'getHighestOffBit': None, # (!) real value is "<method 'getHighestOffBit' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        'getHighestOnBit': None, # (!) real value is "<method 'getHighestOnBit' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        'getKey': None, # (!) real value is "<method 'getKey' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        'getLowestOffBit': None, # (!) real value is "<method 'getLowestOffBit' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        'getLowestOnBit': None, # (!) real value is "<method 'getLowestOnBit' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        'getMaxNumBits': None, # (!) real value is '<staticmethod(<built-in method getMaxNumBits of type object at 0x00007FFCFE370580>)>'
        'getNextHigherDifferentBit': None, # (!) real value is "<method 'getNextHigherDifferentBit' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        'getNumBits': None, # (!) real value is "<method 'getNumBits' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        'getNumOffBits': None, # (!) real value is "<method 'getNumOffBits' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        'getNumOnBits': None, # (!) real value is "<method 'getNumOnBits' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        'getWord': None, # (!) real value is "<method 'getWord' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        'get_bit': None, # (!) real value is "<method 'get_bit' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE370580>)>'
        'get_highest_off_bit': None, # (!) real value is "<method 'get_highest_off_bit' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        'get_highest_on_bit': None, # (!) real value is "<method 'get_highest_on_bit' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        'get_key': None, # (!) real value is "<method 'get_key' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        'get_lowest_off_bit': None, # (!) real value is "<method 'get_lowest_off_bit' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        'get_lowest_on_bit': None, # (!) real value is "<method 'get_lowest_on_bit' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        'get_max_num_bits': None, # (!) real value is '<staticmethod(<built-in method get_max_num_bits of type object at 0x00007FFCFE370580>)>'
        'get_next_higher_different_bit': None, # (!) real value is "<method 'get_next_higher_different_bit' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        'get_num_bits': None, # (!) real value is "<method 'get_num_bits' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        'get_num_off_bits': None, # (!) real value is "<method 'get_num_off_bits' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        'get_num_on_bits': None, # (!) real value is "<method 'get_num_on_bits' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        'get_word': None, # (!) real value is "<method 'get_word' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        'hasAllOf': None, # (!) real value is "<method 'hasAllOf' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        'hasAnyOf': None, # (!) real value is "<method 'hasAnyOf' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        'hasBitsInCommon': None, # (!) real value is "<method 'hasBitsInCommon' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        'hasMaxNumBits': None, # (!) real value is '<staticmethod(<built-in method hasMaxNumBits of type object at 0x00007FFCFE370580>)>'
        'has_all_of': None, # (!) real value is "<method 'has_all_of' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        'has_any_of': None, # (!) real value is "<method 'has_any_of' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        'has_bits_in_common': None, # (!) real value is "<method 'has_bits_in_common' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        'has_max_num_bits': None, # (!) real value is '<staticmethod(<built-in method has_max_num_bits of type object at 0x00007FFCFE370580>)>'
        'invertInPlace': None, # (!) real value is "<method 'invertInPlace' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        'invert_in_place': None, # (!) real value is "<method 'invert_in_place' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        'isAllOn': None, # (!) real value is "<method 'isAllOn' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        'isZero': None, # (!) real value is "<method 'isZero' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        'is_all_on': None, # (!) real value is "<method 'is_all_on' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        'is_zero': None, # (!) real value is "<method 'is_zero' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        'keepNextHighestBit': None, # (!) real value is "<method 'keepNextHighestBit' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        'keepNextLowestBit': None, # (!) real value is "<method 'keepNextLowestBit' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        'keep_next_highest_bit': None, # (!) real value is "<method 'keep_next_highest_bit' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        'keep_next_lowest_bit': None, # (!) real value is "<method 'keep_next_lowest_bit' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        'lowerOn': None, # (!) real value is '<staticmethod(<built-in method lowerOn of type object at 0x00007FFCFE370580>)>'
        'lower_on': None, # (!) real value is '<staticmethod(<built-in method lower_on of type object at 0x00007FFCFE370580>)>'
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        'outputBinary': None, # (!) real value is "<method 'outputBinary' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        'outputHex': None, # (!) real value is "<method 'outputHex' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        'output_binary': None, # (!) real value is "<method 'output_binary' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        'output_hex': None, # (!) real value is "<method 'output_hex' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        'range': None, # (!) real value is '<staticmethod(<built-in method range of type object at 0x00007FFCFE370580>)>'
        'setBit': None, # (!) real value is "<method 'setBit' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        'setBitTo': None, # (!) real value is "<method 'setBitTo' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        'setRange': None, # (!) real value is "<method 'setRange' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        'setRangeTo': None, # (!) real value is "<method 'setRangeTo' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        'setWord': None, # (!) real value is "<method 'setWord' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        'set_bit': None, # (!) real value is "<method 'set_bit' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        'set_bit_to': None, # (!) real value is "<method 'set_bit_to' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        'set_range': None, # (!) real value is "<method 'set_range' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        'set_range_to': None, # (!) real value is "<method 'set_range_to' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        'set_word': None, # (!) real value is "<method 'set_word' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        'store': None, # (!) real value is "<method 'store' of 'panda3d.core.BitMask_uint32_t_32' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.BitMask_uint32_t_32' objects>"
    }


