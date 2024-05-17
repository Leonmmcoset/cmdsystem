# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class PNMImageHeader(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This is the base class of PNMImage, PNMReader, and PNMWriter.  It
     * encapsulates all the information associated with an image that describes
     * its size, number of channels, etc; that is, all the information about the
     * image except the image data itself.  It's the sort of information you
     * typically read from the image file's header.
     */
    """
    def assign(self, const_PNMImageHeader_self, const_PNMImageHeader_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const PNMImageHeader self, const PNMImageHeader copy)
        """
        pass

    def getColorSpace(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_color_space(PNMImageHeader self)
        
        /**
         * Returns the color space that the image is encoded in, or CS_unspecified if
         * unknown.
         */
        """
        pass

    def getColorType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_color_type(PNMImageHeader self)
        
        /**
         * Returns the image type of the image, as an enumerated value.  This is
         * really just the number of channels cast to the enumerated type.
         */
        """
        pass

    def getComment(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_comment(PNMImageHeader self)
        
        /**
         * Gets the user comment from the file.
         */
        """
        pass

    def getMaxval(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_maxval(PNMImageHeader self)
        
        /**
         * Returns the maximum channel value allowable for any pixel in this image;
         * for instance, 255 for a typical 8-bit-per-channel image.  A pixel with this
         * value is full on.
         */
        """
        pass

    def getNumChannels(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_channels(PNMImageHeader self)
        
        /**
         * Returns the number of channels in the image.
         */
        """
        pass

    def getSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_size(PNMImageHeader self)
        
        /**
         * Returns the number of pixels in each direction.  This is one more than the
         * largest allowable coordinates.
         */
        """
        pass

    def getType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_type(PNMImageHeader self)
        
        /**
         * If the file type is known (e.g.  has_type() returns true), returns its
         * PNMFileType pointer; otherwise, returns NULL.
         */
        """
        pass

    def getXSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_x_size(PNMImageHeader self)
        
        /**
         * Returns the number of pixels in the X direction.  This is one more than the
         * largest allowable X coordinate.
         */
        """
        pass

    def getYSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_y_size(PNMImageHeader self)
        
        /**
         * Returns the number of pixels in the Y direction.  This is one more than the
         * largest allowable Y coordinate.
         */
        """
        pass

    def get_color_space(self, PNMImageHeader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_color_space(PNMImageHeader self)
        
        /**
         * Returns the color space that the image is encoded in, or CS_unspecified if
         * unknown.
         */
        """
        pass

    def get_color_type(self, PNMImageHeader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_color_type(PNMImageHeader self)
        
        /**
         * Returns the image type of the image, as an enumerated value.  This is
         * really just the number of channels cast to the enumerated type.
         */
        """
        pass

    def get_comment(self, PNMImageHeader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_comment(PNMImageHeader self)
        
        /**
         * Gets the user comment from the file.
         */
        """
        pass

    def get_maxval(self, PNMImageHeader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_maxval(PNMImageHeader self)
        
        /**
         * Returns the maximum channel value allowable for any pixel in this image;
         * for instance, 255 for a typical 8-bit-per-channel image.  A pixel with this
         * value is full on.
         */
        """
        pass

    def get_num_channels(self, PNMImageHeader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_channels(PNMImageHeader self)
        
        /**
         * Returns the number of channels in the image.
         */
        """
        pass

    def get_size(self, PNMImageHeader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_size(PNMImageHeader self)
        
        /**
         * Returns the number of pixels in each direction.  This is one more than the
         * largest allowable coordinates.
         */
        """
        pass

    def get_type(self, PNMImageHeader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_type(PNMImageHeader self)
        
        /**
         * If the file type is known (e.g.  has_type() returns true), returns its
         * PNMFileType pointer; otherwise, returns NULL.
         */
        """
        pass

    def get_x_size(self, PNMImageHeader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_x_size(PNMImageHeader self)
        
        /**
         * Returns the number of pixels in the X direction.  This is one more than the
         * largest allowable X coordinate.
         */
        """
        pass

    def get_y_size(self, PNMImageHeader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_y_size(PNMImageHeader self)
        
        /**
         * Returns the number of pixels in the Y direction.  This is one more than the
         * largest allowable Y coordinate.
         */
        """
        pass

    def hasAlpha(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_alpha(PNMImageHeader self)
        has_alpha(int color_type)
        
        /**
         * This static variant of has_alpha() returns true if the indicated image type
         * includes an alpha channel, false otherwise.
         */
        
        /**
         * Returns true if the image includes an alpha channel, false otherwise.
         * Unlike is_grayscale(), if this returns false it is an error to call any of
         * the functions accessing the alpha channel.
         */
        """
        pass

    def hasType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_type(PNMImageHeader self)
        
        /**
         * Returns true if the PNMImageHeader knows what type it is, false otherwise.
         */
        """
        pass

    def has_alpha(self, PNMImageHeader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_alpha(PNMImageHeader self)
        has_alpha(int color_type)
        
        /**
         * This static variant of has_alpha() returns true if the indicated image type
         * includes an alpha channel, false otherwise.
         */
        
        /**
         * Returns true if the image includes an alpha channel, false otherwise.
         * Unlike is_grayscale(), if this returns false it is an error to call any of
         * the functions accessing the alpha channel.
         */
        """
        pass

    def has_type(self, PNMImageHeader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_type(PNMImageHeader self)
        
        /**
         * Returns true if the PNMImageHeader knows what type it is, false otherwise.
         */
        """
        pass

    def isGrayscale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_grayscale(PNMImageHeader self)
        is_grayscale(int color_type)
        
        /**
         * This static variant of is_grayscale() returns true if the indicated image
         * type represents a grayscale image, false otherwise.
         */
        
        /**
         * Returns false if the image is a full-color image, and has red, green, and
         * blue components; true if it is a grayscale image and has only a gray
         * component.  (The gray color is actually stored in the blue channel, and the
         * red and green channels are ignored.)
         */
        """
        pass

    def is_grayscale(self, PNMImageHeader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_grayscale(PNMImageHeader self)
        is_grayscale(int color_type)
        
        /**
         * This static variant of is_grayscale() returns true if the indicated image
         * type represents a grayscale image, false otherwise.
         */
        
        /**
         * Returns false if the image is a full-color image, and has red, green, and
         * blue components; true if it is a grayscale image and has only a gray
         * component.  (The gray color is actually stored in the blue channel, and the
         * red and green channels are ignored.)
         */
        """
        pass

    def output(self, PNMImageHeader_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(PNMImageHeader self, ostream out)
        
        /**
         *
         */
        """
        pass

    def readHeader(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        read_header(const PNMImageHeader self, istream data, str filename, PNMFileType type, bool report_unknown_type)
        
        /**
         * Opens up the image file and tries to read its header information to
         * determine its size, number of channels, etc.  If successful, updates the
         * header information and returns true; otherwise, returns false.
         */
        
        /**
         * Reads the image header information only from the indicated stream.
         *
         * The filename is advisory only, and may be used to suggest a type if it has
         * a known extension.
         *
         * If type is non-NULL, it is a suggestion for the type of file it is (and a
         * non-NULL type will override any magic number test or filename extension
         * lookup).
         *
         * Returns true if successful, false on error.
         */
        """
        pass

    def read_header(self, const_PNMImageHeader_self, istream_data, str_filename, PNMFileType_type, bool_report_unknown_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        read_header(const PNMImageHeader self, istream data, str filename, PNMFileType type, bool report_unknown_type)
        
        /**
         * Opens up the image file and tries to read its header information to
         * determine its size, number of channels, etc.  If successful, updates the
         * header information and returns true; otherwise, returns false.
         */
        
        /**
         * Reads the image header information only from the indicated stream.
         *
         * The filename is advisory only, and may be used to suggest a type if it has
         * a known extension.
         *
         * If type is non-NULL, it is a suggestion for the type of file it is (and a
         * non-NULL type will override any magic number test or filename extension
         * lookup).
         *
         * Returns true if successful, false on error.
         */
        """
        pass

    def setComment(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_comment(const PNMImageHeader self, str comment)
        
        /**
         * Writes a user comment string to the image (header).
         */
        """
        pass

    def setType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_type(const PNMImageHeader self, PNMFileType type)
        
        /**
         * Sets the file type of this PNMImage.  This will be the default type used
         * when an image is read, if the type cannot be determined by magic number or
         * inferred by extension, or the type used when the image is written, if the
         * type cannot be inferred from the filename extension.
         */
        """
        pass

    def set_comment(self, const_PNMImageHeader_self, str_comment): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_comment(const PNMImageHeader self, str comment)
        
        /**
         * Writes a user comment string to the image (header).
         */
        """
        pass

    def set_type(self, const_PNMImageHeader_self, PNMFileType_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_type(const PNMImageHeader self, PNMFileType type)
        
        /**
         * Sets the file type of this PNMImage.  This will be the default type used
         * when an image is read, if the type cannot be determined by magic number or
         * inferred by extension, or the type used when the image is written, if the
         * type cannot be inferred from the filename extension.
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

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    color_space = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    comment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    maxval = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    num_channels = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    CTColor = 3
    CTFourChannel = 4
    CTGrayscale = 1
    CTInvalid = 0
    CTTwoChannel = 2
    CT_color = 3
    CT_four_channel = 4
    CT_grayscale = 1
    CT_invalid = 0
    CT_two_channel = 2
    DtoolClassDict = {
        'CTColor': 3,
        'CTFourChannel': 4,
        'CTGrayscale': 1,
        'CTInvalid': 0,
        'CTTwoChannel': 2,
        'CT_color': 3,
        'CT_four_channel': 4,
        'CT_grayscale': 1,
        'CT_invalid': 0,
        'CT_two_channel': 2,
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'Histogram': None, # (!) real value is "<class 'panda3d.core.Histogram'>"
        'PixelSpec': None, # (!) real value is "<class 'panda3d.core.PixelSpec'>"
        'PixelSpecCount': None, # (!) real value is "<class 'panda3d.core.PixelSpecCount'>"
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.PNMImageHeader' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.PNMImageHeader' objects>"
        '__doc__': "/**\n * This is the base class of PNMImage, PNMReader, and PNMWriter.  It\n * encapsulates all the information associated with an image that describes\n * its size, number of channels, etc; that is, all the information about the\n * image except the image data itself.  It's the sort of information you\n * typically read from the image file's header.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.PNMImageHeader' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE355950>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.PNMImageHeader' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.PNMImageHeader' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.PNMImageHeader' objects>"
        'color_space': None, # (!) real value is "<attribute 'color_space' of 'panda3d.core.PNMImageHeader' objects>"
        'comment': None, # (!) real value is "<attribute 'comment' of 'panda3d.core.PNMImageHeader' objects>"
        'getColorSpace': None, # (!) real value is "<method 'getColorSpace' of 'panda3d.core.PNMImageHeader' objects>"
        'getColorType': None, # (!) real value is "<method 'getColorType' of 'panda3d.core.PNMImageHeader' objects>"
        'getComment': None, # (!) real value is "<method 'getComment' of 'panda3d.core.PNMImageHeader' objects>"
        'getMaxval': None, # (!) real value is "<method 'getMaxval' of 'panda3d.core.PNMImageHeader' objects>"
        'getNumChannels': None, # (!) real value is "<method 'getNumChannels' of 'panda3d.core.PNMImageHeader' objects>"
        'getSize': None, # (!) real value is "<method 'getSize' of 'panda3d.core.PNMImageHeader' objects>"
        'getType': None, # (!) real value is "<method 'getType' of 'panda3d.core.PNMImageHeader' objects>"
        'getXSize': None, # (!) real value is "<method 'getXSize' of 'panda3d.core.PNMImageHeader' objects>"
        'getYSize': None, # (!) real value is "<method 'getYSize' of 'panda3d.core.PNMImageHeader' objects>"
        'get_color_space': None, # (!) real value is "<method 'get_color_space' of 'panda3d.core.PNMImageHeader' objects>"
        'get_color_type': None, # (!) real value is "<method 'get_color_type' of 'panda3d.core.PNMImageHeader' objects>"
        'get_comment': None, # (!) real value is "<method 'get_comment' of 'panda3d.core.PNMImageHeader' objects>"
        'get_maxval': None, # (!) real value is "<method 'get_maxval' of 'panda3d.core.PNMImageHeader' objects>"
        'get_num_channels': None, # (!) real value is "<method 'get_num_channels' of 'panda3d.core.PNMImageHeader' objects>"
        'get_size': None, # (!) real value is "<method 'get_size' of 'panda3d.core.PNMImageHeader' objects>"
        'get_type': None, # (!) real value is "<method 'get_type' of 'panda3d.core.PNMImageHeader' objects>"
        'get_x_size': None, # (!) real value is "<method 'get_x_size' of 'panda3d.core.PNMImageHeader' objects>"
        'get_y_size': None, # (!) real value is "<method 'get_y_size' of 'panda3d.core.PNMImageHeader' objects>"
        'hasAlpha': None, # (!) real value is "<method 'hasAlpha' of 'panda3d.core.PNMImageHeader' objects>"
        'hasType': None, # (!) real value is "<method 'hasType' of 'panda3d.core.PNMImageHeader' objects>"
        'has_alpha': None, # (!) real value is "<method 'has_alpha' of 'panda3d.core.PNMImageHeader' objects>"
        'has_type': None, # (!) real value is "<method 'has_type' of 'panda3d.core.PNMImageHeader' objects>"
        'isGrayscale': None, # (!) real value is "<method 'isGrayscale' of 'panda3d.core.PNMImageHeader' objects>"
        'is_grayscale': None, # (!) real value is "<method 'is_grayscale' of 'panda3d.core.PNMImageHeader' objects>"
        'maxval': None, # (!) real value is "<attribute 'maxval' of 'panda3d.core.PNMImageHeader' objects>"
        'num_channels': None, # (!) real value is "<attribute 'num_channels' of 'panda3d.core.PNMImageHeader' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.PNMImageHeader' objects>"
        'readHeader': None, # (!) real value is "<method 'readHeader' of 'panda3d.core.PNMImageHeader' objects>"
        'read_header': None, # (!) real value is "<method 'read_header' of 'panda3d.core.PNMImageHeader' objects>"
        'setComment': None, # (!) real value is "<method 'setComment' of 'panda3d.core.PNMImageHeader' objects>"
        'setType': None, # (!) real value is "<method 'setType' of 'panda3d.core.PNMImageHeader' objects>"
        'set_comment': None, # (!) real value is "<method 'set_comment' of 'panda3d.core.PNMImageHeader' objects>"
        'set_type': None, # (!) real value is "<method 'set_type' of 'panda3d.core.PNMImageHeader' objects>"
        'size': None, # (!) real value is "<attribute 'size' of 'panda3d.core.PNMImageHeader' objects>"
        'type': None, # (!) real value is "<attribute 'type' of 'panda3d.core.PNMImageHeader' objects>"
    }
    Histogram = None # (!) real value is "<class 'panda3d.core.Histogram'>"
    PixelSpec = None # (!) real value is "<class 'panda3d.core.PixelSpec'>"
    PixelSpecCount = None # (!) real value is "<class 'panda3d.core.PixelSpecCount'>"


