# encoding: utf-8
# module panda3d.vision
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\vision.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


# Variables with simple values

Dtool_PyNativeInterface = 1

# functions

def Dtool_BorrowThisReference(*args, **kwargs): # real signature unknown
    """
    Used to borrow 'this' pointer (to, from)
    Assumes no ownership.
    """
    pass

# classes

class ARToolKit(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * ARToolKit is a software library for building Augmented Reality (AR)
     * applications.  These are applications that involve the overlay of virtual
     * imagery on the real world.  It was developed by Dr.  Hirokazu Kato.  Its
     * ongoing development is being supported by the Human Interface Technology
     * Laboratory (HIT Lab) at the University of Washington, HIT Lab NZ at the
     * University of Canterbury, New Zealand, and ARToolworks, Inc, Seattle.  It
     * is available under a GPL license.  It is also possible to negotiate other
     * licenses with the copyright holders.
     *
     * This class is a wrapper around the ARToolKit library.
     */
    """
    def analyze(self, const_ARToolKit_self, Texture_tex, bool_do_flip_texture): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        analyze(const ARToolKit self, Texture tex, bool do_flip_texture)
        
        /**
         * Analyzes the non-pad region of the specified texture.  This causes all
         * attached nodepaths to move.  The parameter do_flip_texture is true by
         * default, because Panda's representation of textures is upside down from
         * ARToolKit.  If you already have a texture that's upside-down, however, you
         * should set it to false.
         */
        """
        pass

    def attachPattern(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        attach_pattern(const ARToolKit self, const Filename pattern, NodePath path)
        
        /**
         * Associates the specified glyph with the specified NodePath.  Each time you
         * call analyze, ARToolKit will update the NodePath's transform.  If the node
         * is not visible, its scale will be set to zero.
         */
        """
        pass

    def attach_pattern(self, const_ARToolKit_self, const_Filename_pattern, NodePath_path): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        attach_pattern(const ARToolKit self, const Filename pattern, NodePath path)
        
        /**
         * Associates the specified glyph with the specified NodePath.  Each time you
         * call analyze, ARToolKit will update the NodePath's transform.  If the node
         * is not visible, its scale will be set to zero.
         */
        """
        pass

    def detachPatterns(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        detach_patterns(const ARToolKit self)
        
        /**
         * Dissociates all patterns from all NodePaths.
         */
        """
        pass

    def detach_patterns(self, const_ARToolKit_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        detach_patterns(const ARToolKit self)
        
        /**
         * Dissociates all patterns from all NodePaths.
         */
        """
        pass

    def make(self, NodePath_camera, const_Filename_paramfile, double_markersize): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make(NodePath camera, const Filename paramfile, double markersize)
        
        /**
         * Create a new ARToolKit instance.
         *
         * Camera must be the nodepath of a panda camera object.  The panda camera's
         * field of view is initialized to match the field of view of the physical
         * webcam.  Each time you call analyze, all marker nodepaths will be moved
         * into a position which is relative to this camera.  The marker_size
         * parameter indicates how large you printed the physical markers.  You should
         * use the same size units that you wish to use in the panda code.
         */
        """
        pass

    def setThreshold(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_threshold(const ARToolKit self, double n)
        
        /**
         * As part of its analysis, the ARToolKit occasionally converts images to
         * black and white by thresholding them.  The threshold is set to 0.5 by
         * default, but you can tweak it here.
         */
        """
        pass

    def set_threshold(self, const_ARToolKit_self, double_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_threshold(const ARToolKit self, double n)
        
        /**
         * As part of its analysis, the ARToolKit occasionally converts images to
         * black and white by thresholding them.  The threshold is set to 0.5 by
         * default, but you can tweak it here.
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
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.vision.ARToolKit' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.vision.ARToolKit' objects>"
        '__doc__': '/**\n * ARToolKit is a software library for building Augmented Reality (AR)\n * applications.  These are applications that involve the overlay of virtual\n * imagery on the real world.  It was developed by Dr.  Hirokazu Kato.  Its\n * ongoing development is being supported by the Human Interface Technology\n * Laboratory (HIT Lab) at the University of Washington, HIT Lab NZ at the\n * University of Canterbury, New Zealand, and ARToolworks, Inc, Seattle.  It\n * is available under a GPL license.  It is also possible to negotiate other\n * licenses with the copyright holders.\n *\n * This class is a wrapper around the ARToolKit library.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.vision.ARToolKit' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDE5661850>'
        'analyze': None, # (!) real value is "<method 'analyze' of 'panda3d.vision.ARToolKit' objects>"
        'attachPattern': None, # (!) real value is "<method 'attachPattern' of 'panda3d.vision.ARToolKit' objects>"
        'attach_pattern': None, # (!) real value is "<method 'attach_pattern' of 'panda3d.vision.ARToolKit' objects>"
        'detachPatterns': None, # (!) real value is "<method 'detachPatterns' of 'panda3d.vision.ARToolKit' objects>"
        'detach_patterns': None, # (!) real value is "<method 'detach_patterns' of 'panda3d.vision.ARToolKit' objects>"
        'make': None, # (!) real value is '<staticmethod(<built-in method make of type object at 0x00007FFDE5661850>)>'
        'setThreshold': None, # (!) real value is "<method 'setThreshold' of 'panda3d.vision.ARToolKit' objects>"
        'set_threshold': None, # (!) real value is "<method 'set_threshold' of 'panda3d.vision.ARToolKit' objects>"
    }


class WebcamVideo(__panda3d_core.MovieVideo):
    """
    /**
     * Allows you to open a webcam or other video capture device as a video
     * stream.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getFps(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_fps(WebcamVideo self)
        
        /**
         * Returns the camera's framerate.  This is a maximum theoretical: the actual
         * performance will depend on the speed of the hardware.
         */
        """
        pass

    def getNumOptions(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_options()
        
        /**
         * Returns the number of webcam options.  An "option" consists of a device
         * plus a set of configuration parameters.  For example, "Creative Webcam Live
         * at 640x480, 30 fps" is an option.
         */
        """
        pass

    def getOption(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_option(int n)
        
        /**
         * Returns the nth webcam option.
         */
        """
        pass

    def getOptions(self, *args, **kwargs): # real signature unknown
        pass

    def getPixelFormat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_pixel_format(WebcamVideo self)
        
        /**
         * Returns the camera's pixel format, as a FourCC code, if known.
         */
        """
        pass

    def getSizeX(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_size_x(WebcamVideo self)
        
        /**
         * Returns the camera's size_x.
         */
        """
        pass

    def getSizeY(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_size_y(WebcamVideo self)
        
        /**
         * Returns the camera's size_y.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_fps(self, WebcamVideo_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_fps(WebcamVideo self)
        
        /**
         * Returns the camera's framerate.  This is a maximum theoretical: the actual
         * performance will depend on the speed of the hardware.
         */
        """
        pass

    def get_num_options(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_options()
        
        /**
         * Returns the number of webcam options.  An "option" consists of a device
         * plus a set of configuration parameters.  For example, "Creative Webcam Live
         * at 640x480, 30 fps" is an option.
         */
        """
        pass

    def get_option(self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_option(int n)
        
        /**
         * Returns the nth webcam option.
         */
        """
        pass

    def get_options(self, *args, **kwargs): # real signature unknown
        pass

    def get_pixel_format(self, WebcamVideo_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_pixel_format(WebcamVideo self)
        
        /**
         * Returns the camera's pixel format, as a FourCC code, if known.
         */
        """
        pass

    def get_size_x(self, WebcamVideo_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_size_x(WebcamVideo self)
        
        /**
         * Returns the camera's size_x.
         */
        """
        pass

    def get_size_y(self, WebcamVideo_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_size_y(WebcamVideo self)
        
        /**
         * Returns the camera's size_y.
         */
        """
        pass

    def output(self, WebcamVideo_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(WebcamVideo self, ostream out)
        
        /**
         * Outputs the WebcamVideo.  This function simply writes the name, size and
         * FPS to the output stream.
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
        '__doc__': '/**\n * Allows you to open a webcam or other video capture device as a video\n * stream.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.vision.WebcamVideo' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDE5661A20>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.vision.WebcamVideo' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.vision.WebcamVideo' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFDE5661A20>)>'
        'getFps': None, # (!) real value is "<method 'getFps' of 'panda3d.vision.WebcamVideo' objects>"
        'getNumOptions': None, # (!) real value is '<staticmethod(<built-in method getNumOptions of type object at 0x00007FFDE5661A20>)>'
        'getOption': None, # (!) real value is '<staticmethod(<built-in method getOption of type object at 0x00007FFDE5661A20>)>'
        'getOptions': None, # (!) real value is '<staticmethod(<built-in method getOptions of type object at 0x00007FFDE5661A20>)>'
        'getPixelFormat': None, # (!) real value is "<method 'getPixelFormat' of 'panda3d.vision.WebcamVideo' objects>"
        'getSizeX': None, # (!) real value is "<method 'getSizeX' of 'panda3d.vision.WebcamVideo' objects>"
        'getSizeY': None, # (!) real value is "<method 'getSizeY' of 'panda3d.vision.WebcamVideo' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFDE5661A20>)>'
        'get_fps': None, # (!) real value is "<method 'get_fps' of 'panda3d.vision.WebcamVideo' objects>"
        'get_num_options': None, # (!) real value is '<staticmethod(<built-in method get_num_options of type object at 0x00007FFDE5661A20>)>'
        'get_option': None, # (!) real value is '<staticmethod(<built-in method get_option of type object at 0x00007FFDE5661A20>)>'
        'get_options': None, # (!) real value is '<staticmethod(<built-in method get_options of type object at 0x00007FFDE5661A20>)>'
        'get_pixel_format': None, # (!) real value is "<method 'get_pixel_format' of 'panda3d.vision.WebcamVideo' objects>"
        'get_size_x': None, # (!) real value is "<method 'get_size_x' of 'panda3d.vision.WebcamVideo' objects>"
        'get_size_y': None, # (!) real value is "<method 'get_size_y' of 'panda3d.vision.WebcamVideo' objects>"
        'options': None, # (!) real value is "<attribute 'options' of 'panda3d.vision.WebcamVideo'>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.vision.WebcamVideo' objects>"
    }
    options = None # (!) real value is '<WebcamVideo.options[0] of <NULL>>'


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001E4817F9D50>'

__spec__ = None # (!) real value is "ModuleSpec(name='panda3d.vision', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001E4817F9D50>, origin='C:\\\\Users\\\\leonm\\\\PycharmProjects\\\\LeonRandomPlus\\\\venv\\\\Lib\\\\site-packages\\\\panda3d\\\\vision.cp311-win_amd64.pyd')"

