# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class Mat3D(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This is a 3-by-3 transform matrix.  It typically will represent either a
     * rotation-and-scale (no translation) matrix in 3-d, or a full affine matrix
     * (rotation, scale, translation) in 2-d, e.g.  for a texture matrix.
     */
    """
    def addHash(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_hash(LMatrix3d self, int hash)
        add_hash(LMatrix3d self, int hash, double threshold)
        
        /**
         * Adds the vector into the running hash.
         */
        
        /**
         * Adds the vector into the running hash.
         */
        """
        pass

    def add_hash(self, LMatrix3d_self, int_hash): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_hash(LMatrix3d self, int hash)
        add_hash(LMatrix3d self, int hash, double threshold)
        
        /**
         * Adds the vector into the running hash.
         */
        
        /**
         * Adds the vector into the running hash.
         */
        """
        pass

    def almostEqual(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        almost_equal(LMatrix3d self, const LMatrix3d other)
        almost_equal(LMatrix3d self, const LMatrix3d other, double threshold)
        
        /**
         * Returns true if two matrices are memberwise equal within a default
         * tolerance based on the numeric type.
         */
        
        /**
         * Returns true if two matrices are memberwise equal within a specified
         * tolerance.
         */
        """
        pass

    def almost_equal(self, LMatrix3d_self, const_LMatrix3d_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        almost_equal(LMatrix3d self, const LMatrix3d other)
        almost_equal(LMatrix3d self, const LMatrix3d other, double threshold)
        
        /**
         * Returns true if two matrices are memberwise equal within a default
         * tolerance based on the numeric type.
         */
        
        /**
         * Returns true if two matrices are memberwise equal within a specified
         * tolerance.
         */
        """
        pass

    def assign(self, const_LMatrix3d_self, const_LMatrix3d_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const LMatrix3d self, const LMatrix3d other)
        assign(const LMatrix3d self, double fill_value)
        
        /**
         *
         */
        
        /**
         *
         */
        """
        pass

    def compareTo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        compare_to(LMatrix3d self, const LMatrix3d other)
        compare_to(LMatrix3d self, const LMatrix3d other, double threshold)
        
        /**
         * This flavor of compare_to uses a default threshold value based on the
         * numeric type.
         */
        
        /**
         * Sorts matrices lexicographically, componentwise.  Returns a number less
         * than 0 if this matrix sorts before the other one, greater than zero if it
         * sorts after, 0 if they are equivalent (within the indicated tolerance).
         */
        """
        pass

    def compare_to(self, LMatrix3d_self, const_LMatrix3d_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        compare_to(LMatrix3d self, const LMatrix3d other)
        compare_to(LMatrix3d self, const LMatrix3d other, double threshold)
        
        /**
         * This flavor of compare_to uses a default threshold value based on the
         * numeric type.
         */
        
        /**
         * Sorts matrices lexicographically, componentwise.  Returns a number less
         * than 0 if this matrix sorts before the other one, greater than zero if it
         * sorts after, 0 if they are equivalent (within the indicated tolerance).
         */
        """
        pass

    def componentwiseMult(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        componentwise_mult(const LMatrix3d self, const LMatrix3d other)
        
        /**
         *
         */
        """
        pass

    def componentwise_mult(self, const_LMatrix3d_self, const_LMatrix3d_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        componentwise_mult(const LMatrix3d self, const LMatrix3d other)
        
        /**
         *
         */
        """
        pass

    def convertMat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        convert_mat(int from, int to)
        
        /**
         * Returns a matrix that transforms from the indicated coordinate system to
         * the indicated coordinate system.
         */
        """
        pass

    def convert_mat(self, int_from, int_to): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        convert_mat(int from, int to)
        
        /**
         * Returns a matrix that transforms from the indicated coordinate system to
         * the indicated coordinate system.
         */
        """
        pass

    def determinant(self, LMatrix3d_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        determinant(LMatrix3d self)
        
        /**
         * Returns the determinant of the matrix.
         */
        """
        pass

    def fill(self, const_LMatrix3d_self, double_fill_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        fill(const LMatrix3d self, double fill_value)
        
        /**
         * Sets each element of the matrix to the indicated fill_value.  This is of
         * questionable value, but is sometimes useful when initializing to zero.
         */
        """
        pass

    def getCell(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_cell(LMatrix3d self, int row, int col)
        
        /**
         * Returns a particular element of the matrix.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getCol(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_col(LMatrix3d self, int col)
        
        /**
         * Returns the indicated column of the matrix as a three-component vector.
         */
        """
        pass

    def getCol2(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_col2(LMatrix3d self, int col)
        
        /**
         * Returns the indicated column of the matrix as a two-component vector,
         * ignoring the last row.
         */
        """
        pass

    def getCol2s(self, *args, **kwargs): # real signature unknown
        pass

    def getCols(self, *args, **kwargs): # real signature unknown
        pass

    def getHash(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_hash(LMatrix3d self)
        get_hash(LMatrix3d self, double threshold)
        
        /**
         * Returns a suitable hash for phash_map.
         */
        
        /**
         * Returns a suitable hash for phash_map.
         */
        """
        pass

    def getNumComponents(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_components(LMatrix3d self)
        
        /**
         * Returns the number of elements in the matrix, nine.
         */
        """
        pass

    def getRow(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_row(LMatrix3d self, int row)
        get_row(LMatrix3d self, LVecBase3d result_vec, int row)
        
        // these versions inline better
        
        /**
         * Returns the indicated row of the matrix as a three-component vector.
         */
        
        /**
         * Stores the indicated row of the matrix as a three-component vector.
         */
        """
        pass

    def getRow2(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_row2(LMatrix3d self, int row)
        
        /**
         * Returns the indicated row of the matrix as a two-component vector, ignoring
         * the last column.
         */
        """
        pass

    def getRow2s(self, *args, **kwargs): # real signature unknown
        pass

    def getRows(self, *args, **kwargs): # real signature unknown
        pass

    def get_cell(self, LMatrix3d_self, int_row, int_col): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_cell(LMatrix3d self, int row, int col)
        
        /**
         * Returns a particular element of the matrix.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_col(self, LMatrix3d_self, int_col): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_col(LMatrix3d self, int col)
        
        /**
         * Returns the indicated column of the matrix as a three-component vector.
         */
        """
        pass

    def get_col2(self, LMatrix3d_self, int_col): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_col2(LMatrix3d self, int col)
        
        /**
         * Returns the indicated column of the matrix as a two-component vector,
         * ignoring the last row.
         */
        """
        pass

    def get_col2s(self, *args, **kwargs): # real signature unknown
        pass

    def get_cols(self, *args, **kwargs): # real signature unknown
        pass

    def get_hash(self, LMatrix3d_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_hash(LMatrix3d self)
        get_hash(LMatrix3d self, double threshold)
        
        /**
         * Returns a suitable hash for phash_map.
         */
        
        /**
         * Returns a suitable hash for phash_map.
         */
        """
        pass

    def get_num_components(self, LMatrix3d_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_components(LMatrix3d self)
        
        /**
         * Returns the number of elements in the matrix, nine.
         */
        """
        pass

    def get_row(self, LMatrix3d_self, int_row): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_row(LMatrix3d self, int row)
        get_row(LMatrix3d self, LVecBase3d result_vec, int row)
        
        // these versions inline better
        
        /**
         * Returns the indicated row of the matrix as a three-component vector.
         */
        
        /**
         * Stores the indicated row of the matrix as a three-component vector.
         */
        """
        pass

    def get_row2(self, LMatrix3d_self, int_row): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_row2(LMatrix3d self, int row)
        
        /**
         * Returns the indicated row of the matrix as a two-component vector, ignoring
         * the last column.
         */
        """
        pass

    def get_row2s(self, *args, **kwargs): # real signature unknown
        pass

    def get_rows(self, *args, **kwargs): # real signature unknown
        pass

    def identMat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        ident_mat()
        
        /**
         * Returns an identity matrix.
         *
         * This function definition must appear first, since some inline functions
         * below take advantage of it.
         */
        """
        pass

    def ident_mat(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        ident_mat()
        
        /**
         * Returns an identity matrix.
         *
         * This function definition must appear first, since some inline functions
         * below take advantage of it.
         */
        """
        pass

    def invertFrom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        invert_from(const LMatrix3d self, const LMatrix3d other)
        
        /**
         * Computes the inverse of the other matrix, and stores the result in this
         * matrix.  This is a fully general operation and makes no assumptions about
         * the type of transform represented by the matrix.
         *
         * The other matrix must be a different object than this matrix.  However, if
         * you need to invert a matrix in place, see invert_in_place.
         *
         * The return value is true if the matrix was successfully inverted, false if
         * there was a singularity.
         */
        """
        pass

    def invertInPlace(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        invert_in_place(const LMatrix3d self)
        
        /**
         * Inverts the current matrix.  Returns true if the inverse is successful,
         * false if the matrix was singular.
         */
        """
        pass

    def invertTransposeFrom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        invert_transpose_from(const LMatrix3d self, const LMatrix4d other)
        invert_transpose_from(const LMatrix3d self, const LMatrix3d other)
        
        /**
         * Simultaneously computes the inverse of the indicated matrix, and then the
         * transpose of that inverse.
         */
        
        /**
         * Simultaneously computes the inverse of the indicated matrix, and then the
         * transpose of that inverse.
         */
        """
        pass

    def invert_from(self, const_LMatrix3d_self, const_LMatrix3d_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        invert_from(const LMatrix3d self, const LMatrix3d other)
        
        /**
         * Computes the inverse of the other matrix, and stores the result in this
         * matrix.  This is a fully general operation and makes no assumptions about
         * the type of transform represented by the matrix.
         *
         * The other matrix must be a different object than this matrix.  However, if
         * you need to invert a matrix in place, see invert_in_place.
         *
         * The return value is true if the matrix was successfully inverted, false if
         * there was a singularity.
         */
        """
        pass

    def invert_in_place(self, const_LMatrix3d_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        invert_in_place(const LMatrix3d self)
        
        /**
         * Inverts the current matrix.  Returns true if the inverse is successful,
         * false if the matrix was singular.
         */
        """
        pass

    def invert_transpose_from(self, const_LMatrix3d_self, const_LMatrix4d_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        invert_transpose_from(const LMatrix3d self, const LMatrix4d other)
        invert_transpose_from(const LMatrix3d self, const LMatrix3d other)
        
        /**
         * Simultaneously computes the inverse of the indicated matrix, and then the
         * transpose of that inverse.
         */
        
        /**
         * Simultaneously computes the inverse of the indicated matrix, and then the
         * transpose of that inverse.
         */
        """
        pass

    def isIdentity(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_identity(LMatrix3d self)
        
        /**
         * Returns true if this is (close enough to) the identity matrix, false
         * otherwise.
         */
        """
        pass

    def isNan(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_nan(LMatrix3d self)
        
        /**
         * Returns true if any component of the matrix is not-a-number, false
         * otherwise.
         */
        """
        pass

    def is_identity(self, LMatrix3d_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_identity(LMatrix3d self)
        
        /**
         * Returns true if this is (close enough to) the identity matrix, false
         * otherwise.
         */
        """
        pass

    def is_nan(self, LMatrix3d_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_nan(LMatrix3d self)
        
        /**
         * Returns true if any component of the matrix is not-a-number, false
         * otherwise.
         */
        """
        pass

    def multiply(self, const_LMatrix3d_self, const_LMatrix3d_other1, const_LMatrix3d_other2): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        multiply(const LMatrix3d self, const LMatrix3d other1, const LMatrix3d other2)
        
        // this = other1 * other2
        
        // this = other1 * other2
        """
        pass

    def output(self, LMatrix3d_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(LMatrix3d self, ostream out)
        
        /**
         *
         */
        """
        pass

    def readDatagram(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        read_datagram(const LMatrix3d self, DatagramIterator source)
        
        /**
         * Reads the matrix from the Datagram using get_stdfloat().
         */
        """
        pass

    def readDatagramFixed(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        read_datagram_fixed(const LMatrix3d self, DatagramIterator scan)
        
        /**
         * Reads the matrix from the Datagram using get_float32() or get_float64().
         * See write_datagram_fixed().
         */
        """
        pass

    def read_datagram(self, const_LMatrix3d_self, DatagramIterator_source): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        read_datagram(const LMatrix3d self, DatagramIterator source)
        
        /**
         * Reads the matrix from the Datagram using get_stdfloat().
         */
        """
        pass

    def read_datagram_fixed(self, const_LMatrix3d_self, DatagramIterator_scan): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        read_datagram_fixed(const LMatrix3d self, DatagramIterator scan)
        
        /**
         * Reads the matrix from the Datagram using get_float32() or get_float64().
         * See write_datagram_fixed().
         */
        """
        pass

    def rotateMat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        rotate_mat(double angle)
        rotate_mat(double angle, const LVecBase3d axis, int cs)
        
        /**
         * Returns a matrix that rotates by the given angle in degrees
         * counterclockwise.
         */
        
        /**
         * Returns a matrix that rotates by the given angle in degrees
         * counterclockwise about the indicated vector.
         */
        """
        pass

    def rotateMatNormaxis(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        rotate_mat_normaxis(double angle, const LVecBase3d axis, int cs)
        
        /**
         * Returns a matrix that rotates by the given angle in degrees
         * counterclockwise about the indicated vector.  Assumes axis has been
         * normalized.
         */
        """
        pass

    def rotate_mat(self, double_angle): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        rotate_mat(double angle)
        rotate_mat(double angle, const LVecBase3d axis, int cs)
        
        /**
         * Returns a matrix that rotates by the given angle in degrees
         * counterclockwise.
         */
        
        /**
         * Returns a matrix that rotates by the given angle in degrees
         * counterclockwise about the indicated vector.
         */
        """
        pass

    def rotate_mat_normaxis(self, double_angle, const_LVecBase3d_axis, int_cs): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        rotate_mat_normaxis(double angle, const LVecBase3d axis, int cs)
        
        /**
         * Returns a matrix that rotates by the given angle in degrees
         * counterclockwise about the indicated vector.  Assumes axis has been
         * normalized.
         */
        """
        pass

    def scaleMat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        scale_mat(const LVecBase3d scale)
        scale_mat(const LVecBase2d scale)
        scale_mat(double sx, double sy)
        scale_mat(double sx, double sy, double sz)
        
        /**
         * Returns a matrix that applies the indicated scale in each of the two axes.
         */
        
        /**
         * Returns a matrix that applies the indicated scale in each of the two axes.
         */
        
        /**
         * Returns a matrix that applies the indicated scale in each of the three
         * axes.
         */
        
        /**
         * Returns a matrix that applies the indicated scale in each of the three
         * axes.
         */
        """
        pass

    def scaleShearMat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        scale_shear_mat(const LVecBase3d scale, const LVecBase3d shear)
        scale_shear_mat(const LVecBase3d scale, const LVecBase3d shear, int cs)
        scale_shear_mat(double sx, double sy, double sz, double shxy, double shxz, double shyz, int cs)
        
        /**
         * Returns a matrix that applies the indicated scale and shear.
         */
        
        /**
         * Returns a matrix that applies the indicated scale and shear.
         */
        """
        pass

    def scale_mat(self, const_LVecBase3d_scale): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        scale_mat(const LVecBase3d scale)
        scale_mat(const LVecBase2d scale)
        scale_mat(double sx, double sy)
        scale_mat(double sx, double sy, double sz)
        
        /**
         * Returns a matrix that applies the indicated scale in each of the two axes.
         */
        
        /**
         * Returns a matrix that applies the indicated scale in each of the two axes.
         */
        
        /**
         * Returns a matrix that applies the indicated scale in each of the three
         * axes.
         */
        
        /**
         * Returns a matrix that applies the indicated scale in each of the three
         * axes.
         */
        """
        pass

    def scale_shear_mat(self, const_LVecBase3d_scale, const_LVecBase3d_shear): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        scale_shear_mat(const LVecBase3d scale, const LVecBase3d shear)
        scale_shear_mat(const LVecBase3d scale, const LVecBase3d shear, int cs)
        scale_shear_mat(double sx, double sy, double sz, double shxy, double shxz, double shyz, int cs)
        
        /**
         * Returns a matrix that applies the indicated scale and shear.
         */
        
        /**
         * Returns a matrix that applies the indicated scale and shear.
         */
        """
        pass

    def set(self, const_LMatrix3d_self, double_e00, double_e01, double_e02, double_e10, double_e11, double_e12, double_e20, double_e21, double_e22): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set(const LMatrix3d self, double e00, double e01, double e02, double e10, double e11, double e12, double e20, double e21, double e22)
        
        /**
         *
         */
        """
        pass

    def setCell(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_cell(const LMatrix3d self, int row, int col, double value)
        
        /**
         * Changes a particular element of the matrix.
         */
        """
        pass

    def setCol(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_col(const LMatrix3d self, int col, const LVecBase2d v)
        set_col(const LMatrix3d self, int col, const LVecBase3d v)
        
        /**
         * Replaces the indicated column of the matrix from a three-component vector.
         */
        
        /**
         * Replaces the indicated column of the matrix from a two-component vector,
         * ignoring the last row.
         */
        """
        pass

    def setRotateMat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_rotate_mat(const LMatrix3d self, double angle)
        set_rotate_mat(const LMatrix3d self, double angle, const LVecBase3d axis, int cs)
        
        /**
         * Fills mat with a matrix that rotates by the given angle in degrees
         * counterclockwise.
         */
        
        /**
         * Fills mat with a matrix that rotates by the given angle in degrees
         * counterclockwise about the indicated vector.
         */
        """
        pass

    def setRotateMatNormaxis(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_rotate_mat_normaxis(const LMatrix3d self, double angle, const LVecBase3d axis, int cs)
        
        /**
         * Fills mat with a matrix that rotates by the given angle in degrees
         * counterclockwise about the indicated vector.  Assumes axis has been
         * normalized.
         */
        """
        pass

    def setRow(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_row(const LMatrix3d self, int row, const LVecBase2d v)
        set_row(const LMatrix3d self, int row, const LVecBase3d v)
        
        /**
         * Replaces the indicated row of the matrix from a three-component vector.
         */
        
        /**
         * Replaces the indicated row of the matrix from a two-component vector,
         * ignoring the last column.
         */
        """
        pass

    def setScaleMat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_scale_mat(const LMatrix3d self, const LVecBase2d scale)
        set_scale_mat(const LMatrix3d self, const LVecBase3d scale)
        
        /**
         * Fills mat with a matrix that applies the indicated scale in each of the two
         * axes.
         */
        
        /**
         * Fills mat with a matrix that applies the indicated scale in each of the
         * three axes.
         */
        """
        pass

    def setScaleShearMat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_scale_shear_mat(const LMatrix3d self, const LVecBase3d scale, const LVecBase3d shear, int cs)
        
        /**
         * Fills mat with a matrix that applies the indicated scale and shear.
         */
        """
        pass

    def setShearMat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_shear_mat(const LMatrix3d self, const LVecBase3d shear, int cs)
        
        /**
         * Fills mat with a matrix that applies the indicated shear in each of the
         * three planes.
         */
        """
        pass

    def setTranslateMat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_translate_mat(const LMatrix3d self, const LVecBase2d trans)
        
        /**
         * Fills mat with a matrix that applies the indicated translation.
         */
        """
        pass

    def set_cell(self, const_LMatrix3d_self, int_row, int_col, double_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_cell(const LMatrix3d self, int row, int col, double value)
        
        /**
         * Changes a particular element of the matrix.
         */
        """
        pass

    def set_col(self, const_LMatrix3d_self, int_col, const_LVecBase2d_v): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_col(const LMatrix3d self, int col, const LVecBase2d v)
        set_col(const LMatrix3d self, int col, const LVecBase3d v)
        
        /**
         * Replaces the indicated column of the matrix from a three-component vector.
         */
        
        /**
         * Replaces the indicated column of the matrix from a two-component vector,
         * ignoring the last row.
         */
        """
        pass

    def set_rotate_mat(self, const_LMatrix3d_self, double_angle): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_rotate_mat(const LMatrix3d self, double angle)
        set_rotate_mat(const LMatrix3d self, double angle, const LVecBase3d axis, int cs)
        
        /**
         * Fills mat with a matrix that rotates by the given angle in degrees
         * counterclockwise.
         */
        
        /**
         * Fills mat with a matrix that rotates by the given angle in degrees
         * counterclockwise about the indicated vector.
         */
        """
        pass

    def set_rotate_mat_normaxis(self, const_LMatrix3d_self, double_angle, const_LVecBase3d_axis, int_cs): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_rotate_mat_normaxis(const LMatrix3d self, double angle, const LVecBase3d axis, int cs)
        
        /**
         * Fills mat with a matrix that rotates by the given angle in degrees
         * counterclockwise about the indicated vector.  Assumes axis has been
         * normalized.
         */
        """
        pass

    def set_row(self, const_LMatrix3d_self, int_row, const_LVecBase2d_v): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_row(const LMatrix3d self, int row, const LVecBase2d v)
        set_row(const LMatrix3d self, int row, const LVecBase3d v)
        
        /**
         * Replaces the indicated row of the matrix from a three-component vector.
         */
        
        /**
         * Replaces the indicated row of the matrix from a two-component vector,
         * ignoring the last column.
         */
        """
        pass

    def set_scale_mat(self, const_LMatrix3d_self, const_LVecBase2d_scale): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_scale_mat(const LMatrix3d self, const LVecBase2d scale)
        set_scale_mat(const LMatrix3d self, const LVecBase3d scale)
        
        /**
         * Fills mat with a matrix that applies the indicated scale in each of the two
         * axes.
         */
        
        /**
         * Fills mat with a matrix that applies the indicated scale in each of the
         * three axes.
         */
        """
        pass

    def set_scale_shear_mat(self, const_LMatrix3d_self, const_LVecBase3d_scale, const_LVecBase3d_shear, int_cs): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_scale_shear_mat(const LMatrix3d self, const LVecBase3d scale, const LVecBase3d shear, int cs)
        
        /**
         * Fills mat with a matrix that applies the indicated scale and shear.
         */
        """
        pass

    def set_shear_mat(self, const_LMatrix3d_self, const_LVecBase3d_shear, int_cs): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_shear_mat(const LMatrix3d self, const LVecBase3d shear, int cs)
        
        /**
         * Fills mat with a matrix that applies the indicated shear in each of the
         * three planes.
         */
        """
        pass

    def set_translate_mat(self, const_LMatrix3d_self, const_LVecBase2d_trans): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_translate_mat(const LMatrix3d self, const LVecBase2d trans)
        
        /**
         * Fills mat with a matrix that applies the indicated translation.
         */
        """
        pass

    def shearMat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        shear_mat(const LVecBase3d shear)
        shear_mat(const LVecBase3d shear, int cs)
        shear_mat(double shxy, double shxz, double shyz, int cs)
        
        /**
         * Returns a matrix that applies the indicated shear in each of the three
         * planes.
         */
        
        /**
         * Returns a matrix that applies the indicated shear in each of the three
         * planes.
         */
        """
        pass

    def shear_mat(self, const_LVecBase3d_shear): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        shear_mat(const LVecBase3d shear)
        shear_mat(const LVecBase3d shear, int cs)
        shear_mat(double shxy, double shxz, double shyz, int cs)
        
        /**
         * Returns a matrix that applies the indicated shear in each of the three
         * planes.
         */
        
        /**
         * Returns a matrix that applies the indicated shear in each of the three
         * planes.
         */
        """
        pass

    def translateMat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        translate_mat(const LVecBase2d trans)
        translate_mat(double tx, double ty)
        
        /**
         * Returns a matrix that applies the indicated translation.
         */
        
        /**
         * Returns a matrix that applies the indicated translation.
         */
        """
        pass

    def translate_mat(self, const_LVecBase2d_trans): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        translate_mat(const LVecBase2d trans)
        translate_mat(double tx, double ty)
        
        /**
         * Returns a matrix that applies the indicated translation.
         */
        
        /**
         * Returns a matrix that applies the indicated translation.
         */
        """
        pass

    def transposeFrom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        transpose_from(const LMatrix3d self, const LMatrix3d other)
        
        /**
         *
         */
        """
        pass

    def transposeInPlace(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        transpose_in_place(const LMatrix3d self)
        
        /**
         *
         */
        """
        pass

    def transpose_from(self, const_LMatrix3d_self, const_LMatrix3d_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        transpose_from(const LMatrix3d self, const LMatrix3d other)
        
        /**
         *
         */
        """
        pass

    def transpose_in_place(self, const_LMatrix3d_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        transpose_in_place(const LMatrix3d self)
        
        /**
         *
         */
        """
        pass

    def write(self, LMatrix3d_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(LMatrix3d self, ostream out, int indent_level)
        
        /**
         *
         */
        """
        pass

    def writeDatagram(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        write_datagram(LMatrix3d self, Datagram destination)
        
        /**
         * Writes the matrix to the Datagram using add_stdfloat().  This is
         * appropriate when you want to write the matrix using the standard width
         * setting, especially when you are writing a bam file.
         */
        """
        pass

    def writeDatagramFixed(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        write_datagram_fixed(LMatrix3d self, Datagram destination)
        
        /**
         * Writes the matrix to the Datagram using add_float32() or add_float64(),
         * depending on the type of floats in the matrix, regardless of the setting of
         * Datagram::set_stdfloat_double().  This is appropriate when you want to
         * write a fixed-width value to the datagram, especially when you are not
         * writing a bam file.
         */
        """
        pass

    def write_datagram(self, LMatrix3d_self, Datagram_destination): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write_datagram(LMatrix3d self, Datagram destination)
        
        /**
         * Writes the matrix to the Datagram using add_stdfloat().  This is
         * appropriate when you want to write the matrix using the standard width
         * setting, especially when you are writing a bam file.
         */
        """
        pass

    def write_datagram_fixed(self, LMatrix3d_self, Datagram_destination): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write_datagram_fixed(LMatrix3d self, Datagram destination)
        
        /**
         * Writes the matrix to the Datagram using add_float32() or add_float64(),
         * depending on the type of floats in the matrix, regardless of the setting of
         * Datagram::set_stdfloat_double().  This is appropriate when you want to
         * write a fixed-width value to the datagram, especially when you are not
         * writing a bam file.
         */
        """
        pass

    def xform(self, LMatrix3d_self, const_LVecBase3d_v): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        xform(LMatrix3d self, const LVecBase3d v)
        
        /**
         * 3-component vector or point times matrix.
         */
        """
        pass

    def xformInPlace(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        xform_in_place(LMatrix3d self, LVecBase3d v)
        
        /**
         * 3-component vector or point times matrix.
         */
        """
        pass

    def xformPoint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        xform_point(LMatrix3d self, const LVecBase2d v)
        
        /**
         * The matrix transforms a 2-component point (including translation component)
         * and returns the result.  This assumes the matrix is an affine transform.
         */
        """
        pass

    def xformPointInPlace(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        xform_point_in_place(LMatrix3d self, LVecBase2d v)
        
        /**
         * The matrix transforms a 2-component point (including translation
         * component).  This assumes the matrix is an affine transform.
         */
        """
        pass

    def xformVec(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        xform_vec(LMatrix3d self, const LVecBase3d v)
        xform_vec(LMatrix3d self, const LVecBase2d v)
        
        /**
         * The matrix transforms a 2-component vector (without translation component)
         * and returns the result.  This assumes the matrix is an affine transform.
         */
        
        /**
         * The matrix transforms a 3-component vector and returns the result.  This
         * assumes the matrix is an orthonormal transform.
         *
         * In practice, this is the same computation as xform().
         */
        """
        pass

    def xformVecGeneral(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        xform_vec_general(LMatrix3d self, const LVecBase3d v)
        
        /**
         * The matrix transforms a 3-component vector (without translation component)
         * and returns the result, as a fully general operation.
         */
        """
        pass

    def xformVecGeneralInPlace(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        xform_vec_general_in_place(LMatrix3d self, LVecBase3d v)
        
        /**
         * The matrix transforms a 3-component vector (without translation component),
         * as a fully general operation.
         */
        """
        pass

    def xformVecInPlace(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        xform_vec_in_place(LMatrix3d self, LVecBase2d v)
        xform_vec_in_place(LMatrix3d self, LVecBase3d v)
        
        /**
         * The matrix transforms a 2-component vector (without translation component).
         * This assumes the matrix is an affine transform.
         */
        
        /**
         * The matrix transforms a 3-component vector.  This assumes the matrix is an
         * orthonormal transform.
         *
         * In practice, this is the same computation as xform().
         */
        """
        pass

    def xform_in_place(self, LMatrix3d_self, LVecBase3d_v): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        xform_in_place(LMatrix3d self, LVecBase3d v)
        
        /**
         * 3-component vector or point times matrix.
         */
        """
        pass

    def xform_point(self, LMatrix3d_self, const_LVecBase2d_v): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        xform_point(LMatrix3d self, const LVecBase2d v)
        
        /**
         * The matrix transforms a 2-component point (including translation component)
         * and returns the result.  This assumes the matrix is an affine transform.
         */
        """
        pass

    def xform_point_in_place(self, LMatrix3d_self, LVecBase2d_v): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        xform_point_in_place(LMatrix3d self, LVecBase2d v)
        
        /**
         * The matrix transforms a 2-component point (including translation
         * component).  This assumes the matrix is an affine transform.
         */
        """
        pass

    def xform_vec(self, LMatrix3d_self, const_LVecBase3d_v): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        xform_vec(LMatrix3d self, const LVecBase3d v)
        xform_vec(LMatrix3d self, const LVecBase2d v)
        
        /**
         * The matrix transforms a 2-component vector (without translation component)
         * and returns the result.  This assumes the matrix is an affine transform.
         */
        
        /**
         * The matrix transforms a 3-component vector and returns the result.  This
         * assumes the matrix is an orthonormal transform.
         *
         * In practice, this is the same computation as xform().
         */
        """
        pass

    def xform_vec_general(self, LMatrix3d_self, const_LVecBase3d_v): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        xform_vec_general(LMatrix3d self, const LVecBase3d v)
        
        /**
         * The matrix transforms a 3-component vector (without translation component)
         * and returns the result, as a fully general operation.
         */
        """
        pass

    def xform_vec_general_in_place(self, LMatrix3d_self, LVecBase3d_v): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        xform_vec_general_in_place(LMatrix3d self, LVecBase3d v)
        
        /**
         * The matrix transforms a 3-component vector (without translation component),
         * as a fully general operation.
         */
        """
        pass

    def xform_vec_in_place(self, LMatrix3d_self, LVecBase2d_v): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        xform_vec_in_place(LMatrix3d self, LVecBase2d v)
        xform_vec_in_place(LMatrix3d self, LVecBase3d v)
        
        /**
         * The matrix transforms a 2-component vector (without translation component).
         * This assumes the matrix is an affine transform.
         */
        
        /**
         * The matrix transforms a 3-component vector.  This assumes the matrix is an
         * orthonormal transform.
         *
         * In practice, this is the same computation as xform().
         */
        """
        pass

    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __iadd__(self, *args, **kwargs): # real signature unknown
        """ Return self+=value. """
        pass

    def __imul__(self, *args, **kwargs): # real signature unknown
        """ Return self*=value. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __isub__(self, *args, **kwargs): # real signature unknown
        """ Return self-=value. """
        pass

    def __itruediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/=value. """
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __reduce__(self, LMatrix3d_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        __reduce__(LMatrix3d self)
        """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    cols = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    rows = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    CRow = None # (!) real value is "<class 'panda3d.core.CRow'>"
    DtoolClassDict = {
        'CRow': None, # (!) real value is "<class 'panda3d.core.CRow'>"
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'Row': None, # (!) real value is "<class 'panda3d.core.Row'>"
        '__call__': None, # (!) real value is "<slot wrapper '__call__' of 'panda3d.core.LMatrix3d' objects>"
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.LMatrix3d' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.LMatrix3d' objects>"
        '__doc__': '/**\n * This is a 3-by-3 transform matrix.  It typically will represent either a\n * rotation-and-scale (no translation) matrix in 3-d, or a full affine matrix\n * (rotation, scale, translation) in 2-d, e.g.  for a texture matrix.\n */',
        '__eq__': None, # (!) real value is "<slot wrapper '__eq__' of 'panda3d.core.LMatrix3d' objects>"
        '__ge__': None, # (!) real value is "<slot wrapper '__ge__' of 'panda3d.core.LMatrix3d' objects>"
        '__getitem__': None, # (!) real value is "<slot wrapper '__getitem__' of 'panda3d.core.LMatrix3d' objects>"
        '__gt__': None, # (!) real value is "<slot wrapper '__gt__' of 'panda3d.core.LMatrix3d' objects>"
        '__hash__': None, # (!) real value is "<slot wrapper '__hash__' of 'panda3d.core.LMatrix3d' objects>"
        '__iadd__': None, # (!) real value is "<slot wrapper '__iadd__' of 'panda3d.core.LMatrix3d' objects>"
        '__imul__': None, # (!) real value is "<slot wrapper '__imul__' of 'panda3d.core.LMatrix3d' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.LMatrix3d' objects>"
        '__isub__': None, # (!) real value is "<slot wrapper '__isub__' of 'panda3d.core.LMatrix3d' objects>"
        '__itruediv__': None, # (!) real value is "<slot wrapper '__itruediv__' of 'panda3d.core.LMatrix3d' objects>"
        '__le__': None, # (!) real value is "<slot wrapper '__le__' of 'panda3d.core.LMatrix3d' objects>"
        '__len__': None, # (!) real value is "<slot wrapper '__len__' of 'panda3d.core.LMatrix3d' objects>"
        '__lt__': None, # (!) real value is "<slot wrapper '__lt__' of 'panda3d.core.LMatrix3d' objects>"
        '__mul__': None, # (!) real value is "<slot wrapper '__mul__' of 'panda3d.core.LMatrix3d' objects>"
        '__ne__': None, # (!) real value is "<slot wrapper '__ne__' of 'panda3d.core.LMatrix3d' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE3249E0>'
        '__reduce__': None, # (!) real value is "<method '__reduce__' of 'panda3d.core.LMatrix3d' objects>"
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.LMatrix3d' objects>"
        '__rmul__': None, # (!) real value is "<slot wrapper '__rmul__' of 'panda3d.core.LMatrix3d' objects>"
        '__rtruediv__': None, # (!) real value is "<slot wrapper '__rtruediv__' of 'panda3d.core.LMatrix3d' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.LMatrix3d' objects>"
        '__truediv__': None, # (!) real value is "<slot wrapper '__truediv__' of 'panda3d.core.LMatrix3d' objects>"
        'addHash': None, # (!) real value is "<method 'addHash' of 'panda3d.core.LMatrix3d' objects>"
        'add_hash': None, # (!) real value is "<method 'add_hash' of 'panda3d.core.LMatrix3d' objects>"
        'almostEqual': None, # (!) real value is "<method 'almostEqual' of 'panda3d.core.LMatrix3d' objects>"
        'almost_equal': None, # (!) real value is "<method 'almost_equal' of 'panda3d.core.LMatrix3d' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.LMatrix3d' objects>"
        'cols': None, # (!) real value is "<attribute 'cols' of 'panda3d.core.LMatrix3d' objects>"
        'compareTo': None, # (!) real value is "<method 'compareTo' of 'panda3d.core.LMatrix3d' objects>"
        'compare_to': None, # (!) real value is "<method 'compare_to' of 'panda3d.core.LMatrix3d' objects>"
        'componentwiseMult': None, # (!) real value is "<method 'componentwiseMult' of 'panda3d.core.LMatrix3d' objects>"
        'componentwise_mult': None, # (!) real value is "<method 'componentwise_mult' of 'panda3d.core.LMatrix3d' objects>"
        'convertMat': None, # (!) real value is '<staticmethod(<built-in method convertMat of type object at 0x00007FFCFE3249E0>)>'
        'convert_mat': None, # (!) real value is '<staticmethod(<built-in method convert_mat of type object at 0x00007FFCFE3249E0>)>'
        'determinant': None, # (!) real value is "<method 'determinant' of 'panda3d.core.LMatrix3d' objects>"
        'fill': None, # (!) real value is "<method 'fill' of 'panda3d.core.LMatrix3d' objects>"
        'getCell': None, # (!) real value is "<method 'getCell' of 'panda3d.core.LMatrix3d' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE3249E0>)>'
        'getCol': None, # (!) real value is "<method 'getCol' of 'panda3d.core.LMatrix3d' objects>"
        'getCol2': None, # (!) real value is "<method 'getCol2' of 'panda3d.core.LMatrix3d' objects>"
        'getCol2s': None, # (!) real value is "<method 'getCol2s' of 'panda3d.core.LMatrix3d' objects>"
        'getCols': None, # (!) real value is "<method 'getCols' of 'panda3d.core.LMatrix3d' objects>"
        'getHash': None, # (!) real value is "<method 'getHash' of 'panda3d.core.LMatrix3d' objects>"
        'getNumComponents': None, # (!) real value is "<method 'getNumComponents' of 'panda3d.core.LMatrix3d' objects>"
        'getRow': None, # (!) real value is "<method 'getRow' of 'panda3d.core.LMatrix3d' objects>"
        'getRow2': None, # (!) real value is "<method 'getRow2' of 'panda3d.core.LMatrix3d' objects>"
        'getRow2s': None, # (!) real value is "<method 'getRow2s' of 'panda3d.core.LMatrix3d' objects>"
        'getRows': None, # (!) real value is "<method 'getRows' of 'panda3d.core.LMatrix3d' objects>"
        'get_cell': None, # (!) real value is "<method 'get_cell' of 'panda3d.core.LMatrix3d' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE3249E0>)>'
        'get_col': None, # (!) real value is "<method 'get_col' of 'panda3d.core.LMatrix3d' objects>"
        'get_col2': None, # (!) real value is "<method 'get_col2' of 'panda3d.core.LMatrix3d' objects>"
        'get_col2s': None, # (!) real value is "<method 'get_col2s' of 'panda3d.core.LMatrix3d' objects>"
        'get_cols': None, # (!) real value is "<method 'get_cols' of 'panda3d.core.LMatrix3d' objects>"
        'get_hash': None, # (!) real value is "<method 'get_hash' of 'panda3d.core.LMatrix3d' objects>"
        'get_num_components': None, # (!) real value is "<method 'get_num_components' of 'panda3d.core.LMatrix3d' objects>"
        'get_row': None, # (!) real value is "<method 'get_row' of 'panda3d.core.LMatrix3d' objects>"
        'get_row2': None, # (!) real value is "<method 'get_row2' of 'panda3d.core.LMatrix3d' objects>"
        'get_row2s': None, # (!) real value is "<method 'get_row2s' of 'panda3d.core.LMatrix3d' objects>"
        'get_rows': None, # (!) real value is "<method 'get_rows' of 'panda3d.core.LMatrix3d' objects>"
        'identMat': None, # (!) real value is '<staticmethod(<built-in method identMat of type object at 0x00007FFCFE3249E0>)>'
        'ident_mat': None, # (!) real value is '<staticmethod(<built-in method ident_mat of type object at 0x00007FFCFE3249E0>)>'
        'invertFrom': None, # (!) real value is "<method 'invertFrom' of 'panda3d.core.LMatrix3d' objects>"
        'invertInPlace': None, # (!) real value is "<method 'invertInPlace' of 'panda3d.core.LMatrix3d' objects>"
        'invertTransposeFrom': None, # (!) real value is "<method 'invertTransposeFrom' of 'panda3d.core.LMatrix3d' objects>"
        'invert_from': None, # (!) real value is "<method 'invert_from' of 'panda3d.core.LMatrix3d' objects>"
        'invert_in_place': None, # (!) real value is "<method 'invert_in_place' of 'panda3d.core.LMatrix3d' objects>"
        'invert_transpose_from': None, # (!) real value is "<method 'invert_transpose_from' of 'panda3d.core.LMatrix3d' objects>"
        'isIdentity': None, # (!) real value is "<method 'isIdentity' of 'panda3d.core.LMatrix3d' objects>"
        'isNan': None, # (!) real value is "<method 'isNan' of 'panda3d.core.LMatrix3d' objects>"
        'is_identity': None, # (!) real value is "<method 'is_identity' of 'panda3d.core.LMatrix3d' objects>"
        'is_int': 0,
        'is_nan': None, # (!) real value is "<method 'is_nan' of 'panda3d.core.LMatrix3d' objects>"
        'multiply': None, # (!) real value is "<method 'multiply' of 'panda3d.core.LMatrix3d' objects>"
        'num_components': 9,
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.LMatrix3d' objects>"
        'readDatagram': None, # (!) real value is "<method 'readDatagram' of 'panda3d.core.LMatrix3d' objects>"
        'readDatagramFixed': None, # (!) real value is "<method 'readDatagramFixed' of 'panda3d.core.LMatrix3d' objects>"
        'read_datagram': None, # (!) real value is "<method 'read_datagram' of 'panda3d.core.LMatrix3d' objects>"
        'read_datagram_fixed': None, # (!) real value is "<method 'read_datagram_fixed' of 'panda3d.core.LMatrix3d' objects>"
        'rotateMat': None, # (!) real value is '<staticmethod(<built-in method rotateMat of type object at 0x00007FFCFE3249E0>)>'
        'rotateMatNormaxis': None, # (!) real value is '<staticmethod(<built-in method rotateMatNormaxis of type object at 0x00007FFCFE3249E0>)>'
        'rotate_mat': None, # (!) real value is '<staticmethod(<built-in method rotate_mat of type object at 0x00007FFCFE3249E0>)>'
        'rotate_mat_normaxis': None, # (!) real value is '<staticmethod(<built-in method rotate_mat_normaxis of type object at 0x00007FFCFE3249E0>)>'
        'rows': None, # (!) real value is "<attribute 'rows' of 'panda3d.core.LMatrix3d' objects>"
        'scaleMat': None, # (!) real value is '<staticmethod(<built-in method scaleMat of type object at 0x00007FFCFE3249E0>)>'
        'scaleShearMat': None, # (!) real value is '<staticmethod(<built-in method scaleShearMat of type object at 0x00007FFCFE3249E0>)>'
        'scale_mat': None, # (!) real value is '<staticmethod(<built-in method scale_mat of type object at 0x00007FFCFE3249E0>)>'
        'scale_shear_mat': None, # (!) real value is '<staticmethod(<built-in method scale_shear_mat of type object at 0x00007FFCFE3249E0>)>'
        'set': None, # (!) real value is "<method 'set' of 'panda3d.core.LMatrix3d' objects>"
        'setCell': None, # (!) real value is "<method 'setCell' of 'panda3d.core.LMatrix3d' objects>"
        'setCol': None, # (!) real value is "<method 'setCol' of 'panda3d.core.LMatrix3d' objects>"
        'setRotateMat': None, # (!) real value is "<method 'setRotateMat' of 'panda3d.core.LMatrix3d' objects>"
        'setRotateMatNormaxis': None, # (!) real value is "<method 'setRotateMatNormaxis' of 'panda3d.core.LMatrix3d' objects>"
        'setRow': None, # (!) real value is "<method 'setRow' of 'panda3d.core.LMatrix3d' objects>"
        'setScaleMat': None, # (!) real value is "<method 'setScaleMat' of 'panda3d.core.LMatrix3d' objects>"
        'setScaleShearMat': None, # (!) real value is "<method 'setScaleShearMat' of 'panda3d.core.LMatrix3d' objects>"
        'setShearMat': None, # (!) real value is "<method 'setShearMat' of 'panda3d.core.LMatrix3d' objects>"
        'setTranslateMat': None, # (!) real value is "<method 'setTranslateMat' of 'panda3d.core.LMatrix3d' objects>"
        'set_cell': None, # (!) real value is "<method 'set_cell' of 'panda3d.core.LMatrix3d' objects>"
        'set_col': None, # (!) real value is "<method 'set_col' of 'panda3d.core.LMatrix3d' objects>"
        'set_rotate_mat': None, # (!) real value is "<method 'set_rotate_mat' of 'panda3d.core.LMatrix3d' objects>"
        'set_rotate_mat_normaxis': None, # (!) real value is "<method 'set_rotate_mat_normaxis' of 'panda3d.core.LMatrix3d' objects>"
        'set_row': None, # (!) real value is "<method 'set_row' of 'panda3d.core.LMatrix3d' objects>"
        'set_scale_mat': None, # (!) real value is "<method 'set_scale_mat' of 'panda3d.core.LMatrix3d' objects>"
        'set_scale_shear_mat': None, # (!) real value is "<method 'set_scale_shear_mat' of 'panda3d.core.LMatrix3d' objects>"
        'set_shear_mat': None, # (!) real value is "<method 'set_shear_mat' of 'panda3d.core.LMatrix3d' objects>"
        'set_translate_mat': None, # (!) real value is "<method 'set_translate_mat' of 'panda3d.core.LMatrix3d' objects>"
        'shearMat': None, # (!) real value is '<staticmethod(<built-in method shearMat of type object at 0x00007FFCFE3249E0>)>'
        'shear_mat': None, # (!) real value is '<staticmethod(<built-in method shear_mat of type object at 0x00007FFCFE3249E0>)>'
        'translateMat': None, # (!) real value is '<staticmethod(<built-in method translateMat of type object at 0x00007FFCFE3249E0>)>'
        'translate_mat': None, # (!) real value is '<staticmethod(<built-in method translate_mat of type object at 0x00007FFCFE3249E0>)>'
        'transposeFrom': None, # (!) real value is "<method 'transposeFrom' of 'panda3d.core.LMatrix3d' objects>"
        'transposeInPlace': None, # (!) real value is "<method 'transposeInPlace' of 'panda3d.core.LMatrix3d' objects>"
        'transpose_from': None, # (!) real value is "<method 'transpose_from' of 'panda3d.core.LMatrix3d' objects>"
        'transpose_in_place': None, # (!) real value is "<method 'transpose_in_place' of 'panda3d.core.LMatrix3d' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.LMatrix3d' objects>"
        'writeDatagram': None, # (!) real value is "<method 'writeDatagram' of 'panda3d.core.LMatrix3d' objects>"
        'writeDatagramFixed': None, # (!) real value is "<method 'writeDatagramFixed' of 'panda3d.core.LMatrix3d' objects>"
        'write_datagram': None, # (!) real value is "<method 'write_datagram' of 'panda3d.core.LMatrix3d' objects>"
        'write_datagram_fixed': None, # (!) real value is "<method 'write_datagram_fixed' of 'panda3d.core.LMatrix3d' objects>"
        'xform': None, # (!) real value is "<method 'xform' of 'panda3d.core.LMatrix3d' objects>"
        'xformInPlace': None, # (!) real value is "<method 'xformInPlace' of 'panda3d.core.LMatrix3d' objects>"
        'xformPoint': None, # (!) real value is "<method 'xformPoint' of 'panda3d.core.LMatrix3d' objects>"
        'xformPointInPlace': None, # (!) real value is "<method 'xformPointInPlace' of 'panda3d.core.LMatrix3d' objects>"
        'xformVec': None, # (!) real value is "<method 'xformVec' of 'panda3d.core.LMatrix3d' objects>"
        'xformVecGeneral': None, # (!) real value is "<method 'xformVecGeneral' of 'panda3d.core.LMatrix3d' objects>"
        'xformVecGeneralInPlace': None, # (!) real value is "<method 'xformVecGeneralInPlace' of 'panda3d.core.LMatrix3d' objects>"
        'xformVecInPlace': None, # (!) real value is "<method 'xformVecInPlace' of 'panda3d.core.LMatrix3d' objects>"
        'xform_in_place': None, # (!) real value is "<method 'xform_in_place' of 'panda3d.core.LMatrix3d' objects>"
        'xform_point': None, # (!) real value is "<method 'xform_point' of 'panda3d.core.LMatrix3d' objects>"
        'xform_point_in_place': None, # (!) real value is "<method 'xform_point_in_place' of 'panda3d.core.LMatrix3d' objects>"
        'xform_vec': None, # (!) real value is "<method 'xform_vec' of 'panda3d.core.LMatrix3d' objects>"
        'xform_vec_general': None, # (!) real value is "<method 'xform_vec_general' of 'panda3d.core.LMatrix3d' objects>"
        'xform_vec_general_in_place': None, # (!) real value is "<method 'xform_vec_general_in_place' of 'panda3d.core.LMatrix3d' objects>"
        'xform_vec_in_place': None, # (!) real value is "<method 'xform_vec_in_place' of 'panda3d.core.LMatrix3d' objects>"
    }
    is_int = 0
    num_components = 9
    Row = None # (!) real value is "<class 'panda3d.core.Row'>"


