# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class MaterialPool(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * The MaterialPool (there is only one in the universe) serves to unify
     * different pointers to the same Material, so we do not (a) waste memory with
     * many different Material objects that are all equivalent, and (b) waste time
     * switching the graphics engine between different Material states that are
     * really the same thing.
     *
     * The idea is to create a temporary Material representing the lighting state
     * you want to apply, then call get_material(), passing in your temporary
     * Material.  The return value will either be a new Material object, or it may
     * be the the same object you supplied; in either case, it will have the same
     * value.
     */
    """
    def garbageCollect(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        garbage_collect()
        
        /**
         * Releases only those materials in the pool that have a reference count of
         * exactly 1; i.e.  only those materials that are not being used outside of
         * the pool.  Returns the number of materials released.
         */
        """
        pass

    def garbage_collect(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        garbage_collect()
        
        /**
         * Releases only those materials in the pool that have a reference count of
         * exactly 1; i.e.  only those materials that are not being used outside of
         * the pool.  Returns the number of materials released.
         */
        """
        pass

    def getMaterial(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_material(Material temp)
        
        /**
         * Returns a Material pointer that represents the same material described by
         * temp, except that it is a shared pointer.
         *
         * Each call to get_material() passing an equivalent Material pointer will
         * return the same shared pointer.
         *
         * If you modify the shared pointer, it will automatically disassociate it
         * from the pool.
         *
         * Also, the return value may be a different pointer than that passed in, or
         * it may be the same pointer.  In either case, the passed in pointer has now
         * been sacrificed to the greater good and should not be used again (like any
         * other PointerTo, it will be freed when the last reference count is
         * removed).
         */
        """
        pass

    def get_material(self, Material_temp): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_material(Material temp)
        
        /**
         * Returns a Material pointer that represents the same material described by
         * temp, except that it is a shared pointer.
         *
         * Each call to get_material() passing an equivalent Material pointer will
         * return the same shared pointer.
         *
         * If you modify the shared pointer, it will automatically disassociate it
         * from the pool.
         *
         * Also, the return value may be a different pointer than that passed in, or
         * it may be the same pointer.  In either case, the passed in pointer has now
         * been sacrificed to the greater good and should not be used again (like any
         * other PointerTo, it will be freed when the last reference count is
         * removed).
         */
        """
        pass

    def listContents(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        list_contents(ostream out)
        
        /**
         * Lists the contents of the material pool to the indicated output stream.
         */
        """
        pass

    def list_contents(self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        list_contents(ostream out)
        
        /**
         * Lists the contents of the material pool to the indicated output stream.
         */
        """
        pass

    def releaseAllMaterials(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        release_all_materials()
        
        /**
         * Releases all materials in the pool and restores the pool to the empty
         * state.
         */
        """
        pass

    def releaseMaterial(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        release_material(Material temp)
        
        /**
         * Removes the indicated material from the pool.
         */
        """
        pass

    def release_all_materials(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        release_all_materials()
        
        /**
         * Releases all materials in the pool and restores the pool to the empty
         * state.
         */
        """
        pass

    def release_material(self, Material_temp): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        release_material(Material temp)
        
        /**
         * Removes the indicated material from the pool.
         */
        """
        pass

    def write(self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(ostream out)
        
        /**
         * Lists the contents of the material pool to the indicated output stream.
         */
        """
        pass

    def __init__(self, there_is_only_one_in_the_universe): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * The MaterialPool (there is only one in the universe) serves to unify\n * different pointers to the same Material, so we do not (a) waste memory with\n * many different Material objects that are all equivalent, and (b) waste time\n * switching the graphics engine between different Material states that are\n * really the same thing.\n *\n * The idea is to create a temporary Material representing the lighting state\n * you want to apply, then call get_material(), passing in your temporary\n * Material.  The return value will either be a new Material object, or it may\n * be the the same object you supplied; in either case, it will have the same\n * value.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.MaterialPool' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2FF9F0>'
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.MaterialPool' objects>"
        'garbageCollect': None, # (!) real value is '<staticmethod(<built-in method garbageCollect of type object at 0x00007FFCFE2FF9F0>)>'
        'garbage_collect': None, # (!) real value is '<staticmethod(<built-in method garbage_collect of type object at 0x00007FFCFE2FF9F0>)>'
        'getMaterial': None, # (!) real value is '<staticmethod(<built-in method getMaterial of type object at 0x00007FFCFE2FF9F0>)>'
        'get_material': None, # (!) real value is '<staticmethod(<built-in method get_material of type object at 0x00007FFCFE2FF9F0>)>'
        'listContents': None, # (!) real value is '<staticmethod(<built-in method listContents of type object at 0x00007FFCFE2FF9F0>)>'
        'list_contents': None, # (!) real value is '<staticmethod(<built-in method list_contents of type object at 0x00007FFCFE2FF9F0>)>'
        'releaseAllMaterials': None, # (!) real value is '<staticmethod(<built-in method releaseAllMaterials of type object at 0x00007FFCFE2FF9F0>)>'
        'releaseMaterial': None, # (!) real value is '<staticmethod(<built-in method releaseMaterial of type object at 0x00007FFCFE2FF9F0>)>'
        'release_all_materials': None, # (!) real value is '<staticmethod(<built-in method release_all_materials of type object at 0x00007FFCFE2FF9F0>)>'
        'release_material': None, # (!) real value is '<staticmethod(<built-in method release_material of type object at 0x00007FFCFE2FF9F0>)>'
        'write': None, # (!) real value is '<staticmethod(<built-in method write of type object at 0x00007FFCFE2FF9F0>)>'
    }


