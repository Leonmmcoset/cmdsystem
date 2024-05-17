# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .PNMImageHeader import PNMImageHeader

class PNMImage(PNMImageHeader):
    """
    /**
     * The name of this class derives from the fact that we originally implemented
     * it as a layer on top of the "pnm library", based on netpbm, which was built
     * to implement pbm, pgm, and pbm files, and is the underlying support of a
     * number of public-domain image file converters.  Nowadays we are no longer
     * derived directly from the pnm library, mainly to allow support of C++
     * iostreams instead of the C stdio FILE interface.
     *
     * Conceptually, a PNMImage is a two-dimensional array of xels, which are the
     * PNM-defined generic pixel type.  Each xel may have a red, green, and blue
     * component, or (if the image is grayscale) a gray component.  The image may
     * be read in, the individual xels manipulated, and written out again, or a
     * black image may be constructed from scratch.
     *
     * A PNMImage has a color space and a maxval, the combination of which defines
     * how a floating-point linear color value is encoded as an integer value in
     * memory.  The functions ending in _val operate on encoded colors, whereas
     * the regular ones work with linear floating-point values.  All operations
     * are color space correct unless otherwise specified.
     *
     * The image is of size XSize() by YSize() xels, numbered from top to bottom,
     * left to right, beginning at zero.
     *
     * Files can be specified by filename, or by an iostream pointer.  The
     * filename "-" refers to stdin or stdout.
     *
     * This class is not inherently thread-safe; use it from a single thread or
     * protect access using a mutex.
     */
    """
    def addAlpha(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_alpha(const PNMImage self)
        
        /**
         * Adds an alpha channel to the image, if it does not already have one.  The
         * alpha channel is initialized to zeros.
         */
        """
        pass

    def addSubImage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_sub_image(const PNMImage self, const PNMImage copy, int xto, int yto, int xfrom, int yfrom, int x_size, int y_size, float pixel_scale)
        
        /**
         * Behaves like copy_sub_image(), except the copy pixels are added to the
         * pixels of the destination, after scaling by the specified pixel_scale.
         * Unlike blend_sub_image(), the alpha channel is not treated specially.
         */
        """
        pass

    def add_alpha(self, const_PNMImage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_alpha(const PNMImage self)
        
        /**
         * Adds an alpha channel to the image, if it does not already have one.  The
         * alpha channel is initialized to zeros.
         */
        """
        pass

    def add_sub_image(self, const_PNMImage_self, const_PNMImage_copy, int_xto, int_yto, int_xfrom, int_yfrom, int_x_size, int_y_size, float_pixel_scale): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_sub_image(const PNMImage self, const PNMImage copy, int xto, int yto, int xfrom, int yfrom, int x_size, int y_size, float pixel_scale)
        
        /**
         * Behaves like copy_sub_image(), except the copy pixels are added to the
         * pixels of the destination, after scaling by the specified pixel_scale.
         * Unlike blend_sub_image(), the alpha channel is not treated specially.
         */
        """
        pass

    def alphaFill(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        alpha_fill(const PNMImage self, float alpha)
        
        /**
         * Sets the entire alpha channel to the given level.
         */
        """
        pass

    def alphaFillVal(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        alpha_fill_val(const PNMImage self, int alpha)
        
        /**
         * Sets the entire alpha channel to the given level.
         */
        """
        pass

    def alpha_fill(self, const_PNMImage_self, float_alpha): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        alpha_fill(const PNMImage self, float alpha)
        
        /**
         * Sets the entire alpha channel to the given level.
         */
        """
        pass

    def alpha_fill_val(self, const_PNMImage_self, int_alpha): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        alpha_fill_val(const PNMImage self, int alpha)
        
        /**
         * Sets the entire alpha channel to the given level.
         */
        """
        pass

    def applyExponent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        apply_exponent(const PNMImage self, float gray_exponent)
        apply_exponent(const PNMImage self, float gray_exponent, float alpha_exponent)
        apply_exponent(const PNMImage self, float red_exponent, float green_exponent, float blue_exponent)
        apply_exponent(const PNMImage self, float red_exponent, float green_exponent, float blue_exponent, float alpha_exponent)
        
        /**
         * Adjusts each channel of the image by raising the corresponding component
         * value to the indicated exponent, such that L' = L ^ exponent.
         */
        
        /**
         * Adjusts each channel of the image by raising the corresponding component
         * value to the indicated exponent, such that L' = L ^ exponent.
         */
        
        /**
         * Adjusts each channel of the image by raising the corresponding component
         * value to the indicated exponent, such that L' = L ^ exponent.  For a
         * grayscale image, the blue_exponent value is used for the grayscale value,
         * and red_exponent and green_exponent are unused.
         */
        
        /**
         * Adjusts each channel of the image by raising the corresponding component
         * value to the indicated exponent, such that L' = L ^ exponent.  For a
         * grayscale image, the blue_exponent value is used for the grayscale value,
         * and red_exponent and green_exponent are unused.
         */
        """
        pass

    def apply_exponent(self, const_PNMImage_self, float_gray_exponent): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        apply_exponent(const PNMImage self, float gray_exponent)
        apply_exponent(const PNMImage self, float gray_exponent, float alpha_exponent)
        apply_exponent(const PNMImage self, float red_exponent, float green_exponent, float blue_exponent)
        apply_exponent(const PNMImage self, float red_exponent, float green_exponent, float blue_exponent, float alpha_exponent)
        
        /**
         * Adjusts each channel of the image by raising the corresponding component
         * value to the indicated exponent, such that L' = L ^ exponent.
         */
        
        /**
         * Adjusts each channel of the image by raising the corresponding component
         * value to the indicated exponent, such that L' = L ^ exponent.
         */
        
        /**
         * Adjusts each channel of the image by raising the corresponding component
         * value to the indicated exponent, such that L' = L ^ exponent.  For a
         * grayscale image, the blue_exponent value is used for the grayscale value,
         * and red_exponent and green_exponent are unused.
         */
        
        /**
         * Adjusts each channel of the image by raising the corresponding component
         * value to the indicated exponent, such that L' = L ^ exponent.  For a
         * grayscale image, the blue_exponent value is used for the grayscale value,
         * and red_exponent and green_exponent are unused.
         */
        """
        pass

    def assign(self, const_PNMImage_self, const_PNMImage_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const PNMImage self, const PNMImage copy)
        """
        pass

    def blend(self, const_PNMImage_self, int_x, int_y, const_LVecBase3f_val, float_alpha): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        blend(const PNMImage self, int x, int y, const LVecBase3f val, float alpha)
        blend(const PNMImage self, int x, int y, float r, float g, float b, float alpha)
        
        /**
         * Smoothly blends the indicated pixel value in with whatever was already in
         * the image, based on the given alpha value.  An alpha of 1.0 is fully opaque
         * and completely replaces whatever was there previously; alpha of 0.0 is
         * fully transparent and does nothing.
         */
        
        /**
         * Smoothly blends the indicated pixel value in with whatever was already in
         * the image, based on the given alpha value.  An alpha of 1.0 is fully opaque
         * and completely replaces whatever was there previously; alpha of 0.0 is
         * fully transparent and does nothing.
         */
        """
        pass

    def blendSubImage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        blend_sub_image(const PNMImage self, const PNMImage copy, int xto, int yto, int xfrom, int yfrom, int x_size, int y_size, float pixel_scale)
        
        /**
         * Behaves like copy_sub_image(), except the alpha channel of the copy is used
         * to blend the copy into the destination image, instead of overwriting pixels
         * unconditionally.
         *
         * If pixel_scale is not 1.0, it specifies an amount to scale each *alpha*
         * value of the source image before applying it to the target image.
         *
         * If pixel_scale is 1.0 and the copy has no alpha channel, this degenerates
         * into copy_sub_image().
         */
        """
        pass

    def blend_sub_image(self, const_PNMImage_self, const_PNMImage_copy, int_xto, int_yto, int_xfrom, int_yfrom, int_x_size, int_y_size, float_pixel_scale): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        blend_sub_image(const PNMImage self, const PNMImage copy, int xto, int yto, int xfrom, int yfrom, int x_size, int y_size, float pixel_scale)
        
        /**
         * Behaves like copy_sub_image(), except the alpha channel of the copy is used
         * to blend the copy into the destination image, instead of overwriting pixels
         * unconditionally.
         *
         * If pixel_scale is not 1.0, it specifies an amount to scale each *alpha*
         * value of the source image before applying it to the target image.
         *
         * If pixel_scale is 1.0 and the copy has no alpha channel, this degenerates
         * into copy_sub_image().
         */
        """
        pass

    def boxFilter(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        box_filter(const PNMImage self, float radius)
        
        /**
         * This flavor of box_filter() will apply the filter over the entire image
         * without resizing or copying; the effect is that of a blur operation.
         */
        """
        pass

    def boxFilterFrom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        box_filter_from(const PNMImage self, float radius, const PNMImage copy)
        
        /**
         * Makes a resized copy of the indicated image into this one using the
         * indicated filter.  The image to be copied is squashed and stretched to
         * match the dimensions of the current image, applying the appropriate filter
         * to perform the stretching.
         */
        """
        pass

    def box_filter(self, const_PNMImage_self, float_radius): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        box_filter(const PNMImage self, float radius)
        
        /**
         * This flavor of box_filter() will apply the filter over the entire image
         * without resizing or copying; the effect is that of a blur operation.
         */
        """
        pass

    def box_filter_from(self, const_PNMImage_self, float_radius, const_PNMImage_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        box_filter_from(const PNMImage self, float radius, const PNMImage copy)
        
        /**
         * Makes a resized copy of the indicated image into this one using the
         * indicated filter.  The image to be copied is squashed and stretched to
         * match the dimensions of the current image, applying the appropriate filter
         * to perform the stretching.
         */
        """
        pass

    def clampVal(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clamp_val(PNMImage self, int input_value)
        
        /**
         * A handy function to clamp values to [0..get_maxval()].
         */
        """
        pass

    def clamp_val(self, PNMImage_self, int_input_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clamp_val(PNMImage self, int input_value)
        
        /**
         * A handy function to clamp values to [0..get_maxval()].
         */
        """
        pass

    def clear(self, const_PNMImage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear(const PNMImage self)
        clear(const PNMImage self, int x_size, int y_size, int num_channels, int maxval, PNMFileType type, int color_space)
        
        /**
         * Frees all memory allocated for the image, and clears all its parameters
         * (size, color, type, etc).
         */
        
        /**
         * This flavor of clear() reinitializes the image to an empty (black) image
         * with the given dimensions.
         */
        """
        pass

    def clearReadSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_read_size(const PNMImage self)
        
        /**
         * Undoes the effect of a previous call to set_read_size().
         */
        """
        pass

    def clear_read_size(self, const_PNMImage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_read_size(const PNMImage self)
        
        /**
         * Undoes the effect of a previous call to set_read_size().
         */
        """
        pass

    def copyChannel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        copy_channel(const PNMImage self, const PNMImage copy, int src_channel, int dest_channel)
        copy_channel(const PNMImage self, const PNMImage copy, int xto, int yto, int cto, int xfrom, int yfrom, int cfrom, int x_size, int y_size)
        
        /**
         * Copies a channel from one image into another.  Images must be the same size
         */
        
        /**
         * Copies just a single channel from the source image into a single channel of
         * this image, leaving the remaining channels alone.
         */
        """
        pass

    def copyChannelBits(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        copy_channel_bits(const PNMImage self, const PNMImage copy, int src_channel, int dest_channel, int src_mask, int right_shift)
        
        /**
         * Copies some subset of the bits of the specified channel from one image into
         * some subset of the bits of the specified channel in another image.  Images
         * must be the same size.
         *
         * If right_shift is negative, it means a left shift.
         */
        """
        pass

    def copyFrom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        copy_from(const PNMImage self, const PNMImage copy)
        
        /**
         * Makes this image become a copy of the other image.
         */
        """
        pass

    def copyHeaderFrom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        copy_header_from(const PNMImage self, const PNMImageHeader header)
        
        /**
         * Copies just the header information into this image.  This will blow away
         * any image data stored in the image.  The new image data will be allocated,
         * but left unitialized.
         */
        """
        pass

    def copySubImage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        copy_sub_image(const PNMImage self, const PNMImage copy, int xto, int yto, int xfrom, int yfrom, int x_size, int y_size)
        
        /**
         * Copies a rectangular area of another image into a rectangular area of this
         * image.  Both images must already have been initialized.  The upper-left
         * corner of the region in both images is specified, and the size of the area;
         * if the size is omitted, it defaults to the entire other image, or the
         * largest piece that will fit.
         */
        """
        pass

    def copy_channel(self, const_PNMImage_self, const_PNMImage_copy, int_src_channel, int_dest_channel): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        copy_channel(const PNMImage self, const PNMImage copy, int src_channel, int dest_channel)
        copy_channel(const PNMImage self, const PNMImage copy, int xto, int yto, int cto, int xfrom, int yfrom, int cfrom, int x_size, int y_size)
        
        /**
         * Copies a channel from one image into another.  Images must be the same size
         */
        
        /**
         * Copies just a single channel from the source image into a single channel of
         * this image, leaving the remaining channels alone.
         */
        """
        pass

    def copy_channel_bits(self, const_PNMImage_self, const_PNMImage_copy, int_src_channel, int_dest_channel, int_src_mask, int_right_shift): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        copy_channel_bits(const PNMImage self, const PNMImage copy, int src_channel, int dest_channel, int src_mask, int right_shift)
        
        /**
         * Copies some subset of the bits of the specified channel from one image into
         * some subset of the bits of the specified channel in another image.  Images
         * must be the same size.
         *
         * If right_shift is negative, it means a left shift.
         */
        """
        pass

    def copy_from(self, const_PNMImage_self, const_PNMImage_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        copy_from(const PNMImage self, const PNMImage copy)
        
        /**
         * Makes this image become a copy of the other image.
         */
        """
        pass

    def copy_header_from(self, const_PNMImage_self, const_PNMImageHeader_header): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        copy_header_from(const PNMImage self, const PNMImageHeader header)
        
        /**
         * Copies just the header information into this image.  This will blow away
         * any image data stored in the image.  The new image data will be allocated,
         * but left unitialized.
         */
        """
        pass

    def copy_sub_image(self, const_PNMImage_self, const_PNMImage_copy, int_xto, int_yto, int_xfrom, int_yfrom, int_x_size, int_y_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        copy_sub_image(const PNMImage self, const PNMImage copy, int xto, int yto, int xfrom, int yfrom, int x_size, int y_size)
        
        /**
         * Copies a rectangular area of another image into a rectangular area of this
         * image.  Both images must already have been initialized.  The upper-left
         * corner of the region in both images is specified, and the size of the area;
         * if the size is omitted, it defaults to the entire other image, or the
         * largest piece that will fit.
         */
        """
        pass

    def darkenSubImage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        darken_sub_image(const PNMImage self, const PNMImage copy, int xto, int yto, int xfrom, int yfrom, int x_size, int y_size, float pixel_scale)
        
        /**
         * Behaves like copy_sub_image(), but the resulting color will be the darker
         * of the source and destination colors at each pixel (and at each R, G, B, A
         * component value).
         *
         * If pixel_scale is not 1.0, it specifies an amount to scale each pixel value
         * of the source image before applying it to the target image.  The scale is
         * applied with the center at 1.0: scaling the pixel value smaller brings it
         * closer to 1.0.
         */
        """
        pass

    def darken_sub_image(self, const_PNMImage_self, const_PNMImage_copy, int_xto, int_yto, int_xfrom, int_yfrom, int_x_size, int_y_size, float_pixel_scale): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        darken_sub_image(const PNMImage self, const PNMImage copy, int xto, int yto, int xfrom, int yfrom, int x_size, int y_size, float pixel_scale)
        
        /**
         * Behaves like copy_sub_image(), but the resulting color will be the darker
         * of the source and destination colors at each pixel (and at each R, G, B, A
         * component value).
         *
         * If pixel_scale is not 1.0, it specifies an amount to scale each pixel value
         * of the source image before applying it to the target image.  The scale is
         * applied with the center at 1.0: scaling the pixel value smaller brings it
         * closer to 1.0.
         */
        """
        pass

    def doFillDistance(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        do_fill_distance(const PNMImage self, int xi, int yi, int d)
        
        /**
         * Recursively fills in the minimum distance measured from a certain set of
         * points into the gray channel.
         */
        """
        pass

    def do_fill_distance(self, const_PNMImage_self, int_xi, int_yi, int_d): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        do_fill_distance(const PNMImage self, int xi, int yi, int d)
        
        /**
         * Recursively fills in the minimum distance measured from a certain set of
         * points into the gray channel.
         */
        """
        pass

    def expandBorder(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        expand_border(const PNMImage self, int left, int right, int bottom, int top, const LVecBase4f color)
        
        /**
         * Expands the image by the indicated number of pixels on each edge.  The new
         * pixels are set to the indicated color.
         *
         * If any of the values is negative, this actually crops the image.
         */
        """
        pass

    def expand_border(self, const_PNMImage_self, int_left, int_right, int_bottom, int_top, const_LVecBase4f_color): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        expand_border(const PNMImage self, int left, int right, int bottom, int top, const LVecBase4f color)
        
        /**
         * Expands the image by the indicated number of pixels on each edge.  The new
         * pixels are set to the indicated color.
         *
         * If any of the values is negative, this actually crops the image.
         */
        """
        pass

    def fill(self, const_PNMImage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        fill(const PNMImage self)
        fill(const PNMImage self, float gray)
        fill(const PNMImage self, float red, float green, float blue)
        
        /**
         * Sets the entire image (except the alpha channel) to the given color.
         */
        
        /**
         * Sets the entire image (except the alpha channel) to the given grayscale
         * level.
         */
        """
        pass

    def fillDistanceInside(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        fill_distance_inside(const PNMImage self, const PNMImage mask, float threshold, int radius, bool shrink_from_border)
        
        /**
         * Replaces this image with a grayscale image whose gray channel represents
         * the linear Manhattan distance from the nearest dark pixel in the given mask
         * image, up to the specified radius value (which also becomes the new
         * maxval).  radius may range from 0 to maxmaxval; smaller values will compute
         * faster.  A dark pixel is defined as one whose pixel value is < threshold.
         *
         * If shrink_from_border is true, then the mask image is considered to be
         * surrounded by a border of dark pixels; otherwise, the border isn't
         * considered.
         *
         * This can be used, in conjunction with threshold, to shrink a mask image
         * inwards by a certain number of pixels.
         *
         * The mask image may be the same image as this one, in which case it is
         * destructively modified by this process.
         */
        """
        pass

    def fillDistanceOutside(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        fill_distance_outside(const PNMImage self, const PNMImage mask, float threshold, int radius)
        
        /**
         * Replaces this image with a grayscale image whose gray channel represents
         * the linear Manhattan distance from the nearest white pixel in the given
         * mask image, up to the specified radius value (which also becomes the new
         * maxval).  radius may range from 0 to maxmaxval; smaller values will compute
         * faster.  A white pixel is defined as one whose pixel value is >= threshold.
         *
         * This can be used, in conjunction with threshold, to grow a mask image
         * outwards by a certain number of pixels.
         *
         * The mask image may be the same image as this one, in which case it is
         * destructively modified by this process.
         */
        """
        pass

    def fillVal(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        fill_val(const PNMImage self)
        fill_val(const PNMImage self, int gray)
        fill_val(const PNMImage self, int red, int green, int blue)
        
        /**
         * Sets the entire image (except the alpha channel) to the given grayscale
         * level.
         */
        
        /**
         * Sets the entire image (except the alpha channel) to the given color.
         */
        """
        pass

    def fill_distance_inside(self, const_PNMImage_self, const_PNMImage_mask, float_threshold, int_radius, bool_shrink_from_border): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        fill_distance_inside(const PNMImage self, const PNMImage mask, float threshold, int radius, bool shrink_from_border)
        
        /**
         * Replaces this image with a grayscale image whose gray channel represents
         * the linear Manhattan distance from the nearest dark pixel in the given mask
         * image, up to the specified radius value (which also becomes the new
         * maxval).  radius may range from 0 to maxmaxval; smaller values will compute
         * faster.  A dark pixel is defined as one whose pixel value is < threshold.
         *
         * If shrink_from_border is true, then the mask image is considered to be
         * surrounded by a border of dark pixels; otherwise, the border isn't
         * considered.
         *
         * This can be used, in conjunction with threshold, to shrink a mask image
         * inwards by a certain number of pixels.
         *
         * The mask image may be the same image as this one, in which case it is
         * destructively modified by this process.
         */
        """
        pass

    def fill_distance_outside(self, const_PNMImage_self, const_PNMImage_mask, float_threshold, int_radius): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        fill_distance_outside(const PNMImage self, const PNMImage mask, float threshold, int radius)
        
        /**
         * Replaces this image with a grayscale image whose gray channel represents
         * the linear Manhattan distance from the nearest white pixel in the given
         * mask image, up to the specified radius value (which also becomes the new
         * maxval).  radius may range from 0 to maxmaxval; smaller values will compute
         * faster.  A white pixel is defined as one whose pixel value is >= threshold.
         *
         * This can be used, in conjunction with threshold, to grow a mask image
         * outwards by a certain number of pixels.
         *
         * The mask image may be the same image as this one, in which case it is
         * destructively modified by this process.
         */
        """
        pass

    def fill_val(self, const_PNMImage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        fill_val(const PNMImage self)
        fill_val(const PNMImage self, int gray)
        fill_val(const PNMImage self, int red, int green, int blue)
        
        /**
         * Sets the entire image (except the alpha channel) to the given grayscale
         * level.
         */
        
        /**
         * Sets the entire image (except the alpha channel) to the given color.
         */
        """
        pass

    def flip(self, const_PNMImage_self, bool_flip_x, bool_flip_y, bool_transpose): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        flip(const PNMImage self, bool flip_x, bool flip_y, bool transpose)
        
        /**
         * Reverses, transposes, and/or rotates the image in-place according to the
         * specified parameters.  If flip_x is true, the x axis is reversed; if flip_y
         * is true, the y axis is reversed.  Then, if transpose is true, the x and y
         * axes are exchanged.  These parameters can be used to select any combination
         * of 90-degree or 180-degree rotations and flips.
         */
        """
        pass

    def fromAlphaVal(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        from_alpha_val(PNMImage self, int input_value)
        
        /**
         * A handy function to scale alpha values from [0..get_maxval()] to [0..1].
         */
        """
        pass

    def fromVal(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        from_val(PNMImage self, const pixel input_value)
        from_val(PNMImage self, int input_value)
        
        /**
         * A handy function to scale non-alpha values from [0..get_maxval()] to
         * [0..1].  Do not use this for alpha values, see from_alpha_val.
         */
        
        /**
         * A handy function to scale non-alpha values from [0..get_maxval()] to
         * [0..1].  Do not use this for alpha values, see from_alpha_val.
         */
        """
        pass

    def from_alpha_val(self, PNMImage_self, int_input_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        from_alpha_val(PNMImage self, int input_value)
        
        /**
         * A handy function to scale alpha values from [0..get_maxval()] to [0..1].
         */
        """
        pass

    def from_val(self, PNMImage_self, const_pixel_input_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        from_val(PNMImage self, const pixel input_value)
        from_val(PNMImage self, int input_value)
        
        /**
         * A handy function to scale non-alpha values from [0..get_maxval()] to
         * [0..1].  Do not use this for alpha values, see from_alpha_val.
         */
        
        /**
         * A handy function to scale non-alpha values from [0..get_maxval()] to
         * [0..1].  Do not use this for alpha values, see from_alpha_val.
         */
        """
        pass

    def gammaCorrect(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        gamma_correct(const PNMImage self, float from_gamma, float to_gamma)
        
        /**
         * Assuming the image was constructed with a gamma curve of from_gamma in the
         * RGB channels, converts it to an image with a gamma curve of to_gamma in the
         * RGB channels.  Does not affect the alpha channel.
         */
        """
        pass

    def gammaCorrectAlpha(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        gamma_correct_alpha(const PNMImage self, float from_gamma, float to_gamma)
        
        /**
         * Assuming the image was constructed with a gamma curve of from_gamma in the
         * alpha channel, converts it to an image with a gamma curve of to_gamma in
         * the alpha channel.  Does not affect the RGB channels.
         */
        """
        pass

    def gamma_correct(self, const_PNMImage_self, float_from_gamma, float_to_gamma): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        gamma_correct(const PNMImage self, float from_gamma, float to_gamma)
        
        /**
         * Assuming the image was constructed with a gamma curve of from_gamma in the
         * RGB channels, converts it to an image with a gamma curve of to_gamma in the
         * RGB channels.  Does not affect the alpha channel.
         */
        """
        pass

    def gamma_correct_alpha(self, const_PNMImage_self, float_from_gamma, float_to_gamma): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        gamma_correct_alpha(const PNMImage self, float from_gamma, float to_gamma)
        
        /**
         * Assuming the image was constructed with a gamma curve of from_gamma in the
         * alpha channel, converts it to an image with a gamma curve of to_gamma in
         * the alpha channel.  Does not affect the RGB channels.
         */
        """
        pass

    def gaussianFilter(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        gaussian_filter(const PNMImage self, float radius)
        
        /**
         * This flavor of gaussian_filter() will apply the filter over the entire
         * image without resizing or copying; the effect is that of a blur operation.
         */
        """
        pass

    def gaussianFilterFrom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        gaussian_filter_from(const PNMImage self, float radius, const PNMImage copy)
        
        /**
         * Makes a resized copy of the indicated image into this one using the
         * indicated filter.  The image to be copied is squashed and stretched to
         * match the dimensions of the current image, applying the appropriate filter
         * to perform the stretching.
         */
        """
        pass

    def gaussian_filter(self, const_PNMImage_self, float_radius): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        gaussian_filter(const PNMImage self, float radius)
        
        /**
         * This flavor of gaussian_filter() will apply the filter over the entire
         * image without resizing or copying; the effect is that of a blur operation.
         */
        """
        pass

    def gaussian_filter_from(self, const_PNMImage_self, float_radius, const_PNMImage_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        gaussian_filter_from(const PNMImage self, float radius, const PNMImage copy)
        
        /**
         * Makes a resized copy of the indicated image into this one using the
         * indicated filter.  The image to be copied is squashed and stretched to
         * match the dimensions of the current image, applying the appropriate filter
         * to perform the stretching.
         */
        """
        pass

    def getAlpha(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_alpha(PNMImage self, int x, int y)
        
        /**
         * Returns the alpha component color at the indicated pixel.  It is an error
         * to call this unless has_alpha() is true.  The value returned is a float in
         * the range 0..1.
         */
        """
        pass

    def getAlphaVal(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_alpha_val(PNMImage self, int x, int y)
        
        /**
         * Returns the alpha component color at the indicated pixel.  It is an error
         * to call this unless has_alpha() is true.  The value returned is in the
         * range 0..maxval and always linear.
         */
        """
        pass

    def getAverageGray(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_average_gray(PNMImage self)
        
        /**
         * Returns the average grayscale component of all of the pixels in the image.
         */
        """
        pass

    def getAverageXel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_average_xel(PNMImage self)
        
        /**
         * Returns the average color of all of the pixels in the image.
         */
        """
        pass

    def getAverageXelA(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_average_xel_a(PNMImage self)
        
        /**
         * Returns the average color of all of the pixels in the image, including the
         * alpha channel.
         */
        """
        pass

    def getBlue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_blue(PNMImage self, int x, int y)
        
        /**
         * Returns the blue component color at the indicated pixel.  The value
         * returned is a linearized float in the range 0..1.
         */
        """
        pass

    def getBlueVal(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_blue_val(PNMImage self, int x, int y)
        
        /**
         * Returns the blue component color at the indicated pixel.  The value
         * returned is in the range 0..maxval and encoded in the configured color
         * space.
         */
        """
        pass

    def getBright(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_bright(PNMImage self, int x, int y)
        get_bright(PNMImage self, int x, int y, float rc, float gc, float bc)
        get_bright(PNMImage self, int x, int y, float rc, float gc, float bc, float ac)
        
        /**
         * Returns the linear brightness of the given xel, as a linearized float in
         * the range 0..1.  This flavor of get_bright() returns the correct grayscale
         * brightness level for both full-color and grayscale images.
         */
        
        /**
         * This flavor of get_bright() works correctly only for color images.  It
         * returns a single brightness value for the RGB color at the indicated pixel,
         * based on the supplied weights for each component.
         */
        
        /**
         * This flavor of get_bright() works correctly only for four-channel images.
         * It returns a single brightness value for the RGBA color at the indicated
         * pixel, based on the supplied weights for each component.
         */
        """
        pass

    def getChannel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_channel(PNMImage self, int x, int y, int channel)
        
        /**
         * Returns the nth component color at the indicated pixel.  The channel index
         * should be in the range 0..(get_num_channels()-1).  The channels are ordered
         * B, G, R, A.  This is slightly less optimal than accessing the component
         * values directly by named methods.  The value returned is a float in the
         * range 0..1.
         */
        """
        pass

    def getChannelVal(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_channel_val(PNMImage self, int x, int y, int channel)
        
        /**
         * Returns the nth component color at the indicated pixel.  The channel index
         * should be in the range 0..(get_num_channels()-1).  The channels are ordered
         * B, G, R, A.  This is slightly less optimal than accessing the component
         * values directly by named methods.  The value returned is in the range
         * 0..maxval.
         */
        """
        pass

    def getColorSpace(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_color_space(PNMImage self)
        
        /**
         * Returns the color space in which the image is encoded.
         */
        """
        pass

    def getGray(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_gray(PNMImage self, int x, int y)
        
        /**
         * Returns the gray component color at the indicated pixel.  This only has a
         * meaningful value for grayscale images; for other image types, this returns
         * the value of the blue channel only.  However, also see the get_bright()
         * function.  The value returned is a linearized float in the range 0..1.
         */
        """
        pass

    def getGrayVal(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_gray_val(PNMImage self, int x, int y)
        
        /**
         * Returns the gray component color at the indicated pixel.  This only has a
         * meaningful value for grayscale images; for other image types, this returns
         * the value of the blue channel only.  However, also see the get_bright()
         * function.  The value returned is in the range 0..maxval and encoded in the
         * configured color space.
         */
        """
        pass

    def getGreen(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_green(PNMImage self, int x, int y)
        
        /**
         * Returns the green component color at the indicated pixel.  The value
         * returned is a linearized float in the range 0..1.
         */
        """
        pass

    def getGreenVal(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_green_val(PNMImage self, int x, int y)
        
        /**
         * Returns the green component color at the indicated pixel.  The value
         * returned is in the range 0..maxval and encoded in the configured color
         * space.
         */
        """
        pass

    def getPixel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_pixel(PNMImage self, int x, int y)
        
        /**
         * Returns the (r, g, b, a) pixel value at the indicated pixel, using a
         * PixelSpec object.
         */
        """
        pass

    def getReadXSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_read_x_size(PNMImage self)
        
        /**
         * Returns the requested x_size of the image if set_read_size() has been
         * called, or the image x_size otherwise (if it is known).
         */
        """
        pass

    def getReadYSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_read_y_size(PNMImage self)
        
        /**
         * Returns the requested y_size of the image if set_read_size() has been
         * called, or the image y_size otherwise (if it is known).
         */
        """
        pass

    def getRed(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_red(PNMImage self, int x, int y)
        
        /**
         * Returns the red component color at the indicated pixel.  The value returned
         * is a linearized float in the range 0..1.
         */
        """
        pass

    def getRedVal(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_red_val(PNMImage self, int x, int y)
        
        /**
         * Returns the red component color at the indicated pixel.  The value returned
         * is in the range 0..maxval and encoded in the configured color space.
         */
        """
        pass

    def getXel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_xel(PNMImage self, int x, int y)
        
        /**
         * Returns the RGB color at the indicated pixel.  Each component is a
         * linearized float in the range 0..1.
         */
        """
        pass

    def getXelA(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_xel_a(PNMImage self, int x, int y)
        
        /**
         * Returns the RGBA color at the indicated pixel.  Each component is a
         * linearized float in the range 0..1.
         */
        """
        pass

    def getXelVal(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_xel_val(const PNMImage self, int x, int y)
        get_xel_val(PNMImage self, int x, int y)
        
        /**
         * Returns the RGB color at the indicated pixel.  Each component is in the
         * range 0..maxval.
         */
        
        /**
         * Returns the RGB color at the indicated pixel.  Each component is in the
         * range 0..maxval.
         */
        """
        pass

    def get_alpha(self, PNMImage_self, int_x, int_y): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_alpha(PNMImage self, int x, int y)
        
        /**
         * Returns the alpha component color at the indicated pixel.  It is an error
         * to call this unless has_alpha() is true.  The value returned is a float in
         * the range 0..1.
         */
        """
        pass

    def get_alpha_val(self, PNMImage_self, int_x, int_y): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_alpha_val(PNMImage self, int x, int y)
        
        /**
         * Returns the alpha component color at the indicated pixel.  It is an error
         * to call this unless has_alpha() is true.  The value returned is in the
         * range 0..maxval and always linear.
         */
        """
        pass

    def get_average_gray(self, PNMImage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_average_gray(PNMImage self)
        
        /**
         * Returns the average grayscale component of all of the pixels in the image.
         */
        """
        pass

    def get_average_xel(self, PNMImage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_average_xel(PNMImage self)
        
        /**
         * Returns the average color of all of the pixels in the image.
         */
        """
        pass

    def get_average_xel_a(self, PNMImage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_average_xel_a(PNMImage self)
        
        /**
         * Returns the average color of all of the pixels in the image, including the
         * alpha channel.
         */
        """
        pass

    def get_blue(self, PNMImage_self, int_x, int_y): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_blue(PNMImage self, int x, int y)
        
        /**
         * Returns the blue component color at the indicated pixel.  The value
         * returned is a linearized float in the range 0..1.
         */
        """
        pass

    def get_blue_val(self, PNMImage_self, int_x, int_y): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_blue_val(PNMImage self, int x, int y)
        
        /**
         * Returns the blue component color at the indicated pixel.  The value
         * returned is in the range 0..maxval and encoded in the configured color
         * space.
         */
        """
        pass

    def get_bright(self, PNMImage_self, int_x, int_y): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_bright(PNMImage self, int x, int y)
        get_bright(PNMImage self, int x, int y, float rc, float gc, float bc)
        get_bright(PNMImage self, int x, int y, float rc, float gc, float bc, float ac)
        
        /**
         * Returns the linear brightness of the given xel, as a linearized float in
         * the range 0..1.  This flavor of get_bright() returns the correct grayscale
         * brightness level for both full-color and grayscale images.
         */
        
        /**
         * This flavor of get_bright() works correctly only for color images.  It
         * returns a single brightness value for the RGB color at the indicated pixel,
         * based on the supplied weights for each component.
         */
        
        /**
         * This flavor of get_bright() works correctly only for four-channel images.
         * It returns a single brightness value for the RGBA color at the indicated
         * pixel, based on the supplied weights for each component.
         */
        """
        pass

    def get_channel(self, PNMImage_self, int_x, int_y, int_channel): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_channel(PNMImage self, int x, int y, int channel)
        
        /**
         * Returns the nth component color at the indicated pixel.  The channel index
         * should be in the range 0..(get_num_channels()-1).  The channels are ordered
         * B, G, R, A.  This is slightly less optimal than accessing the component
         * values directly by named methods.  The value returned is a float in the
         * range 0..1.
         */
        """
        pass

    def get_channel_val(self, PNMImage_self, int_x, int_y, int_channel): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_channel_val(PNMImage self, int x, int y, int channel)
        
        /**
         * Returns the nth component color at the indicated pixel.  The channel index
         * should be in the range 0..(get_num_channels()-1).  The channels are ordered
         * B, G, R, A.  This is slightly less optimal than accessing the component
         * values directly by named methods.  The value returned is in the range
         * 0..maxval.
         */
        """
        pass

    def get_color_space(self, PNMImage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_color_space(PNMImage self)
        
        /**
         * Returns the color space in which the image is encoded.
         */
        """
        pass

    def get_gray(self, PNMImage_self, int_x, int_y): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_gray(PNMImage self, int x, int y)
        
        /**
         * Returns the gray component color at the indicated pixel.  This only has a
         * meaningful value for grayscale images; for other image types, this returns
         * the value of the blue channel only.  However, also see the get_bright()
         * function.  The value returned is a linearized float in the range 0..1.
         */
        """
        pass

    def get_gray_val(self, PNMImage_self, int_x, int_y): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_gray_val(PNMImage self, int x, int y)
        
        /**
         * Returns the gray component color at the indicated pixel.  This only has a
         * meaningful value for grayscale images; for other image types, this returns
         * the value of the blue channel only.  However, also see the get_bright()
         * function.  The value returned is in the range 0..maxval and encoded in the
         * configured color space.
         */
        """
        pass

    def get_green(self, PNMImage_self, int_x, int_y): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_green(PNMImage self, int x, int y)
        
        /**
         * Returns the green component color at the indicated pixel.  The value
         * returned is a linearized float in the range 0..1.
         */
        """
        pass

    def get_green_val(self, PNMImage_self, int_x, int_y): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_green_val(PNMImage self, int x, int y)
        
        /**
         * Returns the green component color at the indicated pixel.  The value
         * returned is in the range 0..maxval and encoded in the configured color
         * space.
         */
        """
        pass

    def get_pixel(self, PNMImage_self, int_x, int_y): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_pixel(PNMImage self, int x, int y)
        
        /**
         * Returns the (r, g, b, a) pixel value at the indicated pixel, using a
         * PixelSpec object.
         */
        """
        pass

    def get_read_x_size(self, PNMImage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_read_x_size(PNMImage self)
        
        /**
         * Returns the requested x_size of the image if set_read_size() has been
         * called, or the image x_size otherwise (if it is known).
         */
        """
        pass

    def get_read_y_size(self, PNMImage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_read_y_size(PNMImage self)
        
        /**
         * Returns the requested y_size of the image if set_read_size() has been
         * called, or the image y_size otherwise (if it is known).
         */
        """
        pass

    def get_red(self, PNMImage_self, int_x, int_y): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_red(PNMImage self, int x, int y)
        
        /**
         * Returns the red component color at the indicated pixel.  The value returned
         * is a linearized float in the range 0..1.
         */
        """
        pass

    def get_red_val(self, PNMImage_self, int_x, int_y): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_red_val(PNMImage self, int x, int y)
        
        /**
         * Returns the red component color at the indicated pixel.  The value returned
         * is in the range 0..maxval and encoded in the configured color space.
         */
        """
        pass

    def get_xel(self, PNMImage_self, int_x, int_y): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_xel(PNMImage self, int x, int y)
        
        /**
         * Returns the RGB color at the indicated pixel.  Each component is a
         * linearized float in the range 0..1.
         */
        """
        pass

    def get_xel_a(self, PNMImage_self, int_x, int_y): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_xel_a(PNMImage self, int x, int y)
        
        /**
         * Returns the RGBA color at the indicated pixel.  Each component is a
         * linearized float in the range 0..1.
         */
        """
        pass

    def get_xel_val(self, const_PNMImage_self, int_x, int_y): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_xel_val(const PNMImage self, int x, int y)
        get_xel_val(PNMImage self, int x, int y)
        
        /**
         * Returns the RGB color at the indicated pixel.  Each component is in the
         * range 0..maxval.
         */
        
        /**
         * Returns the RGB color at the indicated pixel.  Each component is in the
         * range 0..maxval.
         */
        """
        pass

    def hasReadSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_read_size(PNMImage self)
        
        /**
         * Returns true if set_read_size() has been called.
         */
        """
        pass

    def has_read_size(self, PNMImage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_read_size(PNMImage self)
        
        /**
         * Returns true if set_read_size() has been called.
         */
        """
        pass

    def indirect1dLookup(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        indirect_1d_lookup(const PNMImage self, const PNMImage index_image, int channel, const PNMImage pixel_values)
        
        /**
         * index_image is a WxH grayscale image, while pixel_values is an Nx1 color
         * (or grayscale) image.  Typically pixel_values will be a 256x1 image.
         *
         * Fills the PNMImage with a new image the same width and height as
         * index_image, with the same number of channels as pixel_values.
         *
         * Each pixel of the new image is computed with the formula:
         *
         * new_image(x, y) = pixel_values(index_image(x, y)[channel], 0)
         *
         * At present, no interpolation is performed; the nearest value in
         * pixel_values is discovered.  This may change in the future.
         */
        """
        pass

    def indirect_1d_lookup(self, const_PNMImage_self, const_PNMImage_index_image, int_channel, const_PNMImage_pixel_values): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        indirect_1d_lookup(const PNMImage self, const PNMImage index_image, int channel, const PNMImage pixel_values)
        
        /**
         * index_image is a WxH grayscale image, while pixel_values is an Nx1 color
         * (or grayscale) image.  Typically pixel_values will be a 256x1 image.
         *
         * Fills the PNMImage with a new image the same width and height as
         * index_image, with the same number of channels as pixel_values.
         *
         * Each pixel of the new image is computed with the formula:
         *
         * new_image(x, y) = pixel_values(index_image(x, y)[channel], 0)
         *
         * At present, no interpolation is performed; the nearest value in
         * pixel_values is discovered.  This may change in the future.
         */
        """
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_valid(PNMImage self)
        
        /**
         * Returns true if the image has been read in or correctly initialized with a
         * height and width.  If this returns false, virtually all member functions
         * except clear() and read() are invalid function calls.
         */
        """
        pass

    def is_valid(self, PNMImage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_valid(PNMImage self)
        
        /**
         * Returns true if the image has been read in or correctly initialized with a
         * height and width.  If this returns false, virtually all member functions
         * except clear() and read() are invalid function calls.
         */
        """
        pass

    def lightenSubImage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        lighten_sub_image(const PNMImage self, const PNMImage copy, int xto, int yto, int xfrom, int yfrom, int x_size, int y_size, float pixel_scale)
        
        /**
         * Behaves like copy_sub_image(), but the resulting color will be the lighter
         * of the source and destination colors at each pixel (and at each R, G, B, A
         * component value).
         *
         * If pixel_scale is not 1.0, it specifies an amount to scale each pixel value
         * of the source image before applying it to the target image.
         */
        """
        pass

    def lighten_sub_image(self, const_PNMImage_self, const_PNMImage_copy, int_xto, int_yto, int_xfrom, int_yfrom, int_x_size, int_y_size, float_pixel_scale): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        lighten_sub_image(const PNMImage self, const PNMImage copy, int xto, int yto, int xfrom, int yfrom, int x_size, int y_size, float pixel_scale)
        
        /**
         * Behaves like copy_sub_image(), but the resulting color will be the lighter
         * of the source and destination colors at each pixel (and at each R, G, B, A
         * component value).
         *
         * If pixel_scale is not 1.0, it specifies an amount to scale each pixel value
         * of the source image before applying it to the target image.
         */
        """
        pass

    def makeGrayscale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_grayscale(const PNMImage self)
        make_grayscale(const PNMImage self, float rc, float gc, float bc)
        
        /**
         * Converts the image from RGB to grayscale.  Any alpha channel, if present,
         * is left undisturbed.
         */
        
        /**
         * Converts the image from RGB to grayscale.  Any alpha channel, if present,
         * is left undisturbed.  The optional rc, gc, bc values represent the relative
         * weights to apply to each channel to convert it to grayscale.
         */
        """
        pass

    def makeHistogram(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_histogram(const PNMImage self, Histogram hist)
        
        /**
         * Computes a histogram of the colors used in the image.
         */
        """
        pass

    def makeRgb(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_rgb(const PNMImage self)
        
        /**
         * Converts the image from grayscale to RGB.  Any alpha channel, if present,
         * is left undisturbed.
         */
        """
        pass

    def make_grayscale(self, const_PNMImage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_grayscale(const PNMImage self)
        make_grayscale(const PNMImage self, float rc, float gc, float bc)
        
        /**
         * Converts the image from RGB to grayscale.  Any alpha channel, if present,
         * is left undisturbed.
         */
        
        /**
         * Converts the image from RGB to grayscale.  Any alpha channel, if present,
         * is left undisturbed.  The optional rc, gc, bc values represent the relative
         * weights to apply to each channel to convert it to grayscale.
         */
        """
        pass

    def make_histogram(self, const_PNMImage_self, Histogram_hist): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_histogram(const PNMImage self, Histogram hist)
        
        /**
         * Computes a histogram of the colors used in the image.
         */
        """
        pass

    def make_rgb(self, const_PNMImage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_rgb(const PNMImage self)
        
        /**
         * Converts the image from grayscale to RGB.  Any alpha channel, if present,
         * is left undisturbed.
         */
        """
        pass

    def multSubImage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        mult_sub_image(const PNMImage self, const PNMImage copy, int xto, int yto, int xfrom, int yfrom, int x_size, int y_size, float pixel_scale)
        
        /**
         * Behaves like copy_sub_image(), except the copy pixels are multiplied to the
         * pixels of the destination, after scaling by the specified pixel_scale.
         * Unlike blend_sub_image(), the alpha channel is not treated specially.
         */
        """
        pass

    def mult_sub_image(self, const_PNMImage_self, const_PNMImage_copy, int_xto, int_yto, int_xfrom, int_yfrom, int_x_size, int_y_size, float_pixel_scale): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        mult_sub_image(const PNMImage self, const PNMImage copy, int xto, int yto, int xfrom, int yfrom, int x_size, int y_size, float pixel_scale)
        
        /**
         * Behaves like copy_sub_image(), except the copy pixels are multiplied to the
         * pixels of the destination, after scaling by the specified pixel_scale.
         * Unlike blend_sub_image(), the alpha channel is not treated specially.
         */
        """
        pass

    def perlinNoiseFill(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        perlin_noise_fill(const PNMImage self, StackedPerlinNoise2 perlin)
        perlin_noise_fill(const PNMImage self, float sx, float sy, int table_size, int seed)
        
        /**
         * Fills the image with a grayscale perlin noise pattern based on the
         * indicated parameters.  Uses set_xel to set the grayscale values.  The sx
         * and sy parameters are in multiples of the size of this image.  See also the
         * PerlinNoise2 class in mathutil.
         */
        
        /**
         * Variant of perlin_noise_fill that uses an existing StackedPerlinNoise2
         * object.
         */
        """
        pass

    def perlin_noise_fill(self, const_PNMImage_self, StackedPerlinNoise2_perlin): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        perlin_noise_fill(const PNMImage self, StackedPerlinNoise2 perlin)
        perlin_noise_fill(const PNMImage self, float sx, float sy, int table_size, int seed)
        
        /**
         * Fills the image with a grayscale perlin noise pattern based on the
         * indicated parameters.  Uses set_xel to set the grayscale values.  The sx
         * and sy parameters are in multiples of the size of this image.  See also the
         * PerlinNoise2 class in mathutil.
         */
        
        /**
         * Variant of perlin_noise_fill that uses an existing StackedPerlinNoise2
         * object.
         */
        """
        pass

    def premultiplyAlpha(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        premultiply_alpha(const PNMImage self)
        
        /**
         * Converts an image in-place to its "premultiplied" form, where, for every
         * pixel in the image, the red, green, and blue components are multiplied by
         * that pixel's alpha value.
         *
         * This does not modify any alpha values.
         */
        """
        pass

    def premultiply_alpha(self, const_PNMImage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        premultiply_alpha(const PNMImage self)
        
        /**
         * Converts an image in-place to its "premultiplied" form, where, for every
         * pixel in the image, the red, green, and blue components are multiplied by
         * that pixel's alpha value.
         *
         * This does not modify any alpha values.
         */
        """
        pass

    def quantize(self, const_PNMImage_self, int_max_colors): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        quantize(const PNMImage self, int max_colors)
        
        /**
         * Reduces the number of unique colors in the image to (at most) the given
         * count.  Fewer colors than requested may be left in the image after this
         * operation, but never more.
         *
         * At present, this is only supported on images without an alpha channel.
         *
         * @since 1.10.5
         */
        """
        pass

    def quickFilterFrom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        quick_filter_from(const PNMImage self, const PNMImage copy, int xborder, int yborder)
        
        /**
         * Resizes from the given image, with a fixed radius of 0.5. This is a very
         * specialized and simple algorithm that doesn't handle dropping below the
         * Nyquist rate very well, but is quite a bit faster than the more general
         * box_filter(), above.  If borders are specified, they will further restrict
         * the size of the resulting image.  There's no point in using
         * quick_box_filter() on a single image.
         */
        """
        pass

    def quick_filter_from(self, const_PNMImage_self, const_PNMImage_copy, int_xborder, int_yborder): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        quick_filter_from(const PNMImage self, const PNMImage copy, int xborder, int yborder)
        
        /**
         * Resizes from the given image, with a fixed radius of 0.5. This is a very
         * specialized and simple algorithm that doesn't handle dropping below the
         * Nyquist rate very well, but is quite a bit faster than the more general
         * box_filter(), above.  If borders are specified, they will further restrict
         * the size of the resulting image.  There's no point in using
         * quick_box_filter() on a single image.
         */
        """
        pass

    def read(self, const_PNMImage_self, istream_data, str_filename, PNMFileType_type, bool_report_unknown_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        read(const PNMImage self, istream data, str filename, PNMFileType type, bool report_unknown_type)
        
        /**
         * Reads the indicated image filename.  If type is non-NULL, it is a
         * suggestion for the type of file it is.  Returns true if successful, false
         * on error.
         */
        
        /**
         * Reads the image data from the indicated stream.
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
        
        /**
         * This flavor of read() uses an already-existing PNMReader to read the image
         * file.  You can get a reader via the PNMImageHeader::make_reader() methods.
         * This is a good way to examine the header of a file (for instance, to
         * determine its size) before actually reading the entire image.
         *
         * The PNMReader is always deleted upon completion, whether successful or not.
         */
        """
        pass

    def remixChannels(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remix_channels(const PNMImage self, const LMatrix4f conv)
        
        /**
         * Transforms every pixel using the operation (Ro,Go,Bo) =
         * conv.xform_point(Ri,Gi,Bi); Input must be a color image.
         */
        """
        pass

    def remix_channels(self, const_PNMImage_self, const_LMatrix4f_conv): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remix_channels(const PNMImage self, const LMatrix4f conv)
        
        /**
         * Transforms every pixel using the operation (Ro,Go,Bo) =
         * conv.xform_point(Ri,Gi,Bi); Input must be a color image.
         */
        """
        pass

    def removeAlpha(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_alpha(const PNMImage self)
        
        /**
         * Removes the image's alpha channel, if it exists.
         */
        """
        pass

    def remove_alpha(self, const_PNMImage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_alpha(const PNMImage self)
        
        /**
         * Removes the image's alpha channel, if it exists.
         */
        """
        pass

    def renderSpot(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        render_spot(const PNMImage self, const LVecBase4f fg, const LVecBase4f bg, float min_radius, float max_radius)
        
        /**
         * Renders a solid-color circle, with a fuzzy edge, into the center of the
         * PNMImage.  If the PNMImage is non-square, this actually renders an ellipse.
         *
         * The min_radius and max_radius are in the scale 0..1, where 1.0 means the
         * full width of the image.  If min_radius == max_radius, the edge is sharp
         * (but still antialiased); otherwise, the pixels between min_radius and
         * max_radius are smoothly blended between fg and bg colors.
         */
        """
        pass

    def render_spot(self, const_PNMImage_self, const_LVecBase4f_fg, const_LVecBase4f_bg, float_min_radius, float_max_radius): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        render_spot(const PNMImage self, const LVecBase4f fg, const LVecBase4f bg, float min_radius, float max_radius)
        
        /**
         * Renders a solid-color circle, with a fuzzy edge, into the center of the
         * PNMImage.  If the PNMImage is non-square, this actually renders an ellipse.
         *
         * The min_radius and max_radius are in the scale 0..1, where 1.0 means the
         * full width of the image.  If min_radius == max_radius, the edge is sharp
         * (but still antialiased); otherwise, the pixels between min_radius and
         * max_radius are smoothly blended between fg and bg colors.
         */
        """
        pass

    def rescale(self, const_PNMImage_self, float_min_val, float_max_val): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        rescale(const PNMImage self, float min_val, float max_val)
        
        /**
         * Rescales the RGB channel values so that any values in the original image
         * between min_val and max_val are expanded to the range 0 .. 1.  Values below
         * min_val are set to 0, and values above max_val are set to 1. Does not
         * affect the alpha channel, if any.
         */
        """
        pass

    def reverseRows(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        reverse_rows(const PNMImage self)
        
        /**
         * Performs an in-place reversal of the row (y) data.
         */
        """
        pass

    def reverse_rows(self, const_PNMImage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        reverse_rows(const PNMImage self)
        
        /**
         * Performs an in-place reversal of the row (y) data.
         */
        """
        pass

    def setAlpha(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_alpha(const PNMImage self, int x, int y, float a)
        
        /**
         * Sets the alpha component color only at the indicated pixel.  It is an error
         * to call this unless has_alpha() is true.  The value given should be in the
         * range 0..1.
         */
        """
        pass

    def setAlphaVal(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_alpha_val(const PNMImage self, int x, int y, int a)
        
        /**
         * Sets the alpha component color only at the indicated pixel.  It is an error
         * to call this unless has_alpha() is true.  The value given should be in the
         * range 0..maxval.
         *
         * This value is always linearly encoded, even if the image is set to the sRGB
         * color space.
         */
        """
        pass

    def setBlue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_blue(const PNMImage self, int x, int y, float b)
        
        /**
         * Sets the blue component color only at the indicated pixel.  The value given
         * should be a linearized float in the range 0..1.
         */
        """
        pass

    def setBlueVal(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_blue_val(const PNMImage self, int x, int y, int b)
        
        /**
         * Sets the blue component color only at the indicated pixel.  The value given
         * should be in the range 0..maxval, encoded in the configured color space.
         * See set_blue if you instead have a linearized and normalized floating-point
         * value.
         */
        """
        pass

    def setChannel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_channel(const PNMImage self, int x, int y, int channel, float value)
        
        /**
         * Sets the nth component color at the indicated pixel.  The channel index
         * should be in the range 0..(get_num_channels()-1).  The channels are ordered
         * B, G, R, A.  This is slightly less optimal than setting the component
         * values directly by named methods.  The value given should be a float in the
         * range 0..1.
         */
        """
        pass

    def setChannelVal(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_channel_val(const PNMImage self, int x, int y, int channel, int value)
        
        /**
         * Sets the nth component color at the indicated pixel.  The channel index
         * should be in the range 0..(get_num_channels()-1).  The channels are ordered
         * B, G, R, A.  This is slightly less optimal than setting the component
         * values directly by named methods.  The value given should be in the range
         * 0..maxval.
         */
        """
        pass

    def setColorSpace(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_color_space(const PNMImage self, int color_space)
        
        /**
         * Converts the colors in the image to the indicated color space.  This may be
         * a lossy operation, in particular when going from sRGB to linear.  The alpha
         * channel remains untouched.
         *
         * Note that, because functions like get_xel() and set_xel() work on
         * linearized floating-point values, this conversion won't affect those values
         * (aside from some minor discrepancies due to storage precision).  It does
         * affect the values used by get_xel_val() and set_xel_val(), though, since
         * those operate on encoded colors.
         *
         * Some color spaces, particularly scRGB, may enforce the use of a particular
         * maxval setting.
         */
        """
        pass

    def setColorType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_color_type(const PNMImage self, int color_type)
        
        /**
         * Translates the image to or from grayscale, color, or four-color mode.
         * Grayscale images are converted to full-color images with R, G, B set to the
         * original gray level; color images are converted to grayscale according to
         * the value of Bright().  The alpha channel, if added, is initialized to
         * zero.
         */
        """
        pass

    def setGray(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_gray(const PNMImage self, int x, int y, float gray)
        
        /**
         * Sets the gray component color at the indicated pixel.  This is only
         * meaningful for grayscale images; for other image types, this simply sets
         * the blue component color.  However, also see set_xel(), which can set all
         * the component colors to the same grayscale level, and hence works correctly
         * both for grayscale and color images.  The value given should be a
         * linearized float in the range 0..1.
         */
        """
        pass

    def setGrayVal(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_gray_val(const PNMImage self, int x, int y, int gray)
        
        /**
         * Sets the gray component color at the indicated pixel.  This is only
         * meaningful for grayscale images; for other image types, this simply sets
         * the blue component color.  However, also see set_xel_val(), which can set
         * all the component colors to the same grayscale level, and hence works
         * correctly both for grayscale and color images.  The value given should be
         * in the range 0..maxval, encoded in the configured color space.  See
         * set_gray if you instead have a linearized normalized floating-point value.
         */
        """
        pass

    def setGreen(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_green(const PNMImage self, int x, int y, float g)
        
        /**
         * Sets the green component color only at the indicated pixel.  The value
         * given should be a linearized float in the range 0..1.
         */
        """
        pass

    def setGreenVal(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_green_val(const PNMImage self, int x, int y, int g)
        
        /**
         * Sets the green component color only at the indicated pixel.  The value
         * given should be in the range 0..maxval, encoded in the configured color
         * space.  See set_green if you instead have a linearized and normalized
         * floating-point value.
         */
        """
        pass

    def setMaxval(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_maxval(const PNMImage self, int maxval)
        
        /**
         * Rescales the image to the indicated maxval.
         */
        """
        pass

    def setNumChannels(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_num_channels(const PNMImage self, int num_channels)
        
        /**
         * Changes the number of channels associated with the image.  The new number
         * of channels must be an integer in the range 1 through 4, inclusive.  This
         * will allocate and/or deallocate memory as necessary to accommodate; see
         * set_color_type().
         */
        """
        pass

    def setPixel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_pixel(const PNMImage self, int x, int y, const PixelSpec pixel)
        
        /**
         * Sets the (r, g, b, a) pixel value at the indicated pixel, using a PixelSpec
         * object.
         */
        """
        pass

    def setReadSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_read_size(const PNMImage self, int x_size, int y_size)
        
        /**
         * Specifies the size to we'd like to scale the image upon reading it.  This
         * will affect the next call to read().  This is usually used to reduce the
         * image size, e.g.  for a thumbnail.
         *
         * If the file type reader supports it (e.g.  JPEG), then this will scale the
         * image during the read operation, consequently reducing memory and CPU
         * utilization.  If the file type reader does not support it, this will load
         * the image normally, and them perform a linear scale after it has been
         * loaded.
         */
        """
        pass

    def setRed(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_red(const PNMImage self, int x, int y, float r)
        
        /**
         * Sets the red component color only at the indicated pixel.  The value given
         * should be a linearized float in the range 0..1.
         */
        """
        pass

    def setRedVal(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_red_val(const PNMImage self, int x, int y, int r)
        
        /**
         * Sets the red component color only at the indicated pixel.  The value given
         * should be in the range 0..maxval, encoded in the configured color space.
         * See set_red if you instead have a linearized and normalized floating-point
         * value.
         */
        """
        pass

    def setXel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_xel(const PNMImage self, int x, int y, const LVecBase3f value)
        set_xel(const PNMImage self, int x, int y, float gray)
        set_xel(const PNMImage self, int x, int y, float r, float g, float b)
        
        /**
         * Changes the RGB color at the indicated pixel.  Each component is a
         * linearized float in the range 0..1.
         */
        
        /**
         * Changes the RGB color at the indicated pixel.  Each component is a
         * linearized float in the range 0..1.
         */
        
        /**
         * Changes all three color components at the indicated pixel to the same
         * value.  The value is a linearized float in the range 0..1.
         */
        """
        pass

    def setXelA(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_xel_a(const PNMImage self, int x, int y, const LVecBase4f value)
        set_xel_a(const PNMImage self, int x, int y, float r, float g, float b, float a)
        
        /**
         * Changes the RGBA color at the indicated pixel.  Each component is a
         * linearized float in the range 0..1.
         */
        
        /**
         * Changes the RGBA color at the indicated pixel.  Each component is a
         * linearized float in the range 0..1.
         */
        """
        pass

    def setXelVal(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_xel_val(const PNMImage self, int x, int y, const pixel value)
        set_xel_val(const PNMImage self, int x, int y, int gray)
        set_xel_val(const PNMImage self, int x, int y, int r, int g, int b)
        
        /**
         * Changes the RGB color at the indicated pixel.  Each component is in the
         * range 0..maxval, encoded in the configured color space.  See set_xel if you
         * instead have a linearized and normalized floating-point value.
         */
        
        /**
         * Changes the RGB color at the indicated pixel.  Each component is in the
         * range 0..maxval, encoded in the configured color space.  See set_xel if you
         * instead have a linearized and normalized floating-point value.
         */
        
        /**
         * Changes all three color components at the indicated pixel to the same
         * value.  The value is in the range component is in the range 0..maxval,
         * encoded in the configured color space.  See set_xel if you instead have a
         * linearized and normalized floating-point value.
         */
        """
        pass

    def set_alpha(self, const_PNMImage_self, int_x, int_y, float_a): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_alpha(const PNMImage self, int x, int y, float a)
        
        /**
         * Sets the alpha component color only at the indicated pixel.  It is an error
         * to call this unless has_alpha() is true.  The value given should be in the
         * range 0..1.
         */
        """
        pass

    def set_alpha_val(self, const_PNMImage_self, int_x, int_y, int_a): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_alpha_val(const PNMImage self, int x, int y, int a)
        
        /**
         * Sets the alpha component color only at the indicated pixel.  It is an error
         * to call this unless has_alpha() is true.  The value given should be in the
         * range 0..maxval.
         *
         * This value is always linearly encoded, even if the image is set to the sRGB
         * color space.
         */
        """
        pass

    def set_blue(self, const_PNMImage_self, int_x, int_y, float_b): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_blue(const PNMImage self, int x, int y, float b)
        
        /**
         * Sets the blue component color only at the indicated pixel.  The value given
         * should be a linearized float in the range 0..1.
         */
        """
        pass

    def set_blue_val(self, const_PNMImage_self, int_x, int_y, int_b): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_blue_val(const PNMImage self, int x, int y, int b)
        
        /**
         * Sets the blue component color only at the indicated pixel.  The value given
         * should be in the range 0..maxval, encoded in the configured color space.
         * See set_blue if you instead have a linearized and normalized floating-point
         * value.
         */
        """
        pass

    def set_channel(self, const_PNMImage_self, int_x, int_y, int_channel, float_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_channel(const PNMImage self, int x, int y, int channel, float value)
        
        /**
         * Sets the nth component color at the indicated pixel.  The channel index
         * should be in the range 0..(get_num_channels()-1).  The channels are ordered
         * B, G, R, A.  This is slightly less optimal than setting the component
         * values directly by named methods.  The value given should be a float in the
         * range 0..1.
         */
        """
        pass

    def set_channel_val(self, const_PNMImage_self, int_x, int_y, int_channel, int_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_channel_val(const PNMImage self, int x, int y, int channel, int value)
        
        /**
         * Sets the nth component color at the indicated pixel.  The channel index
         * should be in the range 0..(get_num_channels()-1).  The channels are ordered
         * B, G, R, A.  This is slightly less optimal than setting the component
         * values directly by named methods.  The value given should be in the range
         * 0..maxval.
         */
        """
        pass

    def set_color_space(self, const_PNMImage_self, int_color_space): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_color_space(const PNMImage self, int color_space)
        
        /**
         * Converts the colors in the image to the indicated color space.  This may be
         * a lossy operation, in particular when going from sRGB to linear.  The alpha
         * channel remains untouched.
         *
         * Note that, because functions like get_xel() and set_xel() work on
         * linearized floating-point values, this conversion won't affect those values
         * (aside from some minor discrepancies due to storage precision).  It does
         * affect the values used by get_xel_val() and set_xel_val(), though, since
         * those operate on encoded colors.
         *
         * Some color spaces, particularly scRGB, may enforce the use of a particular
         * maxval setting.
         */
        """
        pass

    def set_color_type(self, const_PNMImage_self, int_color_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_color_type(const PNMImage self, int color_type)
        
        /**
         * Translates the image to or from grayscale, color, or four-color mode.
         * Grayscale images are converted to full-color images with R, G, B set to the
         * original gray level; color images are converted to grayscale according to
         * the value of Bright().  The alpha channel, if added, is initialized to
         * zero.
         */
        """
        pass

    def set_gray(self, const_PNMImage_self, int_x, int_y, float_gray): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_gray(const PNMImage self, int x, int y, float gray)
        
        /**
         * Sets the gray component color at the indicated pixel.  This is only
         * meaningful for grayscale images; for other image types, this simply sets
         * the blue component color.  However, also see set_xel(), which can set all
         * the component colors to the same grayscale level, and hence works correctly
         * both for grayscale and color images.  The value given should be a
         * linearized float in the range 0..1.
         */
        """
        pass

    def set_gray_val(self, const_PNMImage_self, int_x, int_y, int_gray): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_gray_val(const PNMImage self, int x, int y, int gray)
        
        /**
         * Sets the gray component color at the indicated pixel.  This is only
         * meaningful for grayscale images; for other image types, this simply sets
         * the blue component color.  However, also see set_xel_val(), which can set
         * all the component colors to the same grayscale level, and hence works
         * correctly both for grayscale and color images.  The value given should be
         * in the range 0..maxval, encoded in the configured color space.  See
         * set_gray if you instead have a linearized normalized floating-point value.
         */
        """
        pass

    def set_green(self, const_PNMImage_self, int_x, int_y, float_g): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_green(const PNMImage self, int x, int y, float g)
        
        /**
         * Sets the green component color only at the indicated pixel.  The value
         * given should be a linearized float in the range 0..1.
         */
        """
        pass

    def set_green_val(self, const_PNMImage_self, int_x, int_y, int_g): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_green_val(const PNMImage self, int x, int y, int g)
        
        /**
         * Sets the green component color only at the indicated pixel.  The value
         * given should be in the range 0..maxval, encoded in the configured color
         * space.  See set_green if you instead have a linearized and normalized
         * floating-point value.
         */
        """
        pass

    def set_maxval(self, const_PNMImage_self, int_maxval): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_maxval(const PNMImage self, int maxval)
        
        /**
         * Rescales the image to the indicated maxval.
         */
        """
        pass

    def set_num_channels(self, const_PNMImage_self, int_num_channels): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_num_channels(const PNMImage self, int num_channels)
        
        /**
         * Changes the number of channels associated with the image.  The new number
         * of channels must be an integer in the range 1 through 4, inclusive.  This
         * will allocate and/or deallocate memory as necessary to accommodate; see
         * set_color_type().
         */
        """
        pass

    def set_pixel(self, const_PNMImage_self, int_x, int_y, const_PixelSpec_pixel): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_pixel(const PNMImage self, int x, int y, const PixelSpec pixel)
        
        /**
         * Sets the (r, g, b, a) pixel value at the indicated pixel, using a PixelSpec
         * object.
         */
        """
        pass

    def set_read_size(self, const_PNMImage_self, int_x_size, int_y_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_read_size(const PNMImage self, int x_size, int y_size)
        
        /**
         * Specifies the size to we'd like to scale the image upon reading it.  This
         * will affect the next call to read().  This is usually used to reduce the
         * image size, e.g.  for a thumbnail.
         *
         * If the file type reader supports it (e.g.  JPEG), then this will scale the
         * image during the read operation, consequently reducing memory and CPU
         * utilization.  If the file type reader does not support it, this will load
         * the image normally, and them perform a linear scale after it has been
         * loaded.
         */
        """
        pass

    def set_red(self, const_PNMImage_self, int_x, int_y, float_r): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_red(const PNMImage self, int x, int y, float r)
        
        /**
         * Sets the red component color only at the indicated pixel.  The value given
         * should be a linearized float in the range 0..1.
         */
        """
        pass

    def set_red_val(self, const_PNMImage_self, int_x, int_y, int_r): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_red_val(const PNMImage self, int x, int y, int r)
        
        /**
         * Sets the red component color only at the indicated pixel.  The value given
         * should be in the range 0..maxval, encoded in the configured color space.
         * See set_red if you instead have a linearized and normalized floating-point
         * value.
         */
        """
        pass

    def set_xel(self, const_PNMImage_self, int_x, int_y, const_LVecBase3f_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_xel(const PNMImage self, int x, int y, const LVecBase3f value)
        set_xel(const PNMImage self, int x, int y, float gray)
        set_xel(const PNMImage self, int x, int y, float r, float g, float b)
        
        /**
         * Changes the RGB color at the indicated pixel.  Each component is a
         * linearized float in the range 0..1.
         */
        
        /**
         * Changes the RGB color at the indicated pixel.  Each component is a
         * linearized float in the range 0..1.
         */
        
        /**
         * Changes all three color components at the indicated pixel to the same
         * value.  The value is a linearized float in the range 0..1.
         */
        """
        pass

    def set_xel_a(self, const_PNMImage_self, int_x, int_y, const_LVecBase4f_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_xel_a(const PNMImage self, int x, int y, const LVecBase4f value)
        set_xel_a(const PNMImage self, int x, int y, float r, float g, float b, float a)
        
        /**
         * Changes the RGBA color at the indicated pixel.  Each component is a
         * linearized float in the range 0..1.
         */
        
        /**
         * Changes the RGBA color at the indicated pixel.  Each component is a
         * linearized float in the range 0..1.
         */
        """
        pass

    def set_xel_val(self, const_PNMImage_self, int_x, int_y, const_pixel_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_xel_val(const PNMImage self, int x, int y, const pixel value)
        set_xel_val(const PNMImage self, int x, int y, int gray)
        set_xel_val(const PNMImage self, int x, int y, int r, int g, int b)
        
        /**
         * Changes the RGB color at the indicated pixel.  Each component is in the
         * range 0..maxval, encoded in the configured color space.  See set_xel if you
         * instead have a linearized and normalized floating-point value.
         */
        
        /**
         * Changes the RGB color at the indicated pixel.  Each component is in the
         * range 0..maxval, encoded in the configured color space.  See set_xel if you
         * instead have a linearized and normalized floating-point value.
         */
        
        /**
         * Changes all three color components at the indicated pixel to the same
         * value.  The value is in the range component is in the range 0..maxval,
         * encoded in the configured color space.  See set_xel if you instead have a
         * linearized and normalized floating-point value.
         */
        """
        pass

    def takeFrom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        take_from(const PNMImage self, PNMImage orig)
        
        /**
         * Move the contents of the other image into this one, and empty the other
         * image.
         */
        """
        pass

    def take_from(self, const_PNMImage_self, PNMImage_orig): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        take_from(const PNMImage self, PNMImage orig)
        
        /**
         * Move the contents of the other image into this one, and empty the other
         * image.
         */
        """
        pass

    def threshold(self, const_PNMImage_self, const_PNMImage_select_image, int_channel, float_threshold, const_PNMImage_lt, const_PNMImage_ge): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        threshold(const PNMImage self, const PNMImage select_image, int channel, float threshold, const PNMImage lt, const PNMImage ge)
        
        /**
         * Selectively copies each pixel from either one source or another source,
         * depending on the pixel value of the indicated channel of select_image.
         *
         * For each pixel (x, y):
         *
         * s = select_image.get_channel(x, y, channel). Set this image's (x, y) to:
         *
         * lt.get_xel(x, y) if s < threshold, or
         *
         * ge.get_xel(x, y) if s >= threshold
         *
         * Any of select_image, lt, or ge may be the same PNMImge object as this
         * image, or the same as each other; or they may all be different.  All images
         * must be the same size.  As a special case, lt and ge may both be 1x1 images
         * instead of the source image size.
         */
        """
        pass

    def toAlphaVal(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        to_alpha_val(PNMImage self, float input_value)
        
        /**
         * A handy function to scale alpha values from [0..1] to [0..get_maxval()].
         */
        """
        pass

    def toVal(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        to_val(PNMImage self, const LVecBase3f input_value)
        to_val(PNMImage self, float input_value)
        
        /**
         * A handy function to scale non-alpha values from [0..1] to
         * [0..get_maxval()].  Do not use this for alpha values, see to_alpha_val.
         */
        
        /**
         * A handy function to scale non-alpha values from [0..1] to
         * [0..get_maxval()].  Do not use this for alpha values, see to_alpha_val.
         */
        """
        pass

    def to_alpha_val(self, PNMImage_self, float_input_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        to_alpha_val(PNMImage self, float input_value)
        
        /**
         * A handy function to scale alpha values from [0..1] to [0..get_maxval()].
         */
        """
        pass

    def to_val(self, PNMImage_self, const_LVecBase3f_input_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        to_val(PNMImage self, const LVecBase3f input_value)
        to_val(PNMImage self, float input_value)
        
        /**
         * A handy function to scale non-alpha values from [0..1] to
         * [0..get_maxval()].  Do not use this for alpha values, see to_alpha_val.
         */
        
        /**
         * A handy function to scale non-alpha values from [0..1] to
         * [0..get_maxval()].  Do not use this for alpha values, see to_alpha_val.
         */
        """
        pass

    def unfilteredStretchFrom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        unfiltered_stretch_from(const PNMImage self, const PNMImage copy)
        
        /**
         * Resizes from the indicated image into this one by performing a nearest-
         * point sample.
         */
        """
        pass

    def unfiltered_stretch_from(self, const_PNMImage_self, const_PNMImage_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        unfiltered_stretch_from(const PNMImage self, const PNMImage copy)
        
        /**
         * Resizes from the indicated image into this one by performing a nearest-
         * point sample.
         */
        """
        pass

    def unpremultiplyAlpha(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        unpremultiply_alpha(const PNMImage self)
        
        /**
         * Converts an image in-place to its "straight alpha" form (presumably from a
         * "premultiplied" form), where, for every pixel in the image, the red, green,
         * and blue components are divided by that pixel's alpha value.
         *
         * This does not modify any alpha values.
         */
        """
        pass

    def unpremultiply_alpha(self, const_PNMImage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        unpremultiply_alpha(const PNMImage self)
        
        /**
         * Converts an image in-place to its "straight alpha" form (presumably from a
         * "premultiplied" form), where, for every pixel in the image, the red, green,
         * and blue components are divided by that pixel's alpha value.
         *
         * This does not modify any alpha values.
         */
        """
        pass

    def write(self, PNMImage_self, ostream_data, str_filename, PNMFileType_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(PNMImage self, ostream data, str filename, PNMFileType type)
        
        /**
         * Writes the image to the indicated filename.  If type is non-NULL, it is a
         * suggestion for the type of image file to write.
         */
        
        /**
         * Writes the image to the indicated ostream.
         *
         * The filename is advisory only, and may be used suggest a type if it has a
         * known extension.
         *
         * If type is non-NULL, it is a suggestion for the type of image file to
         * write.
         */
        
        /**
         * This flavor of write() uses an already-existing PNMWriter to write the
         * image file.  You can get a writer via the PNMImageHeader::make_writer()
         * methods.
         *
         * The PNMWriter is always deleted upon completion, whether successful or not.
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

    def __imul__(self, *args, **kwargs): # real signature unknown
        """ Return self*=value. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __invert__(self, *args, **kwargs): # real signature unknown
        """ ~self """
        pass

    def __isub__(self, *args, **kwargs): # real signature unknown
        """ Return self-=value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    CRow = None # (!) real value is "<class 'panda3d.core.CRow'>"
    DtoolClassDict = {
        'CRow': None, # (!) real value is "<class 'panda3d.core.CRow'>"
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'Row': None, # (!) real value is "<class 'panda3d.core.Row'>"
        '__add__': None, # (!) real value is "<slot wrapper '__add__' of 'panda3d.core.PNMImage' objects>"
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.PNMImage' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.PNMImage' objects>"
        '__doc__': '/**\n * The name of this class derives from the fact that we originally implemented\n * it as a layer on top of the "pnm library", based on netpbm, which was built\n * to implement pbm, pgm, and pbm files, and is the underlying support of a\n * number of public-domain image file converters.  Nowadays we are no longer\n * derived directly from the pnm library, mainly to allow support of C++\n * iostreams instead of the C stdio FILE interface.\n *\n * Conceptually, a PNMImage is a two-dimensional array of xels, which are the\n * PNM-defined generic pixel type.  Each xel may have a red, green, and blue\n * component, or (if the image is grayscale) a gray component.  The image may\n * be read in, the individual xels manipulated, and written out again, or a\n * black image may be constructed from scratch.\n *\n * A PNMImage has a color space and a maxval, the combination of which defines\n * how a floating-point linear color value is encoded as an integer value in\n * memory.  The functions ending in _val operate on encoded colors, whereas\n * the regular ones work with linear floating-point values.  All operations\n * are color space correct unless otherwise specified.\n *\n * The image is of size XSize() by YSize() xels, numbered from top to bottom,\n * left to right, beginning at zero.\n *\n * Files can be specified by filename, or by an iostream pointer.  The\n * filename "-" refers to stdin or stdout.\n *\n * This class is not inherently thread-safe; use it from a single thread or\n * protect access using a mutex.\n */',
        '__getitem__': None, # (!) real value is "<slot wrapper '__getitem__' of 'panda3d.core.PNMImage' objects>"
        '__iadd__': None, # (!) real value is "<slot wrapper '__iadd__' of 'panda3d.core.PNMImage' objects>"
        '__imul__': None, # (!) real value is "<slot wrapper '__imul__' of 'panda3d.core.PNMImage' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.PNMImage' objects>"
        '__invert__': None, # (!) real value is "<slot wrapper '__invert__' of 'panda3d.core.PNMImage' objects>"
        '__isub__': None, # (!) real value is "<slot wrapper '__isub__' of 'panda3d.core.PNMImage' objects>"
        '__mul__': None, # (!) real value is "<slot wrapper '__mul__' of 'panda3d.core.PNMImage' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE356430>'
        '__radd__': None, # (!) real value is "<slot wrapper '__radd__' of 'panda3d.core.PNMImage' objects>"
        '__rmul__': None, # (!) real value is "<slot wrapper '__rmul__' of 'panda3d.core.PNMImage' objects>"
        '__rsub__': None, # (!) real value is "<slot wrapper '__rsub__' of 'panda3d.core.PNMImage' objects>"
        '__sub__': None, # (!) real value is "<slot wrapper '__sub__' of 'panda3d.core.PNMImage' objects>"
        'addAlpha': None, # (!) real value is "<method 'addAlpha' of 'panda3d.core.PNMImage' objects>"
        'addSubImage': None, # (!) real value is "<method 'addSubImage' of 'panda3d.core.PNMImage' objects>"
        'add_alpha': None, # (!) real value is "<method 'add_alpha' of 'panda3d.core.PNMImage' objects>"
        'add_sub_image': None, # (!) real value is "<method 'add_sub_image' of 'panda3d.core.PNMImage' objects>"
        'alphaFill': None, # (!) real value is "<method 'alphaFill' of 'panda3d.core.PNMImage' objects>"
        'alphaFillVal': None, # (!) real value is "<method 'alphaFillVal' of 'panda3d.core.PNMImage' objects>"
        'alpha_fill': None, # (!) real value is "<method 'alpha_fill' of 'panda3d.core.PNMImage' objects>"
        'alpha_fill_val': None, # (!) real value is "<method 'alpha_fill_val' of 'panda3d.core.PNMImage' objects>"
        'applyExponent': None, # (!) real value is "<method 'applyExponent' of 'panda3d.core.PNMImage' objects>"
        'apply_exponent': None, # (!) real value is "<method 'apply_exponent' of 'panda3d.core.PNMImage' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.PNMImage' objects>"
        'blend': None, # (!) real value is "<method 'blend' of 'panda3d.core.PNMImage' objects>"
        'blendSubImage': None, # (!) real value is "<method 'blendSubImage' of 'panda3d.core.PNMImage' objects>"
        'blend_sub_image': None, # (!) real value is "<method 'blend_sub_image' of 'panda3d.core.PNMImage' objects>"
        'boxFilter': None, # (!) real value is "<method 'boxFilter' of 'panda3d.core.PNMImage' objects>"
        'boxFilterFrom': None, # (!) real value is "<method 'boxFilterFrom' of 'panda3d.core.PNMImage' objects>"
        'box_filter': None, # (!) real value is "<method 'box_filter' of 'panda3d.core.PNMImage' objects>"
        'box_filter_from': None, # (!) real value is "<method 'box_filter_from' of 'panda3d.core.PNMImage' objects>"
        'clampVal': None, # (!) real value is "<method 'clampVal' of 'panda3d.core.PNMImage' objects>"
        'clamp_val': None, # (!) real value is "<method 'clamp_val' of 'panda3d.core.PNMImage' objects>"
        'clear': None, # (!) real value is "<method 'clear' of 'panda3d.core.PNMImage' objects>"
        'clearReadSize': None, # (!) real value is "<method 'clearReadSize' of 'panda3d.core.PNMImage' objects>"
        'clear_read_size': None, # (!) real value is "<method 'clear_read_size' of 'panda3d.core.PNMImage' objects>"
        'copyChannel': None, # (!) real value is "<method 'copyChannel' of 'panda3d.core.PNMImage' objects>"
        'copyChannelBits': None, # (!) real value is "<method 'copyChannelBits' of 'panda3d.core.PNMImage' objects>"
        'copyFrom': None, # (!) real value is "<method 'copyFrom' of 'panda3d.core.PNMImage' objects>"
        'copyHeaderFrom': None, # (!) real value is "<method 'copyHeaderFrom' of 'panda3d.core.PNMImage' objects>"
        'copySubImage': None, # (!) real value is "<method 'copySubImage' of 'panda3d.core.PNMImage' objects>"
        'copy_channel': None, # (!) real value is "<method 'copy_channel' of 'panda3d.core.PNMImage' objects>"
        'copy_channel_bits': None, # (!) real value is "<method 'copy_channel_bits' of 'panda3d.core.PNMImage' objects>"
        'copy_from': None, # (!) real value is "<method 'copy_from' of 'panda3d.core.PNMImage' objects>"
        'copy_header_from': None, # (!) real value is "<method 'copy_header_from' of 'panda3d.core.PNMImage' objects>"
        'copy_sub_image': None, # (!) real value is "<method 'copy_sub_image' of 'panda3d.core.PNMImage' objects>"
        'darkenSubImage': None, # (!) real value is "<method 'darkenSubImage' of 'panda3d.core.PNMImage' objects>"
        'darken_sub_image': None, # (!) real value is "<method 'darken_sub_image' of 'panda3d.core.PNMImage' objects>"
        'doFillDistance': None, # (!) real value is "<method 'doFillDistance' of 'panda3d.core.PNMImage' objects>"
        'do_fill_distance': None, # (!) real value is "<method 'do_fill_distance' of 'panda3d.core.PNMImage' objects>"
        'expandBorder': None, # (!) real value is "<method 'expandBorder' of 'panda3d.core.PNMImage' objects>"
        'expand_border': None, # (!) real value is "<method 'expand_border' of 'panda3d.core.PNMImage' objects>"
        'fill': None, # (!) real value is "<method 'fill' of 'panda3d.core.PNMImage' objects>"
        'fillDistanceInside': None, # (!) real value is "<method 'fillDistanceInside' of 'panda3d.core.PNMImage' objects>"
        'fillDistanceOutside': None, # (!) real value is "<method 'fillDistanceOutside' of 'panda3d.core.PNMImage' objects>"
        'fillVal': None, # (!) real value is "<method 'fillVal' of 'panda3d.core.PNMImage' objects>"
        'fill_distance_inside': None, # (!) real value is "<method 'fill_distance_inside' of 'panda3d.core.PNMImage' objects>"
        'fill_distance_outside': None, # (!) real value is "<method 'fill_distance_outside' of 'panda3d.core.PNMImage' objects>"
        'fill_val': None, # (!) real value is "<method 'fill_val' of 'panda3d.core.PNMImage' objects>"
        'flip': None, # (!) real value is "<method 'flip' of 'panda3d.core.PNMImage' objects>"
        'fromAlphaVal': None, # (!) real value is "<method 'fromAlphaVal' of 'panda3d.core.PNMImage' objects>"
        'fromVal': None, # (!) real value is "<method 'fromVal' of 'panda3d.core.PNMImage' objects>"
        'from_alpha_val': None, # (!) real value is "<method 'from_alpha_val' of 'panda3d.core.PNMImage' objects>"
        'from_val': None, # (!) real value is "<method 'from_val' of 'panda3d.core.PNMImage' objects>"
        'gammaCorrect': None, # (!) real value is "<method 'gammaCorrect' of 'panda3d.core.PNMImage' objects>"
        'gammaCorrectAlpha': None, # (!) real value is "<method 'gammaCorrectAlpha' of 'panda3d.core.PNMImage' objects>"
        'gamma_correct': None, # (!) real value is "<method 'gamma_correct' of 'panda3d.core.PNMImage' objects>"
        'gamma_correct_alpha': None, # (!) real value is "<method 'gamma_correct_alpha' of 'panda3d.core.PNMImage' objects>"
        'gaussianFilter': None, # (!) real value is "<method 'gaussianFilter' of 'panda3d.core.PNMImage' objects>"
        'gaussianFilterFrom': None, # (!) real value is "<method 'gaussianFilterFrom' of 'panda3d.core.PNMImage' objects>"
        'gaussian_filter': None, # (!) real value is "<method 'gaussian_filter' of 'panda3d.core.PNMImage' objects>"
        'gaussian_filter_from': None, # (!) real value is "<method 'gaussian_filter_from' of 'panda3d.core.PNMImage' objects>"
        'getAlpha': None, # (!) real value is "<method 'getAlpha' of 'panda3d.core.PNMImage' objects>"
        'getAlphaVal': None, # (!) real value is "<method 'getAlphaVal' of 'panda3d.core.PNMImage' objects>"
        'getAverageGray': None, # (!) real value is "<method 'getAverageGray' of 'panda3d.core.PNMImage' objects>"
        'getAverageXel': None, # (!) real value is "<method 'getAverageXel' of 'panda3d.core.PNMImage' objects>"
        'getAverageXelA': None, # (!) real value is "<method 'getAverageXelA' of 'panda3d.core.PNMImage' objects>"
        'getBlue': None, # (!) real value is "<method 'getBlue' of 'panda3d.core.PNMImage' objects>"
        'getBlueVal': None, # (!) real value is "<method 'getBlueVal' of 'panda3d.core.PNMImage' objects>"
        'getBright': None, # (!) real value is "<method 'getBright' of 'panda3d.core.PNMImage' objects>"
        'getChannel': None, # (!) real value is "<method 'getChannel' of 'panda3d.core.PNMImage' objects>"
        'getChannelVal': None, # (!) real value is "<method 'getChannelVal' of 'panda3d.core.PNMImage' objects>"
        'getColorSpace': None, # (!) real value is "<method 'getColorSpace' of 'panda3d.core.PNMImage' objects>"
        'getGray': None, # (!) real value is "<method 'getGray' of 'panda3d.core.PNMImage' objects>"
        'getGrayVal': None, # (!) real value is "<method 'getGrayVal' of 'panda3d.core.PNMImage' objects>"
        'getGreen': None, # (!) real value is "<method 'getGreen' of 'panda3d.core.PNMImage' objects>"
        'getGreenVal': None, # (!) real value is "<method 'getGreenVal' of 'panda3d.core.PNMImage' objects>"
        'getPixel': None, # (!) real value is "<method 'getPixel' of 'panda3d.core.PNMImage' objects>"
        'getReadXSize': None, # (!) real value is "<method 'getReadXSize' of 'panda3d.core.PNMImage' objects>"
        'getReadYSize': None, # (!) real value is "<method 'getReadYSize' of 'panda3d.core.PNMImage' objects>"
        'getRed': None, # (!) real value is "<method 'getRed' of 'panda3d.core.PNMImage' objects>"
        'getRedVal': None, # (!) real value is "<method 'getRedVal' of 'panda3d.core.PNMImage' objects>"
        'getXel': None, # (!) real value is "<method 'getXel' of 'panda3d.core.PNMImage' objects>"
        'getXelA': None, # (!) real value is "<method 'getXelA' of 'panda3d.core.PNMImage' objects>"
        'getXelVal': None, # (!) real value is "<method 'getXelVal' of 'panda3d.core.PNMImage' objects>"
        'get_alpha': None, # (!) real value is "<method 'get_alpha' of 'panda3d.core.PNMImage' objects>"
        'get_alpha_val': None, # (!) real value is "<method 'get_alpha_val' of 'panda3d.core.PNMImage' objects>"
        'get_average_gray': None, # (!) real value is "<method 'get_average_gray' of 'panda3d.core.PNMImage' objects>"
        'get_average_xel': None, # (!) real value is "<method 'get_average_xel' of 'panda3d.core.PNMImage' objects>"
        'get_average_xel_a': None, # (!) real value is "<method 'get_average_xel_a' of 'panda3d.core.PNMImage' objects>"
        'get_blue': None, # (!) real value is "<method 'get_blue' of 'panda3d.core.PNMImage' objects>"
        'get_blue_val': None, # (!) real value is "<method 'get_blue_val' of 'panda3d.core.PNMImage' objects>"
        'get_bright': None, # (!) real value is "<method 'get_bright' of 'panda3d.core.PNMImage' objects>"
        'get_channel': None, # (!) real value is "<method 'get_channel' of 'panda3d.core.PNMImage' objects>"
        'get_channel_val': None, # (!) real value is "<method 'get_channel_val' of 'panda3d.core.PNMImage' objects>"
        'get_color_space': None, # (!) real value is "<method 'get_color_space' of 'panda3d.core.PNMImage' objects>"
        'get_gray': None, # (!) real value is "<method 'get_gray' of 'panda3d.core.PNMImage' objects>"
        'get_gray_val': None, # (!) real value is "<method 'get_gray_val' of 'panda3d.core.PNMImage' objects>"
        'get_green': None, # (!) real value is "<method 'get_green' of 'panda3d.core.PNMImage' objects>"
        'get_green_val': None, # (!) real value is "<method 'get_green_val' of 'panda3d.core.PNMImage' objects>"
        'get_pixel': None, # (!) real value is "<method 'get_pixel' of 'panda3d.core.PNMImage' objects>"
        'get_read_x_size': None, # (!) real value is "<method 'get_read_x_size' of 'panda3d.core.PNMImage' objects>"
        'get_read_y_size': None, # (!) real value is "<method 'get_read_y_size' of 'panda3d.core.PNMImage' objects>"
        'get_red': None, # (!) real value is "<method 'get_red' of 'panda3d.core.PNMImage' objects>"
        'get_red_val': None, # (!) real value is "<method 'get_red_val' of 'panda3d.core.PNMImage' objects>"
        'get_xel': None, # (!) real value is "<method 'get_xel' of 'panda3d.core.PNMImage' objects>"
        'get_xel_a': None, # (!) real value is "<method 'get_xel_a' of 'panda3d.core.PNMImage' objects>"
        'get_xel_val': None, # (!) real value is "<method 'get_xel_val' of 'panda3d.core.PNMImage' objects>"
        'hasReadSize': None, # (!) real value is "<method 'hasReadSize' of 'panda3d.core.PNMImage' objects>"
        'has_read_size': None, # (!) real value is "<method 'has_read_size' of 'panda3d.core.PNMImage' objects>"
        'indirect1dLookup': None, # (!) real value is "<method 'indirect1dLookup' of 'panda3d.core.PNMImage' objects>"
        'indirect_1d_lookup': None, # (!) real value is "<method 'indirect_1d_lookup' of 'panda3d.core.PNMImage' objects>"
        'isValid': None, # (!) real value is "<method 'isValid' of 'panda3d.core.PNMImage' objects>"
        'is_valid': None, # (!) real value is "<method 'is_valid' of 'panda3d.core.PNMImage' objects>"
        'lightenSubImage': None, # (!) real value is "<method 'lightenSubImage' of 'panda3d.core.PNMImage' objects>"
        'lighten_sub_image': None, # (!) real value is "<method 'lighten_sub_image' of 'panda3d.core.PNMImage' objects>"
        'makeGrayscale': None, # (!) real value is "<method 'makeGrayscale' of 'panda3d.core.PNMImage' objects>"
        'makeHistogram': None, # (!) real value is "<method 'makeHistogram' of 'panda3d.core.PNMImage' objects>"
        'makeRgb': None, # (!) real value is "<method 'makeRgb' of 'panda3d.core.PNMImage' objects>"
        'make_grayscale': None, # (!) real value is "<method 'make_grayscale' of 'panda3d.core.PNMImage' objects>"
        'make_histogram': None, # (!) real value is "<method 'make_histogram' of 'panda3d.core.PNMImage' objects>"
        'make_rgb': None, # (!) real value is "<method 'make_rgb' of 'panda3d.core.PNMImage' objects>"
        'multSubImage': None, # (!) real value is "<method 'multSubImage' of 'panda3d.core.PNMImage' objects>"
        'mult_sub_image': None, # (!) real value is "<method 'mult_sub_image' of 'panda3d.core.PNMImage' objects>"
        'perlinNoiseFill': None, # (!) real value is "<method 'perlinNoiseFill' of 'panda3d.core.PNMImage' objects>"
        'perlin_noise_fill': None, # (!) real value is "<method 'perlin_noise_fill' of 'panda3d.core.PNMImage' objects>"
        'premultiplyAlpha': None, # (!) real value is "<method 'premultiplyAlpha' of 'panda3d.core.PNMImage' objects>"
        'premultiply_alpha': None, # (!) real value is "<method 'premultiply_alpha' of 'panda3d.core.PNMImage' objects>"
        'quantize': None, # (!) real value is "<method 'quantize' of 'panda3d.core.PNMImage' objects>"
        'quickFilterFrom': None, # (!) real value is "<method 'quickFilterFrom' of 'panda3d.core.PNMImage' objects>"
        'quick_filter_from': None, # (!) real value is "<method 'quick_filter_from' of 'panda3d.core.PNMImage' objects>"
        'read': None, # (!) real value is "<method 'read' of 'panda3d.core.PNMImage' objects>"
        'remixChannels': None, # (!) real value is "<method 'remixChannels' of 'panda3d.core.PNMImage' objects>"
        'remix_channels': None, # (!) real value is "<method 'remix_channels' of 'panda3d.core.PNMImage' objects>"
        'removeAlpha': None, # (!) real value is "<method 'removeAlpha' of 'panda3d.core.PNMImage' objects>"
        'remove_alpha': None, # (!) real value is "<method 'remove_alpha' of 'panda3d.core.PNMImage' objects>"
        'renderSpot': None, # (!) real value is "<method 'renderSpot' of 'panda3d.core.PNMImage' objects>"
        'render_spot': None, # (!) real value is "<method 'render_spot' of 'panda3d.core.PNMImage' objects>"
        'rescale': None, # (!) real value is "<method 'rescale' of 'panda3d.core.PNMImage' objects>"
        'reverseRows': None, # (!) real value is "<method 'reverseRows' of 'panda3d.core.PNMImage' objects>"
        'reverse_rows': None, # (!) real value is "<method 'reverse_rows' of 'panda3d.core.PNMImage' objects>"
        'setAlpha': None, # (!) real value is "<method 'setAlpha' of 'panda3d.core.PNMImage' objects>"
        'setAlphaVal': None, # (!) real value is "<method 'setAlphaVal' of 'panda3d.core.PNMImage' objects>"
        'setBlue': None, # (!) real value is "<method 'setBlue' of 'panda3d.core.PNMImage' objects>"
        'setBlueVal': None, # (!) real value is "<method 'setBlueVal' of 'panda3d.core.PNMImage' objects>"
        'setChannel': None, # (!) real value is "<method 'setChannel' of 'panda3d.core.PNMImage' objects>"
        'setChannelVal': None, # (!) real value is "<method 'setChannelVal' of 'panda3d.core.PNMImage' objects>"
        'setColorSpace': None, # (!) real value is "<method 'setColorSpace' of 'panda3d.core.PNMImage' objects>"
        'setColorType': None, # (!) real value is "<method 'setColorType' of 'panda3d.core.PNMImage' objects>"
        'setGray': None, # (!) real value is "<method 'setGray' of 'panda3d.core.PNMImage' objects>"
        'setGrayVal': None, # (!) real value is "<method 'setGrayVal' of 'panda3d.core.PNMImage' objects>"
        'setGreen': None, # (!) real value is "<method 'setGreen' of 'panda3d.core.PNMImage' objects>"
        'setGreenVal': None, # (!) real value is "<method 'setGreenVal' of 'panda3d.core.PNMImage' objects>"
        'setMaxval': None, # (!) real value is "<method 'setMaxval' of 'panda3d.core.PNMImage' objects>"
        'setNumChannels': None, # (!) real value is "<method 'setNumChannels' of 'panda3d.core.PNMImage' objects>"
        'setPixel': None, # (!) real value is "<method 'setPixel' of 'panda3d.core.PNMImage' objects>"
        'setReadSize': None, # (!) real value is "<method 'setReadSize' of 'panda3d.core.PNMImage' objects>"
        'setRed': None, # (!) real value is "<method 'setRed' of 'panda3d.core.PNMImage' objects>"
        'setRedVal': None, # (!) real value is "<method 'setRedVal' of 'panda3d.core.PNMImage' objects>"
        'setXel': None, # (!) real value is "<method 'setXel' of 'panda3d.core.PNMImage' objects>"
        'setXelA': None, # (!) real value is "<method 'setXelA' of 'panda3d.core.PNMImage' objects>"
        'setXelVal': None, # (!) real value is "<method 'setXelVal' of 'panda3d.core.PNMImage' objects>"
        'set_alpha': None, # (!) real value is "<method 'set_alpha' of 'panda3d.core.PNMImage' objects>"
        'set_alpha_val': None, # (!) real value is "<method 'set_alpha_val' of 'panda3d.core.PNMImage' objects>"
        'set_blue': None, # (!) real value is "<method 'set_blue' of 'panda3d.core.PNMImage' objects>"
        'set_blue_val': None, # (!) real value is "<method 'set_blue_val' of 'panda3d.core.PNMImage' objects>"
        'set_channel': None, # (!) real value is "<method 'set_channel' of 'panda3d.core.PNMImage' objects>"
        'set_channel_val': None, # (!) real value is "<method 'set_channel_val' of 'panda3d.core.PNMImage' objects>"
        'set_color_space': None, # (!) real value is "<method 'set_color_space' of 'panda3d.core.PNMImage' objects>"
        'set_color_type': None, # (!) real value is "<method 'set_color_type' of 'panda3d.core.PNMImage' objects>"
        'set_gray': None, # (!) real value is "<method 'set_gray' of 'panda3d.core.PNMImage' objects>"
        'set_gray_val': None, # (!) real value is "<method 'set_gray_val' of 'panda3d.core.PNMImage' objects>"
        'set_green': None, # (!) real value is "<method 'set_green' of 'panda3d.core.PNMImage' objects>"
        'set_green_val': None, # (!) real value is "<method 'set_green_val' of 'panda3d.core.PNMImage' objects>"
        'set_maxval': None, # (!) real value is "<method 'set_maxval' of 'panda3d.core.PNMImage' objects>"
        'set_num_channels': None, # (!) real value is "<method 'set_num_channels' of 'panda3d.core.PNMImage' objects>"
        'set_pixel': None, # (!) real value is "<method 'set_pixel' of 'panda3d.core.PNMImage' objects>"
        'set_read_size': None, # (!) real value is "<method 'set_read_size' of 'panda3d.core.PNMImage' objects>"
        'set_red': None, # (!) real value is "<method 'set_red' of 'panda3d.core.PNMImage' objects>"
        'set_red_val': None, # (!) real value is "<method 'set_red_val' of 'panda3d.core.PNMImage' objects>"
        'set_xel': None, # (!) real value is "<method 'set_xel' of 'panda3d.core.PNMImage' objects>"
        'set_xel_a': None, # (!) real value is "<method 'set_xel_a' of 'panda3d.core.PNMImage' objects>"
        'set_xel_val': None, # (!) real value is "<method 'set_xel_val' of 'panda3d.core.PNMImage' objects>"
        'takeFrom': None, # (!) real value is "<method 'takeFrom' of 'panda3d.core.PNMImage' objects>"
        'take_from': None, # (!) real value is "<method 'take_from' of 'panda3d.core.PNMImage' objects>"
        'threshold': None, # (!) real value is "<method 'threshold' of 'panda3d.core.PNMImage' objects>"
        'toAlphaVal': None, # (!) real value is "<method 'toAlphaVal' of 'panda3d.core.PNMImage' objects>"
        'toVal': None, # (!) real value is "<method 'toVal' of 'panda3d.core.PNMImage' objects>"
        'to_alpha_val': None, # (!) real value is "<method 'to_alpha_val' of 'panda3d.core.PNMImage' objects>"
        'to_val': None, # (!) real value is "<method 'to_val' of 'panda3d.core.PNMImage' objects>"
        'unfilteredStretchFrom': None, # (!) real value is "<method 'unfilteredStretchFrom' of 'panda3d.core.PNMImage' objects>"
        'unfiltered_stretch_from': None, # (!) real value is "<method 'unfiltered_stretch_from' of 'panda3d.core.PNMImage' objects>"
        'unpremultiplyAlpha': None, # (!) real value is "<method 'unpremultiplyAlpha' of 'panda3d.core.PNMImage' objects>"
        'unpremultiply_alpha': None, # (!) real value is "<method 'unpremultiply_alpha' of 'panda3d.core.PNMImage' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.PNMImage' objects>"
    }
    Row = None # (!) real value is "<class 'panda3d.core.Row'>"


