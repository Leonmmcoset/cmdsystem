# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .DisplayRegion import DisplayRegion

class StereoDisplayRegion(DisplayRegion):
    """
    /**
     * This is a special DisplayRegion wrapper that actually includes a pair of
     * DisplayRegions internally: the left and right eyes.  The DisplayRegion
     * represented here does not have a physical association with the window, but
     * it pretends it does.  Instead, it maintains a pointer to the left and right
     * DisplayRegions separately.
     *
     * Operations on the StereoDisplayRegion object affect both left and right
     * eyes together.  To access the left or right eyes independently, use
     * get_left_eye() and get_right_eye().
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getLeftEye(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_left_eye(const StereoDisplayRegion self)
        
        /**
         * Returns a pointer to the left DisplayRegion managed by this stereo object.
         */
        """
        pass

    def getRightEye(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_right_eye(const StereoDisplayRegion self)
        
        /**
         * Returns a pointer to the right DisplayRegion managed by this stereo object.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_left_eye(self, const_StereoDisplayRegion_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_left_eye(const StereoDisplayRegion self)
        
        /**
         * Returns a pointer to the left DisplayRegion managed by this stereo object.
         */
        """
        pass

    def get_right_eye(self, const_StereoDisplayRegion_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_right_eye(const StereoDisplayRegion self)
        
        /**
         * Returns a pointer to the right DisplayRegion managed by this stereo object.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    left_eye = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    right_eye = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * This is a special DisplayRegion wrapper that actually includes a pair of\n * DisplayRegions internally: the left and right eyes.  The DisplayRegion\n * represented here does not have a physical association with the window, but\n * it pretends it does.  Instead, it maintains a pointer to the left and right\n * DisplayRegions separately.\n *\n * Operations on the StereoDisplayRegion object affect both left and right\n * eyes together.  To access the left or right eyes independently, use\n * get_left_eye() and get_right_eye().\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.StereoDisplayRegion' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2DDE40>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2DDE40>)>'
        'getLeftEye': None, # (!) real value is "<method 'getLeftEye' of 'panda3d.core.StereoDisplayRegion' objects>"
        'getRightEye': None, # (!) real value is "<method 'getRightEye' of 'panda3d.core.StereoDisplayRegion' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2DDE40>)>'
        'get_left_eye': None, # (!) real value is "<method 'get_left_eye' of 'panda3d.core.StereoDisplayRegion' objects>"
        'get_right_eye': None, # (!) real value is "<method 'get_right_eye' of 'panda3d.core.StereoDisplayRegion' objects>"
        'left_eye': None, # (!) real value is "<attribute 'left_eye' of 'panda3d.core.StereoDisplayRegion' objects>"
        'right_eye': None, # (!) real value is "<attribute 'right_eye' of 'panda3d.core.StereoDisplayRegion' objects>"
    }


