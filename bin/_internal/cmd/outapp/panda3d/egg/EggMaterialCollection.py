# encoding: utf-8
# module panda3d.egg
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\egg.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


class EggMaterialCollection(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This is a collection of materials by MRef name.  It can extract the
     * materials from an egg file and sort them all together; it can also manage
     * the creation of unique materials and the assignment of unique MRef names.
     */
    """
    def addMaterial(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_material(const EggMaterialCollection self, EggMaterial material)
        
        /**
         * Explicitly adds a new material to the collection.  Returns true if the
         * material was added, false if it was already there or if there was some
         * error.
         */
        """
        pass

    def add_material(self, const_EggMaterialCollection_self, EggMaterial_material): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_material(const EggMaterialCollection self, EggMaterial material)
        
        /**
         * Explicitly adds a new material to the collection.  Returns true if the
         * material was added, false if it was already there or if there was some
         * error.
         */
        """
        pass

    def assign(self, const_EggMaterialCollection_self, const_EggMaterialCollection_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const EggMaterialCollection self, const EggMaterialCollection copy)
        
        /**
         *
         */
        """
        pass

    def clear(self, const_EggMaterialCollection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear(const EggMaterialCollection self)
        
        /**
         * Removes all materials from the collection.
         */
        """
        pass

    def collapseEquivalentMaterials(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        collapse_equivalent_materials(const EggMaterialCollection self, int eq, EggGroupNode node)
        
        /**
         * Walks through the collection and collapses together any separate materials
         * that are equivalent according to the indicated equivalence factor, eq (see
         * EggMaterial::is_equivalent_to()).  The return value is the number of
         * materials removed.
         *
         * This flavor of collapse_equivalent_materials() automatically adjusts all
         * the primitives in the egg hierarchy to refer to the new material pointers.
         */
        
        /**
         * Walks through the collection and collapses together any separate materials
         * that are equivalent according to the indicated equivalence factor, eq (see
         * EggMaterial::is_equivalent_to()).  The return value is the number of
         * materials removed.
         *
         * This flavor of collapse_equivalent_materials() does not adjust any
         * primitives in the egg hierarchy; instead, it fills up the 'removed' map
         * with an entry for each removed material, mapping it back to the equivalent
         * retained material.  It's up to the user to then call replace_materials()
         * with this map, if desired, to apply these changes to the egg hierarchy.
         */
        """
        pass

    def collapse_equivalent_materials(self, const_EggMaterialCollection_self, int_eq, EggGroupNode_node): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        collapse_equivalent_materials(const EggMaterialCollection self, int eq, EggGroupNode node)
        
        /**
         * Walks through the collection and collapses together any separate materials
         * that are equivalent according to the indicated equivalence factor, eq (see
         * EggMaterial::is_equivalent_to()).  The return value is the number of
         * materials removed.
         *
         * This flavor of collapse_equivalent_materials() automatically adjusts all
         * the primitives in the egg hierarchy to refer to the new material pointers.
         */
        
        /**
         * Walks through the collection and collapses together any separate materials
         * that are equivalent according to the indicated equivalence factor, eq (see
         * EggMaterial::is_equivalent_to()).  The return value is the number of
         * materials removed.
         *
         * This flavor of collapse_equivalent_materials() does not adjust any
         * primitives in the egg hierarchy; instead, it fills up the 'removed' map
         * with an entry for each removed material, mapping it back to the equivalent
         * retained material.  It's up to the user to then call replace_materials()
         * with this map, if desired, to apply these changes to the egg hierarchy.
         */
        """
        pass

    def createUniqueMaterial(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        create_unique_material(const EggMaterialCollection self, const EggMaterial copy, int eq)
        
        // create_unique_material() creates a new material if there is not already
        // one equivalent (according to eq, see EggMaterial::is_equivalent_to()) to
        // the indicated material, or returns the existing one if there is.
        
        /**
         * Creates a new material if there is not already one equivalent (according to
         * eq, see EggMaterial::is_equivalent_to()) to the indicated material, or
         * returns the existing one if there is.
         */
        """
        pass

    def create_unique_material(self, const_EggMaterialCollection_self, const_EggMaterial_copy, int_eq): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        create_unique_material(const EggMaterialCollection self, const EggMaterial copy, int eq)
        
        // create_unique_material() creates a new material if there is not already
        // one equivalent (according to eq, see EggMaterial::is_equivalent_to()) to
        // the indicated material, or returns the existing one if there is.
        
        /**
         * Creates a new material if there is not already one equivalent (according to
         * eq, see EggMaterial::is_equivalent_to()) to the indicated material, or
         * returns the existing one if there is.
         */
        """
        pass

    def extractMaterials(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        extract_materials(const EggMaterialCollection self, EggGroupNode node)
        
        /**
         * Walks the egg hierarchy beginning at the indicated node, and removes any
         * EggMaterials encountered in the hierarchy, adding them to the collection.
         * Returns the number of EggMaterials encountered.
         */
        """
        pass

    def extract_materials(self, const_EggMaterialCollection_self, EggGroupNode_node): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        extract_materials(const EggMaterialCollection self, EggGroupNode node)
        
        /**
         * Walks the egg hierarchy beginning at the indicated node, and removes any
         * EggMaterials encountered in the hierarchy, adding them to the collection.
         * Returns the number of EggMaterials encountered.
         */
        """
        pass

    def findMref(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        find_mref(EggMaterialCollection self, str mref_name)
        
        // Find a material with a particular MRef name.
        
        /**
         * Returns the material with the indicated MRef name, or NULL if no material
         * matches.
         */
        """
        pass

    def findUsedMaterials(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        find_used_materials(const EggMaterialCollection self, EggNode node)
        
        /**
         * Walks the egg hierarchy beginning at the indicated node, looking for
         * materials that are referenced by primitives but are not already members of
         * the collection, adding them to the collection.
         *
         * If this is called following extract_materials(), it can be used to pick up
         * any additional material references that appeared in the egg hierarchy (but
         * whose EggMaterial node was not actually part of the hierarchy).
         *
         * If this is called in lieu of extract_materials(), it will fill up the
         * collection with all of the referenced materials (and only the referenced
         * materials), without destructively removing the EggMaterials from the
         * hierarchy.
         *
         * This also has the side effect of incrementing the internal usage count for
         * a material in the collection each time a material reference is encountered.
         * This side effect is taken advantage of by remove_unused_materials().
         */
        """
        pass

    def find_mref(self, EggMaterialCollection_self, str_mref_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        find_mref(EggMaterialCollection self, str mref_name)
        
        // Find a material with a particular MRef name.
        
        /**
         * Returns the material with the indicated MRef name, or NULL if no material
         * matches.
         */
        """
        pass

    def find_used_materials(self, const_EggMaterialCollection_self, EggNode_node): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        find_used_materials(const EggMaterialCollection self, EggNode node)
        
        /**
         * Walks the egg hierarchy beginning at the indicated node, looking for
         * materials that are referenced by primitives but are not already members of
         * the collection, adding them to the collection.
         *
         * If this is called following extract_materials(), it can be used to pick up
         * any additional material references that appeared in the egg hierarchy (but
         * whose EggMaterial node was not actually part of the hierarchy).
         *
         * If this is called in lieu of extract_materials(), it will fill up the
         * collection with all of the referenced materials (and only the referenced
         * materials), without destructively removing the EggMaterials from the
         * hierarchy.
         *
         * This also has the side effect of incrementing the internal usage count for
         * a material in the collection each time a material reference is encountered.
         * This side effect is taken advantage of by remove_unused_materials().
         */
        """
        pass

    def removeMaterial(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_material(const EggMaterialCollection self, EggMaterial material)
        
        /**
         * Explicitly removes a material from the collection.  Returns true if the
         * material was removed, false if it wasn't there or if there was some error.
         */
        """
        pass

    def removeUnusedMaterials(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_unused_materials(const EggMaterialCollection self, EggNode node)
        
        /**
         * Removes any materials from the collection that aren't referenced by any
         * primitives in the indicated egg hierarchy.  This also, incidentally, adds
         * materials to the collection that had been referenced by primitives but had
         * not previously appeared in the collection.
         */
        """
        pass

    def remove_material(self, const_EggMaterialCollection_self, EggMaterial_material): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_material(const EggMaterialCollection self, EggMaterial material)
        
        /**
         * Explicitly removes a material from the collection.  Returns true if the
         * material was removed, false if it wasn't there or if there was some error.
         */
        """
        pass

    def remove_unused_materials(self, const_EggMaterialCollection_self, EggNode_node): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_unused_materials(const EggMaterialCollection self, EggNode node)
        
        /**
         * Removes any materials from the collection that aren't referenced by any
         * primitives in the indicated egg hierarchy.  This also, incidentally, adds
         * materials to the collection that had been referenced by primitives but had
         * not previously appeared in the collection.
         */
        """
        pass

    def sortByMref(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        sort_by_mref(const EggMaterialCollection self)
        
        /**
         * Sorts all the materials into alphabetical order by MRef name.  Subsequent
         * operations using begin()/end() will traverse in this sorted order.
         */
        """
        pass

    def sort_by_mref(self, const_EggMaterialCollection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        sort_by_mref(const EggMaterialCollection self)
        
        /**
         * Sorts all the materials into alphabetical order by MRef name.  Subsequent
         * operations using begin()/end() will traverse in this sorted order.
         */
        """
        pass

    def uniquifyMrefs(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        uniquify_mrefs(const EggMaterialCollection self)
        
        /**
         * Guarantees that each material in the collection has a unique MRef name.
         * This is essential before writing an egg file.
         */
        """
        pass

    def uniquify_mrefs(self, const_EggMaterialCollection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        uniquify_mrefs(const EggMaterialCollection self)
        
        /**
         * Guarantees that each material in the collection has a unique MRef name.
         * This is essential before writing an egg file.
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

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.egg.EggMaterialCollection' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.egg.EggMaterialCollection' objects>"
        '__doc__': '/**\n * This is a collection of materials by MRef name.  It can extract the\n * materials from an egg file and sort them all together; it can also manage\n * the creation of unique materials and the assignment of unique MRef names.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.egg.EggMaterialCollection' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC68CFFB0>'
        'addMaterial': None, # (!) real value is "<method 'addMaterial' of 'panda3d.egg.EggMaterialCollection' objects>"
        'add_material': None, # (!) real value is "<method 'add_material' of 'panda3d.egg.EggMaterialCollection' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.egg.EggMaterialCollection' objects>"
        'clear': None, # (!) real value is "<method 'clear' of 'panda3d.egg.EggMaterialCollection' objects>"
        'collapseEquivalentMaterials': None, # (!) real value is "<method 'collapseEquivalentMaterials' of 'panda3d.egg.EggMaterialCollection' objects>"
        'collapse_equivalent_materials': None, # (!) real value is "<method 'collapse_equivalent_materials' of 'panda3d.egg.EggMaterialCollection' objects>"
        'createUniqueMaterial': None, # (!) real value is "<method 'createUniqueMaterial' of 'panda3d.egg.EggMaterialCollection' objects>"
        'create_unique_material': None, # (!) real value is "<method 'create_unique_material' of 'panda3d.egg.EggMaterialCollection' objects>"
        'extractMaterials': None, # (!) real value is "<method 'extractMaterials' of 'panda3d.egg.EggMaterialCollection' objects>"
        'extract_materials': None, # (!) real value is "<method 'extract_materials' of 'panda3d.egg.EggMaterialCollection' objects>"
        'findMref': None, # (!) real value is "<method 'findMref' of 'panda3d.egg.EggMaterialCollection' objects>"
        'findUsedMaterials': None, # (!) real value is "<method 'findUsedMaterials' of 'panda3d.egg.EggMaterialCollection' objects>"
        'find_mref': None, # (!) real value is "<method 'find_mref' of 'panda3d.egg.EggMaterialCollection' objects>"
        'find_used_materials': None, # (!) real value is "<method 'find_used_materials' of 'panda3d.egg.EggMaterialCollection' objects>"
        'removeMaterial': None, # (!) real value is "<method 'removeMaterial' of 'panda3d.egg.EggMaterialCollection' objects>"
        'removeUnusedMaterials': None, # (!) real value is "<method 'removeUnusedMaterials' of 'panda3d.egg.EggMaterialCollection' objects>"
        'remove_material': None, # (!) real value is "<method 'remove_material' of 'panda3d.egg.EggMaterialCollection' objects>"
        'remove_unused_materials': None, # (!) real value is "<method 'remove_unused_materials' of 'panda3d.egg.EggMaterialCollection' objects>"
        'sortByMref': None, # (!) real value is "<method 'sortByMref' of 'panda3d.egg.EggMaterialCollection' objects>"
        'sort_by_mref': None, # (!) real value is "<method 'sort_by_mref' of 'panda3d.egg.EggMaterialCollection' objects>"
        'uniquifyMrefs': None, # (!) real value is "<method 'uniquifyMrefs' of 'panda3d.egg.EggMaterialCollection' objects>"
        'uniquify_mrefs': None, # (!) real value is "<method 'uniquify_mrefs' of 'panda3d.egg.EggMaterialCollection' objects>"
    }


