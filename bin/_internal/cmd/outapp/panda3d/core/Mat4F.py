# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class Mat4F(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This is a 4-by-4 transform matrix.
     */
    """
    def accumulate(self, const_LMatrix4f_self, const_LMatrix4f_other, float_weight): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        accumulate(const LMatrix4f self, const LMatrix4f other, float weight)
        
        /**
         * Computes `(*this) += other * weight`.
         */
        """
        pass

    def addHash(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_hash(LMatrix4f self, int hash)
        add_hash(LMatrix4f self, int hash, float threshold)
        
        /**
         * Adds the vector into the running hash.
         */
        
        /**
         * Adds the vector into the running hash.
         */
        """
        pass

    def add_hash(self, LMatrix4f_self, int_hash): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_hash(LMatrix4f self, int hash)
        add_hash(LMatrix4f self, int hash, float threshold)
        
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
        almost_equal(LMatrix4f self, const LMatrix4f other)
        almost_equal(LMatrix4f self, const LMatrix4f other, float threshold)
        
        /**
         * Returns true if two matrices are memberwise equal within a default
         * tolerance based on the numeric type.
         */
        
        /**
         * Returns true if two matrices are memberwise equal within a specified
         * tolerance.  This is faster than the equivalence operator as this doesn't
         * have to guarantee that it is transitive.
         */
        """
        pass

    def almost_equal(self, LMatrix4f_self, const_LMatrix4f_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        almost_equal(LMatrix4f self, const LMatrix4f other)
        almost_equal(LMatrix4f self, const LMatrix4f other, float threshold)
        
        /**
         * Returns true if two matrices are memberwise equal within a default
         * tolerance based on the numeric type.
         */
        
        /**
         * Returns true if two matrices are memberwise equal within a specified
         * tolerance.  This is faster than the equivalence operator as this doesn't
         * have to guarantee that it is transitive.
         */
        """
        pass

    def assign(self, const_LMatrix4f_self, const_UnalignedLMatrix4f_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const LMatrix4f self, const UnalignedLMatrix4f other)
        assign(const LMatrix4f self, const LMatrix4f other)
        assign(const LMatrix4f self, float fill_value)
        
        /**
         *
         */
        
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
        compare_to(LMatrix4f self, const LMatrix4f other)
        compare_to(LMatrix4f self, const LMatrix4f other, float threshold)
        
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

    def compare_to(self, LMatrix4f_self, const_LMatrix4f_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        compare_to(LMatrix4f self, const LMatrix4f other)
        compare_to(LMatrix4f self, const LMatrix4f other, float threshold)
        
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
        componentwise_mult(const LMatrix4f self, const LMatrix4f other)
        
        /**
         *
         */
        """
        pass

    def componentwise_mult(self, const_LMatrix4f_self, const_LMatrix4f_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        componentwise_mult(const LMatrix4f self, const LMatrix4f other)
        
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

    def fill(self, const_LMatrix4f_self, float_fill_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        fill(const LMatrix4f self, float fill_value)
        
        /**
         * Sets each element of the matrix to the indicated fill_value.  This is of
         * questionable value, but is sometimes useful when initializing to zero.
         */
        """
        pass

    def getCell(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_cell(LMatrix4f self, int row, int col)
        
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
        get_col(LMatrix4f self, int col)
        
        /**
         * Retrieves the indicated column of the matrix as a 4-component vector.
         */
        """
        pass

    def getCol3(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_col3(LMatrix4f self, int col)
        
        /**
         * Retrieves the indicated column of the matrix as a 3-component vector,
         * ignoring the last row.
         */
        """
        pass

    def getCols(self, *args, **kwargs): # real signature unknown
        pass

    def getHash(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_hash(LMatrix4f self)
        get_hash(LMatrix4f self, float threshold)
        
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
        get_num_components(LMatrix4f self)
        
        /**
         * Returns the number of elements in the matrix, 16.
         */
        """
        pass

    def getRow(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_row(LMatrix4f self, int row)
        get_row(LMatrix4f self, LVecBase4f result_vec, int row)
        
        // these versions inline better
        
        /**
         * Retrieves the indicated row of the matrix as a 4-component vector.
         */
        
        /**
         * Stores the indicated row of the matrix as a 4-component vector.
         */
        """
        pass

    def getRow3(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_row3(LMatrix4f self, int row)
        get_row3(LMatrix4f self, LVecBase3f result_vec, int row)
        
        /**
         * Retrieves the row column of the matrix as a 3-component vector, ignoring
         * the last column.
         */
        
        /**
         * Stores the row column of the matrix as a 3-component vector, ignoring the
         * last column.
         */
        """
        pass

    def getRow3s(self, *args, **kwargs): # real signature unknown
        pass

    def getRows(self, *args, **kwargs): # real signature unknown
        pass

    def getUpper3(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_upper_3(LMatrix4f self)
        
        /**
         * Retrieves the upper 3x3 submatrix.
         */
        """
        pass

    def get_cell(self, LMatrix4f_self, int_row, int_col): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_cell(LMatrix4f self, int row, int col)
        
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

    def get_col(self, LMatrix4f_self, int_col): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_col(LMatrix4f self, int col)
        
        /**
         * Retrieves the indicated column of the matrix as a 4-component vector.
         */
        """
        pass

    def get_col3(self, LMatrix4f_self, int_col): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_col3(LMatrix4f self, int col)
        
        /**
         * Retrieves the indicated column of the matrix as a 3-component vector,
         * ignoring the last row.
         */
        """
        pass

    def get_cols(self, *args, **kwargs): # real signature unknown
        pass

    def get_hash(self, LMatrix4f_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_hash(LMatrix4f self)
        get_hash(LMatrix4f self, float threshold)
        
        /**
         * Returns a suitable hash for phash_map.
         */
        
        /**
         * Returns a suitable hash for phash_map.
         */
        """
        pass

    def get_num_components(self, LMatrix4f_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_components(LMatrix4f self)
        
        /**
         * Returns the number of elements in the matrix, 16.
         */
        """
        pass

    def get_row(self, LMatrix4f_self, int_row): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_row(LMatrix4f self, int row)
        get_row(LMatrix4f self, LVecBase4f result_vec, int row)
        
        // these versions inline better
        
        /**
         * Retrieves the indicated row of the matrix as a 4-component vector.
         */
        
        /**
         * Stores the indicated row of the matrix as a 4-component vector.
         */
        """
        pass

    def get_row3(self, LMatrix4f_self, int_row): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_row3(LMatrix4f self, int row)
        get_row3(LMatrix4f self, LVecBase3f result_vec, int row)
        
        /**
         * Retrieves the row column of the matrix as a 3-component vector, ignoring
         * the last column.
         */
        
        /**
         * Stores the row column of the matrix as a 3-component vector, ignoring the
         * last column.
         */
        """
        pass

    def get_row3s(self, *args, **kwargs): # real signature unknown
        pass

    def get_rows(self, *args, **kwargs): # real signature unknown
        pass

    def get_upper_3(self, LMatrix4f_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_upper_3(LMatrix4f self)
        
        /**
         * Retrieves the upper 3x3 submatrix.
         */
        """
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

    def invertAffineFrom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        invert_affine_from(const LMatrix4f self, const LMatrix4f other)
        
        // bugbug: we could optimize this for rotationscaletranslation matrices
        // (transpose upper 3x3 and take negative of translation component)
        """
        pass

    def invertFrom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        invert_from(const LMatrix4f self, const LMatrix4f other)
        
        /**
         * Computes the inverse of the other matrix, and stores the result in this
         * matrix.  This is a fully general operation and makes no assumptions about
         * the type of transform represented by the matrix.
         *
         * The other matrix must be a different object than this matrix.  However, if
         * you need to invert a matrix in place, see invert_in_place.
         *
         * The return value is true if the matrix was successfully inverted, false if
         * the was a singularity.
         */
        """
        pass

    def invertInPlace(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        invert_in_place(const LMatrix4f self)
        
        /**
         * Inverts the current matrix.  Returns true if the inverse is successful,
         * false if the matrix was singular.
         */
        """
        pass

    def invert_affine_from(self, const_LMatrix4f_self, const_LMatrix4f_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        invert_affine_from(const LMatrix4f self, const LMatrix4f other)
        
        // bugbug: we could optimize this for rotationscaletranslation matrices
        // (transpose upper 3x3 and take negative of translation component)
        """
        pass

    def invert_from(self, const_LMatrix4f_self, const_LMatrix4f_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        invert_from(const LMatrix4f self, const LMatrix4f other)
        
        /**
         * Computes the inverse of the other matrix, and stores the result in this
         * matrix.  This is a fully general operation and makes no assumptions about
         * the type of transform represented by the matrix.
         *
         * The other matrix must be a different object than this matrix.  However, if
         * you need to invert a matrix in place, see invert_in_place.
         *
         * The return value is true if the matrix was successfully inverted, false if
         * the was a singularity.
         */
        """
        pass

    def invert_in_place(self, const_LMatrix4f_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        invert_in_place(const LMatrix4f self)
        
        /**
         * Inverts the current matrix.  Returns true if the inverse is successful,
         * false if the matrix was singular.
         */
        """
        pass

    def isIdentity(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_identity(LMatrix4f self)
        
        /**
         * Returns true if this is (close enough to) the identity matrix, false
         * otherwise.
         */
        """
        pass

    def isNan(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_nan(LMatrix4f self)
        
        /**
         * Returns true if any component of the matrix is not-a-number, false
         * otherwise.
         */
        """
        pass

    def is_identity(self, LMatrix4f_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_identity(LMatrix4f self)
        
        /**
         * Returns true if this is (close enough to) the identity matrix, false
         * otherwise.
         */
        """
        pass

    def is_nan(self, LMatrix4f_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_nan(LMatrix4f self)
        
        /**
         * Returns true if any component of the matrix is not-a-number, false
         * otherwise.
         */
        """
        pass

    def multiply(self, const_LMatrix4f_self, const_LMatrix4f_other1, const_LMatrix4f_other2): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        multiply(const LMatrix4f self, const LMatrix4f other1, const LMatrix4f other2)
        
        // this = other1 * other2
        
        // this = other1 * other2
        """
        pass

    def onesMat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        ones_mat()
        
        /**
         * Returns an matrix filled with ones.
         */
        """
        pass

    def ones_mat(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        ones_mat()
        
        /**
         * Returns an matrix filled with ones.
         */
        """
        pass

    def output(self, LMatrix4f_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(LMatrix4f self, ostream out)
        
        /**
         *
         */
        """
        pass

    def readDatagram(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        read_datagram(const LMatrix4f self, DatagramIterator source)
        
        /**
         * Reads the matrix from the Datagram using get_stdfloat().
         */
        """
        pass

    def readDatagramFixed(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        read_datagram_fixed(const LMatrix4f self, DatagramIterator scan)
        
        /**
         * Reads the matrix from the Datagram using get_float32() or get_float64().
         * See write_datagram_fixed().
         */
        """
        pass

    def read_datagram(self, const_LMatrix4f_self, DatagramIterator_source): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        read_datagram(const LMatrix4f self, DatagramIterator source)
        
        /**
         * Reads the matrix from the Datagram using get_stdfloat().
         */
        """
        pass

    def read_datagram_fixed(self, const_LMatrix4f_self, DatagramIterator_scan): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        read_datagram_fixed(const LMatrix4f self, DatagramIterator scan)
        
        /**
         * Reads the matrix from the Datagram using get_float32() or get_float64().
         * See write_datagram_fixed().
         */
        """
        pass

    def rotateMat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        rotate_mat(float angle, const LVecBase3f axis, int cs)
        
        /**
         * Returns a matrix that rotates by the given angle in degrees
         * counterclockwise about the indicated vector.
         */
        """
        pass

    def rotateMatNormaxis(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        rotate_mat_normaxis(float angle, const LVecBase3f axis, int cs)
        
        /**
         * Returns a matrix that rotates by the given angle in degrees
         * counterclockwise about the indicated vector.  Assumes axis has been
         * prenormalized.
         */
        """
        pass

    def rotate_mat(self, float_angle, const_LVecBase3f_axis, int_cs): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        rotate_mat(float angle, const LVecBase3f axis, int cs)
        
        /**
         * Returns a matrix that rotates by the given angle in degrees
         * counterclockwise about the indicated vector.
         */
        """
        pass

    def rotate_mat_normaxis(self, float_angle, const_LVecBase3f_axis, int_cs): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        rotate_mat_normaxis(float angle, const LVecBase3f axis, int cs)
        
        /**
         * Returns a matrix that rotates by the given angle in degrees
         * counterclockwise about the indicated vector.  Assumes axis has been
         * prenormalized.
         */
        """
        pass

    def scaleMat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        scale_mat(const LVecBase3f scale)
        scale_mat(float scale)
        scale_mat(float sx, float sy, float sz)
        
        /**
         * Returns a matrix that applies the indicated scale in each of the three
         * axes.
         */
        
        /**
         * Returns a matrix that applies the indicated scale in each of the three
         * axes.
         */
        
        /**
         * Returns a matrix that applies the indicated uniform scale.
         */
        """
        pass

    def scaleShearMat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        scale_shear_mat(const LVecBase3f scale, const LVecBase3f shear)
        scale_shear_mat(const LVecBase3f scale, const LVecBase3f shear, int cs)
        scale_shear_mat(float sx, float sy, float sz, float shxy, float shxz, float shyz, int cs)
        
        /**
         * Returns a matrix that applies the indicated scale and shear.
         */
        
        /**
         * Returns a matrix that applies the indicated scale and shear.
         */
        """
        pass

    def scale_mat(self, const_LVecBase3f_scale): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        scale_mat(const LVecBase3f scale)
        scale_mat(float scale)
        scale_mat(float sx, float sy, float sz)
        
        /**
         * Returns a matrix that applies the indicated scale in each of the three
         * axes.
         */
        
        /**
         * Returns a matrix that applies the indicated scale in each of the three
         * axes.
         */
        
        /**
         * Returns a matrix that applies the indicated uniform scale.
         */
        """
        pass

    def scale_shear_mat(self, const_LVecBase3f_scale, const_LVecBase3f_shear): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        scale_shear_mat(const LVecBase3f scale, const LVecBase3f shear)
        scale_shear_mat(const LVecBase3f scale, const LVecBase3f shear, int cs)
        scale_shear_mat(float sx, float sy, float sz, float shxy, float shxz, float shyz, int cs)
        
        /**
         * Returns a matrix that applies the indicated scale and shear.
         */
        
        /**
         * Returns a matrix that applies the indicated scale and shear.
         */
        """
        pass

    def set(self, const_LMatrix4f_self, float_e00, float_e01, float_e02, float_e03, float_e10, float_e11, float_e12, float_e13, float_e20, float_e21, float_e22, float_e23, float_e30, float_e31, float_e32, float_e33): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set(const LMatrix4f self, float e00, float e01, float e02, float e03, float e10, float e11, float e12, float e13, float e20, float e21, float e22, float e23, float e30, float e31, float e32, float e33)
        
        /**
         *
         */
        """
        pass

    def setCell(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_cell(const LMatrix4f self, int row, int col, float value)
        
        /**
         * Changes a particular element of the matrix.
         */
        """
        pass

    def setCol(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_col(const LMatrix4f self, int col, const LVecBase3f v)
        set_col(const LMatrix4f self, int col, const LVecBase4f v)
        
        /**
         * Replaces the indicated column of the matrix.
         */
        
        /**
         * Replaces the indicated column of the matrix with the indicated 3-component
         * vector, ignoring the last row.
         */
        """
        pass

    def setRotateMat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_rotate_mat(const LMatrix4f self, float angle, const LVecBase3f axis, int cs)
        
        /**
         * Sets mat to a matrix that rotates by the given angle in degrees
         * counterclockwise about the indicated vector.
         */
        """
        pass

    def setRotateMatNormaxis(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_rotate_mat_normaxis(const LMatrix4f self, float angle, const LVecBase3f axis, int cs)
        
        /**
         * Fills mat with a matrix that rotates by the given angle in degrees
         * counterclockwise about the indicated vector.  Assumes axis has been
         * prenormalized.
         */
        """
        pass

    def setRow(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_row(const LMatrix4f self, int row, const LVecBase3f v)
        set_row(const LMatrix4f self, int row, const LVecBase4f v)
        
        /**
         * Replaces the indicated row of the matrix.
         */
        
        /**
         * Replaces the indicated row of the matrix with the indicated 3-component
         * vector, ignoring the last column.
         */
        """
        pass

    def setScaleMat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_scale_mat(const LMatrix4f self, const LVecBase3f scale)
        
        /**
         * Fills mat with a matrix that applies the indicated scale in each of the
         * three axes.
         */
        """
        pass

    def setScaleShearMat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_scale_shear_mat(const LMatrix4f self, const LVecBase3f scale, const LVecBase3f shear, int cs)
        
        /**
         * Fills mat with a matrix that applies the indicated scale and shear.
         */
        """
        pass

    def setShearMat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_shear_mat(const LMatrix4f self, const LVecBase3f shear, int cs)
        
        /**
         * Fills mat with a matrix that applies the indicated shear in each of the
         * three planes.
         */
        """
        pass

    def setTranslateMat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_translate_mat(const LMatrix4f self, const LVecBase3f trans)
        
        /**
         * Fills mat with a matrix that applies the indicated translation.
         */
        """
        pass

    def setUpper3(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_upper_3(const LMatrix4f self, const LMatrix3f upper3)
        
        // Get and set the upper 3x3 rotation matrix.
        
        /**
         * Sets the upper 3x3 submatrix.
         */
        """
        pass

    def set_cell(self, const_LMatrix4f_self, int_row, int_col, float_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_cell(const LMatrix4f self, int row, int col, float value)
        
        /**
         * Changes a particular element of the matrix.
         */
        """
        pass

    def set_col(self, const_LMatrix4f_self, int_col, const_LVecBase3f_v): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_col(const LMatrix4f self, int col, const LVecBase3f v)
        set_col(const LMatrix4f self, int col, const LVecBase4f v)
        
        /**
         * Replaces the indicated column of the matrix.
         */
        
        /**
         * Replaces the indicated column of the matrix with the indicated 3-component
         * vector, ignoring the last row.
         */
        """
        pass

    def set_rotate_mat(self, const_LMatrix4f_self, float_angle, const_LVecBase3f_axis, int_cs): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_rotate_mat(const LMatrix4f self, float angle, const LVecBase3f axis, int cs)
        
        /**
         * Sets mat to a matrix that rotates by the given angle in degrees
         * counterclockwise about the indicated vector.
         */
        """
        pass

    def set_rotate_mat_normaxis(self, const_LMatrix4f_self, float_angle, const_LVecBase3f_axis, int_cs): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_rotate_mat_normaxis(const LMatrix4f self, float angle, const LVecBase3f axis, int cs)
        
        /**
         * Fills mat with a matrix that rotates by the given angle in degrees
         * counterclockwise about the indicated vector.  Assumes axis has been
         * prenormalized.
         */
        """
        pass

    def set_row(self, const_LMatrix4f_self, int_row, const_LVecBase3f_v): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_row(const LMatrix4f self, int row, const LVecBase3f v)
        set_row(const LMatrix4f self, int row, const LVecBase4f v)
        
        /**
         * Replaces the indicated row of the matrix.
         */
        
        /**
         * Replaces the indicated row of the matrix with the indicated 3-component
         * vector, ignoring the last column.
         */
        """
        pass

    def set_scale_mat(self, const_LMatrix4f_self, const_LVecBase3f_scale): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_scale_mat(const LMatrix4f self, const LVecBase3f scale)
        
        /**
         * Fills mat with a matrix that applies the indicated scale in each of the
         * three axes.
         */
        """
        pass

    def set_scale_shear_mat(self, const_LMatrix4f_self, const_LVecBase3f_scale, const_LVecBase3f_shear, int_cs): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_scale_shear_mat(const LMatrix4f self, const LVecBase3f scale, const LVecBase3f shear, int cs)
        
        /**
         * Fills mat with a matrix that applies the indicated scale and shear.
         */
        """
        pass

    def set_shear_mat(self, const_LMatrix4f_self, const_LVecBase3f_shear, int_cs): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_shear_mat(const LMatrix4f self, const LVecBase3f shear, int cs)
        
        /**
         * Fills mat with a matrix that applies the indicated shear in each of the
         * three planes.
         */
        """
        pass

    def set_translate_mat(self, const_LMatrix4f_self, const_LVecBase3f_trans): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_translate_mat(const LMatrix4f self, const LVecBase3f trans)
        
        /**
         * Fills mat with a matrix that applies the indicated translation.
         */
        """
        pass

    def set_upper_3(self, const_LMatrix4f_self, const_LMatrix3f_upper3): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_upper_3(const LMatrix4f self, const LMatrix3f upper3)
        
        // Get and set the upper 3x3 rotation matrix.
        
        /**
         * Sets the upper 3x3 submatrix.
         */
        """
        pass

    def shearMat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        shear_mat(const LVecBase3f shear)
        shear_mat(const LVecBase3f shear, int cs)
        shear_mat(float shxy, float shxz, float shyz, int cs)
        
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

    def shear_mat(self, const_LVecBase3f_shear): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        shear_mat(const LVecBase3f shear)
        shear_mat(const LVecBase3f shear, int cs)
        shear_mat(float shxy, float shxz, float shyz, int cs)
        
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
        translate_mat(const LVecBase3f trans)
        translate_mat(float tx, float ty, float tz)
        
        /**
         * Returns a matrix that applies the indicated translation.
         */
        
        /**
         * Returns a matrix that applies the indicated translation.
         */
        """
        pass

    def translate_mat(self, const_LVecBase3f_trans): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        translate_mat(const LVecBase3f trans)
        translate_mat(float tx, float ty, float tz)
        
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
        transpose_from(const LMatrix4f self, const LMatrix4f other)
        
        /**
         *
         */
        """
        pass

    def transposeInPlace(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        transpose_in_place(const LMatrix4f self)
        
        /**
         *
         */
        """
        pass

    def transpose_from(self, const_LMatrix4f_self, const_LMatrix4f_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        transpose_from(const LMatrix4f self, const LMatrix4f other)
        
        /**
         *
         */
        """
        pass

    def transpose_in_place(self, const_LMatrix4f_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        transpose_in_place(const LMatrix4f self)
        
        /**
         *
         */
        """
        pass

    def write(self, LMatrix4f_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(LMatrix4f self, ostream out, int indent_level)
        
        /**
         *
         */
        """
        pass

    def writeDatagram(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        write_datagram(LMatrix4f self, Datagram destination)
        
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
        write_datagram_fixed(LMatrix4f self, Datagram destination)
        
        /**
         * Writes the matrix to the Datagram using add_float32() or add_float64(),
         * depending on the type of floats in the matrix, regardless of the setting of
         * Datagram::set_stdfloat_double().  This is appropriate when you want to
         * write a fixed-width value to the datagram, especially when you are not
         * writing a bam file.
         */
        """
        pass

    def write_datagram(self, LMatrix4f_self, Datagram_destination): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write_datagram(LMatrix4f self, Datagram destination)
        
        /**
         * Writes the matrix to the Datagram using add_stdfloat().  This is
         * appropriate when you want to write the matrix using the standard width
         * setting, especially when you are writing a bam file.
         */
        """
        pass

    def write_datagram_fixed(self, LMatrix4f_self, Datagram_destination): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write_datagram_fixed(LMatrix4f self, Datagram destination)
        
        /**
         * Writes the matrix to the Datagram using add_float32() or add_float64(),
         * depending on the type of floats in the matrix, regardless of the setting of
         * Datagram::set_stdfloat_double().  This is appropriate when you want to
         * write a fixed-width value to the datagram, especially when you are not
         * writing a bam file.
         */
        """
        pass

    def xform(self, LMatrix4f_self, const_LVecBase4f_v): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        xform(LMatrix4f self, const LVecBase4f v)
        
        /**
         * 4-component vector or point times matrix.  This is a fully general
         * operation.
         */
        """
        pass

    def xformInPlace(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        xform_in_place(LMatrix4f self, LVecBase4f v)
        
        /**
         * 4-component vector or point times matrix.  This is a fully general
         * operation.
         */
        """
        pass

    def xformPoint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        xform_point(LMatrix4f self, const LVecBase3f v)
        
        /**
         * The matrix transforms a 3-component point (including translation component)
         * and returns the result.  This assumes the matrix is an affine transform.
         */
        """
        pass

    def xformPointGeneral(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        xform_point_general(LMatrix4f self, const LVecBase3f v)
        
        /**
         * The matrix transforms a 3-component point (including translation component)
         * and returns the result, as a fully general operation.
         */
        """
        pass

    def xformPointGeneralInPlace(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        xform_point_general_in_place(LMatrix4f self, LVecBase3f v)
        
        /**
         * The matrix transforms a 3-component point (including translation
         * component), as a fully general operation.
         */
        """
        pass

    def xformPointInPlace(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        xform_point_in_place(LMatrix4f self, LVecBase3f v)
        
        /**
         * The matrix transforms a 3-component point (including translation
         * component).  This assumes the matrix is an affine transform.
         */
        """
        pass

    def xformVec(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        xform_vec(LMatrix4f self, const LVecBase3f v)
        
        /**
         * The matrix transforms a 3-component vector (without translation component)
         * and returns the result.  This assumes the matrix is an orthonormal
         * transform.
         */
        """
        pass

    def xformVecGeneral(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        xform_vec_general(LMatrix4f self, const LVecBase3f v)
        
        /**
         * The matrix transforms a 3-component vector (without translation component)
         * and returns the result, as a fully general operation.
         */
        """
        pass

    def xformVecGeneralInPlace(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        xform_vec_general_in_place(LMatrix4f self, LVecBase3f v)
        
        /**
         * The matrix transforms a 3-component vector (without translation component),
         * as a fully general operation.
         */
        """
        pass

    def xformVecInPlace(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        xform_vec_in_place(LMatrix4f self, LVecBase3f v)
        
        /**
         * The matrix transforms a 3-component vector (without translation component).
         * This assumes the matrix is an orthonormal transform.
         */
        """
        pass

    def xform_in_place(self, LMatrix4f_self, LVecBase4f_v): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        xform_in_place(LMatrix4f self, LVecBase4f v)
        
        /**
         * 4-component vector or point times matrix.  This is a fully general
         * operation.
         */
        """
        pass

    def xform_point(self, LMatrix4f_self, const_LVecBase3f_v): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        xform_point(LMatrix4f self, const LVecBase3f v)
        
        /**
         * The matrix transforms a 3-component point (including translation component)
         * and returns the result.  This assumes the matrix is an affine transform.
         */
        """
        pass

    def xform_point_general(self, LMatrix4f_self, const_LVecBase3f_v): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        xform_point_general(LMatrix4f self, const LVecBase3f v)
        
        /**
         * The matrix transforms a 3-component point (including translation component)
         * and returns the result, as a fully general operation.
         */
        """
        pass

    def xform_point_general_in_place(self, LMatrix4f_self, LVecBase3f_v): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        xform_point_general_in_place(LMatrix4f self, LVecBase3f v)
        
        /**
         * The matrix transforms a 3-component point (including translation
         * component), as a fully general operation.
         */
        """
        pass

    def xform_point_in_place(self, LMatrix4f_self, LVecBase3f_v): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        xform_point_in_place(LMatrix4f self, LVecBase3f v)
        
        /**
         * The matrix transforms a 3-component point (including translation
         * component).  This assumes the matrix is an affine transform.
         */
        """
        pass

    def xform_vec(self, LMatrix4f_self, const_LVecBase3f_v): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        xform_vec(LMatrix4f self, const LVecBase3f v)
        
        /**
         * The matrix transforms a 3-component vector (without translation component)
         * and returns the result.  This assumes the matrix is an orthonormal
         * transform.
         */
        """
        pass

    def xform_vec_general(self, LMatrix4f_self, const_LVecBase3f_v): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        xform_vec_general(LMatrix4f self, const LVecBase3f v)
        
        /**
         * The matrix transforms a 3-component vector (without translation component)
         * and returns the result, as a fully general operation.
         */
        """
        pass

    def xform_vec_general_in_place(self, LMatrix4f_self, LVecBase3f_v): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        xform_vec_general_in_place(LMatrix4f self, LVecBase3f v)
        
        /**
         * The matrix transforms a 3-component vector (without translation component),
         * as a fully general operation.
         */
        """
        pass

    def xform_vec_in_place(self, LMatrix4f_self, LVecBase3f_v): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        xform_vec_in_place(LMatrix4f self, LVecBase3f v)
        
        /**
         * The matrix transforms a 3-component vector (without translation component).
         * This assumes the matrix is an orthonormal transform.
         */
        """
        pass

    def yToZUpMat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        y_to_z_up_mat()
        
        /**
         * Returns a matrix that transforms from the Y-up coordinate system to the
         * Z-up coordinate system.
         */
        """
        pass

    def y_to_z_up_mat(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        y_to_z_up_mat()
        
        /**
         * Returns a matrix that transforms from the Y-up coordinate system to the
         * Z-up coordinate system.
         */
        """
        pass

    def zerosMat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        zeros_mat()
        
        /**
         * Returns an matrix filled with zeros.
         */
        """
        pass

    def zeros_mat(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        zeros_mat()
        
        /**
         * Returns an matrix filled with zeros.
         */
        """
        pass

    def zToYUpMat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        z_to_y_up_mat()
        
        /**
         * Returns a matrix that transforms from the Y-up coordinate system to the
         * Z-up coordinate system.
         */
        """
        pass

    def z_to_y_up_mat(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        z_to_y_up_mat()
        
        /**
         * Returns a matrix that transforms from the Y-up coordinate system to the
         * Z-up coordinate system.
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

    def __reduce__(self, LMatrix4f_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        __reduce__(LMatrix4f self)
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
        '__call__': None, # (!) real value is "<slot wrapper '__call__' of 'panda3d.core.LMatrix4f' objects>"
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.LMatrix4f' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.LMatrix4f' objects>"
        '__doc__': '/**\n * This is a 4-by-4 transform matrix.\n */',
        '__eq__': None, # (!) real value is "<slot wrapper '__eq__' of 'panda3d.core.LMatrix4f' objects>"
        '__ge__': None, # (!) real value is "<slot wrapper '__ge__' of 'panda3d.core.LMatrix4f' objects>"
        '__getitem__': None, # (!) real value is "<slot wrapper '__getitem__' of 'panda3d.core.LMatrix4f' objects>"
        '__gt__': None, # (!) real value is "<slot wrapper '__gt__' of 'panda3d.core.LMatrix4f' objects>"
        '__hash__': None, # (!) real value is "<slot wrapper '__hash__' of 'panda3d.core.LMatrix4f' objects>"
        '__iadd__': None, # (!) real value is "<slot wrapper '__iadd__' of 'panda3d.core.LMatrix4f' objects>"
        '__imul__': None, # (!) real value is "<slot wrapper '__imul__' of 'panda3d.core.LMatrix4f' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.LMatrix4f' objects>"
        '__isub__': None, # (!) real value is "<slot wrapper '__isub__' of 'panda3d.core.LMatrix4f' objects>"
        '__itruediv__': None, # (!) real value is "<slot wrapper '__itruediv__' of 'panda3d.core.LMatrix4f' objects>"
        '__le__': None, # (!) real value is "<slot wrapper '__le__' of 'panda3d.core.LMatrix4f' objects>"
        '__len__': None, # (!) real value is "<slot wrapper '__len__' of 'panda3d.core.LMatrix4f' objects>"
        '__lt__': None, # (!) real value is "<slot wrapper '__lt__' of 'panda3d.core.LMatrix4f' objects>"
        '__mul__': None, # (!) real value is "<slot wrapper '__mul__' of 'panda3d.core.LMatrix4f' objects>"
        '__ne__': None, # (!) real value is "<slot wrapper '__ne__' of 'panda3d.core.LMatrix4f' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE3242A0>'
        '__reduce__': None, # (!) real value is "<method '__reduce__' of 'panda3d.core.LMatrix4f' objects>"
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.LMatrix4f' objects>"
        '__rmul__': None, # (!) real value is "<slot wrapper '__rmul__' of 'panda3d.core.LMatrix4f' objects>"
        '__rtruediv__': None, # (!) real value is "<slot wrapper '__rtruediv__' of 'panda3d.core.LMatrix4f' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.LMatrix4f' objects>"
        '__truediv__': None, # (!) real value is "<slot wrapper '__truediv__' of 'panda3d.core.LMatrix4f' objects>"
        'accumulate': None, # (!) real value is "<method 'accumulate' of 'panda3d.core.LMatrix4f' objects>"
        'addHash': None, # (!) real value is "<method 'addHash' of 'panda3d.core.LMatrix4f' objects>"
        'add_hash': None, # (!) real value is "<method 'add_hash' of 'panda3d.core.LMatrix4f' objects>"
        'almostEqual': None, # (!) real value is "<method 'almostEqual' of 'panda3d.core.LMatrix4f' objects>"
        'almost_equal': None, # (!) real value is "<method 'almost_equal' of 'panda3d.core.LMatrix4f' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.LMatrix4f' objects>"
        'cols': None, # (!) real value is "<attribute 'cols' of 'panda3d.core.LMatrix4f' objects>"
        'compareTo': None, # (!) real value is "<method 'compareTo' of 'panda3d.core.LMatrix4f' objects>"
        'compare_to': None, # (!) real value is "<method 'compare_to' of 'panda3d.core.LMatrix4f' objects>"
        'componentwiseMult': None, # (!) real value is "<method 'componentwiseMult' of 'panda3d.core.LMatrix4f' objects>"
        'componentwise_mult': None, # (!) real value is "<method 'componentwise_mult' of 'panda3d.core.LMatrix4f' objects>"
        'convertMat': None, # (!) real value is '<staticmethod(<built-in method convertMat of type object at 0x00007FFCFE3242A0>)>'
        'convert_mat': None, # (!) real value is '<staticmethod(<built-in method convert_mat of type object at 0x00007FFCFE3242A0>)>'
        'fill': None, # (!) real value is "<method 'fill' of 'panda3d.core.LMatrix4f' objects>"
        'getCell': None, # (!) real value is "<method 'getCell' of 'panda3d.core.LMatrix4f' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE3242A0>)>'
        'getCol': None, # (!) real value is "<method 'getCol' of 'panda3d.core.LMatrix4f' objects>"
        'getCol3': None, # (!) real value is "<method 'getCol3' of 'panda3d.core.LMatrix4f' objects>"
        'getCols': None, # (!) real value is "<method 'getCols' of 'panda3d.core.LMatrix4f' objects>"
        'getHash': None, # (!) real value is "<method 'getHash' of 'panda3d.core.LMatrix4f' objects>"
        'getNumComponents': None, # (!) real value is "<method 'getNumComponents' of 'panda3d.core.LMatrix4f' objects>"
        'getRow': None, # (!) real value is "<method 'getRow' of 'panda3d.core.LMatrix4f' objects>"
        'getRow3': None, # (!) real value is "<method 'getRow3' of 'panda3d.core.LMatrix4f' objects>"
        'getRow3s': None, # (!) real value is "<method 'getRow3s' of 'panda3d.core.LMatrix4f' objects>"
        'getRows': None, # (!) real value is "<method 'getRows' of 'panda3d.core.LMatrix4f' objects>"
        'getUpper3': None, # (!) real value is "<method 'getUpper3' of 'panda3d.core.LMatrix4f' objects>"
        'get_cell': None, # (!) real value is "<method 'get_cell' of 'panda3d.core.LMatrix4f' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE3242A0>)>'
        'get_col': None, # (!) real value is "<method 'get_col' of 'panda3d.core.LMatrix4f' objects>"
        'get_col3': None, # (!) real value is "<method 'get_col3' of 'panda3d.core.LMatrix4f' objects>"
        'get_cols': None, # (!) real value is "<method 'get_cols' of 'panda3d.core.LMatrix4f' objects>"
        'get_hash': None, # (!) real value is "<method 'get_hash' of 'panda3d.core.LMatrix4f' objects>"
        'get_num_components': None, # (!) real value is "<method 'get_num_components' of 'panda3d.core.LMatrix4f' objects>"
        'get_row': None, # (!) real value is "<method 'get_row' of 'panda3d.core.LMatrix4f' objects>"
        'get_row3': None, # (!) real value is "<method 'get_row3' of 'panda3d.core.LMatrix4f' objects>"
        'get_row3s': None, # (!) real value is "<method 'get_row3s' of 'panda3d.core.LMatrix4f' objects>"
        'get_rows': None, # (!) real value is "<method 'get_rows' of 'panda3d.core.LMatrix4f' objects>"
        'get_upper_3': None, # (!) real value is "<method 'get_upper_3' of 'panda3d.core.LMatrix4f' objects>"
        'identMat': None, # (!) real value is '<staticmethod(<built-in method identMat of type object at 0x00007FFCFE3242A0>)>'
        'ident_mat': None, # (!) real value is '<staticmethod(<built-in method ident_mat of type object at 0x00007FFCFE3242A0>)>'
        'invertAffineFrom': None, # (!) real value is "<method 'invertAffineFrom' of 'panda3d.core.LMatrix4f' objects>"
        'invertFrom': None, # (!) real value is "<method 'invertFrom' of 'panda3d.core.LMatrix4f' objects>"
        'invertInPlace': None, # (!) real value is "<method 'invertInPlace' of 'panda3d.core.LMatrix4f' objects>"
        'invert_affine_from': None, # (!) real value is "<method 'invert_affine_from' of 'panda3d.core.LMatrix4f' objects>"
        'invert_from': None, # (!) real value is "<method 'invert_from' of 'panda3d.core.LMatrix4f' objects>"
        'invert_in_place': None, # (!) real value is "<method 'invert_in_place' of 'panda3d.core.LMatrix4f' objects>"
        'isIdentity': None, # (!) real value is "<method 'isIdentity' of 'panda3d.core.LMatrix4f' objects>"
        'isNan': None, # (!) real value is "<method 'isNan' of 'panda3d.core.LMatrix4f' objects>"
        'is_identity': None, # (!) real value is "<method 'is_identity' of 'panda3d.core.LMatrix4f' objects>"
        'is_int': 0,
        'is_nan': None, # (!) real value is "<method 'is_nan' of 'panda3d.core.LMatrix4f' objects>"
        'multiply': None, # (!) real value is "<method 'multiply' of 'panda3d.core.LMatrix4f' objects>"
        'num_components': 16,
        'onesMat': None, # (!) real value is '<staticmethod(<built-in method onesMat of type object at 0x00007FFCFE3242A0>)>'
        'ones_mat': None, # (!) real value is '<staticmethod(<built-in method ones_mat of type object at 0x00007FFCFE3242A0>)>'
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.LMatrix4f' objects>"
        'readDatagram': None, # (!) real value is "<method 'readDatagram' of 'panda3d.core.LMatrix4f' objects>"
        'readDatagramFixed': None, # (!) real value is "<method 'readDatagramFixed' of 'panda3d.core.LMatrix4f' objects>"
        'read_datagram': None, # (!) real value is "<method 'read_datagram' of 'panda3d.core.LMatrix4f' objects>"
        'read_datagram_fixed': None, # (!) real value is "<method 'read_datagram_fixed' of 'panda3d.core.LMatrix4f' objects>"
        'rotateMat': None, # (!) real value is '<staticmethod(<built-in method rotateMat of type object at 0x00007FFCFE3242A0>)>'
        'rotateMatNormaxis': None, # (!) real value is '<staticmethod(<built-in method rotateMatNormaxis of type object at 0x00007FFCFE3242A0>)>'
        'rotate_mat': None, # (!) real value is '<staticmethod(<built-in method rotate_mat of type object at 0x00007FFCFE3242A0>)>'
        'rotate_mat_normaxis': None, # (!) real value is '<staticmethod(<built-in method rotate_mat_normaxis of type object at 0x00007FFCFE3242A0>)>'
        'rows': None, # (!) real value is "<attribute 'rows' of 'panda3d.core.LMatrix4f' objects>"
        'scaleMat': None, # (!) real value is '<staticmethod(<built-in method scaleMat of type object at 0x00007FFCFE3242A0>)>'
        'scaleShearMat': None, # (!) real value is '<staticmethod(<built-in method scaleShearMat of type object at 0x00007FFCFE3242A0>)>'
        'scale_mat': None, # (!) real value is '<staticmethod(<built-in method scale_mat of type object at 0x00007FFCFE3242A0>)>'
        'scale_shear_mat': None, # (!) real value is '<staticmethod(<built-in method scale_shear_mat of type object at 0x00007FFCFE3242A0>)>'
        'set': None, # (!) real value is "<method 'set' of 'panda3d.core.LMatrix4f' objects>"
        'setCell': None, # (!) real value is "<method 'setCell' of 'panda3d.core.LMatrix4f' objects>"
        'setCol': None, # (!) real value is "<method 'setCol' of 'panda3d.core.LMatrix4f' objects>"
        'setRotateMat': None, # (!) real value is "<method 'setRotateMat' of 'panda3d.core.LMatrix4f' objects>"
        'setRotateMatNormaxis': None, # (!) real value is "<method 'setRotateMatNormaxis' of 'panda3d.core.LMatrix4f' objects>"
        'setRow': None, # (!) real value is "<method 'setRow' of 'panda3d.core.LMatrix4f' objects>"
        'setScaleMat': None, # (!) real value is "<method 'setScaleMat' of 'panda3d.core.LMatrix4f' objects>"
        'setScaleShearMat': None, # (!) real value is "<method 'setScaleShearMat' of 'panda3d.core.LMatrix4f' objects>"
        'setShearMat': None, # (!) real value is "<method 'setShearMat' of 'panda3d.core.LMatrix4f' objects>"
        'setTranslateMat': None, # (!) real value is "<method 'setTranslateMat' of 'panda3d.core.LMatrix4f' objects>"
        'setUpper3': None, # (!) real value is "<method 'setUpper3' of 'panda3d.core.LMatrix4f' objects>"
        'set_cell': None, # (!) real value is "<method 'set_cell' of 'panda3d.core.LMatrix4f' objects>"
        'set_col': None, # (!) real value is "<method 'set_col' of 'panda3d.core.LMatrix4f' objects>"
        'set_rotate_mat': None, # (!) real value is "<method 'set_rotate_mat' of 'panda3d.core.LMatrix4f' objects>"
        'set_rotate_mat_normaxis': None, # (!) real value is "<method 'set_rotate_mat_normaxis' of 'panda3d.core.LMatrix4f' objects>"
        'set_row': None, # (!) real value is "<method 'set_row' of 'panda3d.core.LMatrix4f' objects>"
        'set_scale_mat': None, # (!) real value is "<method 'set_scale_mat' of 'panda3d.core.LMatrix4f' objects>"
        'set_scale_shear_mat': None, # (!) real value is "<method 'set_scale_shear_mat' of 'panda3d.core.LMatrix4f' objects>"
        'set_shear_mat': None, # (!) real value is "<method 'set_shear_mat' of 'panda3d.core.LMatrix4f' objects>"
        'set_translate_mat': None, # (!) real value is "<method 'set_translate_mat' of 'panda3d.core.LMatrix4f' objects>"
        'set_upper_3': None, # (!) real value is "<method 'set_upper_3' of 'panda3d.core.LMatrix4f' objects>"
        'shearMat': None, # (!) real value is '<staticmethod(<built-in method shearMat of type object at 0x00007FFCFE3242A0>)>'
        'shear_mat': None, # (!) real value is '<staticmethod(<built-in method shear_mat of type object at 0x00007FFCFE3242A0>)>'
        'translateMat': None, # (!) real value is '<staticmethod(<built-in method translateMat of type object at 0x00007FFCFE3242A0>)>'
        'translate_mat': None, # (!) real value is '<staticmethod(<built-in method translate_mat of type object at 0x00007FFCFE3242A0>)>'
        'transposeFrom': None, # (!) real value is "<method 'transposeFrom' of 'panda3d.core.LMatrix4f' objects>"
        'transposeInPlace': None, # (!) real value is "<method 'transposeInPlace' of 'panda3d.core.LMatrix4f' objects>"
        'transpose_from': None, # (!) real value is "<method 'transpose_from' of 'panda3d.core.LMatrix4f' objects>"
        'transpose_in_place': None, # (!) real value is "<method 'transpose_in_place' of 'panda3d.core.LMatrix4f' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.LMatrix4f' objects>"
        'writeDatagram': None, # (!) real value is "<method 'writeDatagram' of 'panda3d.core.LMatrix4f' objects>"
        'writeDatagramFixed': None, # (!) real value is "<method 'writeDatagramFixed' of 'panda3d.core.LMatrix4f' objects>"
        'write_datagram': None, # (!) real value is "<method 'write_datagram' of 'panda3d.core.LMatrix4f' objects>"
        'write_datagram_fixed': None, # (!) real value is "<method 'write_datagram_fixed' of 'panda3d.core.LMatrix4f' objects>"
        'xform': None, # (!) real value is "<method 'xform' of 'panda3d.core.LMatrix4f' objects>"
        'xformInPlace': None, # (!) real value is "<method 'xformInPlace' of 'panda3d.core.LMatrix4f' objects>"
        'xformPoint': None, # (!) real value is "<method 'xformPoint' of 'panda3d.core.LMatrix4f' objects>"
        'xformPointGeneral': None, # (!) real value is "<method 'xformPointGeneral' of 'panda3d.core.LMatrix4f' objects>"
        'xformPointGeneralInPlace': None, # (!) real value is "<method 'xformPointGeneralInPlace' of 'panda3d.core.LMatrix4f' objects>"
        'xformPointInPlace': None, # (!) real value is "<method 'xformPointInPlace' of 'panda3d.core.LMatrix4f' objects>"
        'xformVec': None, # (!) real value is "<method 'xformVec' of 'panda3d.core.LMatrix4f' objects>"
        'xformVecGeneral': None, # (!) real value is "<method 'xformVecGeneral' of 'panda3d.core.LMatrix4f' objects>"
        'xformVecGeneralInPlace': None, # (!) real value is "<method 'xformVecGeneralInPlace' of 'panda3d.core.LMatrix4f' objects>"
        'xformVecInPlace': None, # (!) real value is "<method 'xformVecInPlace' of 'panda3d.core.LMatrix4f' objects>"
        'xform_in_place': None, # (!) real value is "<method 'xform_in_place' of 'panda3d.core.LMatrix4f' objects>"
        'xform_point': None, # (!) real value is "<method 'xform_point' of 'panda3d.core.LMatrix4f' objects>"
        'xform_point_general': None, # (!) real value is "<method 'xform_point_general' of 'panda3d.core.LMatrix4f' objects>"
        'xform_point_general_in_place': None, # (!) real value is "<method 'xform_point_general_in_place' of 'panda3d.core.LMatrix4f' objects>"
        'xform_point_in_place': None, # (!) real value is "<method 'xform_point_in_place' of 'panda3d.core.LMatrix4f' objects>"
        'xform_vec': None, # (!) real value is "<method 'xform_vec' of 'panda3d.core.LMatrix4f' objects>"
        'xform_vec_general': None, # (!) real value is "<method 'xform_vec_general' of 'panda3d.core.LMatrix4f' objects>"
        'xform_vec_general_in_place': None, # (!) real value is "<method 'xform_vec_general_in_place' of 'panda3d.core.LMatrix4f' objects>"
        'xform_vec_in_place': None, # (!) real value is "<method 'xform_vec_in_place' of 'panda3d.core.LMatrix4f' objects>"
        'yToZUpMat': None, # (!) real value is '<staticmethod(<built-in method yToZUpMat of type object at 0x00007FFCFE3242A0>)>'
        'y_to_z_up_mat': None, # (!) real value is '<staticmethod(<built-in method y_to_z_up_mat of type object at 0x00007FFCFE3242A0>)>'
        'zToYUpMat': None, # (!) real value is '<staticmethod(<built-in method zToYUpMat of type object at 0x00007FFCFE3242A0>)>'
        'z_to_y_up_mat': None, # (!) real value is '<staticmethod(<built-in method z_to_y_up_mat of type object at 0x00007FFCFE3242A0>)>'
        'zerosMat': None, # (!) real value is '<staticmethod(<built-in method zerosMat of type object at 0x00007FFCFE3242A0>)>'
        'zeros_mat': None, # (!) real value is '<staticmethod(<built-in method zeros_mat of type object at 0x00007FFCFE3242A0>)>'
    }
    is_int = 0
    num_components = 16
    Row = None # (!) real value is "<class 'panda3d.core.Row'>"


