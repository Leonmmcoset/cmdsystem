# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class LFrustumf(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     *
     */
    """
    def makeOrtho(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_ortho(const LFrustumf self, float fnear, float ffar)
        make_ortho(const LFrustumf self, float fnear, float ffar, float l, float r, float t, float b)
        
        /**
         * Behaves like gluOrtho
         */
        
        /**
         * Behaves like gluOrtho
         */
        """
        pass

    def makeOrtho2D(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_ortho_2D(const LFrustumf self)
        make_ortho_2D(const LFrustumf self, float l, float r, float t, float b)
        
        /**
         * Sets up a two-dimensional orthographic frustum
         */
        
        /**
         * Sets up a two-dimensional orthographic frustum
         */
        """
        pass

    def makePerspective(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_perspective(const LFrustumf self, float xfov, float yfov, float fnear, float ffar)
        
        /**
         *
         */
        """
        pass

    def makePerspectiveHfov(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_perspective_hfov(const LFrustumf self, float xfov, float aspect, float fnear, float ffar)
        
        /**
         * Behaves like gluPerspective (Aspect = width/height, Yfov in degrees)
         */
        """
        pass

    def makePerspectiveVfov(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_perspective_vfov(const LFrustumf self, float yfov, float aspect, float fnear, float ffar)
        
        /**
         *
         */
        """
        pass

    def make_ortho(self, const_LFrustumf_self, float_fnear, float_ffar): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_ortho(const LFrustumf self, float fnear, float ffar)
        make_ortho(const LFrustumf self, float fnear, float ffar, float l, float r, float t, float b)
        
        /**
         * Behaves like gluOrtho
         */
        
        /**
         * Behaves like gluOrtho
         */
        """
        pass

    def make_ortho_2D(self, const_LFrustumf_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_ortho_2D(const LFrustumf self)
        make_ortho_2D(const LFrustumf self, float l, float r, float t, float b)
        
        /**
         * Sets up a two-dimensional orthographic frustum
         */
        
        /**
         * Sets up a two-dimensional orthographic frustum
         */
        """
        pass

    def make_perspective(self, const_LFrustumf_self, float_xfov, float_yfov, float_fnear, float_ffar): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_perspective(const LFrustumf self, float xfov, float yfov, float fnear, float ffar)
        
        /**
         *
         */
        """
        pass

    def make_perspective_hfov(self, const_LFrustumf_self, float_xfov, float_aspect, float_fnear, float_ffar): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_perspective_hfov(const LFrustumf self, float xfov, float aspect, float fnear, float ffar)
        
        /**
         * Behaves like gluPerspective (Aspect = width/height, Yfov in degrees)
         */
        """
        pass

    def make_perspective_vfov(self, const_LFrustumf_self, float_yfov, float_aspect, float_fnear, float_ffar): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_perspective_vfov(const LFrustumf self, float yfov, float aspect, float fnear, float ffar)
        
        /**
         *
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
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.LFrustumf' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.LFrustumf' objects>"
        '__doc__': '/**\n *\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.LFrustumf' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE3418B0>'
        'makeOrtho': None, # (!) real value is "<method 'makeOrtho' of 'panda3d.core.LFrustumf' objects>"
        'makeOrtho2D': None, # (!) real value is "<method 'makeOrtho2D' of 'panda3d.core.LFrustumf' objects>"
        'makePerspective': None, # (!) real value is "<method 'makePerspective' of 'panda3d.core.LFrustumf' objects>"
        'makePerspectiveHfov': None, # (!) real value is "<method 'makePerspectiveHfov' of 'panda3d.core.LFrustumf' objects>"
        'makePerspectiveVfov': None, # (!) real value is "<method 'makePerspectiveVfov' of 'panda3d.core.LFrustumf' objects>"
        'make_ortho': None, # (!) real value is "<method 'make_ortho' of 'panda3d.core.LFrustumf' objects>"
        'make_ortho_2D': None, # (!) real value is "<method 'make_ortho_2D' of 'panda3d.core.LFrustumf' objects>"
        'make_perspective': None, # (!) real value is "<method 'make_perspective' of 'panda3d.core.LFrustumf' objects>"
        'make_perspective_hfov': None, # (!) real value is "<method 'make_perspective_hfov' of 'panda3d.core.LFrustumf' objects>"
        'make_perspective_vfov': None, # (!) real value is "<method 'make_perspective_vfov' of 'panda3d.core.LFrustumf' objects>"
    }


