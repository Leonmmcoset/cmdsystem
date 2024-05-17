# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .AnimGroup import AnimGroup

class AnimBundle(AnimGroup):
    """
    /**
     * This is the root of an AnimChannel hierarchy.  It knows the frame rate and
     * number of frames of all the channels in the hierarchy (which must all
     * match).
     */
    """
    def copyBundle(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        copy_bundle(AnimBundle self)
        
        /**
         * Returns a full copy of the bundle and its entire tree of nested AnimGroups.
         * However, the actual data stored in the leaves--that is, animation tables,
         * such as those stored in an AnimChannelMatrixXfmTable--will be shared.
         */
        """
        pass

    def copy_bundle(self, AnimBundle_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        copy_bundle(AnimBundle self)
        
        /**
         * Returns a full copy of the bundle and its entire tree of nested AnimGroups.
         * However, the actual data stored in the leaves--that is, animation tables,
         * such as those stored in an AnimChannelMatrixXfmTable--will be shared.
         */
        """
        pass

    def getBaseFrameRate(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_base_frame_rate(AnimBundle self)
        
        /**
         * Returns the ideal number of frames per second of the animation, when it is
         * running at normal speed.  This may not be the same as the actual playing
         * frame rate, as it might have been adjusted through set_play_rate() on the
         * AnimControl object.  See AnimControl::get_effective_frame_rate().
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getNumFrames(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_frames(AnimBundle self)
        
        /**
         * Returns the number of frames of animation, or 0 if the animation has no
         * fixed number of frames.
         */
        """
        pass

    def get_base_frame_rate(self, AnimBundle_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_base_frame_rate(AnimBundle self)
        
        /**
         * Returns the ideal number of frames per second of the animation, when it is
         * running at normal speed.  This may not be the same as the actual playing
         * frame rate, as it might have been adjusted through set_play_rate() on the
         * AnimControl object.  See AnimControl::get_effective_frame_rate().
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_num_frames(self, AnimBundle_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_frames(AnimBundle self)
        
        /**
         * Returns the number of frames of animation, or 0 if the animation has no
         * fixed number of frames.
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

    base_frame_rate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    num_frames = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.AnimBundle' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.AnimBundle' objects>"
        '__doc__': '/**\n * This is the root of an AnimChannel hierarchy.  It knows the frame rate and\n * number of frames of all the channels in the hierarchy (which must all\n * match).\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.AnimBundle' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2C2C40>'
        'base_frame_rate': None, # (!) real value is "<attribute 'base_frame_rate' of 'panda3d.core.AnimBundle' objects>"
        'copyBundle': None, # (!) real value is "<method 'copyBundle' of 'panda3d.core.AnimBundle' objects>"
        'copy_bundle': None, # (!) real value is "<method 'copy_bundle' of 'panda3d.core.AnimBundle' objects>"
        'getBaseFrameRate': None, # (!) real value is "<method 'getBaseFrameRate' of 'panda3d.core.AnimBundle' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2C2C40>)>'
        'getNumFrames': None, # (!) real value is "<method 'getNumFrames' of 'panda3d.core.AnimBundle' objects>"
        'get_base_frame_rate': None, # (!) real value is "<method 'get_base_frame_rate' of 'panda3d.core.AnimBundle' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2C2C40>)>'
        'get_num_frames': None, # (!) real value is "<method 'get_num_frames' of 'panda3d.core.AnimBundle' objects>"
        'num_frames': None, # (!) real value is "<attribute 'num_frames' of 'panda3d.core.AnimBundle' objects>"
    }


