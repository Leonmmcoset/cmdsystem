# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .RenderAttrib import RenderAttrib

class AuxBitplaneAttrib(RenderAttrib):
    """
    /**
     * Modern frame buffers can have 'aux' bitplanes, which are additional
     * bitplanes above and beyond the standard depth and color.  This attrib
     * controls what gets rendered into those additional bitplanes.  It can also
     * affect what goes into the alpha channel of the primary color buffer.
     *
     * ABO_glow: copy the glow map into the alpha channel of the primary frame
     * buffer.  If there is no glow map, set it to zero.  Caveat: it is not
     * possible to write glow or depth values to the framebuffer alpha channel at
     * the same time as using alpha blending or alpha testing.  Any attempt to use
     * transparency, blending, or alpha testing will cause this flag to be
     * overridden.
     *
     * ABO_aux_normal: put the camera-space normal into the into the R,G
     * components of the first auxiliary bitplane.
     *
     * ABO_aux_modelz: put the clip-space Z coordinate of the center of the model
     * (after perspective divide) into the B channel of the first auxiliary
     * bitplane.
     *
     * ABO_aux_glow: put a copy of the glow map into the alpha channel of the
     * first auxiliary bitplane.  If there is no glow map, set it to zero.
     *
     * AuxBitplaneAttrib is relevant only when shader generation is enabled.
     * Otherwise, it has no effect.
     *
     */
    """
    def getClassSlot(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_slot()
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getOutputs(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_outputs(AuxBitplaneAttrib self)
        
        /**
         * Returns the AuxBitplaneAttrib output bits.
         */
        """
        pass

    def get_class_slot(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_slot()
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_outputs(self, AuxBitplaneAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_outputs(AuxBitplaneAttrib self)
        
        /**
         * Returns the AuxBitplaneAttrib output bits.
         */
        """
        pass

    def make(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make()
        make(int outputs)
        
        /**
         * Constructs a default AuxBitplaneAttrib object.
         */
        
        /**
         * Constructs a specified AuxBitplaneAttrib object.
         */
        """
        pass

    def makeDefault(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_default()
        
        /**
         * Returns a RenderAttrib that corresponds to whatever the standard default
         * properties for render attributes of this type ought to be.
         */
        """
        pass

    def make_default(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_default()
        
        /**
         * Returns a RenderAttrib that corresponds to whatever the standard default
         * properties for render attributes of this type ought to be.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    outputs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    ABOAuxGlow = 4
    ABOAuxNormal = 2
    ABOGlow = 1
    ABO_aux_glow = 4
    ABO_aux_normal = 2
    ABO_glow = 1
    class_slot = 4
    DtoolClassDict = {
        'ABOAuxGlow': 4,
        'ABOAuxNormal': 2,
        'ABOGlow': 1,
        'ABO_aux_glow': 4,
        'ABO_aux_normal': 2,
        'ABO_glow': 1,
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': "/**\n * Modern frame buffers can have 'aux' bitplanes, which are additional\n * bitplanes above and beyond the standard depth and color.  This attrib\n * controls what gets rendered into those additional bitplanes.  It can also\n * affect what goes into the alpha channel of the primary color buffer.\n *\n * ABO_glow: copy the glow map into the alpha channel of the primary frame\n * buffer.  If there is no glow map, set it to zero.  Caveat: it is not\n * possible to write glow or depth values to the framebuffer alpha channel at\n * the same time as using alpha blending or alpha testing.  Any attempt to use\n * transparency, blending, or alpha testing will cause this flag to be\n * overridden.\n *\n * ABO_aux_normal: put the camera-space normal into the into the R,G\n * components of the first auxiliary bitplane.\n *\n * ABO_aux_modelz: put the clip-space Z coordinate of the center of the model\n * (after perspective divide) into the B channel of the first auxiliary\n * bitplane.\n *\n * ABO_aux_glow: put a copy of the glow map into the alpha channel of the\n * first auxiliary bitplane.  If there is no glow map, set it to zero.\n *\n * AuxBitplaneAttrib is relevant only when shader generation is enabled.\n * Otherwise, it has no effect.\n *\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.AuxBitplaneAttrib' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2941B0>'
        'class_slot': None, # (!) real value is "<attribute 'class_slot' of 'panda3d.core.AuxBitplaneAttrib'>"
        'getClassSlot': None, # (!) real value is '<staticmethod(<built-in method getClassSlot of type object at 0x00007FFCFE2941B0>)>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2941B0>)>'
        'getOutputs': None, # (!) real value is "<method 'getOutputs' of 'panda3d.core.AuxBitplaneAttrib' objects>"
        'get_class_slot': None, # (!) real value is '<staticmethod(<built-in method get_class_slot of type object at 0x00007FFCFE2941B0>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2941B0>)>'
        'get_outputs': None, # (!) real value is "<method 'get_outputs' of 'panda3d.core.AuxBitplaneAttrib' objects>"
        'make': None, # (!) real value is '<staticmethod(<built-in method make of type object at 0x00007FFCFE2941B0>)>'
        'makeDefault': None, # (!) real value is '<staticmethod(<built-in method makeDefault of type object at 0x00007FFCFE2941B0>)>'
        'make_default': None, # (!) real value is '<staticmethod(<built-in method make_default of type object at 0x00007FFCFE2941B0>)>'
        'outputs': None, # (!) real value is "<attribute 'outputs' of 'panda3d.core.AuxBitplaneAttrib' objects>"
    }


