# encoding: utf-8
# module panda3d.physics
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\physics.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


class BaseParticleRenderer(__panda3d_core.ReferenceCount):
    """
    /**
     * Pure virtual particle renderer base class
     */
    """
    def getAlphaMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_alpha_mode(BaseParticleRenderer self)
        
        /**
        
         */
        """
        pass

    def getIgnoreScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_ignore_scale(BaseParticleRenderer self)
        
        /**
         * Returns the "ignore scale" flag.  See set_ignore_scale().
         */
        """
        pass

    def getRenderNode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_render_node(BaseParticleRenderer self)
        
        /**
         * Query the geomnode pointer
         */
        """
        pass

    def getRenderNodePath(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_render_node_path(BaseParticleRenderer self)
        
        /**
         * Query the geomnode pointer
         */
        """
        pass

    def getUserAlpha(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_user_alpha(BaseParticleRenderer self)
        
        /**
         * gets alpha for "user" alpha mode
         */
        """
        pass

    def get_alpha_mode(self, BaseParticleRenderer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_alpha_mode(BaseParticleRenderer self)
        
        /**
        
         */
        """
        pass

    def get_ignore_scale(self, BaseParticleRenderer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_ignore_scale(BaseParticleRenderer self)
        
        /**
         * Returns the "ignore scale" flag.  See set_ignore_scale().
         */
        """
        pass

    def get_render_node(self, BaseParticleRenderer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_render_node(BaseParticleRenderer self)
        
        /**
         * Query the geomnode pointer
         */
        """
        pass

    def get_render_node_path(self, BaseParticleRenderer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_render_node_path(BaseParticleRenderer self)
        
        /**
         * Query the geomnode pointer
         */
        """
        pass

    def get_user_alpha(self, BaseParticleRenderer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_user_alpha(BaseParticleRenderer self)
        
        /**
         * gets alpha for "user" alpha mode
         */
        """
        pass

    def output(self, BaseParticleRenderer_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(BaseParticleRenderer self, ostream out)
        
        /**
         * Write a string representation of this instance to <out>.
         */
        """
        pass

    def setAlphaMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_alpha_mode(const BaseParticleRenderer self, int am)
        
        /**
        
         */
        """
        pass

    def setColorBlendMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_color_blend_mode(const BaseParticleRenderer self, int bm, int oa, int ob)
        
        /**
         * sets the ColorBlendAttrib on the _render_node
         */
        """
        pass

    def setIgnoreScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_ignore_scale(const BaseParticleRenderer self, bool ignore_scale)
        
        /**
         * Sets the "ignore scale" flag.  When this is true, particles will be drawn
         * as if they had no scale, regardless of whatever scale might be inherited
         * from above the render node in the scene graph.
         *
         * This flag is mainly useful to support legacy code that was written for a
         * very early version of Panda, whose sprite particle renderer had a bug that
         * incorrectly ignored the inherited scale.
         */
        """
        pass

    def setUserAlpha(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_user_alpha(const BaseParticleRenderer self, float ua)
        
        /**
         * sets alpha for "user" alpha mode
         */
        """
        pass

    def set_alpha_mode(self, const_BaseParticleRenderer_self, int_am): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_alpha_mode(const BaseParticleRenderer self, int am)
        
        /**
        
         */
        """
        pass

    def set_color_blend_mode(self, const_BaseParticleRenderer_self, int_bm, int_oa, int_ob): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_color_blend_mode(const BaseParticleRenderer self, int bm, int oa, int ob)
        
        /**
         * sets the ColorBlendAttrib on the _render_node
         */
        """
        pass

    def set_ignore_scale(self, const_BaseParticleRenderer_self, bool_ignore_scale): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_ignore_scale(const BaseParticleRenderer self, bool ignore_scale)
        
        /**
         * Sets the "ignore scale" flag.  When this is true, particles will be drawn
         * as if they had no scale, regardless of whatever scale might be inherited
         * from above the render node in the scene graph.
         *
         * This flag is mainly useful to support legacy code that was written for a
         * very early version of Panda, whose sprite particle renderer had a bug that
         * incorrectly ignored the inherited scale.
         */
        """
        pass

    def set_user_alpha(self, const_BaseParticleRenderer_self, float_ua): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_user_alpha(const BaseParticleRenderer self, float ua)
        
        /**
         * sets alpha for "user" alpha mode
         */
        """
        pass

    def write(self, BaseParticleRenderer_self, ostream_out, int_indent): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(BaseParticleRenderer self, ostream out, int indent)
        
        /**
         * Write a string representation of this instance to <out>.
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
        'PPBLENDCUBIC': 2,
        'PPBLENDLINEAR': 1,
        'PPNOBLEND': 0,
        'PP_BLEND_CUBIC': 2,
        'PP_BLEND_LINEAR': 1,
        'PP_NO_BLEND': 0,
        'PRALPHAIN': 2,
        'PRALPHAINOUT': 3,
        'PRALPHANONE': 0,
        'PRALPHAOUT': 1,
        'PRALPHAUSER': 4,
        'PRNOTINITIALIZEDYET': 5,
        'PR_ALPHA_IN': 2,
        'PR_ALPHA_IN_OUT': 3,
        'PR_ALPHA_NONE': 0,
        'PR_ALPHA_OUT': 1,
        'PR_ALPHA_USER': 4,
        'PR_NOT_INITIALIZED_YET': 5,
        '__doc__': '/**\n * Pure virtual particle renderer base class\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.physics.BaseParticleRenderer' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC9DF3620>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.physics.BaseParticleRenderer' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.physics.BaseParticleRenderer' objects>"
        'getAlphaMode': None, # (!) real value is "<method 'getAlphaMode' of 'panda3d.physics.BaseParticleRenderer' objects>"
        'getIgnoreScale': None, # (!) real value is "<method 'getIgnoreScale' of 'panda3d.physics.BaseParticleRenderer' objects>"
        'getRenderNode': None, # (!) real value is "<method 'getRenderNode' of 'panda3d.physics.BaseParticleRenderer' objects>"
        'getRenderNodePath': None, # (!) real value is "<method 'getRenderNodePath' of 'panda3d.physics.BaseParticleRenderer' objects>"
        'getUserAlpha': None, # (!) real value is "<method 'getUserAlpha' of 'panda3d.physics.BaseParticleRenderer' objects>"
        'get_alpha_mode': None, # (!) real value is "<method 'get_alpha_mode' of 'panda3d.physics.BaseParticleRenderer' objects>"
        'get_ignore_scale': None, # (!) real value is "<method 'get_ignore_scale' of 'panda3d.physics.BaseParticleRenderer' objects>"
        'get_render_node': None, # (!) real value is "<method 'get_render_node' of 'panda3d.physics.BaseParticleRenderer' objects>"
        'get_render_node_path': None, # (!) real value is "<method 'get_render_node_path' of 'panda3d.physics.BaseParticleRenderer' objects>"
        'get_user_alpha': None, # (!) real value is "<method 'get_user_alpha' of 'panda3d.physics.BaseParticleRenderer' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.physics.BaseParticleRenderer' objects>"
        'setAlphaMode': None, # (!) real value is "<method 'setAlphaMode' of 'panda3d.physics.BaseParticleRenderer' objects>"
        'setColorBlendMode': None, # (!) real value is "<method 'setColorBlendMode' of 'panda3d.physics.BaseParticleRenderer' objects>"
        'setIgnoreScale': None, # (!) real value is "<method 'setIgnoreScale' of 'panda3d.physics.BaseParticleRenderer' objects>"
        'setUserAlpha': None, # (!) real value is "<method 'setUserAlpha' of 'panda3d.physics.BaseParticleRenderer' objects>"
        'set_alpha_mode': None, # (!) real value is "<method 'set_alpha_mode' of 'panda3d.physics.BaseParticleRenderer' objects>"
        'set_color_blend_mode': None, # (!) real value is "<method 'set_color_blend_mode' of 'panda3d.physics.BaseParticleRenderer' objects>"
        'set_ignore_scale': None, # (!) real value is "<method 'set_ignore_scale' of 'panda3d.physics.BaseParticleRenderer' objects>"
        'set_user_alpha': None, # (!) real value is "<method 'set_user_alpha' of 'panda3d.physics.BaseParticleRenderer' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.physics.BaseParticleRenderer' objects>"
    }
    PPBLENDCUBIC = 2
    PPBLENDLINEAR = 1
    PPNOBLEND = 0
    PP_BLEND_CUBIC = 2
    PP_BLEND_LINEAR = 1
    PP_NO_BLEND = 0
    PRALPHAIN = 2
    PRALPHAINOUT = 3
    PRALPHANONE = 0
    PRALPHAOUT = 1
    PRALPHAUSER = 4
    PRNOTINITIALIZEDYET = 5
    PR_ALPHA_IN = 2
    PR_ALPHA_IN_OUT = 3
    PR_ALPHA_NONE = 0
    PR_ALPHA_OUT = 1
    PR_ALPHA_USER = 4
    PR_NOT_INITIALIZED_YET = 5


