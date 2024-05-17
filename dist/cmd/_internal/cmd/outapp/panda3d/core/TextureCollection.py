# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class TextureCollection(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * Manages a list of Texture objects, as returned by
     * TexturePool::find_all_textures().
     */
    """
    def addTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_texture(const TextureCollection self, Texture texture)
        
        /**
         * Adds a new Texture to the collection.
         */
        """
        pass

    def addTexturesFrom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_textures_from(const TextureCollection self, const TextureCollection other)
        
        /**
         * Adds all the Textures indicated in the other collection to this texture.
         * The other textures are simply appended to the end of the textures in this
         * list; duplicates are not automatically removed.
         */
        """
        pass

    def add_texture(self, const_TextureCollection_self, Texture_texture): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_texture(const TextureCollection self, Texture texture)
        
        /**
         * Adds a new Texture to the collection.
         */
        """
        pass

    def add_textures_from(self, const_TextureCollection_self, const_TextureCollection_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_textures_from(const TextureCollection self, const TextureCollection other)
        
        /**
         * Adds all the Textures indicated in the other collection to this texture.
         * The other textures are simply appended to the end of the textures in this
         * list; duplicates are not automatically removed.
         */
        """
        pass

    def append(self, const_TextureCollection_self, Texture_texture): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        append(const TextureCollection self, Texture texture)
        
        // Method names to satisfy Python's conventions.
        
        /**
         * Adds a new Texture to the collection.  This method duplicates the
         * add_texture() method; it is provided to satisfy Python's naming convention.
         */
        """
        pass

    def assign(self, const_TextureCollection_self, const_TextureCollection_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const TextureCollection self, const TextureCollection copy)
        """
        pass

    def clear(self, const_TextureCollection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear(const TextureCollection self)
        
        /**
         * Removes all Textures from the collection.
         */
        """
        pass

    def extend(self, const_TextureCollection_self, const_TextureCollection_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        extend(const TextureCollection self, const TextureCollection other)
        
        /**
         * Appends the other list onto the end of this one.  This method duplicates
         * the += operator; it is provided to satisfy Python's naming convention.
         */
        """
        pass

    def findTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        find_texture(TextureCollection self, str name)
        
        /**
         * Returns the texture in the collection with the indicated name, if any, or
         * NULL if no texture has that name.
         */
        """
        pass

    def find_texture(self, TextureCollection_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        find_texture(TextureCollection self, str name)
        
        /**
         * Returns the texture in the collection with the indicated name, if any, or
         * NULL if no texture has that name.
         */
        """
        pass

    def getNumTextures(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_textures(TextureCollection self)
        
        /**
         * Returns the number of Textures in the collection.
         */
        """
        pass

    def getTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_texture(TextureCollection self, int index)
        
        /**
         * Returns the nth Texture in the collection.
         */
        """
        pass

    def getTextures(self, *args, **kwargs): # real signature unknown
        pass

    def get_num_textures(self, TextureCollection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_textures(TextureCollection self)
        
        /**
         * Returns the number of Textures in the collection.
         */
        """
        pass

    def get_texture(self, TextureCollection_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_texture(TextureCollection self, int index)
        
        /**
         * Returns the nth Texture in the collection.
         */
        """
        pass

    def get_textures(self, *args, **kwargs): # real signature unknown
        pass

    def hasTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_texture(TextureCollection self, Texture texture)
        
        /**
         * Returns true if the indicated Texture appears in this collection, false
         * otherwise.
         */
        """
        pass

    def has_texture(self, TextureCollection_self, Texture_texture): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_texture(TextureCollection self, Texture texture)
        
        /**
         * Returns true if the indicated Texture appears in this collection, false
         * otherwise.
         */
        """
        pass

    def output(self, TextureCollection_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(TextureCollection self, ostream out)
        
        /**
         * Writes a brief one-line description of the TextureCollection to the
         * indicated output stream.
         */
        """
        pass

    def removeDuplicateTextures(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_duplicate_textures(const TextureCollection self)
        
        /**
         * Removes any duplicate entries of the same Textures on this collection.  If
         * a Texture appears multiple times, the first appearance is retained;
         * subsequent appearances are removed.
         */
        """
        pass

    def removeTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_texture(const TextureCollection self, Texture texture)
        
        /**
         * Removes the indicated Texture from the collection.  Returns true if the
         * texture was removed, false if it was not a member of the collection.
         */
        """
        pass

    def removeTexturesFrom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_textures_from(const TextureCollection self, const TextureCollection other)
        
        /**
         * Removes from this collection all of the Textures listed in the other
         * collection.
         */
        """
        pass

    def remove_duplicate_textures(self, const_TextureCollection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_duplicate_textures(const TextureCollection self)
        
        /**
         * Removes any duplicate entries of the same Textures on this collection.  If
         * a Texture appears multiple times, the first appearance is retained;
         * subsequent appearances are removed.
         */
        """
        pass

    def remove_texture(self, const_TextureCollection_self, Texture_texture): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_texture(const TextureCollection self, Texture texture)
        
        /**
         * Removes the indicated Texture from the collection.  Returns true if the
         * texture was removed, false if it was not a member of the collection.
         */
        """
        pass

    def remove_textures_from(self, const_TextureCollection_self, const_TextureCollection_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_textures_from(const TextureCollection self, const TextureCollection other)
        
        /**
         * Removes from this collection all of the Textures listed in the other
         * collection.
         */
        """
        pass

    def reserve(self, const_TextureCollection_self, int_num): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        reserve(const TextureCollection self, int num)
        
        /**
         * This is a hint to Panda to allocate enough memory to hold the given number
         * of NodePaths, if you know ahead of time how many you will be adding.
         */
        """
        pass

    def write(self, TextureCollection_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(TextureCollection self, ostream out, int indent_level)
        
        /**
         * Writes a complete multi-line description of the TextureCollection to the
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

    def __reduce__(self, TextureCollection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        __reduce__(TextureCollection self)
        """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__add__': None, # (!) real value is "<slot wrapper '__add__' of 'panda3d.core.TextureCollection' objects>"
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.TextureCollection' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.TextureCollection' objects>"
        '__doc__': '/**\n * Manages a list of Texture objects, as returned by\n * TexturePool::find_all_textures().\n */',
        '__getitem__': None, # (!) real value is "<slot wrapper '__getitem__' of 'panda3d.core.TextureCollection' objects>"
        '__iadd__': None, # (!) real value is "<slot wrapper '__iadd__' of 'panda3d.core.TextureCollection' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.TextureCollection' objects>"
        '__len__': None, # (!) real value is "<slot wrapper '__len__' of 'panda3d.core.TextureCollection' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE301180>'
        '__radd__': None, # (!) real value is "<slot wrapper '__radd__' of 'panda3d.core.TextureCollection' objects>"
        '__reduce__': None, # (!) real value is "<method '__reduce__' of 'panda3d.core.TextureCollection' objects>"
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.TextureCollection' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.TextureCollection' objects>"
        'addTexture': None, # (!) real value is "<method 'addTexture' of 'panda3d.core.TextureCollection' objects>"
        'addTexturesFrom': None, # (!) real value is "<method 'addTexturesFrom' of 'panda3d.core.TextureCollection' objects>"
        'add_texture': None, # (!) real value is "<method 'add_texture' of 'panda3d.core.TextureCollection' objects>"
        'add_textures_from': None, # (!) real value is "<method 'add_textures_from' of 'panda3d.core.TextureCollection' objects>"
        'append': None, # (!) real value is "<method 'append' of 'panda3d.core.TextureCollection' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.TextureCollection' objects>"
        'clear': None, # (!) real value is "<method 'clear' of 'panda3d.core.TextureCollection' objects>"
        'extend': None, # (!) real value is "<method 'extend' of 'panda3d.core.TextureCollection' objects>"
        'findTexture': None, # (!) real value is "<method 'findTexture' of 'panda3d.core.TextureCollection' objects>"
        'find_texture': None, # (!) real value is "<method 'find_texture' of 'panda3d.core.TextureCollection' objects>"
        'getNumTextures': None, # (!) real value is "<method 'getNumTextures' of 'panda3d.core.TextureCollection' objects>"
        'getTexture': None, # (!) real value is "<method 'getTexture' of 'panda3d.core.TextureCollection' objects>"
        'getTextures': None, # (!) real value is "<method 'getTextures' of 'panda3d.core.TextureCollection' objects>"
        'get_num_textures': None, # (!) real value is "<method 'get_num_textures' of 'panda3d.core.TextureCollection' objects>"
        'get_texture': None, # (!) real value is "<method 'get_texture' of 'panda3d.core.TextureCollection' objects>"
        'get_textures': None, # (!) real value is "<method 'get_textures' of 'panda3d.core.TextureCollection' objects>"
        'hasTexture': None, # (!) real value is "<method 'hasTexture' of 'panda3d.core.TextureCollection' objects>"
        'has_texture': None, # (!) real value is "<method 'has_texture' of 'panda3d.core.TextureCollection' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.TextureCollection' objects>"
        'removeDuplicateTextures': None, # (!) real value is "<method 'removeDuplicateTextures' of 'panda3d.core.TextureCollection' objects>"
        'removeTexture': None, # (!) real value is "<method 'removeTexture' of 'panda3d.core.TextureCollection' objects>"
        'removeTexturesFrom': None, # (!) real value is "<method 'removeTexturesFrom' of 'panda3d.core.TextureCollection' objects>"
        'remove_duplicate_textures': None, # (!) real value is "<method 'remove_duplicate_textures' of 'panda3d.core.TextureCollection' objects>"
        'remove_texture': None, # (!) real value is "<method 'remove_texture' of 'panda3d.core.TextureCollection' objects>"
        'remove_textures_from': None, # (!) real value is "<method 'remove_textures_from' of 'panda3d.core.TextureCollection' objects>"
        'reserve': None, # (!) real value is "<method 'reserve' of 'panda3d.core.TextureCollection' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.TextureCollection' objects>"
    }


