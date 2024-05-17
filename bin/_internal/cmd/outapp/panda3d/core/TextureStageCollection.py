# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class TextureStageCollection(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     *
     */
    """
    def addTextureStage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_texture_stage(const TextureStageCollection self, TextureStage node_texture_stage)
        
        /**
         * Adds a new TextureStage to the collection.
         */
        """
        pass

    def addTextureStagesFrom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_texture_stages_from(const TextureStageCollection self, const TextureStageCollection other)
        
        /**
         * Adds all the TextureStages indicated in the other collection to this
         * texture_stage.  The other texture_stages are simply appended to the end of
         * the texture_stages in this list; duplicates are not automatically removed.
         */
        """
        pass

    def add_texture_stage(self, const_TextureStageCollection_self, TextureStage_node_texture_stage): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_texture_stage(const TextureStageCollection self, TextureStage node_texture_stage)
        
        /**
         * Adds a new TextureStage to the collection.
         */
        """
        pass

    def add_texture_stages_from(self, const_TextureStageCollection_self, const_TextureStageCollection_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_texture_stages_from(const TextureStageCollection self, const TextureStageCollection other)
        
        /**
         * Adds all the TextureStages indicated in the other collection to this
         * texture_stage.  The other texture_stages are simply appended to the end of
         * the texture_stages in this list; duplicates are not automatically removed.
         */
        """
        pass

    def assign(self, const_TextureStageCollection_self, const_TextureStageCollection_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const TextureStageCollection self, const TextureStageCollection copy)
        """
        pass

    def clear(self, const_TextureStageCollection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear(const TextureStageCollection self)
        
        /**
         * Removes all TextureStages from the collection.
         */
        """
        pass

    def findTextureStage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        find_texture_stage(TextureStageCollection self, str name)
        
        /**
         * Returns the texture_stage in the collection with the indicated name, if
         * any, or NULL if no texture_stage has that name.
         */
        """
        pass

    def find_texture_stage(self, TextureStageCollection_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        find_texture_stage(TextureStageCollection self, str name)
        
        /**
         * Returns the texture_stage in the collection with the indicated name, if
         * any, or NULL if no texture_stage has that name.
         */
        """
        pass

    def getNumTextureStages(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_texture_stages(TextureStageCollection self)
        
        /**
         * Returns the number of TextureStages in the collection.
         */
        """
        pass

    def getTextureStage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_texture_stage(TextureStageCollection self, int index)
        
        /**
         * Returns the nth TextureStage in the collection.
         */
        """
        pass

    def getTextureStages(self, *args, **kwargs): # real signature unknown
        pass

    def get_num_texture_stages(self, TextureStageCollection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_texture_stages(TextureStageCollection self)
        
        /**
         * Returns the number of TextureStages in the collection.
         */
        """
        pass

    def get_texture_stage(self, TextureStageCollection_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_texture_stage(TextureStageCollection self, int index)
        
        /**
         * Returns the nth TextureStage in the collection.
         */
        """
        pass

    def get_texture_stages(self, *args, **kwargs): # real signature unknown
        pass

    def hasTextureStage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_texture_stage(TextureStageCollection self, TextureStage texture_stage)
        
        /**
         * Returns true if the indicated TextureStage appears in this collection,
         * false otherwise.
         */
        """
        pass

    def has_texture_stage(self, TextureStageCollection_self, TextureStage_texture_stage): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_texture_stage(TextureStageCollection self, TextureStage texture_stage)
        
        /**
         * Returns true if the indicated TextureStage appears in this collection,
         * false otherwise.
         */
        """
        pass

    def output(self, TextureStageCollection_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(TextureStageCollection self, ostream out)
        
        /**
         * Writes a brief one-line description of the TextureStageCollection to the
         * indicated output stream.
         */
        """
        pass

    def removeDuplicateTextureStages(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_duplicate_texture_stages(const TextureStageCollection self)
        
        /**
         * Removes any duplicate entries of the same TextureStages on this collection.
         * If a TextureStage appears multiple times, the first appearance is retained;
         * subsequent appearances are removed.
         */
        """
        pass

    def removeTextureStage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_texture_stage(const TextureStageCollection self, TextureStage node_texture_stage)
        
        /**
         * Removes the indicated TextureStage from the collection.  Returns true if
         * the texture_stage was removed, false if it was not a member of the
         * collection.
         */
        """
        pass

    def removeTextureStagesFrom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_texture_stages_from(const TextureStageCollection self, const TextureStageCollection other)
        
        /**
         * Removes from this collection all of the TextureStages listed in the other
         * collection.
         */
        """
        pass

    def remove_duplicate_texture_stages(self, const_TextureStageCollection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_duplicate_texture_stages(const TextureStageCollection self)
        
        /**
         * Removes any duplicate entries of the same TextureStages on this collection.
         * If a TextureStage appears multiple times, the first appearance is retained;
         * subsequent appearances are removed.
         */
        """
        pass

    def remove_texture_stage(self, const_TextureStageCollection_self, TextureStage_node_texture_stage): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_texture_stage(const TextureStageCollection self, TextureStage node_texture_stage)
        
        /**
         * Removes the indicated TextureStage from the collection.  Returns true if
         * the texture_stage was removed, false if it was not a member of the
         * collection.
         */
        """
        pass

    def remove_texture_stages_from(self, const_TextureStageCollection_self, const_TextureStageCollection_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_texture_stages_from(const TextureStageCollection self, const TextureStageCollection other)
        
        /**
         * Removes from this collection all of the TextureStages listed in the other
         * collection.
         */
        """
        pass

    def sort(self, const_TextureStageCollection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        sort(const TextureStageCollection self)
        
        /**
         * Sorts the TextureStages in this collection into order by
         * TextureStage::sort(), from lowest to highest.
         */
        """
        pass

    def write(self, TextureStageCollection_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(TextureStageCollection self, ostream out, int indent_level)
        
        /**
         * Writes a complete multi-line description of the TextureStageCollection to
         * the indicated output stream.
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
        '__add__': None, # (!) real value is "<slot wrapper '__add__' of 'panda3d.core.TextureStageCollection' objects>"
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.TextureStageCollection' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.TextureStageCollection' objects>"
        '__doc__': '/**\n *\n */',
        '__getitem__': None, # (!) real value is "<slot wrapper '__getitem__' of 'panda3d.core.TextureStageCollection' objects>"
        '__iadd__': None, # (!) real value is "<slot wrapper '__iadd__' of 'panda3d.core.TextureStageCollection' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.TextureStageCollection' objects>"
        '__len__': None, # (!) real value is "<slot wrapper '__len__' of 'panda3d.core.TextureStageCollection' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2938A0>'
        '__radd__': None, # (!) real value is "<slot wrapper '__radd__' of 'panda3d.core.TextureStageCollection' objects>"
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.TextureStageCollection' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.TextureStageCollection' objects>"
        'addTextureStage': None, # (!) real value is "<method 'addTextureStage' of 'panda3d.core.TextureStageCollection' objects>"
        'addTextureStagesFrom': None, # (!) real value is "<method 'addTextureStagesFrom' of 'panda3d.core.TextureStageCollection' objects>"
        'add_texture_stage': None, # (!) real value is "<method 'add_texture_stage' of 'panda3d.core.TextureStageCollection' objects>"
        'add_texture_stages_from': None, # (!) real value is "<method 'add_texture_stages_from' of 'panda3d.core.TextureStageCollection' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.TextureStageCollection' objects>"
        'clear': None, # (!) real value is "<method 'clear' of 'panda3d.core.TextureStageCollection' objects>"
        'findTextureStage': None, # (!) real value is "<method 'findTextureStage' of 'panda3d.core.TextureStageCollection' objects>"
        'find_texture_stage': None, # (!) real value is "<method 'find_texture_stage' of 'panda3d.core.TextureStageCollection' objects>"
        'getNumTextureStages': None, # (!) real value is "<method 'getNumTextureStages' of 'panda3d.core.TextureStageCollection' objects>"
        'getTextureStage': None, # (!) real value is "<method 'getTextureStage' of 'panda3d.core.TextureStageCollection' objects>"
        'getTextureStages': None, # (!) real value is "<method 'getTextureStages' of 'panda3d.core.TextureStageCollection' objects>"
        'get_num_texture_stages': None, # (!) real value is "<method 'get_num_texture_stages' of 'panda3d.core.TextureStageCollection' objects>"
        'get_texture_stage': None, # (!) real value is "<method 'get_texture_stage' of 'panda3d.core.TextureStageCollection' objects>"
        'get_texture_stages': None, # (!) real value is "<method 'get_texture_stages' of 'panda3d.core.TextureStageCollection' objects>"
        'hasTextureStage': None, # (!) real value is "<method 'hasTextureStage' of 'panda3d.core.TextureStageCollection' objects>"
        'has_texture_stage': None, # (!) real value is "<method 'has_texture_stage' of 'panda3d.core.TextureStageCollection' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.TextureStageCollection' objects>"
        'removeDuplicateTextureStages': None, # (!) real value is "<method 'removeDuplicateTextureStages' of 'panda3d.core.TextureStageCollection' objects>"
        'removeTextureStage': None, # (!) real value is "<method 'removeTextureStage' of 'panda3d.core.TextureStageCollection' objects>"
        'removeTextureStagesFrom': None, # (!) real value is "<method 'removeTextureStagesFrom' of 'panda3d.core.TextureStageCollection' objects>"
        'remove_duplicate_texture_stages': None, # (!) real value is "<method 'remove_duplicate_texture_stages' of 'panda3d.core.TextureStageCollection' objects>"
        'remove_texture_stage': None, # (!) real value is "<method 'remove_texture_stage' of 'panda3d.core.TextureStageCollection' objects>"
        'remove_texture_stages_from': None, # (!) real value is "<method 'remove_texture_stages_from' of 'panda3d.core.TextureStageCollection' objects>"
        'sort': None, # (!) real value is "<method 'sort' of 'panda3d.core.TextureStageCollection' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.TextureStageCollection' objects>"
    }


