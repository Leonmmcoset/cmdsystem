# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .PNMImageHeader import PNMImageHeader

class PfmFile(PNMImageHeader):
    """
    /**
     * Defines a pfm file, a 2-d table of floating-point numbers, either
     * 3-component or 1-component, or with a special extension, 2- or 4-component.
     */
    """
    def addSubImage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_sub_image(const PfmFile self, const PfmFile copy, int xto, int yto, int xfrom, int yfrom, int x_size, int y_size, float pixel_scale)
        
        /**
         * Behaves like copy_sub_image(), except the copy pixels are added to the
         * pixels of the destination, after scaling by the specified pixel_scale.
         */
        """
        pass

    def add_sub_image(self, const_PfmFile_self, const_PfmFile_copy, int_xto, int_yto, int_xfrom, int_yfrom, int_x_size, int_y_size, float_pixel_scale): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_sub_image(const PfmFile self, const PfmFile copy, int xto, int yto, int xfrom, int yfrom, int x_size, int y_size, float pixel_scale)
        
        /**
         * Behaves like copy_sub_image(), except the copy pixels are added to the
         * pixels of the destination, after scaling by the specified pixel_scale.
         */
        """
        pass

    def apply1dLut(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        apply_1d_lut(const PfmFile self, int channel, const PfmFile lut, float x_scale)
        
        /**
         * Assumes that lut is an X by 1, 1-component PfmFile whose X axis maps points
         * to target points.  For each point in this pfm file, computes: p(u,
         * v)[channel] = lut(p(u, v)[channel] * x_scale, 0)[0]
         */
        """
        pass

    def applyCrop(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        apply_crop(const PfmFile self, int x_begin, int x_end, int y_begin, int y_end)
        
        /**
         * Reduces the PFM file to the cells in the rectangle bounded by (x_begin,
         * x_end, y_begin, y_end), where the _end cells are not included.
         */
        """
        pass

    def applyExponent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        apply_exponent(const PfmFile self, float gray_exponent)
        apply_exponent(const PfmFile self, float gray_exponent, float alpha_exponent)
        apply_exponent(const PfmFile self, float c0_exponent, float c1_exponent, float c2_exponent)
        apply_exponent(const PfmFile self, float c0_exponent, float c1_exponent, float c2_exponent, float c3_exponent)
        
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
         * value to the indicated exponent, such that L' = L ^ exponent.
         */
        """
        pass

    def applyMask(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        apply_mask(const PfmFile self, const PfmFile other)
        
        /**
         * Wherever there is missing data in the other PfmFile, set this the
         * corresponding point in this PfmFile to missing as well, so that this
         * PfmFile has only points where both files have points.
         *
         * The point is set to "missing" by setting it the no_data_value.
         */
        """
        pass

    def apply_1d_lut(self, const_PfmFile_self, int_channel, const_PfmFile_lut, float_x_scale): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        apply_1d_lut(const PfmFile self, int channel, const PfmFile lut, float x_scale)
        
        /**
         * Assumes that lut is an X by 1, 1-component PfmFile whose X axis maps points
         * to target points.  For each point in this pfm file, computes: p(u,
         * v)[channel] = lut(p(u, v)[channel] * x_scale, 0)[0]
         */
        """
        pass

    def apply_crop(self, const_PfmFile_self, int_x_begin, int_x_end, int_y_begin, int_y_end): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        apply_crop(const PfmFile self, int x_begin, int x_end, int y_begin, int y_end)
        
        /**
         * Reduces the PFM file to the cells in the rectangle bounded by (x_begin,
         * x_end, y_begin, y_end), where the _end cells are not included.
         */
        """
        pass

    def apply_exponent(self, const_PfmFile_self, float_gray_exponent): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        apply_exponent(const PfmFile self, float gray_exponent)
        apply_exponent(const PfmFile self, float gray_exponent, float alpha_exponent)
        apply_exponent(const PfmFile self, float c0_exponent, float c1_exponent, float c2_exponent)
        apply_exponent(const PfmFile self, float c0_exponent, float c1_exponent, float c2_exponent, float c3_exponent)
        
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
         * value to the indicated exponent, such that L' = L ^ exponent.
         */
        """
        pass

    def apply_mask(self, const_PfmFile_self, const_PfmFile_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        apply_mask(const PfmFile self, const PfmFile other)
        
        /**
         * Wherever there is missing data in the other PfmFile, set this the
         * corresponding point in this PfmFile to missing as well, so that this
         * PfmFile has only points where both files have points.
         *
         * The point is set to "missing" by setting it the no_data_value.
         */
        """
        pass

    def assign(self, const_PfmFile_self, const_PfmFile_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const PfmFile self, const PfmFile copy)
        """
        pass

    def boxFilterFrom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        box_filter_from(const PfmFile self, float radius, const PfmFile copy)
        
        /**
         * Makes a resized copy of the indicated image into this one using the
         * indicated filter.  The image to be copied is squashed and stretched to
         * match the dimensions of the current image, applying the appropriate filter
         * to perform the stretching.
         */
        """
        pass

    def box_filter_from(self, const_PfmFile_self, float_radius, const_PfmFile_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        box_filter_from(const PfmFile self, float radius, const PfmFile copy)
        
        /**
         * Makes a resized copy of the indicated image into this one using the
         * indicated filter.  The image to be copied is squashed and stretched to
         * match the dimensions of the current image, applying the appropriate filter
         * to perform the stretching.
         */
        """
        pass

    def calcAutocrop(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        calc_autocrop(PfmFile self, LVecBase4f range)
        calc_autocrop(PfmFile self, LVecBase4d range)
        
        /**
         * Computes the minimum range of x and y across the PFM file that include all
         * points.  If there are no points with no_data_value in the grid--that is,
         * all points are included--then this will return (0, get_x_size(), 0,
         * get_y_size()).
         */
        
        /**
         * Computes the minimum range of x and y across the PFM file that include all
         * points.  If there are no points with no_data_value in the grid--that is,
         * all points are included--then this will return (0, get_x_size(), 0,
         * get_y_size()).
         */
        
        /**
         * Computes the minimum range of x and y across the PFM file that include all
         * points.  If there are no points with no_data_value in the grid--that is,
         * all points are included--then this will return (0, get_x_size(), 0,
         * get_y_size()).
         */
        """
        pass

    def calcAveragePoint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        calc_average_point(PfmFile self, LPoint3f result, float x, float y, float radius)
        
        /**
         * Computes the unweighted average point of all points within the box centered
         * at (x, y) with the indicated Manhattan-distance radius.  Missing points are
         * assigned the value of their nearest neighbor.  Returns true if successful,
         * or false if the point value cannot be determined.
         */
        """
        pass

    def calcBilinearPoint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        calc_bilinear_point(PfmFile self, LPoint3f result, float x, float y)
        
        /**
         * Computes the weighted average of the four nearest points to the floating-
         * point index (x, y).  Returns true if the point has any contributors, false
         * if the point is unknown.
         */
        """
        pass

    def calcMinMax(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        calc_min_max(PfmFile self, LVecBase3f min_points, LVecBase3f max_points)
        
        /**
         * Calculates the minimum and maximum x, y, and z depth component values,
         * representing the bounding box of depth values, and places them in the
         * indicated vectors.  Returns true if successful, false if the mesh contains
         * no points.
         */
        """
        pass

    def calcTightBounds(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        calc_tight_bounds(PfmFile self, LPoint3f min_point, LPoint3f max_point)
        
        /**
         * Calculates the minimum and maximum vertices of all points within the table.
         * Assumes the table contains 3-D points.
         *
         * The return value is true if any points in the table, or false if none are.
         */
        """
        pass

    def calc_autocrop(self, PfmFile_self, LVecBase4f_range): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        calc_autocrop(PfmFile self, LVecBase4f range)
        calc_autocrop(PfmFile self, LVecBase4d range)
        
        /**
         * Computes the minimum range of x and y across the PFM file that include all
         * points.  If there are no points with no_data_value in the grid--that is,
         * all points are included--then this will return (0, get_x_size(), 0,
         * get_y_size()).
         */
        
        /**
         * Computes the minimum range of x and y across the PFM file that include all
         * points.  If there are no points with no_data_value in the grid--that is,
         * all points are included--then this will return (0, get_x_size(), 0,
         * get_y_size()).
         */
        
        /**
         * Computes the minimum range of x and y across the PFM file that include all
         * points.  If there are no points with no_data_value in the grid--that is,
         * all points are included--then this will return (0, get_x_size(), 0,
         * get_y_size()).
         */
        """
        pass

    def calc_average_point(self, PfmFile_self, LPoint3f_result, float_x, float_y, float_radius): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        calc_average_point(PfmFile self, LPoint3f result, float x, float y, float radius)
        
        /**
         * Computes the unweighted average point of all points within the box centered
         * at (x, y) with the indicated Manhattan-distance radius.  Missing points are
         * assigned the value of their nearest neighbor.  Returns true if successful,
         * or false if the point value cannot be determined.
         */
        """
        pass

    def calc_bilinear_point(self, PfmFile_self, LPoint3f_result, float_x, float_y): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        calc_bilinear_point(PfmFile self, LPoint3f result, float x, float y)
        
        /**
         * Computes the weighted average of the four nearest points to the floating-
         * point index (x, y).  Returns true if the point has any contributors, false
         * if the point is unknown.
         */
        """
        pass

    def calc_min_max(self, PfmFile_self, LVecBase3f_min_points, LVecBase3f_max_points): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        calc_min_max(PfmFile self, LVecBase3f min_points, LVecBase3f max_points)
        
        /**
         * Calculates the minimum and maximum x, y, and z depth component values,
         * representing the bounding box of depth values, and places them in the
         * indicated vectors.  Returns true if successful, false if the mesh contains
         * no points.
         */
        """
        pass

    def calc_tight_bounds(self, PfmFile_self, LPoint3f_min_point, LPoint3f_max_point): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        calc_tight_bounds(PfmFile self, LPoint3f min_point, LPoint3f max_point)
        
        /**
         * Calculates the minimum and maximum vertices of all points within the table.
         * Assumes the table contains 3-D points.
         *
         * The return value is true if any points in the table, or false if none are.
         */
        """
        pass

    def clear(self, const_PfmFile_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear(const PfmFile self)
        clear(const PfmFile self, int x_size, int y_size, int num_channels)
        
        /**
         * Eliminates all data in the file.
         */
        
        /**
         * Resets to an empty table with a specific size.  The case of num_channels ==
         * 0 is allowed only in the case that x_size and y_size are also == 0; and
         * this makes an empty (and invalid) PfmFile.
         */
        """
        pass

    def clearNoDataValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_no_data_value(const PfmFile self)
        
        /**
         * Removes the special value that means "no data" when it appears in the pfm
         * file.  All points will thus be considered valid.
         */
        """
        pass

    def clearToTexcoords(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_to_texcoords(const PfmFile self, int x_size, int y_size)
        
        /**
         * Replaces this PfmFile with a new PfmFile of size x_size x y_size x 3,
         * containing the x y 0 values in the range 0 .. 1 according to the x y index.
         */
        """
        pass

    def clear_no_data_value(self, const_PfmFile_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_no_data_value(const PfmFile self)
        
        /**
         * Removes the special value that means "no data" when it appears in the pfm
         * file.  All points will thus be considered valid.
         */
        """
        pass

    def clear_to_texcoords(self, const_PfmFile_self, int_x_size, int_y_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_to_texcoords(const PfmFile self, int x_size, int y_size)
        
        /**
         * Replaces this PfmFile with a new PfmFile of size x_size x y_size x 3,
         * containing the x y 0 values in the range 0 .. 1 according to the x y index.
         */
        """
        pass

    def computePlanarBounds(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        compute_planar_bounds(PfmFile self, const LPoint2f center, float point_dist, float sample_radius, bool points_only)
        compute_planar_bounds(PfmFile self, const LPoint2d center, float point_dist, float sample_radius, bool points_only)
        
        /**
         * Computes the minmax bounding volume of the points in 3-D space, assuming
         * the points represent a mostly-planar surface.
         *
         * This algorithm works by sampling the (square) sample_radius pixels at the
         * four point_dist corners around the center (cx - pd, cx + pd) and so on, to
         * approximate the plane of the surface.  Then all of the points are projected
         * into that plane and the bounding volume of the entire mesh within that
         * plane is determined.  If points_only is true, the bounding volume of only
         * those four points is determined.
         *
         * center, point_dist and sample_radius are in UV space, i.e.  in the range
         * 0..1.
         */
        
        /**
         * Computes the minmax bounding volume of the points in 3-D space, assuming
         * the points represent a mostly-planar surface.
         *
         * This algorithm works by sampling the (square) sample_radius pixels at the
         * four point_dist corners around the center (cx - pd, cx + pd) and so on, to
         * approximate the plane of the surface.  Then all of the points are projected
         * into that plane and the bounding volume of the entire mesh within that
         * plane is determined.  If points_only is true, the bounding volume of only
         * those four points is determined.
         *
         * center, point_dist and sample_radius are in UV space, i.e.  in the range
         * 0..1.
         */
        """
        pass

    def computeSamplePoint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        compute_sample_point(PfmFile self, LPoint3f result, float x, float y, float sample_radius)
        
        /**
         * Computes the average of all the point within sample_radius (manhattan
         * distance) and the indicated point.
         *
         * The point coordinates are given in UV space, in the range 0..1.
         */
        """
        pass

    def compute_planar_bounds(self, PfmFile_self, const_LPoint2f_center, float_point_dist, float_sample_radius, bool_points_only): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        compute_planar_bounds(PfmFile self, const LPoint2f center, float point_dist, float sample_radius, bool points_only)
        compute_planar_bounds(PfmFile self, const LPoint2d center, float point_dist, float sample_radius, bool points_only)
        
        /**
         * Computes the minmax bounding volume of the points in 3-D space, assuming
         * the points represent a mostly-planar surface.
         *
         * This algorithm works by sampling the (square) sample_radius pixels at the
         * four point_dist corners around the center (cx - pd, cx + pd) and so on, to
         * approximate the plane of the surface.  Then all of the points are projected
         * into that plane and the bounding volume of the entire mesh within that
         * plane is determined.  If points_only is true, the bounding volume of only
         * those four points is determined.
         *
         * center, point_dist and sample_radius are in UV space, i.e.  in the range
         * 0..1.
         */
        
        /**
         * Computes the minmax bounding volume of the points in 3-D space, assuming
         * the points represent a mostly-planar surface.
         *
         * This algorithm works by sampling the (square) sample_radius pixels at the
         * four point_dist corners around the center (cx - pd, cx + pd) and so on, to
         * approximate the plane of the surface.  Then all of the points are projected
         * into that plane and the bounding volume of the entire mesh within that
         * plane is determined.  If points_only is true, the bounding volume of only
         * those four points is determined.
         *
         * center, point_dist and sample_radius are in UV space, i.e.  in the range
         * 0..1.
         */
        """
        pass

    def compute_sample_point(self, PfmFile_self, LPoint3f_result, float_x, float_y, float_sample_radius): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        compute_sample_point(PfmFile self, LPoint3f result, float x, float y, float sample_radius)
        
        /**
         * Computes the average of all the point within sample_radius (manhattan
         * distance) and the indicated point.
         *
         * The point coordinates are given in UV space, in the range 0..1.
         */
        """
        pass

    def copyChannel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        copy_channel(const PfmFile self, int to_channel, const PfmFile other, int from_channel)
        
        /**
         * Copies just the specified channel values from the indicated PfmFile (which
         * could be same as this PfmFile) into the specified channel of this one.
         */
        """
        pass

    def copyChannelMasked(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        copy_channel_masked(const PfmFile self, int to_channel, const PfmFile other, int from_channel)
        
        /**
         * Copies just the specified channel values from the indicated PfmFile, but
         * only where the other file has a data point.
         */
        """
        pass

    def copySubImage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        copy_sub_image(const PfmFile self, const PfmFile copy, int xto, int yto, int xfrom, int yfrom, int x_size, int y_size)
        
        /**
         * Copies a rectangular area of another image into a rectangular area of this
         * image.  Both images must already have been initialized.  The upper-left
         * corner of the region in both images is specified, and the size of the area;
         * if the size is omitted, it defaults to the entire other image, or the
         * largest piece that will fit.
         */
        """
        pass

    def copy_channel(self, const_PfmFile_self, int_to_channel, const_PfmFile_other, int_from_channel): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        copy_channel(const PfmFile self, int to_channel, const PfmFile other, int from_channel)
        
        /**
         * Copies just the specified channel values from the indicated PfmFile (which
         * could be same as this PfmFile) into the specified channel of this one.
         */
        """
        pass

    def copy_channel_masked(self, const_PfmFile_self, int_to_channel, const_PfmFile_other, int_from_channel): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        copy_channel_masked(const PfmFile self, int to_channel, const PfmFile other, int from_channel)
        
        /**
         * Copies just the specified channel values from the indicated PfmFile, but
         * only where the other file has a data point.
         */
        """
        pass

    def copy_sub_image(self, const_PfmFile_self, const_PfmFile_copy, int_xto, int_yto, int_xfrom, int_yfrom, int_x_size, int_y_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        copy_sub_image(const PfmFile self, const PfmFile copy, int xto, int yto, int xfrom, int yfrom, int x_size, int y_size)
        
        /**
         * Copies a rectangular area of another image into a rectangular area of this
         * image.  Both images must already have been initialized.  The upper-left
         * corner of the region in both images is specified, and the size of the area;
         * if the size is omitted, it defaults to the entire other image, or the
         * largest piece that will fit.
         */
        """
        pass

    def divideSubImage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        divide_sub_image(const PfmFile self, const PfmFile copy, int xto, int yto, int xfrom, int yfrom, int x_size, int y_size, float pixel_scale)
        
        /**
         * Behaves like copy_sub_image(), except the copy pixels are divided into the
         * pixels of the destination, after scaling by the specified pixel_scale.
         * dest(x, y) = dest(x, y) / (copy(x, y) * pixel_scale).
         */
        """
        pass

    def divide_sub_image(self, const_PfmFile_self, const_PfmFile_copy, int_xto, int_yto, int_xfrom, int_yfrom, int_x_size, int_y_size, float_pixel_scale): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        divide_sub_image(const PfmFile self, const PfmFile copy, int xto, int yto, int xfrom, int yfrom, int x_size, int y_size, float pixel_scale)
        
        /**
         * Behaves like copy_sub_image(), except the copy pixels are divided into the
         * pixels of the destination, after scaling by the specified pixel_scale.
         * dest(x, y) = dest(x, y) / (copy(x, y) * pixel_scale).
         */
        """
        pass

    def fill(self, const_PfmFile_self, const_LPoint4f_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        fill(const PfmFile self, const LPoint4f value)
        fill(const PfmFile self, const LPoint2f value)
        fill(const PfmFile self, const LPoint3f value)
        fill(const PfmFile self, float value)
        
        /**
         * Fills the table with all of the same value.
         */
        
        /**
         * Fills the table with all of the same value.
         */
        
        /**
         * Fills the table with all of the same value.
         */
        
        /**
         * Fills the table with all of the same value.
         */
        """
        pass

    def fillChannel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        fill_channel(const PfmFile self, int channel, float value)
        
        /**
         * Fills the indicated channel with all of the same value, leaving the other
         * channels unchanged.
         */
        """
        pass

    def fillChannelMasked(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        fill_channel_masked(const PfmFile self, int channel, float value)
        
        /**
         * Fills the indicated channel with all of the same value, but only where the
         * table already has a data point.  Leaves empty points unchanged.
         */
        """
        pass

    def fillChannelMaskedNan(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        fill_channel_masked_nan(const PfmFile self, int channel)
        
        /**
         * Fills the indicated channel with NaN, but only where the table already has
         * a data point.  Leaves empty points unchanged.
         */
        """
        pass

    def fillChannelNan(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        fill_channel_nan(const PfmFile self, int channel)
        
        /**
         * Fills the indicated channel with NaN, leaving the other channels unchanged.
         */
        """
        pass

    def fillNan(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        fill_nan(const PfmFile self)
        
        /**
         * Fills the table with all NaN.
         */
        """
        pass

    def fillNoDataValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        fill_no_data_value(const PfmFile self)
        
        /**
         * Fills the table with the current no_data value, so that the table is empty.
         */
        """
        pass

    def fill_channel(self, const_PfmFile_self, int_channel, float_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        fill_channel(const PfmFile self, int channel, float value)
        
        /**
         * Fills the indicated channel with all of the same value, leaving the other
         * channels unchanged.
         */
        """
        pass

    def fill_channel_masked(self, const_PfmFile_self, int_channel, float_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        fill_channel_masked(const PfmFile self, int channel, float value)
        
        /**
         * Fills the indicated channel with all of the same value, but only where the
         * table already has a data point.  Leaves empty points unchanged.
         */
        """
        pass

    def fill_channel_masked_nan(self, const_PfmFile_self, int_channel): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        fill_channel_masked_nan(const PfmFile self, int channel)
        
        /**
         * Fills the indicated channel with NaN, but only where the table already has
         * a data point.  Leaves empty points unchanged.
         */
        """
        pass

    def fill_channel_nan(self, const_PfmFile_self, int_channel): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        fill_channel_nan(const PfmFile self, int channel)
        
        /**
         * Fills the indicated channel with NaN, leaving the other channels unchanged.
         */
        """
        pass

    def fill_nan(self, const_PfmFile_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        fill_nan(const PfmFile self)
        
        /**
         * Fills the table with all NaN.
         */
        """
        pass

    def fill_no_data_value(self, const_PfmFile_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        fill_no_data_value(const PfmFile self)
        
        /**
         * Fills the table with the current no_data value, so that the table is empty.
         */
        """
        pass

    def flip(self, const_PfmFile_self, bool_flip_x, bool_flip_y, bool_transpose): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        flip(const PfmFile self, bool flip_x, bool flip_y, bool transpose)
        
        /**
         * Reverses, transposes, and/or rotates the table in-place according to the
         * specified parameters.  If flip_x is true, the x axis is reversed; if flip_y
         * is true, the y axis is reversed.  Then, if transpose is true, the x and y
         * axes are exchanged.  These parameters can be used to select any combination
         * of 90-degree or 180-degree rotations and flips.
         */
        """
        pass

    def forwardDistort(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        forward_distort(const PfmFile self, const PfmFile dist, float scale_factor)
        
        /**
         * Applies the distortion indicated in the supplied dist map to the current
         * map.  The dist map is understood to be a mapping of points in the range
         * 0..1 in the first two dimensions.
         *
         * The operation can be expressed symbolically as:
         *
         * this(u, v) = this(dist(u, v))
         *
         * If scale_factor is not 1, it should be a value > 1, and it specifies the
         * factor to upscale the working table while processing, to reduce artifacts
         * from integer truncation.
         *
         * By convention, the y axis is inverted in the distortion map relative to the
         * coordinates here.  A y value of 0 in the distortion map corresponds with a
         * v value of 1 in this file.
         */
        """
        pass

    def forward_distort(self, const_PfmFile_self, const_PfmFile_dist, float_scale_factor): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        forward_distort(const PfmFile self, const PfmFile dist, float scale_factor)
        
        /**
         * Applies the distortion indicated in the supplied dist map to the current
         * map.  The dist map is understood to be a mapping of points in the range
         * 0..1 in the first two dimensions.
         *
         * The operation can be expressed symbolically as:
         *
         * this(u, v) = this(dist(u, v))
         *
         * If scale_factor is not 1, it should be a value > 1, and it specifies the
         * factor to upscale the working table while processing, to reduce artifacts
         * from integer truncation.
         *
         * By convention, the y axis is inverted in the distortion map relative to the
         * coordinates here.  A y value of 0 in the distortion map corresponds with a
         * v value of 1 in this file.
         */
        """
        pass

    def gammaCorrect(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        gamma_correct(const PfmFile self, float from_gamma, float to_gamma)
        
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
        gamma_correct_alpha(const PfmFile self, float from_gamma, float to_gamma)
        
        /**
         * Assuming the image was constructed with a gamma curve of from_gamma in the
         * alpha channel, converts it to an image with a gamma curve of to_gamma in
         * the alpha channel.  Does not affect the RGB channels.
         */
        """
        pass

    def gamma_correct(self, const_PfmFile_self, float_from_gamma, float_to_gamma): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        gamma_correct(const PfmFile self, float from_gamma, float to_gamma)
        
        /**
         * Assuming the image was constructed with a gamma curve of from_gamma in the
         * RGB channels, converts it to an image with a gamma curve of to_gamma in the
         * RGB channels.  Does not affect the alpha channel.
         */
        """
        pass

    def gamma_correct_alpha(self, const_PfmFile_self, float_from_gamma, float_to_gamma): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        gamma_correct_alpha(const PfmFile self, float from_gamma, float to_gamma)
        
        /**
         * Assuming the image was constructed with a gamma curve of from_gamma in the
         * alpha channel, converts it to an image with a gamma curve of to_gamma in
         * the alpha channel.  Does not affect the RGB channels.
         */
        """
        pass

    def gaussianFilterFrom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        gaussian_filter_from(const PfmFile self, float radius, const PfmFile copy)
        
        /**
         * Makes a resized copy of the indicated image into this one using the
         * indicated filter.  The image to be copied is squashed and stretched to
         * match the dimensions of the current image, applying the appropriate filter
         * to perform the stretching.
         */
        """
        pass

    def gaussian_filter_from(self, const_PfmFile_self, float_radius, const_PfmFile_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        gaussian_filter_from(const PfmFile self, float radius, const PfmFile copy)
        
        /**
         * Makes a resized copy of the indicated image into this one using the
         * indicated filter.  The image to be copied is squashed and stretched to
         * match the dimensions of the current image, applying the appropriate filter
         * to perform the stretching.
         */
        """
        pass

    def getChannel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_channel(PfmFile self, int x, int y, int c)
        
        /**
         * Returns the cth channel of the point value at the indicated point.
         */
        """
        pass

    def getNoDataValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_no_data_value(PfmFile self)
        
        /**
         * If has_no_data_value() returns true, this returns the particular "no data"
         * value.
         */
        """
        pass

    def getPoint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_point(PfmFile self, int x, int y)
        
        /**
         * Returns the 3-component point value at the indicated point.  In a 1-channel
         * image, the channel value is in the x component.
         */
        """
        pass

    def getPoint1(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_point1(PfmFile self, int x, int y)
        
        /**
         * Returns the 1-component point value at the indicated point.
         */
        """
        pass

    def getPoint2(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_point2(PfmFile self, int x, int y)
        
        /**
         * Returns the 2-component point value at the indicated point.  In a 1-channel
         * image, the channel value is in the x component.
         */
        """
        pass

    def getPoint3(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_point3(PfmFile self, int x, int y)
        
        /**
         * Returns the 3-component point value at the indicated point.  In a 1-channel
         * image, the channel value is in the x component.
         */
        """
        pass

    def getPoint4(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_point4(PfmFile self, int x, int y)
        
        /**
         * Returns the 4-component point value at the indicated point.  In a 1-channel
         * image, the channel value is in the x component.
         */
        """
        pass

    def getPoints(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_points(PfmFile self)
        """
        pass

    def getScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_scale(PfmFile self)
        
        /**
         * The "scale" is reported in the pfm header and is probably meaningless.
         */
        """
        pass

    def get_channel(self, PfmFile_self, int_x, int_y, int_c): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_channel(PfmFile self, int x, int y, int c)
        
        /**
         * Returns the cth channel of the point value at the indicated point.
         */
        """
        pass

    def get_no_data_value(self, PfmFile_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_no_data_value(PfmFile self)
        
        /**
         * If has_no_data_value() returns true, this returns the particular "no data"
         * value.
         */
        """
        pass

    def get_point(self, PfmFile_self, int_x, int_y): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_point(PfmFile self, int x, int y)
        
        /**
         * Returns the 3-component point value at the indicated point.  In a 1-channel
         * image, the channel value is in the x component.
         */
        """
        pass

    def get_point1(self, PfmFile_self, int_x, int_y): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_point1(PfmFile self, int x, int y)
        
        /**
         * Returns the 1-component point value at the indicated point.
         */
        """
        pass

    def get_point2(self, PfmFile_self, int_x, int_y): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_point2(PfmFile self, int x, int y)
        
        /**
         * Returns the 2-component point value at the indicated point.  In a 1-channel
         * image, the channel value is in the x component.
         */
        """
        pass

    def get_point3(self, PfmFile_self, int_x, int_y): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_point3(PfmFile self, int x, int y)
        
        /**
         * Returns the 3-component point value at the indicated point.  In a 1-channel
         * image, the channel value is in the x component.
         */
        """
        pass

    def get_point4(self, PfmFile_self, int_x, int_y): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_point4(PfmFile self, int x, int y)
        
        /**
         * Returns the 4-component point value at the indicated point.  In a 1-channel
         * image, the channel value is in the x component.
         */
        """
        pass

    def get_points(self, PfmFile_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_points(PfmFile self)
        """
        pass

    def get_scale(self, PfmFile_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_scale(PfmFile self)
        
        /**
         * The "scale" is reported in the pfm header and is probably meaningless.
         */
        """
        pass

    def hasNoDataThreshold(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_no_data_threshold(PfmFile self)
        
        /**
         * Returns whether a "no data" threshold value has been established by
         * set_no_data_threshold().
         */
        """
        pass

    def hasNoDataValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_no_data_value(PfmFile self)
        
        /**
         * Returns whether a "no data" value has been established by
         * set_no_data_value().
         */
        """
        pass

    def hasPoint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_point(PfmFile self, int x, int y)
        
        /**
         * Returns true if there is a valid point at x, y.  This always returns true
         * unless a "no data" value has been set, in which case it returns false if
         * the point at x, y is the "no data" value.
         */
        """
        pass

    def has_no_data_threshold(self, PfmFile_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_no_data_threshold(PfmFile self)
        
        /**
         * Returns whether a "no data" threshold value has been established by
         * set_no_data_threshold().
         */
        """
        pass

    def has_no_data_value(self, PfmFile_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_no_data_value(PfmFile self)
        
        /**
         * Returns whether a "no data" value has been established by
         * set_no_data_value().
         */
        """
        pass

    def has_point(self, PfmFile_self, int_x, int_y): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_point(PfmFile self, int x, int y)
        
        /**
         * Returns true if there is a valid point at x, y.  This always returns true
         * unless a "no data" value has been set, in which case it returns false if
         * the point at x, y is the "no data" value.
         */
        """
        pass

    def indirect1dLookup(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        indirect_1d_lookup(const PfmFile self, const PfmFile index_image, int channel, const PfmFile pixel_values)
        
        /**
         * index_image is a WxH 1-channel image, while pixel_values is an Nx1
         * image with any number of channels.  Typically pixel_values will be
         * a 256x1 image.
         *
         * Fills the PfmFile with a new image the same width and height as
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

    def indirect_1d_lookup(self, const_PfmFile_self, const_PfmFile_index_image, int_channel, const_PfmFile_pixel_values): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        indirect_1d_lookup(const PfmFile self, const PfmFile index_image, int channel, const PfmFile pixel_values)
        
        /**
         * index_image is a WxH 1-channel image, while pixel_values is an Nx1
         * image with any number of channels.  Typically pixel_values will be
         * a 256x1 image.
         *
         * Fills the PfmFile with a new image the same width and height as
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

    def isColumnEmpty(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_column_empty(PfmFile self, int x, int y_begin, int y_end)
        
        /**
         * Returns true if all of the points on column x, from [y_begin, y_end), are
         * the no_data value, or false if any one of these points has a value.
         */
        """
        pass

    def isRowEmpty(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_row_empty(PfmFile self, int y, int x_begin, int x_end)
        
        /**
         * Returns true if all of the points on row y, in the range [x_begin, x_end),
         * are the no_data value, or false if any one of these points has a value.
         */
        """
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_valid(PfmFile self)
        
        /**
         *
         */
        """
        pass

    def is_column_empty(self, PfmFile_self, int_x, int_y_begin, int_y_end): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_column_empty(PfmFile self, int x, int y_begin, int y_end)
        
        /**
         * Returns true if all of the points on column x, from [y_begin, y_end), are
         * the no_data value, or false if any one of these points has a value.
         */
        """
        pass

    def is_row_empty(self, PfmFile_self, int_y, int_x_begin, int_x_end): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_row_empty(PfmFile self, int y, int x_begin, int x_end)
        
        /**
         * Returns true if all of the points on row y, in the range [x_begin, x_end),
         * are the no_data value, or false if any one of these points has a value.
         */
        """
        pass

    def is_valid(self, PfmFile_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_valid(PfmFile self)
        
        /**
         *
         */
        """
        pass

    def load(self, const_PfmFile_self, const_PNMImage_pnmimage): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        load(const PfmFile self, const PNMImage pnmimage)
        
        /**
         * Fills the PfmFile with the data from the indicated PNMImage, converted to
         * floating-point values.
         */
        """
        pass

    def merge(self, const_PfmFile_self, const_PfmFile_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        merge(const PfmFile self, const PfmFile other)
        
        /**
         * Wherever there is missing data in this PfmFile (that is, wherever
         * has_point() returns false), copy data from the other PfmFile, which must be
         * exactly the same dimensions as this one.
         */
        """
        pass

    def modifyPoint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        modify_point(const PfmFile self, int x, int y)
        
        /**
         * Returns a modifiable 3-component point value at the indicated point.
         */
        """
        pass

    def modifyPoint2(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        modify_point2(const PfmFile self, int x, int y)
        
        /**
         * Returns a modifiable 2-component point value at the indicated point.
         */
        """
        pass

    def modifyPoint3(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        modify_point3(const PfmFile self, int x, int y)
        
        /**
         * Returns a modifiable 3-component point value at the indicated point.
         */
        """
        pass

    def modifyPoint4(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        modify_point4(const PfmFile self, int x, int y)
        
        /**
         * Returns a modifiable 4-component point value at the indicated point.
         */
        """
        pass

    def modify_point(self, const_PfmFile_self, int_x, int_y): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        modify_point(const PfmFile self, int x, int y)
        
        /**
         * Returns a modifiable 3-component point value at the indicated point.
         */
        """
        pass

    def modify_point2(self, const_PfmFile_self, int_x, int_y): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        modify_point2(const PfmFile self, int x, int y)
        
        /**
         * Returns a modifiable 2-component point value at the indicated point.
         */
        """
        pass

    def modify_point3(self, const_PfmFile_self, int_x, int_y): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        modify_point3(const PfmFile self, int x, int y)
        
        /**
         * Returns a modifiable 3-component point value at the indicated point.
         */
        """
        pass

    def modify_point4(self, const_PfmFile_self, int_x, int_y): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        modify_point4(const PfmFile self, int x, int y)
        
        /**
         * Returns a modifiable 4-component point value at the indicated point.
         */
        """
        pass

    def multSubImage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        mult_sub_image(const PfmFile self, const PfmFile copy, int xto, int yto, int xfrom, int yfrom, int x_size, int y_size, float pixel_scale)
        
        /**
         * Behaves like copy_sub_image(), except the copy pixels are multiplied to the
         * pixels of the destination, after scaling by the specified pixel_scale.
         */
        """
        pass

    def mult_sub_image(self, const_PfmFile_self, const_PfmFile_copy, int_xto, int_yto, int_xfrom, int_yfrom, int_x_size, int_y_size, float_pixel_scale): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        mult_sub_image(const PfmFile self, const PfmFile copy, int xto, int yto, int xfrom, int yfrom, int x_size, int y_size, float pixel_scale)
        
        /**
         * Behaves like copy_sub_image(), except the copy pixels are multiplied to the
         * pixels of the destination, after scaling by the specified pixel_scale.
         */
        """
        pass

    def output(self, PfmFile_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(PfmFile self, ostream out)
        
        /**
         *
         */
        """
        pass

    def pullSpot(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        pull_spot(const PfmFile self, const LPoint4f delta, float xc, float yc, float xr, float yr, float exponent)
        
        /**
         * Applies delta * t to the point values within radius (xr, yr) distance of
         * (xc, yc).  The t value is scaled from 1.0 at the center to 0.0 at radius
         * (xr, yr), and this scale follows the specified exponent.  Returns the
         * number of points affected.
         */
        """
        pass

    def pull_spot(self, const_PfmFile_self, const_LPoint4f_delta, float_xc, float_yc, float_xr, float_yr, float_exponent): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        pull_spot(const PfmFile self, const LPoint4f delta, float xc, float yc, float xr, float yr, float exponent)
        
        /**
         * Applies delta * t to the point values within radius (xr, yr) distance of
         * (xc, yc).  The t value is scaled from 1.0 at the center to 0.0 at radius
         * (xr, yr), and this scale follows the specified exponent.  Returns the
         * number of points affected.
         */
        """
        pass

    def quickFilterFrom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        quick_filter_from(const PfmFile self, const PfmFile copy)
        
        /**
         * Resizes from the given image, with a fixed radius of 0.5. This is a very
         * specialized and simple algorithm that doesn't handle dropping below the
         * Nyquist rate very well, but is quite a bit faster than the more general
         * box_filter(), above.
         */
        """
        pass

    def quick_filter_from(self, const_PfmFile_self, const_PfmFile_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        quick_filter_from(const PfmFile self, const PfmFile copy)
        
        /**
         * Resizes from the given image, with a fixed radius of 0.5. This is a very
         * specialized and simple algorithm that doesn't handle dropping below the
         * Nyquist rate very well, but is quite a bit faster than the more general
         * box_filter(), above.
         */
        """
        pass

    def read(self, const_PfmFile_self, istream_in, const_Filename_fullpath): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        read(const PfmFile self, istream in, const Filename fullpath)
        read(const PfmFile self, const Filename fullpath)
        
        /**
         * Reads the PFM data from the indicated file, returning true on success,
         * false on failure.
         *
         * This can also handle reading a standard image file supported by PNMImage;
         * it will be quietly converted to a floating-point type.
         */
        
        /**
         * Reads the PFM data from the indicated stream, returning true on success,
         * false on failure.
         *
         * This can also handle reading a standard image file supported by PNMImage;
         * it will be quietly converted to a floating-point type.
         */
        
        /**
         * Reads the PFM data using the indicated PNMReader.
         *
         * The PNMReader is always deleted upon completion, whether successful or not.
         */
        """
        pass

    def resize(self, const_PfmFile_self, int_new_x_size, int_new_y_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        resize(const PfmFile self, int new_x_size, int new_y_size)
        
        /**
         * Applies a simple filter to resample the pfm file in-place to the indicated
         * size.  Don't confuse this with applying a scale to all of the points via
         * xform().
         */
        """
        pass

    def reverseDistort(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        reverse_distort(const PfmFile self, const PfmFile dist, float scale_factor)
        
        /**
         * Applies the distortion indicated in the supplied dist map to the current
         * map.  The dist map is understood to be a mapping of points in the range
         * 0..1 in the first two dimensions.
         *
         * The operation can be expressed symbolically as:
         *
         * this(u, v) = dist(this(u, v))
         *
         * If scale_factor is not 1, it should be a value > 1, and it specifies the
         * factor to upscale the working table while processing, to reduce artifacts
         * from integer truncation.
         *
         * By convention, the y axis in inverted in the distortion map relative to the
         * coordinates here.  A y value of 0 in the distortion map corresponds with a
         * v value of 1 in this file.
         */
        """
        pass

    def reverseRows(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        reverse_rows(const PfmFile self)
        
        /**
         * Performs an in-place reversal of the row (y) data.
         */
        """
        pass

    def reverse_distort(self, const_PfmFile_self, const_PfmFile_dist, float_scale_factor): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        reverse_distort(const PfmFile self, const PfmFile dist, float scale_factor)
        
        /**
         * Applies the distortion indicated in the supplied dist map to the current
         * map.  The dist map is understood to be a mapping of points in the range
         * 0..1 in the first two dimensions.
         *
         * The operation can be expressed symbolically as:
         *
         * this(u, v) = dist(this(u, v))
         *
         * If scale_factor is not 1, it should be a value > 1, and it specifies the
         * factor to upscale the working table while processing, to reduce artifacts
         * from integer truncation.
         *
         * By convention, the y axis in inverted in the distortion map relative to the
         * coordinates here.  A y value of 0 in the distortion map corresponds with a
         * v value of 1 in this file.
         */
        """
        pass

    def reverse_rows(self, const_PfmFile_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        reverse_rows(const PfmFile self)
        
        /**
         * Performs an in-place reversal of the row (y) data.
         */
        """
        pass

    def setChannel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_channel(const PfmFile self, int x, int y, int c, float value)
        
        /**
         * Replaces the cth channel of the point value at the indicated point.
         */
        """
        pass

    def setNoDataChan4(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_no_data_chan4(const PfmFile self, bool chan4)
        
        /**
         * Sets the no_data_chan4 flag.  When this flag is true, and the pfm file has
         * 4 channels, then a negative value in the fourth channel indicates no data.
         * When it is false, all points are valid.
         *
         * This is a special case of set_no_data_value().
         */
        """
        pass

    def setNoDataNan(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_no_data_nan(const PfmFile self, int num_channels)
        
        /**
         * Sets the no_data_nan flag.  When num_channels is nonzero, then a NaN value
         * in any of the first num_channels channels indicates no data for that point.
         * If num_channels is zero, then all points are valid.
         *
         * This is a special case of set_no_data_value().
         */
        """
        pass

    def setNoDataThreshold(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_no_data_threshold(const PfmFile self, const LPoint4d no_data_value)
        set_no_data_threshold(const PfmFile self, const LPoint4f no_data_value)
        
        /**
         * Sets the special threshold value.  Points that are below this value in all
         * components are considered "no value".
         */
        
        /**
         * Sets the special threshold value.  Points that are below this value in all
         * components are considered "no value".
         */
        """
        pass

    def setNoDataValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_no_data_value(const PfmFile self, const LPoint4d no_data_value)
        set_no_data_value(const PfmFile self, const LPoint4f no_data_value)
        
        /**
         * Sets the special value that means "no data" when it appears in the pfm
         * file.
         */
        
        /**
         * Sets the special value that means "no data" when it appears in the pfm
         * file.
         */
        """
        pass

    def setPoint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_point(const PfmFile self, int x, int y, const LVecBase3d point)
        set_point(const PfmFile self, int x, int y, const LVecBase3f point)
        
        /**
         * Replaces the 3-component point value at the indicated point.  In a
         * 1-channel image, the channel value is in the x component.
         */
        
        /**
         * Replaces the 3-component point value at the indicated point.  In a
         * 1-channel image, the channel value is in the x component.
         */
        """
        pass

    def setPoint1(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_point1(const PfmFile self, int x, int y, float point)
        
        /**
         * Replaces the 1-component point value at the indicated point.
         */
        """
        pass

    def setPoint2(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_point2(const PfmFile self, int x, int y, const LVecBase2d point)
        set_point2(const PfmFile self, int x, int y, const LVecBase2f point)
        
        /**
         * Replaces the 2-component point value at the indicated point.  In a
         * 1-channel image, the channel value is in the x component.
         */
        
        /**
         * Replaces the 2-component point value at the indicated point.  In a
         * 1-channel image, the channel value is in the x component.
         */
        """
        pass

    def setPoint3(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_point3(const PfmFile self, int x, int y, const LVecBase3d point)
        set_point3(const PfmFile self, int x, int y, const LVecBase3f point)
        
        /**
         * Replaces the 3-component point value at the indicated point.  In a
         * 1-channel image, the channel value is in the x component.
         */
        
        /**
         * Replaces the 3-component point value at the indicated point.  In a
         * 1-channel image, the channel value is in the x component.
         */
        """
        pass

    def setPoint4(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_point4(const PfmFile self, int x, int y, const LVecBase4d point)
        set_point4(const PfmFile self, int x, int y, const LVecBase4f point)
        
        /**
         * Replaces the 4-component point value at the indicated point.  In a
         * 1-channel image, the channel value is in the x component.
         */
        
        /**
         * Replaces the 4-component point value at the indicated point.  In a
         * 1-channel image, the channel value is in the x component.
         */
        """
        pass

    def setScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_scale(const PfmFile self, float scale)
        
        /**
         * The "scale" is reported in the pfm header and is probably meaningless.
         */
        """
        pass

    def setZeroSpecial(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_zero_special(const PfmFile self, bool zero_special)
        
        /**
         * Sets the zero_special flag.  When this flag is true, values of (0, 0, 0) in
         * the pfm file are treated as a special case, and are not processed.
         *
         * This is a special case of set_no_data_value().
         */
        """
        pass

    def set_channel(self, const_PfmFile_self, int_x, int_y, int_c, float_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_channel(const PfmFile self, int x, int y, int c, float value)
        
        /**
         * Replaces the cth channel of the point value at the indicated point.
         */
        """
        pass

    def set_no_data_chan4(self, const_PfmFile_self, bool_chan4): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_no_data_chan4(const PfmFile self, bool chan4)
        
        /**
         * Sets the no_data_chan4 flag.  When this flag is true, and the pfm file has
         * 4 channels, then a negative value in the fourth channel indicates no data.
         * When it is false, all points are valid.
         *
         * This is a special case of set_no_data_value().
         */
        """
        pass

    def set_no_data_nan(self, const_PfmFile_self, int_num_channels): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_no_data_nan(const PfmFile self, int num_channels)
        
        /**
         * Sets the no_data_nan flag.  When num_channels is nonzero, then a NaN value
         * in any of the first num_channels channels indicates no data for that point.
         * If num_channels is zero, then all points are valid.
         *
         * This is a special case of set_no_data_value().
         */
        """
        pass

    def set_no_data_threshold(self, const_PfmFile_self, const_LPoint4d_no_data_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_no_data_threshold(const PfmFile self, const LPoint4d no_data_value)
        set_no_data_threshold(const PfmFile self, const LPoint4f no_data_value)
        
        /**
         * Sets the special threshold value.  Points that are below this value in all
         * components are considered "no value".
         */
        
        /**
         * Sets the special threshold value.  Points that are below this value in all
         * components are considered "no value".
         */
        """
        pass

    def set_no_data_value(self, const_PfmFile_self, const_LPoint4d_no_data_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_no_data_value(const PfmFile self, const LPoint4d no_data_value)
        set_no_data_value(const PfmFile self, const LPoint4f no_data_value)
        
        /**
         * Sets the special value that means "no data" when it appears in the pfm
         * file.
         */
        
        /**
         * Sets the special value that means "no data" when it appears in the pfm
         * file.
         */
        """
        pass

    def set_point(self, const_PfmFile_self, int_x, int_y, const_LVecBase3d_point): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_point(const PfmFile self, int x, int y, const LVecBase3d point)
        set_point(const PfmFile self, int x, int y, const LVecBase3f point)
        
        /**
         * Replaces the 3-component point value at the indicated point.  In a
         * 1-channel image, the channel value is in the x component.
         */
        
        /**
         * Replaces the 3-component point value at the indicated point.  In a
         * 1-channel image, the channel value is in the x component.
         */
        """
        pass

    def set_point1(self, const_PfmFile_self, int_x, int_y, float_point): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_point1(const PfmFile self, int x, int y, float point)
        
        /**
         * Replaces the 1-component point value at the indicated point.
         */
        """
        pass

    def set_point2(self, const_PfmFile_self, int_x, int_y, const_LVecBase2d_point): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_point2(const PfmFile self, int x, int y, const LVecBase2d point)
        set_point2(const PfmFile self, int x, int y, const LVecBase2f point)
        
        /**
         * Replaces the 2-component point value at the indicated point.  In a
         * 1-channel image, the channel value is in the x component.
         */
        
        /**
         * Replaces the 2-component point value at the indicated point.  In a
         * 1-channel image, the channel value is in the x component.
         */
        """
        pass

    def set_point3(self, const_PfmFile_self, int_x, int_y, const_LVecBase3d_point): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_point3(const PfmFile self, int x, int y, const LVecBase3d point)
        set_point3(const PfmFile self, int x, int y, const LVecBase3f point)
        
        /**
         * Replaces the 3-component point value at the indicated point.  In a
         * 1-channel image, the channel value is in the x component.
         */
        
        /**
         * Replaces the 3-component point value at the indicated point.  In a
         * 1-channel image, the channel value is in the x component.
         */
        """
        pass

    def set_point4(self, const_PfmFile_self, int_x, int_y, const_LVecBase4d_point): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_point4(const PfmFile self, int x, int y, const LVecBase4d point)
        set_point4(const PfmFile self, int x, int y, const LVecBase4f point)
        
        /**
         * Replaces the 4-component point value at the indicated point.  In a
         * 1-channel image, the channel value is in the x component.
         */
        
        /**
         * Replaces the 4-component point value at the indicated point.  In a
         * 1-channel image, the channel value is in the x component.
         */
        """
        pass

    def set_scale(self, const_PfmFile_self, float_scale): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_scale(const PfmFile self, float scale)
        
        /**
         * The "scale" is reported in the pfm header and is probably meaningless.
         */
        """
        pass

    def set_zero_special(self, const_PfmFile_self, bool_zero_special): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_zero_special(const PfmFile self, bool zero_special)
        
        /**
         * Sets the zero_special flag.  When this flag is true, values of (0, 0, 0) in
         * the pfm file are treated as a special case, and are not processed.
         *
         * This is a special case of set_no_data_value().
         */
        """
        pass

    def store(self, PfmFile_self, PNMImage_pnmimage): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        store(PfmFile self, PNMImage pnmimage)
        
        /**
         * Copies the data to the indicated PNMImage, converting to RGB values.
         */
        """
        pass

    def storeMask(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        store_mask(PfmFile self, PNMImage pnmimage)
        store_mask(PfmFile self, PNMImage pnmimage, const LVecBase4f min_point, const LVecBase4f max_point)
        
        /**
         * Stores 1 or 0 values into the indicated PNMImage, according to has_point()
         * for each pixel.  Each valid point gets a 1 value; each nonexistent point
         * gets a 0 value.
         */
        
        /**
         * Stores 1 or 0 values into the indicated PNMImage, according to has_point()
         * for each pixel.  Each valid point gets a 1 value; each nonexistent point
         * gets a 0 value.
         *
         * This flavor of store_mask also checks whether the valid points are within
         * the specified min/max range.  Any valid points without the condition
         * min_point[c] <= value[c] <= max_point[c], for any c, are stored with a 0 in
         * the mask.
         */
        """
        pass

    def store_mask(self, PfmFile_self, PNMImage_pnmimage): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        store_mask(PfmFile self, PNMImage pnmimage)
        store_mask(PfmFile self, PNMImage pnmimage, const LVecBase4f min_point, const LVecBase4f max_point)
        
        /**
         * Stores 1 or 0 values into the indicated PNMImage, according to has_point()
         * for each pixel.  Each valid point gets a 1 value; each nonexistent point
         * gets a 0 value.
         */
        
        /**
         * Stores 1 or 0 values into the indicated PNMImage, according to has_point()
         * for each pixel.  Each valid point gets a 1 value; each nonexistent point
         * gets a 0 value.
         *
         * This flavor of store_mask also checks whether the valid points are within
         * the specified min/max range.  Any valid points without the condition
         * min_point[c] <= value[c] <= max_point[c], for any c, are stored with a 0 in
         * the mask.
         */
        """
        pass

    def write(self, const_PfmFile_self, ostream_out, const_Filename_fullpath): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(const PfmFile self, ostream out, const Filename fullpath)
        write(const PfmFile self, const Filename fullpath)
        
        /**
         * Writes the PFM data to the indicated file, returning true on success, false
         * on failure.
         *
         * If the type implied by the filename extension supports floating-point, the
         * data will be written directly; otherwise, the floating-point data will be
         * quietly converted to the appropriate integer type.
         */
        
        /**
         * Writes the PFM data to the indicated stream, returning true on success,
         * false on failure.
         */
        
        /**
         * Writes the PFM data using the indicated PNMWriter.
         *
         * The PNMWriter is always deleted upon completion, whether successful or not.
         */
        """
        pass

    def xform(self, const_PfmFile_self, const_LMatrix4d_transform): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        xform(const PfmFile self, const LMatrix4d transform)
        xform(const PfmFile self, const LMatrix4f transform)
        
        /**
         * Applies the indicated transform matrix to all points in-place.
         */
        
        /**
         * Applies the indicated transform matrix to all points in-place.
         */
        """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        pass

    def __imul__(self, *args, **kwargs): # real signature unknown
        """ Return self*=value. """
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

    scale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    valid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.PfmFile' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.PfmFile' objects>"
        '__doc__': '/**\n * Defines a pfm file, a 2-d table of floating-point numbers, either\n * 3-component or 1-component, or with a special extension, 2- or 4-component.\n */',
        '__imul__': None, # (!) real value is "<slot wrapper '__imul__' of 'panda3d.core.PfmFile' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.PfmFile' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE356090>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.PfmFile' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.PfmFile' objects>"
        'addSubImage': None, # (!) real value is "<method 'addSubImage' of 'panda3d.core.PfmFile' objects>"
        'add_sub_image': None, # (!) real value is "<method 'add_sub_image' of 'panda3d.core.PfmFile' objects>"
        'apply1dLut': None, # (!) real value is "<method 'apply1dLut' of 'panda3d.core.PfmFile' objects>"
        'applyCrop': None, # (!) real value is "<method 'applyCrop' of 'panda3d.core.PfmFile' objects>"
        'applyExponent': None, # (!) real value is "<method 'applyExponent' of 'panda3d.core.PfmFile' objects>"
        'applyMask': None, # (!) real value is "<method 'applyMask' of 'panda3d.core.PfmFile' objects>"
        'apply_1d_lut': None, # (!) real value is "<method 'apply_1d_lut' of 'panda3d.core.PfmFile' objects>"
        'apply_crop': None, # (!) real value is "<method 'apply_crop' of 'panda3d.core.PfmFile' objects>"
        'apply_exponent': None, # (!) real value is "<method 'apply_exponent' of 'panda3d.core.PfmFile' objects>"
        'apply_mask': None, # (!) real value is "<method 'apply_mask' of 'panda3d.core.PfmFile' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.PfmFile' objects>"
        'boxFilterFrom': None, # (!) real value is "<method 'boxFilterFrom' of 'panda3d.core.PfmFile' objects>"
        'box_filter_from': None, # (!) real value is "<method 'box_filter_from' of 'panda3d.core.PfmFile' objects>"
        'calcAutocrop': None, # (!) real value is "<method 'calcAutocrop' of 'panda3d.core.PfmFile' objects>"
        'calcAveragePoint': None, # (!) real value is "<method 'calcAveragePoint' of 'panda3d.core.PfmFile' objects>"
        'calcBilinearPoint': None, # (!) real value is "<method 'calcBilinearPoint' of 'panda3d.core.PfmFile' objects>"
        'calcMinMax': None, # (!) real value is "<method 'calcMinMax' of 'panda3d.core.PfmFile' objects>"
        'calcTightBounds': None, # (!) real value is "<method 'calcTightBounds' of 'panda3d.core.PfmFile' objects>"
        'calc_autocrop': None, # (!) real value is "<method 'calc_autocrop' of 'panda3d.core.PfmFile' objects>"
        'calc_average_point': None, # (!) real value is "<method 'calc_average_point' of 'panda3d.core.PfmFile' objects>"
        'calc_bilinear_point': None, # (!) real value is "<method 'calc_bilinear_point' of 'panda3d.core.PfmFile' objects>"
        'calc_min_max': None, # (!) real value is "<method 'calc_min_max' of 'panda3d.core.PfmFile' objects>"
        'calc_tight_bounds': None, # (!) real value is "<method 'calc_tight_bounds' of 'panda3d.core.PfmFile' objects>"
        'clear': None, # (!) real value is "<method 'clear' of 'panda3d.core.PfmFile' objects>"
        'clearNoDataValue': None, # (!) real value is "<method 'clearNoDataValue' of 'panda3d.core.PfmFile' objects>"
        'clearToTexcoords': None, # (!) real value is "<method 'clearToTexcoords' of 'panda3d.core.PfmFile' objects>"
        'clear_no_data_value': None, # (!) real value is "<method 'clear_no_data_value' of 'panda3d.core.PfmFile' objects>"
        'clear_to_texcoords': None, # (!) real value is "<method 'clear_to_texcoords' of 'panda3d.core.PfmFile' objects>"
        'computePlanarBounds': None, # (!) real value is "<method 'computePlanarBounds' of 'panda3d.core.PfmFile' objects>"
        'computeSamplePoint': None, # (!) real value is "<method 'computeSamplePoint' of 'panda3d.core.PfmFile' objects>"
        'compute_planar_bounds': None, # (!) real value is "<method 'compute_planar_bounds' of 'panda3d.core.PfmFile' objects>"
        'compute_sample_point': None, # (!) real value is "<method 'compute_sample_point' of 'panda3d.core.PfmFile' objects>"
        'copyChannel': None, # (!) real value is "<method 'copyChannel' of 'panda3d.core.PfmFile' objects>"
        'copyChannelMasked': None, # (!) real value is "<method 'copyChannelMasked' of 'panda3d.core.PfmFile' objects>"
        'copySubImage': None, # (!) real value is "<method 'copySubImage' of 'panda3d.core.PfmFile' objects>"
        'copy_channel': None, # (!) real value is "<method 'copy_channel' of 'panda3d.core.PfmFile' objects>"
        'copy_channel_masked': None, # (!) real value is "<method 'copy_channel_masked' of 'panda3d.core.PfmFile' objects>"
        'copy_sub_image': None, # (!) real value is "<method 'copy_sub_image' of 'panda3d.core.PfmFile' objects>"
        'divideSubImage': None, # (!) real value is "<method 'divideSubImage' of 'panda3d.core.PfmFile' objects>"
        'divide_sub_image': None, # (!) real value is "<method 'divide_sub_image' of 'panda3d.core.PfmFile' objects>"
        'fill': None, # (!) real value is "<method 'fill' of 'panda3d.core.PfmFile' objects>"
        'fillChannel': None, # (!) real value is "<method 'fillChannel' of 'panda3d.core.PfmFile' objects>"
        'fillChannelMasked': None, # (!) real value is "<method 'fillChannelMasked' of 'panda3d.core.PfmFile' objects>"
        'fillChannelMaskedNan': None, # (!) real value is "<method 'fillChannelMaskedNan' of 'panda3d.core.PfmFile' objects>"
        'fillChannelNan': None, # (!) real value is "<method 'fillChannelNan' of 'panda3d.core.PfmFile' objects>"
        'fillNan': None, # (!) real value is "<method 'fillNan' of 'panda3d.core.PfmFile' objects>"
        'fillNoDataValue': None, # (!) real value is "<method 'fillNoDataValue' of 'panda3d.core.PfmFile' objects>"
        'fill_channel': None, # (!) real value is "<method 'fill_channel' of 'panda3d.core.PfmFile' objects>"
        'fill_channel_masked': None, # (!) real value is "<method 'fill_channel_masked' of 'panda3d.core.PfmFile' objects>"
        'fill_channel_masked_nan': None, # (!) real value is "<method 'fill_channel_masked_nan' of 'panda3d.core.PfmFile' objects>"
        'fill_channel_nan': None, # (!) real value is "<method 'fill_channel_nan' of 'panda3d.core.PfmFile' objects>"
        'fill_nan': None, # (!) real value is "<method 'fill_nan' of 'panda3d.core.PfmFile' objects>"
        'fill_no_data_value': None, # (!) real value is "<method 'fill_no_data_value' of 'panda3d.core.PfmFile' objects>"
        'flip': None, # (!) real value is "<method 'flip' of 'panda3d.core.PfmFile' objects>"
        'forwardDistort': None, # (!) real value is "<method 'forwardDistort' of 'panda3d.core.PfmFile' objects>"
        'forward_distort': None, # (!) real value is "<method 'forward_distort' of 'panda3d.core.PfmFile' objects>"
        'gammaCorrect': None, # (!) real value is "<method 'gammaCorrect' of 'panda3d.core.PfmFile' objects>"
        'gammaCorrectAlpha': None, # (!) real value is "<method 'gammaCorrectAlpha' of 'panda3d.core.PfmFile' objects>"
        'gamma_correct': None, # (!) real value is "<method 'gamma_correct' of 'panda3d.core.PfmFile' objects>"
        'gamma_correct_alpha': None, # (!) real value is "<method 'gamma_correct_alpha' of 'panda3d.core.PfmFile' objects>"
        'gaussianFilterFrom': None, # (!) real value is "<method 'gaussianFilterFrom' of 'panda3d.core.PfmFile' objects>"
        'gaussian_filter_from': None, # (!) real value is "<method 'gaussian_filter_from' of 'panda3d.core.PfmFile' objects>"
        'getChannel': None, # (!) real value is "<method 'getChannel' of 'panda3d.core.PfmFile' objects>"
        'getNoDataValue': None, # (!) real value is "<method 'getNoDataValue' of 'panda3d.core.PfmFile' objects>"
        'getPoint': None, # (!) real value is "<method 'getPoint' of 'panda3d.core.PfmFile' objects>"
        'getPoint1': None, # (!) real value is "<method 'getPoint1' of 'panda3d.core.PfmFile' objects>"
        'getPoint2': None, # (!) real value is "<method 'getPoint2' of 'panda3d.core.PfmFile' objects>"
        'getPoint3': None, # (!) real value is "<method 'getPoint3' of 'panda3d.core.PfmFile' objects>"
        'getPoint4': None, # (!) real value is "<method 'getPoint4' of 'panda3d.core.PfmFile' objects>"
        'getPoints': None, # (!) real value is "<method 'getPoints' of 'panda3d.core.PfmFile' objects>"
        'getScale': None, # (!) real value is "<method 'getScale' of 'panda3d.core.PfmFile' objects>"
        'get_channel': None, # (!) real value is "<method 'get_channel' of 'panda3d.core.PfmFile' objects>"
        'get_no_data_value': None, # (!) real value is "<method 'get_no_data_value' of 'panda3d.core.PfmFile' objects>"
        'get_point': None, # (!) real value is "<method 'get_point' of 'panda3d.core.PfmFile' objects>"
        'get_point1': None, # (!) real value is "<method 'get_point1' of 'panda3d.core.PfmFile' objects>"
        'get_point2': None, # (!) real value is "<method 'get_point2' of 'panda3d.core.PfmFile' objects>"
        'get_point3': None, # (!) real value is "<method 'get_point3' of 'panda3d.core.PfmFile' objects>"
        'get_point4': None, # (!) real value is "<method 'get_point4' of 'panda3d.core.PfmFile' objects>"
        'get_points': None, # (!) real value is "<method 'get_points' of 'panda3d.core.PfmFile' objects>"
        'get_scale': None, # (!) real value is "<method 'get_scale' of 'panda3d.core.PfmFile' objects>"
        'hasNoDataThreshold': None, # (!) real value is "<method 'hasNoDataThreshold' of 'panda3d.core.PfmFile' objects>"
        'hasNoDataValue': None, # (!) real value is "<method 'hasNoDataValue' of 'panda3d.core.PfmFile' objects>"
        'hasPoint': None, # (!) real value is "<method 'hasPoint' of 'panda3d.core.PfmFile' objects>"
        'has_no_data_threshold': None, # (!) real value is "<method 'has_no_data_threshold' of 'panda3d.core.PfmFile' objects>"
        'has_no_data_value': None, # (!) real value is "<method 'has_no_data_value' of 'panda3d.core.PfmFile' objects>"
        'has_point': None, # (!) real value is "<method 'has_point' of 'panda3d.core.PfmFile' objects>"
        'indirect1dLookup': None, # (!) real value is "<method 'indirect1dLookup' of 'panda3d.core.PfmFile' objects>"
        'indirect_1d_lookup': None, # (!) real value is "<method 'indirect_1d_lookup' of 'panda3d.core.PfmFile' objects>"
        'isColumnEmpty': None, # (!) real value is "<method 'isColumnEmpty' of 'panda3d.core.PfmFile' objects>"
        'isRowEmpty': None, # (!) real value is "<method 'isRowEmpty' of 'panda3d.core.PfmFile' objects>"
        'isValid': None, # (!) real value is "<method 'isValid' of 'panda3d.core.PfmFile' objects>"
        'is_column_empty': None, # (!) real value is "<method 'is_column_empty' of 'panda3d.core.PfmFile' objects>"
        'is_row_empty': None, # (!) real value is "<method 'is_row_empty' of 'panda3d.core.PfmFile' objects>"
        'is_valid': None, # (!) real value is "<method 'is_valid' of 'panda3d.core.PfmFile' objects>"
        'load': None, # (!) real value is "<method 'load' of 'panda3d.core.PfmFile' objects>"
        'merge': None, # (!) real value is "<method 'merge' of 'panda3d.core.PfmFile' objects>"
        'modifyPoint': None, # (!) real value is "<method 'modifyPoint' of 'panda3d.core.PfmFile' objects>"
        'modifyPoint2': None, # (!) real value is "<method 'modifyPoint2' of 'panda3d.core.PfmFile' objects>"
        'modifyPoint3': None, # (!) real value is "<method 'modifyPoint3' of 'panda3d.core.PfmFile' objects>"
        'modifyPoint4': None, # (!) real value is "<method 'modifyPoint4' of 'panda3d.core.PfmFile' objects>"
        'modify_point': None, # (!) real value is "<method 'modify_point' of 'panda3d.core.PfmFile' objects>"
        'modify_point2': None, # (!) real value is "<method 'modify_point2' of 'panda3d.core.PfmFile' objects>"
        'modify_point3': None, # (!) real value is "<method 'modify_point3' of 'panda3d.core.PfmFile' objects>"
        'modify_point4': None, # (!) real value is "<method 'modify_point4' of 'panda3d.core.PfmFile' objects>"
        'multSubImage': None, # (!) real value is "<method 'multSubImage' of 'panda3d.core.PfmFile' objects>"
        'mult_sub_image': None, # (!) real value is "<method 'mult_sub_image' of 'panda3d.core.PfmFile' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.PfmFile' objects>"
        'pullSpot': None, # (!) real value is "<method 'pullSpot' of 'panda3d.core.PfmFile' objects>"
        'pull_spot': None, # (!) real value is "<method 'pull_spot' of 'panda3d.core.PfmFile' objects>"
        'quickFilterFrom': None, # (!) real value is "<method 'quickFilterFrom' of 'panda3d.core.PfmFile' objects>"
        'quick_filter_from': None, # (!) real value is "<method 'quick_filter_from' of 'panda3d.core.PfmFile' objects>"
        'read': None, # (!) real value is "<method 'read' of 'panda3d.core.PfmFile' objects>"
        'resize': None, # (!) real value is "<method 'resize' of 'panda3d.core.PfmFile' objects>"
        'reverseDistort': None, # (!) real value is "<method 'reverseDistort' of 'panda3d.core.PfmFile' objects>"
        'reverseRows': None, # (!) real value is "<method 'reverseRows' of 'panda3d.core.PfmFile' objects>"
        'reverse_distort': None, # (!) real value is "<method 'reverse_distort' of 'panda3d.core.PfmFile' objects>"
        'reverse_rows': None, # (!) real value is "<method 'reverse_rows' of 'panda3d.core.PfmFile' objects>"
        'scale': None, # (!) real value is "<attribute 'scale' of 'panda3d.core.PfmFile' objects>"
        'setChannel': None, # (!) real value is "<method 'setChannel' of 'panda3d.core.PfmFile' objects>"
        'setNoDataChan4': None, # (!) real value is "<method 'setNoDataChan4' of 'panda3d.core.PfmFile' objects>"
        'setNoDataNan': None, # (!) real value is "<method 'setNoDataNan' of 'panda3d.core.PfmFile' objects>"
        'setNoDataThreshold': None, # (!) real value is "<method 'setNoDataThreshold' of 'panda3d.core.PfmFile' objects>"
        'setNoDataValue': None, # (!) real value is "<method 'setNoDataValue' of 'panda3d.core.PfmFile' objects>"
        'setPoint': None, # (!) real value is "<method 'setPoint' of 'panda3d.core.PfmFile' objects>"
        'setPoint1': None, # (!) real value is "<method 'setPoint1' of 'panda3d.core.PfmFile' objects>"
        'setPoint2': None, # (!) real value is "<method 'setPoint2' of 'panda3d.core.PfmFile' objects>"
        'setPoint3': None, # (!) real value is "<method 'setPoint3' of 'panda3d.core.PfmFile' objects>"
        'setPoint4': None, # (!) real value is "<method 'setPoint4' of 'panda3d.core.PfmFile' objects>"
        'setScale': None, # (!) real value is "<method 'setScale' of 'panda3d.core.PfmFile' objects>"
        'setZeroSpecial': None, # (!) real value is "<method 'setZeroSpecial' of 'panda3d.core.PfmFile' objects>"
        'set_channel': None, # (!) real value is "<method 'set_channel' of 'panda3d.core.PfmFile' objects>"
        'set_no_data_chan4': None, # (!) real value is "<method 'set_no_data_chan4' of 'panda3d.core.PfmFile' objects>"
        'set_no_data_nan': None, # (!) real value is "<method 'set_no_data_nan' of 'panda3d.core.PfmFile' objects>"
        'set_no_data_threshold': None, # (!) real value is "<method 'set_no_data_threshold' of 'panda3d.core.PfmFile' objects>"
        'set_no_data_value': None, # (!) real value is "<method 'set_no_data_value' of 'panda3d.core.PfmFile' objects>"
        'set_point': None, # (!) real value is "<method 'set_point' of 'panda3d.core.PfmFile' objects>"
        'set_point1': None, # (!) real value is "<method 'set_point1' of 'panda3d.core.PfmFile' objects>"
        'set_point2': None, # (!) real value is "<method 'set_point2' of 'panda3d.core.PfmFile' objects>"
        'set_point3': None, # (!) real value is "<method 'set_point3' of 'panda3d.core.PfmFile' objects>"
        'set_point4': None, # (!) real value is "<method 'set_point4' of 'panda3d.core.PfmFile' objects>"
        'set_scale': None, # (!) real value is "<method 'set_scale' of 'panda3d.core.PfmFile' objects>"
        'set_zero_special': None, # (!) real value is "<method 'set_zero_special' of 'panda3d.core.PfmFile' objects>"
        'store': None, # (!) real value is "<method 'store' of 'panda3d.core.PfmFile' objects>"
        'storeMask': None, # (!) real value is "<method 'storeMask' of 'panda3d.core.PfmFile' objects>"
        'store_mask': None, # (!) real value is "<method 'store_mask' of 'panda3d.core.PfmFile' objects>"
        'valid': None, # (!) real value is "<attribute 'valid' of 'panda3d.core.PfmFile' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.PfmFile' objects>"
        'xform': None, # (!) real value is "<method 'xform' of 'panda3d.core.PfmFile' objects>"
    }


