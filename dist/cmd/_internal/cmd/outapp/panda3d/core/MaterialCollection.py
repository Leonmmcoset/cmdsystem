# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class MaterialCollection(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     *
     */
    """
    def addMaterial(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_material(const MaterialCollection self, Material node_material)
        
        /**
         * Adds a new Material to the collection.
         */
        """
        pass

    def addMaterialsFrom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_materials_from(const MaterialCollection self, const MaterialCollection other)
        
        /**
         * Adds all the Materials indicated in the other collection to this material.
         * The other materials are simply appended to the end of the materials in this
         * list; duplicates are not automatically removed.
         */
        """
        pass

    def add_material(self, const_MaterialCollection_self, Material_node_material): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_material(const MaterialCollection self, Material node_material)
        
        /**
         * Adds a new Material to the collection.
         */
        """
        pass

    def add_materials_from(self, const_MaterialCollection_self, const_MaterialCollection_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_materials_from(const MaterialCollection self, const MaterialCollection other)
        
        /**
         * Adds all the Materials indicated in the other collection to this material.
         * The other materials are simply appended to the end of the materials in this
         * list; duplicates are not automatically removed.
         */
        """
        pass

    def assign(self, const_MaterialCollection_self, const_MaterialCollection_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const MaterialCollection self, const MaterialCollection copy)
        """
        pass

    def clear(self, const_MaterialCollection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear(const MaterialCollection self)
        
        /**
         * Removes all Materials from the collection.
         */
        """
        pass

    def findMaterial(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        find_material(MaterialCollection self, str name)
        
        /**
         * Returns the material in the collection with the indicated name, if any, or
         * NULL if no material has that name.
         */
        """
        pass

    def find_material(self, MaterialCollection_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        find_material(MaterialCollection self, str name)
        
        /**
         * Returns the material in the collection with the indicated name, if any, or
         * NULL if no material has that name.
         */
        """
        pass

    def getMaterial(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_material(MaterialCollection self, int index)
        
        /**
         * Returns the nth Material in the collection.
         */
        """
        pass

    def getNumMaterials(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_materials(MaterialCollection self)
        
        /**
         * Returns the number of Materials in the collection.
         */
        """
        pass

    def get_material(self, MaterialCollection_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_material(MaterialCollection self, int index)
        
        /**
         * Returns the nth Material in the collection.
         */
        """
        pass

    def get_num_materials(self, MaterialCollection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_materials(MaterialCollection self)
        
        /**
         * Returns the number of Materials in the collection.
         */
        """
        pass

    def hasMaterial(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_material(MaterialCollection self, Material material)
        
        /**
         * Returns true if the indicated Material appears in this collection, false
         * otherwise.
         */
        """
        pass

    def has_material(self, MaterialCollection_self, Material_material): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_material(MaterialCollection self, Material material)
        
        /**
         * Returns true if the indicated Material appears in this collection, false
         * otherwise.
         */
        """
        pass

    def output(self, MaterialCollection_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(MaterialCollection self, ostream out)
        
        /**
         * Writes a brief one-line description of the MaterialCollection to the
         * indicated output stream.
         */
        """
        pass

    def removeDuplicateMaterials(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_duplicate_materials(const MaterialCollection self)
        
        /**
         * Removes any duplicate entries of the same Materials on this collection.  If
         * a Material appears multiple times, the first appearance is retained;
         * subsequent appearances are removed.
         */
        """
        pass

    def removeMaterial(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_material(const MaterialCollection self, Material node_material)
        
        /**
         * Removes the indicated Material from the collection.  Returns true if the
         * material was removed, false if it was not a member of the collection.
         */
        """
        pass

    def removeMaterialsFrom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_materials_from(const MaterialCollection self, const MaterialCollection other)
        
        /**
         * Removes from this collection all of the Materials listed in the other
         * collection.
         */
        """
        pass

    def remove_duplicate_materials(self, const_MaterialCollection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_duplicate_materials(const MaterialCollection self)
        
        /**
         * Removes any duplicate entries of the same Materials on this collection.  If
         * a Material appears multiple times, the first appearance is retained;
         * subsequent appearances are removed.
         */
        """
        pass

    def remove_material(self, const_MaterialCollection_self, Material_node_material): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_material(const MaterialCollection self, Material node_material)
        
        /**
         * Removes the indicated Material from the collection.  Returns true if the
         * material was removed, false if it was not a member of the collection.
         */
        """
        pass

    def remove_materials_from(self, const_MaterialCollection_self, const_MaterialCollection_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_materials_from(const MaterialCollection self, const MaterialCollection other)
        
        /**
         * Removes from this collection all of the Materials listed in the other
         * collection.
         */
        """
        pass

    def write(self, MaterialCollection_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(MaterialCollection self, ostream out, int indent_level)
        
        /**
         * Writes a complete multi-line description of the MaterialCollection to the
         * indicated output stream.
         */
        """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __iadd__(self, *args, **kwargs): # real signature unknown
        """ Return self+=value. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__add__': None, # (!) real value is "<slot wrapper '__add__' of 'panda3d.core.MaterialCollection' objects>"
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.MaterialCollection' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.MaterialCollection' objects>"
        '__doc__': '/**\n *\n */',
        '__getitem__': None, # (!) real value is "<slot wrapper '__getitem__' of 'panda3d.core.MaterialCollection' objects>"
        '__iadd__': None, # (!) real value is "<slot wrapper '__iadd__' of 'panda3d.core.MaterialCollection' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.MaterialCollection' objects>"
        '__len__': None, # (!) real value is "<slot wrapper '__len__' of 'panda3d.core.MaterialCollection' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2936D0>'
        '__radd__': None, # (!) real value is "<slot wrapper '__radd__' of 'panda3d.core.MaterialCollection' objects>"
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.MaterialCollection' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.MaterialCollection' objects>"
        'addMaterial': None, # (!) real value is "<method 'addMaterial' of 'panda3d.core.MaterialCollection' objects>"
        'addMaterialsFrom': None, # (!) real value is "<method 'addMaterialsFrom' of 'panda3d.core.MaterialCollection' objects>"
        'add_material': None, # (!) real value is "<method 'add_material' of 'panda3d.core.MaterialCollection' objects>"
        'add_materials_from': None, # (!) real value is "<method 'add_materials_from' of 'panda3d.core.MaterialCollection' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.MaterialCollection' objects>"
        'clear': None, # (!) real value is "<method 'clear' of 'panda3d.core.MaterialCollection' objects>"
        'findMaterial': None, # (!) real value is "<method 'findMaterial' of 'panda3d.core.MaterialCollection' objects>"
        'find_material': None, # (!) real value is "<method 'find_material' of 'panda3d.core.MaterialCollection' objects>"
        'getMaterial': None, # (!) real value is "<method 'getMaterial' of 'panda3d.core.MaterialCollection' objects>"
        'getNumMaterials': None, # (!) real value is "<method 'getNumMaterials' of 'panda3d.core.MaterialCollection' objects>"
        'get_material': None, # (!) real value is "<method 'get_material' of 'panda3d.core.MaterialCollection' objects>"
        'get_num_materials': None, # (!) real value is "<method 'get_num_materials' of 'panda3d.core.MaterialCollection' objects>"
        'hasMaterial': None, # (!) real value is "<method 'hasMaterial' of 'panda3d.core.MaterialCollection' objects>"
        'has_material': None, # (!) real value is "<method 'has_material' of 'panda3d.core.MaterialCollection' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.MaterialCollection' objects>"
        'removeDuplicateMaterials': None, # (!) real value is "<method 'removeDuplicateMaterials' of 'panda3d.core.MaterialCollection' objects>"
        'removeMaterial': None, # (!) real value is "<method 'removeMaterial' of 'panda3d.core.MaterialCollection' objects>"
        'removeMaterialsFrom': None, # (!) real value is "<method 'removeMaterialsFrom' of 'panda3d.core.MaterialCollection' objects>"
        'remove_duplicate_materials': None, # (!) real value is "<method 'remove_duplicate_materials' of 'panda3d.core.MaterialCollection' objects>"
        'remove_material': None, # (!) real value is "<method 'remove_material' of 'panda3d.core.MaterialCollection' objects>"
        'remove_materials_from': None, # (!) real value is "<method 'remove_materials_from' of 'panda3d.core.MaterialCollection' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.MaterialCollection' objects>"
    }


