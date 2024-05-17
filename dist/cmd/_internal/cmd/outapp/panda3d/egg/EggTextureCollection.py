# encoding: utf-8
# module panda3d.egg
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\egg.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


class EggTextureCollection(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This is a collection of textures by TRef name.  It can extract the textures
     * from an egg file and sort them all together; it can also manage the
     * creation of unique textures and the assignment of unique TRef names.
     */
    """
    def addTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_texture(const EggTextureCollection self, EggTexture texture)
        
        /**
         * Explicitly adds a new texture to the collection.  Returns true if the
         * texture was added, false if it was already there or if there was some
         * error.
         */
        """
        pass

    def add_texture(self, const_EggTextureCollection_self, EggTexture_texture): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_texture(const EggTextureCollection self, EggTexture texture)
        
        /**
         * Explicitly adds a new texture to the collection.  Returns true if the
         * texture was added, false if it was already there or if there was some
         * error.
         */
        """
        pass

    def assign(self, const_EggTextureCollection_self, const_EggTextureCollection_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const EggTextureCollection self, const EggTextureCollection copy)
        
        /**
         *
         */
        """
        pass

    def clear(self, const_EggTextureCollection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear(const EggTextureCollection self)
        
        /**
         * Removes all textures from the collection.
         */
        """
        pass

    def collapseEquivalentTextures(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        collapse_equivalent_textures(const EggTextureCollection self, int eq, EggGroupNode node)
        
        /**
         * Walks through the collection and collapses together any separate textures
         * that are equivalent according to the indicated equivalence factor, eq (see
         * EggTexture::is_equivalent_to()).  The return value is the number of
         * textures removed.
         *
         * This flavor of collapse_equivalent_textures() automatically adjusts all the
         * primitives in the egg hierarchy to refer to the new texture pointers.
         */
        
        /**
         * Walks through the collection and collapses together any separate textures
         * that are equivalent according to the indicated equivalence factor, eq (see
         * EggTexture::is_equivalent_to()).  The return value is the number of
         * textures removed.
         *
         * This flavor of collapse_equivalent_textures() does not adjust any
         * primitives in the egg hierarchy; instead, it fills up the 'removed' map
         * with an entry for each removed texture, mapping it back to the equivalent
         * retained texture.  It's up to the user to then call replace_textures() with
         * this map, if desired, to apply these changes to the egg hierarchy.
         */
        """
        pass

    def collapse_equivalent_textures(self, const_EggTextureCollection_self, int_eq, EggGroupNode_node): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        collapse_equivalent_textures(const EggTextureCollection self, int eq, EggGroupNode node)
        
        /**
         * Walks through the collection and collapses together any separate textures
         * that are equivalent according to the indicated equivalence factor, eq (see
         * EggTexture::is_equivalent_to()).  The return value is the number of
         * textures removed.
         *
         * This flavor of collapse_equivalent_textures() automatically adjusts all the
         * primitives in the egg hierarchy to refer to the new texture pointers.
         */
        
        /**
         * Walks through the collection and collapses together any separate textures
         * that are equivalent according to the indicated equivalence factor, eq (see
         * EggTexture::is_equivalent_to()).  The return value is the number of
         * textures removed.
         *
         * This flavor of collapse_equivalent_textures() does not adjust any
         * primitives in the egg hierarchy; instead, it fills up the 'removed' map
         * with an entry for each removed texture, mapping it back to the equivalent
         * retained texture.  It's up to the user to then call replace_textures() with
         * this map, if desired, to apply these changes to the egg hierarchy.
         */
        """
        pass

    def createUniqueTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        create_unique_texture(const EggTextureCollection self, const EggTexture copy, int eq)
        
        // create_unique_texture() creates a new texture if there is not already one
        // equivalent (according to eq, see EggTexture::is_equivalent_to()) to the
        // indicated texture, or returns the existing one if there is.
        
        /**
         * Creates a new texture if there is not already one equivalent (according to
         * eq, see EggTexture::is_equivalent_to()) to the indicated texture, or
         * returns the existing one if there is.
         */
        """
        pass

    def create_unique_texture(self, const_EggTextureCollection_self, const_EggTexture_copy, int_eq): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        create_unique_texture(const EggTextureCollection self, const EggTexture copy, int eq)
        
        // create_unique_texture() creates a new texture if there is not already one
        // equivalent (according to eq, see EggTexture::is_equivalent_to()) to the
        // indicated texture, or returns the existing one if there is.
        
        /**
         * Creates a new texture if there is not already one equivalent (according to
         * eq, see EggTexture::is_equivalent_to()) to the indicated texture, or
         * returns the existing one if there is.
         */
        """
        pass

    def extractTextures(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        extract_textures(const EggTextureCollection self, EggGroupNode node)
        
        /**
         * Walks the egg hierarchy beginning at the indicated node, and removes any
         * EggTextures encountered in the hierarchy, adding them to the collection.
         * Returns the number of EggTextures encountered.
         */
        """
        pass

    def extract_textures(self, const_EggTextureCollection_self, EggGroupNode_node): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        extract_textures(const EggTextureCollection self, EggGroupNode node)
        
        /**
         * Walks the egg hierarchy beginning at the indicated node, and removes any
         * EggTextures encountered in the hierarchy, adding them to the collection.
         * Returns the number of EggTextures encountered.
         */
        """
        pass

    def findFilename(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        find_filename(EggTextureCollection self, const Filename filename)
        
        // Find a texture with a particular filename.
        
        /**
         * Returns the texture with the indicated filename, or NULL if no texture
         * matches.
         */
        """
        pass

    def findTref(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        find_tref(EggTextureCollection self, str tref_name)
        
        // Find a texture with a particular TRef name.
        
        /**
         * Returns the texture with the indicated TRef name, or NULL if no texture
         * matches.
         */
        """
        pass

    def findUsedTextures(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        find_used_textures(const EggTextureCollection self, EggNode node)
        
        /**
         * Walks the egg hierarchy beginning at the indicated node, looking for
         * textures that are referenced by primitives but are not already members of
         * the collection, adding them to the collection.
         *
         * If this is called following extract_textures(), it can be used to pick up
         * any additional texture references that appeared in the egg hierarchy (but
         * whose EggTexture node was not actually part of the hierarchy).
         *
         * If this is called in lieu of extract_textures(), it will fill up the
         * collection with all of the referenced textures (and only the referenced
         * textures), without destructively removing the EggTextures from the
         * hierarchy.
         *
         * This also has the side effect of incrementing the internal usage count for
         * a texture in the collection each time a texture reference is encountered.
         * This side effect is taken advantage of by remove_unused_textures().
         *
         * And one more side effect: this function identifies the presence of
         * multitexturing in the egg file, and calls multitexture_over() on each
         * texture appropriately so that, after this call, you may expect
         * get_multitexture_sort() to return a reasonable value for each texture.
         */
        """
        pass

    def find_filename(self, EggTextureCollection_self, const_Filename_filename): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        find_filename(EggTextureCollection self, const Filename filename)
        
        // Find a texture with a particular filename.
        
        /**
         * Returns the texture with the indicated filename, or NULL if no texture
         * matches.
         */
        """
        pass

    def find_tref(self, EggTextureCollection_self, str_tref_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        find_tref(EggTextureCollection self, str tref_name)
        
        // Find a texture with a particular TRef name.
        
        /**
         * Returns the texture with the indicated TRef name, or NULL if no texture
         * matches.
         */
        """
        pass

    def find_used_textures(self, const_EggTextureCollection_self, EggNode_node): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        find_used_textures(const EggTextureCollection self, EggNode node)
        
        /**
         * Walks the egg hierarchy beginning at the indicated node, looking for
         * textures that are referenced by primitives but are not already members of
         * the collection, adding them to the collection.
         *
         * If this is called following extract_textures(), it can be used to pick up
         * any additional texture references that appeared in the egg hierarchy (but
         * whose EggTexture node was not actually part of the hierarchy).
         *
         * If this is called in lieu of extract_textures(), it will fill up the
         * collection with all of the referenced textures (and only the referenced
         * textures), without destructively removing the EggTextures from the
         * hierarchy.
         *
         * This also has the side effect of incrementing the internal usage count for
         * a texture in the collection each time a texture reference is encountered.
         * This side effect is taken advantage of by remove_unused_textures().
         *
         * And one more side effect: this function identifies the presence of
         * multitexturing in the egg file, and calls multitexture_over() on each
         * texture appropriately so that, after this call, you may expect
         * get_multitexture_sort() to return a reasonable value for each texture.
         */
        """
        pass

    def getNumTextures(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_textures(EggTextureCollection self)
        
        /**
         * Returns the number of EggTextures in the collection.
         */
        """
        pass

    def getTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_texture(EggTextureCollection self, int index)
        
        /**
         * Returns the nth EggTexture in the collection.
         */
        """
        pass

    def getTextures(self, *args, **kwargs): # real signature unknown
        pass

    def get_num_textures(self, EggTextureCollection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_textures(EggTextureCollection self)
        
        /**
         * Returns the number of EggTextures in the collection.
         */
        """
        pass

    def get_texture(self, EggTextureCollection_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_texture(EggTextureCollection self, int index)
        
        /**
         * Returns the nth EggTexture in the collection.
         */
        """
        pass

    def get_textures(self, *args, **kwargs): # real signature unknown
        pass

    def isEmpty(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_empty(EggTextureCollection self)
        
        /**
         * Returns true if there are no EggTexures in the collection, false otherwise.
         */
        """
        pass

    def is_empty(self, EggTextureCollection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_empty(EggTextureCollection self)
        
        /**
         * Returns true if there are no EggTexures in the collection, false otherwise.
         */
        """
        pass

    def removeTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_texture(const EggTextureCollection self, EggTexture texture)
        
        /**
         * Explicitly removes a texture from the collection.  Returns true if the
         * texture was removed, false if it wasn't there or if there was some error.
         */
        """
        pass

    def removeUnusedTextures(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_unused_textures(const EggTextureCollection self, EggNode node)
        
        /**
         * Removes any textures from the collection that aren't referenced by any
         * primitives in the indicated egg hierarchy.  This also, incidentally, adds
         * textures to the collection that had been referenced by primitives but had
         * not previously appeared in the collection.
         */
        """
        pass

    def remove_texture(self, const_EggTextureCollection_self, EggTexture_texture): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_texture(const EggTextureCollection self, EggTexture texture)
        
        /**
         * Explicitly removes a texture from the collection.  Returns true if the
         * texture was removed, false if it wasn't there or if there was some error.
         */
        """
        pass

    def remove_unused_textures(self, const_EggTextureCollection_self, EggNode_node): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_unused_textures(const EggTextureCollection self, EggNode node)
        
        /**
         * Removes any textures from the collection that aren't referenced by any
         * primitives in the indicated egg hierarchy.  This also, incidentally, adds
         * textures to the collection that had been referenced by primitives but had
         * not previously appeared in the collection.
         */
        """
        pass

    def sortByBasename(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        sort_by_basename(const EggTextureCollection self)
        
        /**
         * Sorts all the textures into alphabetical order by the basename part
         * (including extension) of the filename.  Subsequent operations using
         * begin()/end() will traverse in this sorted order.
         */
        """
        pass

    def sortByTref(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        sort_by_tref(const EggTextureCollection self)
        
        /**
         * Sorts all the textures into alphabetical order by TRef name.  Subsequent
         * operations using begin()/end() will traverse in this sorted order.
         */
        """
        pass

    def sort_by_basename(self, const_EggTextureCollection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        sort_by_basename(const EggTextureCollection self)
        
        /**
         * Sorts all the textures into alphabetical order by the basename part
         * (including extension) of the filename.  Subsequent operations using
         * begin()/end() will traverse in this sorted order.
         */
        """
        pass

    def sort_by_tref(self, const_EggTextureCollection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        sort_by_tref(const EggTextureCollection self)
        
        /**
         * Sorts all the textures into alphabetical order by TRef name.  Subsequent
         * operations using begin()/end() will traverse in this sorted order.
         */
        """
        pass

    def uniquifyTrefs(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        uniquify_trefs(const EggTextureCollection self)
        
        /**
         * Guarantees that each texture in the collection has a unique TRef name.
         * This is essential before writing an egg file.
         */
        """
        pass

    def uniquify_trefs(self, const_EggTextureCollection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        uniquify_trefs(const EggTextureCollection self)
        
        /**
         * Guarantees that each texture in the collection has a unique TRef name.
         * This is essential before writing an egg file.
         */
        """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
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

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.egg.EggTextureCollection' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.egg.EggTextureCollection' objects>"
        '__doc__': '/**\n * This is a collection of textures by TRef name.  It can extract the textures\n * from an egg file and sort them all together; it can also manage the\n * creation of unique textures and the assignment of unique TRef names.\n */',
        '__getitem__': None, # (!) real value is "<slot wrapper '__getitem__' of 'panda3d.egg.EggTextureCollection' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.egg.EggTextureCollection' objects>"
        '__len__': None, # (!) real value is "<slot wrapper '__len__' of 'panda3d.egg.EggTextureCollection' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC68D13A0>'
        'addTexture': None, # (!) real value is "<method 'addTexture' of 'panda3d.egg.EggTextureCollection' objects>"
        'add_texture': None, # (!) real value is "<method 'add_texture' of 'panda3d.egg.EggTextureCollection' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.egg.EggTextureCollection' objects>"
        'clear': None, # (!) real value is "<method 'clear' of 'panda3d.egg.EggTextureCollection' objects>"
        'collapseEquivalentTextures': None, # (!) real value is "<method 'collapseEquivalentTextures' of 'panda3d.egg.EggTextureCollection' objects>"
        'collapse_equivalent_textures': None, # (!) real value is "<method 'collapse_equivalent_textures' of 'panda3d.egg.EggTextureCollection' objects>"
        'createUniqueTexture': None, # (!) real value is "<method 'createUniqueTexture' of 'panda3d.egg.EggTextureCollection' objects>"
        'create_unique_texture': None, # (!) real value is "<method 'create_unique_texture' of 'panda3d.egg.EggTextureCollection' objects>"
        'extractTextures': None, # (!) real value is "<method 'extractTextures' of 'panda3d.egg.EggTextureCollection' objects>"
        'extract_textures': None, # (!) real value is "<method 'extract_textures' of 'panda3d.egg.EggTextureCollection' objects>"
        'findFilename': None, # (!) real value is "<method 'findFilename' of 'panda3d.egg.EggTextureCollection' objects>"
        'findTref': None, # (!) real value is "<method 'findTref' of 'panda3d.egg.EggTextureCollection' objects>"
        'findUsedTextures': None, # (!) real value is "<method 'findUsedTextures' of 'panda3d.egg.EggTextureCollection' objects>"
        'find_filename': None, # (!) real value is "<method 'find_filename' of 'panda3d.egg.EggTextureCollection' objects>"
        'find_tref': None, # (!) real value is "<method 'find_tref' of 'panda3d.egg.EggTextureCollection' objects>"
        'find_used_textures': None, # (!) real value is "<method 'find_used_textures' of 'panda3d.egg.EggTextureCollection' objects>"
        'getNumTextures': None, # (!) real value is "<method 'getNumTextures' of 'panda3d.egg.EggTextureCollection' objects>"
        'getTexture': None, # (!) real value is "<method 'getTexture' of 'panda3d.egg.EggTextureCollection' objects>"
        'getTextures': None, # (!) real value is "<method 'getTextures' of 'panda3d.egg.EggTextureCollection' objects>"
        'get_num_textures': None, # (!) real value is "<method 'get_num_textures' of 'panda3d.egg.EggTextureCollection' objects>"
        'get_texture': None, # (!) real value is "<method 'get_texture' of 'panda3d.egg.EggTextureCollection' objects>"
        'get_textures': None, # (!) real value is "<method 'get_textures' of 'panda3d.egg.EggTextureCollection' objects>"
        'isEmpty': None, # (!) real value is "<method 'isEmpty' of 'panda3d.egg.EggTextureCollection' objects>"
        'is_empty': None, # (!) real value is "<method 'is_empty' of 'panda3d.egg.EggTextureCollection' objects>"
        'removeTexture': None, # (!) real value is "<method 'removeTexture' of 'panda3d.egg.EggTextureCollection' objects>"
        'removeUnusedTextures': None, # (!) real value is "<method 'removeUnusedTextures' of 'panda3d.egg.EggTextureCollection' objects>"
        'remove_texture': None, # (!) real value is "<method 'remove_texture' of 'panda3d.egg.EggTextureCollection' objects>"
        'remove_unused_textures': None, # (!) real value is "<method 'remove_unused_textures' of 'panda3d.egg.EggTextureCollection' objects>"
        'sortByBasename': None, # (!) real value is "<method 'sortByBasename' of 'panda3d.egg.EggTextureCollection' objects>"
        'sortByTref': None, # (!) real value is "<method 'sortByTref' of 'panda3d.egg.EggTextureCollection' objects>"
        'sort_by_basename': None, # (!) real value is "<method 'sort_by_basename' of 'panda3d.egg.EggTextureCollection' objects>"
        'sort_by_tref': None, # (!) real value is "<method 'sort_by_tref' of 'panda3d.egg.EggTextureCollection' objects>"
        'uniquifyTrefs': None, # (!) real value is "<method 'uniquifyTrefs' of 'panda3d.egg.EggTextureCollection' objects>"
        'uniquify_trefs': None, # (!) real value is "<method 'uniquify_trefs' of 'panda3d.egg.EggTextureCollection' objects>"
    }


