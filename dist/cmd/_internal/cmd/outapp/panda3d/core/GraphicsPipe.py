# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TypedReferenceCount import TypedReferenceCount

class GraphicsPipe(TypedReferenceCount):
    """
    /**
     * An object to create GraphicsOutputs that share a particular 3-D API.
     * Normally, there will only be one GraphicsPipe in an application, although
     * it is possible to have multiple of these at once if there are multiple
     * different API's available in the same machine.
     *
     * Often, the GraphicsPipe corresponds to a physical output device, hence the
     * term "pipe", but this is not necessarily the case.
     *
     * The GraphicsPipe is used by the GraphicsEngine object to create and destroy
     * windows; it keeps ownership of the windows it creates.
     *
     * M. Asad added new/interim functionality where GraphicsPipe now contains a
     * device interface to directx/opengl which will be used to handle multiple
     * windows from same device.
     *
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getDisplayHeight(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_display_height(GraphicsPipe self)
        
        /**
         * Returns the height of the entire display, if it is known.  This may return
         * 0.  See the caveats for get_display_width().
         */
        """
        pass

    def getDisplayInformation(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_display_information(const GraphicsPipe self)
        
        /**
         * Gets the pipe's DisplayInformation.
         */
        """
        pass

    def getDisplayWidth(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_display_width(GraphicsPipe self)
        
        /**
         * Returns the width of the entire display, if it is known.  This may return
         * 0.  This is not a guarantee that windows (particularly fullscreen windows)
         * may not be created larger than this width, but it is intended to provide a
         * hint to the application.
         */
        """
        pass

    def getDisplayZoom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_display_zoom(GraphicsPipe self)
        
        /**
         * Returns the display zoom factor configured in the operating system.  If the
         * operating system automatically scales windows to match the DPI (such as when
         * dpi-aware is set to false), this will be 1.0.  Otherwise, this will be set to
         * a value approximating the density of the monitor divided by the standard
         * density of the operating system (usually 96), yielding a value like 1.5 or
         * 2.0.
         *
         * @since 1.10.8
         */
        """
        pass

    def getInterfaceName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_interface_name(GraphicsPipe self)
        """
        pass

    def getSupportedTypes(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_supported_types(GraphicsPipe self)
        
        /**
         * Returns the mask of bits that represents the kinds of GraphicsOutput
         * objects this pipe might be able to successfully create.  The return value
         * is the union of bits in GraphicsPipe::OutputTypes that represents the set
         * of GraphicsOutput types.
         *
         * A 1 bit in a particular position is not a guarantee of success, but a 0 bit
         * is a guarantee of failure.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_display_height(self, GraphicsPipe_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_display_height(GraphicsPipe self)
        
        /**
         * Returns the height of the entire display, if it is known.  This may return
         * 0.  See the caveats for get_display_width().
         */
        """
        pass

    def get_display_information(self, const_GraphicsPipe_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_display_information(const GraphicsPipe self)
        
        /**
         * Gets the pipe's DisplayInformation.
         */
        """
        pass

    def get_display_width(self, GraphicsPipe_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_display_width(GraphicsPipe self)
        
        /**
         * Returns the width of the entire display, if it is known.  This may return
         * 0.  This is not a guarantee that windows (particularly fullscreen windows)
         * may not be created larger than this width, but it is intended to provide a
         * hint to the application.
         */
        """
        pass

    def get_display_zoom(self, GraphicsPipe_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_display_zoom(GraphicsPipe self)
        
        /**
         * Returns the display zoom factor configured in the operating system.  If the
         * operating system automatically scales windows to match the DPI (such as when
         * dpi-aware is set to false), this will be 1.0.  Otherwise, this will be set to
         * a value approximating the density of the monitor divided by the standard
         * density of the operating system (usually 96), yielding a value like 1.5 or
         * 2.0.
         *
         * @since 1.10.8
         */
        """
        pass

    def get_interface_name(self, GraphicsPipe_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_interface_name(GraphicsPipe self)
        """
        pass

    def get_supported_types(self, GraphicsPipe_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_supported_types(GraphicsPipe self)
        
        /**
         * Returns the mask of bits that represents the kinds of GraphicsOutput
         * objects this pipe might be able to successfully create.  The return value
         * is the union of bits in GraphicsPipe::OutputTypes that represents the set
         * of GraphicsOutput types.
         *
         * A 1 bit in a particular position is not a guarantee of success, but a 0 bit
         * is a guarantee of failure.
         */
        """
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_valid(GraphicsPipe self)
        
        /**
         * Returns false if this pipe is known to be invalid, meaning that an attempt
         * to create a GraphicsWindow with the pipe will certainly fail.  Returns true
         * if the pipe is probably valid (is this case, an attempt to create a
         * GraphicsWindow should succeed, but might still fail).
         *
         * Use the GraphicsEngine class to create a GraphicsWindow on a particular
         * pipe.
         */
        """
        pass

    def is_valid(self, GraphicsPipe_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_valid(GraphicsPipe self)
        
        /**
         * Returns false if this pipe is known to be invalid, meaning that an attempt
         * to create a GraphicsWindow with the pipe will certainly fail.  Returns true
         * if the pipe is probably valid (is this case, an attempt to create a
         * GraphicsWindow should succeed, but might still fail).
         *
         * Use the GraphicsEngine class to create a GraphicsWindow on a particular
         * pipe.
         */
        """
        pass

    def lookupCpuData(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        lookup_cpu_data(const GraphicsPipe self)
        
        /**
         * Looks up the detailed CPU information and stores it in
         * _display_information, if supported by the OS. This may take a second or
         * two.
         */
        """
        pass

    def lookup_cpu_data(self, const_GraphicsPipe_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        lookup_cpu_data(const GraphicsPipe self)
        
        /**
         * Looks up the detailed CPU information and stores it in
         * _display_information, if supported by the OS. This may take a second or
         * two.
         */
        """
        pass

    def supportsType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        supports_type(GraphicsPipe self, int flags)
        
        /**
         * A convenience function to ask if a particular type or types of
         * GraphicsObjects are supported.  The parameter is a union of one or more
         * bits defined in GrpahicsPipe::OutputTypes.
         *
         * Returns true if all of the requested types are listed in the
         * supported_types mask, false if any one of them is not.  This is not a
         * guarantee that the indicated output type will successfully be created when
         * it is attempted.
         */
        """
        pass

    def supports_type(self, GraphicsPipe_self, int_flags): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        supports_type(GraphicsPipe self, int flags)
        
        /**
         * A convenience function to ask if a particular type or types of
         * GraphicsObjects are supported.  The parameter is a union of one or more
         * bits defined in GrpahicsPipe::OutputTypes.
         *
         * Returns true if all of the requested types are listed in the
         * supported_types mask, false if any one of them is not.  This is not a
         * guarantee that the indicated output type will successfully be created when
         * it is attempted.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    display_height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    display_information = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    display_width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    display_zoom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    interface_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    BFCanBindColor = 64
    BFCanBindEvery = 128
    BFCanBindLayered = 16384
    BFFbPropsOptional = 2048
    BFRefuseParasite = 1
    BFRefuseWindow = 4
    BFRequireCallbackWindow = 16
    BFRequireParasite = 2
    BFRequireWindow = 8
    BFResizeable = 256
    BFRttCumulative = 1024
    BFSizePower2 = 8192
    BFSizeSquare = 4096
    BFSizeTrackHost = 512
    BF_can_bind_color = 64
    BF_can_bind_every = 128
    BF_can_bind_layered = 16384
    BF_fb_props_optional = 2048
    BF_refuse_parasite = 1
    BF_refuse_window = 4
    BF_require_callback_window = 16
    BF_require_parasite = 2
    BF_require_window = 8
    BF_resizeable = 256
    BF_rtt_cumulative = 1024
    BF_size_power_2 = 8192
    BF_size_square = 4096
    BF_size_track_host = 512
    DtoolClassDict = {
        'BFCanBindColor': 64,
        'BFCanBindEvery': 128,
        'BFCanBindLayered': 16384,
        'BFFbPropsOptional': 2048,
        'BFRefuseParasite': 1,
        'BFRefuseWindow': 4,
        'BFRequireCallbackWindow': 16,
        'BFRequireParasite': 2,
        'BFRequireWindow': 8,
        'BFResizeable': 256,
        'BFRttCumulative': 1024,
        'BFSizePower2': 8192,
        'BFSizeSquare': 4096,
        'BFSizeTrackHost': 512,
        'BF_can_bind_color': 64,
        'BF_can_bind_every': 128,
        'BF_can_bind_layered': 16384,
        'BF_fb_props_optional': 2048,
        'BF_refuse_parasite': 1,
        'BF_refuse_window': 4,
        'BF_require_callback_window': 16,
        'BF_require_parasite': 2,
        'BF_require_window': 8,
        'BF_resizeable': 256,
        'BF_rtt_cumulative': 1024,
        'BF_size_power_2': 8192,
        'BF_size_square': 4096,
        'BF_size_track_host': 512,
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'OTBuffer': 4,
        'OTFullscreenWindow': 2,
        'OTTextureBuffer': 8,
        'OTWindow': 1,
        'OT_buffer': 4,
        'OT_fullscreen_window': 2,
        'OT_texture_buffer': 8,
        'OT_window': 1,
        '__doc__': '/**\n * An object to create GraphicsOutputs that share a particular 3-D API.\n * Normally, there will only be one GraphicsPipe in an application, although\n * it is possible to have multiple of these at once if there are multiple\n * different API\'s available in the same machine.\n *\n * Often, the GraphicsPipe corresponds to a physical output device, hence the\n * term "pipe", but this is not necessarily the case.\n *\n * The GraphicsPipe is used by the GraphicsEngine object to create and destroy\n * windows; it keeps ownership of the windows it creates.\n *\n * M. Asad added new/interim functionality where GraphicsPipe now contains a\n * device interface to directx/opengl which will be used to handle multiple\n * windows from same device.\n *\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.GraphicsPipe' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2DCA50>'
        'display_height': None, # (!) real value is "<attribute 'display_height' of 'panda3d.core.GraphicsPipe' objects>"
        'display_information': None, # (!) real value is "<attribute 'display_information' of 'panda3d.core.GraphicsPipe' objects>"
        'display_width': None, # (!) real value is "<attribute 'display_width' of 'panda3d.core.GraphicsPipe' objects>"
        'display_zoom': None, # (!) real value is "<attribute 'display_zoom' of 'panda3d.core.GraphicsPipe' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2DCA50>)>'
        'getDisplayHeight': None, # (!) real value is "<method 'getDisplayHeight' of 'panda3d.core.GraphicsPipe' objects>"
        'getDisplayInformation': None, # (!) real value is "<method 'getDisplayInformation' of 'panda3d.core.GraphicsPipe' objects>"
        'getDisplayWidth': None, # (!) real value is "<method 'getDisplayWidth' of 'panda3d.core.GraphicsPipe' objects>"
        'getDisplayZoom': None, # (!) real value is "<method 'getDisplayZoom' of 'panda3d.core.GraphicsPipe' objects>"
        'getInterfaceName': None, # (!) real value is "<method 'getInterfaceName' of 'panda3d.core.GraphicsPipe' objects>"
        'getSupportedTypes': None, # (!) real value is "<method 'getSupportedTypes' of 'panda3d.core.GraphicsPipe' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2DCA50>)>'
        'get_display_height': None, # (!) real value is "<method 'get_display_height' of 'panda3d.core.GraphicsPipe' objects>"
        'get_display_information': None, # (!) real value is "<method 'get_display_information' of 'panda3d.core.GraphicsPipe' objects>"
        'get_display_width': None, # (!) real value is "<method 'get_display_width' of 'panda3d.core.GraphicsPipe' objects>"
        'get_display_zoom': None, # (!) real value is "<method 'get_display_zoom' of 'panda3d.core.GraphicsPipe' objects>"
        'get_interface_name': None, # (!) real value is "<method 'get_interface_name' of 'panda3d.core.GraphicsPipe' objects>"
        'get_supported_types': None, # (!) real value is "<method 'get_supported_types' of 'panda3d.core.GraphicsPipe' objects>"
        'interface_name': None, # (!) real value is "<attribute 'interface_name' of 'panda3d.core.GraphicsPipe' objects>"
        'isValid': None, # (!) real value is "<method 'isValid' of 'panda3d.core.GraphicsPipe' objects>"
        'is_valid': None, # (!) real value is "<method 'is_valid' of 'panda3d.core.GraphicsPipe' objects>"
        'lookupCpuData': None, # (!) real value is "<method 'lookupCpuData' of 'panda3d.core.GraphicsPipe' objects>"
        'lookup_cpu_data': None, # (!) real value is "<method 'lookup_cpu_data' of 'panda3d.core.GraphicsPipe' objects>"
        'supportsType': None, # (!) real value is "<method 'supportsType' of 'panda3d.core.GraphicsPipe' objects>"
        'supports_type': None, # (!) real value is "<method 'supports_type' of 'panda3d.core.GraphicsPipe' objects>"
    }
    OTBuffer = 4
    OTFullscreenWindow = 2
    OTTextureBuffer = 8
    OTWindow = 1
    OT_buffer = 4
    OT_fullscreen_window = 2
    OT_texture_buffer = 8
    OT_window = 1


