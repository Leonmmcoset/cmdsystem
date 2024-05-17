# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class UniqueIdAllocator(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * Manage a set of ID values from min to max inclusive.  The ID numbers that
     * are freed will be allocated (reused) in the same order.  I.e.  the oldest
     * ID numbers will be allocated.
     *
     * This implementation will use 4 bytes per id number, plus a few bytes of
     * management data.  e.g.  10,000 ID numbers will use 40KB.
     *
     * Also be advised that ID -1 and -2 are used internally by the allocator.  If
     * allocate returns IndexEnd (-1) then the allocator is out of free ID
     * numbers.
     *
     * There are other implementations that can better leverage runs of used or
     * unused IDs or use bit arrays for the IDs.  But, it takes extra work to
     * track the age of freed IDs, which is required for what we wanted.  If you
     * would like to kick around other implementation ideas, please contact
     * Schuyler.
     */
    """
    def allocate(self, const_UniqueIdAllocator_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        allocate(const UniqueIdAllocator self)
        
        /**
         * Returns an id between _min and _max (that were passed to the constructor).
         * IndexEnd is returned if no ids are available.
         */
        """
        pass

    def fractionUsed(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        fraction_used(UniqueIdAllocator self)
        
        /**
         * return the decimal fraction of the pool that is used.  The range is 0 to
         * 1.0 (e.g.  75% would be 0.75).
         */
        """
        pass

    def fraction_used(self, UniqueIdAllocator_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        fraction_used(UniqueIdAllocator self)
        
        /**
         * return the decimal fraction of the pool that is used.  The range is 0 to
         * 1.0 (e.g.  75% would be 0.75).
         */
        """
        pass

    def free(self, const_UniqueIdAllocator_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        free(const UniqueIdAllocator self, int index)
        
        /**
         * Free an allocated index (index must be between _min and _max that were
         * passed to the constructor).
         */
        """
        pass

    def initialReserveId(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        initial_reserve_id(const UniqueIdAllocator self, int id)
        
        /**
         * This may be called to mark a particular id as having already been allocated
         * (for instance, by a prior pass).  The specified id is removed from the
         * available pool.
         *
         * Because of the limitations of this algorithm, this is most efficient when
         * it is called before the first call to allocate(), and when all the calls to
         * initial_reserve_id() are made in descending order by id.  However, this is
         * a performance warning only; if performance is not an issue, any id may be
         * reserved at any time.
         */
        """
        pass

    def initial_reserve_id(self, const_UniqueIdAllocator_self, int_id): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        initial_reserve_id(const UniqueIdAllocator self, int id)
        
        /**
         * This may be called to mark a particular id as having already been allocated
         * (for instance, by a prior pass).  The specified id is removed from the
         * available pool.
         *
         * Because of the limitations of this algorithm, this is most efficient when
         * it is called before the first call to allocate(), and when all the calls to
         * initial_reserve_id() are made in descending order by id.  However, this is
         * a performance warning only; if performance is not an issue, any id may be
         * reserved at any time.
         */
        """
        pass

    def output(self, UniqueIdAllocator_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(UniqueIdAllocator self, ostream out)
        
        /**
         * ...intended for debugging only.
         */
        """
        pass

    def write(self, UniqueIdAllocator_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(UniqueIdAllocator self, ostream out)
        
        /**
         * ...intended for debugging only.
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

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.UniqueIdAllocator' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.UniqueIdAllocator' objects>"
        '__doc__': '/**\n * Manage a set of ID values from min to max inclusive.  The ID numbers that\n * are freed will be allocated (reused) in the same order.  I.e.  the oldest\n * ID numbers will be allocated.\n *\n * This implementation will use 4 bytes per id number, plus a few bytes of\n * management data.  e.g.  10,000 ID numbers will use 40KB.\n *\n * Also be advised that ID -1 and -2 are used internally by the allocator.  If\n * allocate returns IndexEnd (-1) then the allocator is out of free ID\n * numbers.\n *\n * There are other implementations that can better leverage runs of used or\n * unused IDs or use bit arrays for the IDs.  But, it takes extra work to\n * track the age of freed IDs, which is required for what we wanted.  If you\n * would like to kick around other implementation ideas, please contact\n * Schuyler.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.UniqueIdAllocator' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE375370>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.UniqueIdAllocator' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.UniqueIdAllocator' objects>"
        'allocate': None, # (!) real value is "<method 'allocate' of 'panda3d.core.UniqueIdAllocator' objects>"
        'fractionUsed': None, # (!) real value is "<method 'fractionUsed' of 'panda3d.core.UniqueIdAllocator' objects>"
        'fraction_used': None, # (!) real value is "<method 'fraction_used' of 'panda3d.core.UniqueIdAllocator' objects>"
        'free': None, # (!) real value is "<method 'free' of 'panda3d.core.UniqueIdAllocator' objects>"
        'initialReserveId': None, # (!) real value is "<method 'initialReserveId' of 'panda3d.core.UniqueIdAllocator' objects>"
        'initial_reserve_id': None, # (!) real value is "<method 'initial_reserve_id' of 'panda3d.core.UniqueIdAllocator' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.UniqueIdAllocator' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.UniqueIdAllocator' objects>"
    }


