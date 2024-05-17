# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .CopyOnWriteObject import CopyOnWriteObject

class AnimPreloadTable(CopyOnWriteObject):
    """
    /**
     * This table records data about a list of animations for a particular model,
     * such as number of frames and frame rate.  It's used for implementating
     * asynchronous binding.
     *
     * This table is normally built by an offline tool, such as egg-optchar.
     */
    """
    def addAnim(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_anim(const AnimPreloadTable self, str basename, float base_frame_rate, int num_frames)
        
        /**
         * Adds a new animation record to the table.  If there is already a record of
         * this name, no operation is performed (the original record is unchanged).
         * See find_anim().  This will invalidate existing index numbers.
         */
        """
        pass

    def addAnimsFrom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_anims_from(const AnimPreloadTable self, const AnimPreloadTable other)
        
        /**
         * Copies the animation records from the other table into this one.  If a
         * given record name exists in both tables, the record in this one supercedes.
         */
        """
        pass

    def add_anim(self, const_AnimPreloadTable_self, str_basename, float_base_frame_rate, int_num_frames): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_anim(const AnimPreloadTable self, str basename, float base_frame_rate, int num_frames)
        
        /**
         * Adds a new animation record to the table.  If there is already a record of
         * this name, no operation is performed (the original record is unchanged).
         * See find_anim().  This will invalidate existing index numbers.
         */
        """
        pass

    def add_anims_from(self, const_AnimPreloadTable_self, const_AnimPreloadTable_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_anims_from(const AnimPreloadTable self, const AnimPreloadTable other)
        
        /**
         * Copies the animation records from the other table into this one.  If a
         * given record name exists in both tables, the record in this one supercedes.
         */
        """
        pass

    def clearAnims(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_anims(const AnimPreloadTable self)
        
        /**
         * Removes all animation records from the table.
         */
        """
        pass

    def clear_anims(self, const_AnimPreloadTable_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_anims(const AnimPreloadTable self)
        
        /**
         * Removes all animation records from the table.
         */
        """
        pass

    def findAnim(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        find_anim(AnimPreloadTable self, str basename)
        
        /**
         * Returns the index number in the table of the animation record with the
         * indicated name, or -1 if the name is not present.  By convention, the
         * basename is the filename of the egg or bam file, without the directory part
         * and without the extension.  That is, it is
         * Filename::get_basename_wo_extension().
         */
        """
        pass

    def find_anim(self, AnimPreloadTable_self, str_basename): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        find_anim(AnimPreloadTable self, str basename)
        
        /**
         * Returns the index number in the table of the animation record with the
         * indicated name, or -1 if the name is not present.  By convention, the
         * basename is the filename of the egg or bam file, without the directory part
         * and without the extension.  That is, it is
         * Filename::get_basename_wo_extension().
         */
        """
        pass

    def getBaseFrameRate(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_base_frame_rate(AnimPreloadTable self, int n)
        
        /**
         * Returns the frame rate stored for the nth animation record.
         */
        """
        pass

    def getBasename(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_basename(AnimPreloadTable self, int n)
        
        /**
         * Returns the basename stored for the nth animation record.  See find_anim().
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getNumAnims(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_anims(AnimPreloadTable self)
        
        /**
         * Returns the number of animation records in the table.
         */
        """
        pass

    def getNumFrames(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_frames(AnimPreloadTable self, int n)
        
        /**
         * Returns the number of frames stored for the nth animation record.
         */
        """
        pass

    def get_basename(self, AnimPreloadTable_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_basename(AnimPreloadTable self, int n)
        
        /**
         * Returns the basename stored for the nth animation record.  See find_anim().
         */
        """
        pass

    def get_base_frame_rate(self, AnimPreloadTable_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_base_frame_rate(AnimPreloadTable self, int n)
        
        /**
         * Returns the frame rate stored for the nth animation record.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_num_anims(self, AnimPreloadTable_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_anims(AnimPreloadTable self)
        
        /**
         * Returns the number of animation records in the table.
         */
        """
        pass

    def get_num_frames(self, AnimPreloadTable_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_frames(AnimPreloadTable self, int n)
        
        /**
         * Returns the number of frames stored for the nth animation record.
         */
        """
        pass

    def output(self, AnimPreloadTable_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(AnimPreloadTable self, ostream out)
        
        /**
         *
         */
        """
        pass

    def removeAnim(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_anim(const AnimPreloadTable self, int n)
        
        /**
         * Removes the nth animation records from the table.  This renumbers indexes
         * for following animations.
         */
        """
        pass

    def remove_anim(self, const_AnimPreloadTable_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_anim(const AnimPreloadTable self, int n)
        
        /**
         * Removes the nth animation records from the table.  This renumbers indexes
         * for following animations.
         */
        """
        pass

    def write(self, AnimPreloadTable_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(AnimPreloadTable self, ostream out, int indent_level)
        
        /**
         *
         */
        """
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
        '__doc__': "/**\n * This table records data about a list of animations for a particular model,\n * such as number of frames and frame rate.  It's used for implementating\n * asynchronous binding.\n *\n * This table is normally built by an offline tool, such as egg-optchar.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.AnimPreloadTable' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2C4200>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.AnimPreloadTable' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.AnimPreloadTable' objects>"
        'addAnim': None, # (!) real value is "<method 'addAnim' of 'panda3d.core.AnimPreloadTable' objects>"
        'addAnimsFrom': None, # (!) real value is "<method 'addAnimsFrom' of 'panda3d.core.AnimPreloadTable' objects>"
        'add_anim': None, # (!) real value is "<method 'add_anim' of 'panda3d.core.AnimPreloadTable' objects>"
        'add_anims_from': None, # (!) real value is "<method 'add_anims_from' of 'panda3d.core.AnimPreloadTable' objects>"
        'clearAnims': None, # (!) real value is "<method 'clearAnims' of 'panda3d.core.AnimPreloadTable' objects>"
        'clear_anims': None, # (!) real value is "<method 'clear_anims' of 'panda3d.core.AnimPreloadTable' objects>"
        'findAnim': None, # (!) real value is "<method 'findAnim' of 'panda3d.core.AnimPreloadTable' objects>"
        'find_anim': None, # (!) real value is "<method 'find_anim' of 'panda3d.core.AnimPreloadTable' objects>"
        'getBaseFrameRate': None, # (!) real value is "<method 'getBaseFrameRate' of 'panda3d.core.AnimPreloadTable' objects>"
        'getBasename': None, # (!) real value is "<method 'getBasename' of 'panda3d.core.AnimPreloadTable' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2C4200>)>'
        'getNumAnims': None, # (!) real value is "<method 'getNumAnims' of 'panda3d.core.AnimPreloadTable' objects>"
        'getNumFrames': None, # (!) real value is "<method 'getNumFrames' of 'panda3d.core.AnimPreloadTable' objects>"
        'get_base_frame_rate': None, # (!) real value is "<method 'get_base_frame_rate' of 'panda3d.core.AnimPreloadTable' objects>"
        'get_basename': None, # (!) real value is "<method 'get_basename' of 'panda3d.core.AnimPreloadTable' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2C4200>)>'
        'get_num_anims': None, # (!) real value is "<method 'get_num_anims' of 'panda3d.core.AnimPreloadTable' objects>"
        'get_num_frames': None, # (!) real value is "<method 'get_num_frames' of 'panda3d.core.AnimPreloadTable' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.AnimPreloadTable' objects>"
        'removeAnim': None, # (!) real value is "<method 'removeAnim' of 'panda3d.core.AnimPreloadTable' objects>"
        'remove_anim': None, # (!) real value is "<method 'remove_anim' of 'panda3d.core.AnimPreloadTable' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.AnimPreloadTable' objects>"
    }


