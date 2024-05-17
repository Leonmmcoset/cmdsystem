# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .PiecewiseCurve import PiecewiseCurve

class HermiteCurve(PiecewiseCurve):
    """
    /**
     * A parametric curve defined by a sequence of control vertices, each with an
     * in and out tangent.
     *
     * This class is actually implemented as a PiecewiseCurve made up of several
     * CubicCurvesegs, each of which is created using the hermite_basis() method.
     * The HermiteCurve class itself keeps its own list of the CV's that are used
     * to define the curve (since the CubicCurveseg class doesn't retain these).
     */
    """
    def appendCv(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        append_cv(const HermiteCurve self, int type, const LVecBase3f v)
        append_cv(const HermiteCurve self, int type, float x, float y, float z)
        
        /**
         * Adds a new CV to the end of the curve.  The new CV is given initial in/out
         * tangents of 0.  The return value is the index of the new CV.
         */
        """
        pass

    def append_cv(self, const_HermiteCurve_self, int_type, const_LVecBase3f_v): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        append_cv(const HermiteCurve self, int type, const LVecBase3f v)
        append_cv(const HermiteCurve self, int type, float x, float y, float z)
        
        /**
         * Adds a new CV to the end of the curve.  The new CV is given initial in/out
         * tangents of 0.  The return value is the index of the new CV.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getCvIn(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_cv_in(HermiteCurve self, int n)
        get_cv_in(HermiteCurve self, int n, LVecBase3f v)
        
        /**
         * Returns the in tangent of the given CV.
         */
        """
        pass

    def getCvName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_cv_name(HermiteCurve self, int n)
        
        /**
         * Returns the name of the given CV, or NULL.
         */
        """
        pass

    def getCvOut(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_cv_out(HermiteCurve self, int n)
        get_cv_out(HermiteCurve self, int n, LVecBase3f v)
        
        /**
         * Returns the out tangent of the given CV.
         */
        """
        pass

    def getCvPoint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_cv_point(HermiteCurve self, int n)
        get_cv_point(HermiteCurve self, int n, LVecBase3f v)
        
        /**
         * Returns the position of the given CV.
         */
        """
        pass

    def getCvTstart(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_cv_tstart(HermiteCurve self, int n)
        
        /**
         * Returns the starting point in parametric space of the given CV.
         */
        """
        pass

    def getCvType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_cv_type(HermiteCurve self, int n)
        
        /**
         * Returns the given CV's continuity type, HC_CUT, HC_FREE, HC_G1, or
         * HC_SMOOTH, or 0 if there is no such CV.
         */
        """
        pass

    def getNumCvs(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_cvs(HermiteCurve self)
        
        /**
         * Returns the number of CV's in the curve.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_cv_in(self, HermiteCurve_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_cv_in(HermiteCurve self, int n)
        get_cv_in(HermiteCurve self, int n, LVecBase3f v)
        
        /**
         * Returns the in tangent of the given CV.
         */
        """
        pass

    def get_cv_name(self, HermiteCurve_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_cv_name(HermiteCurve self, int n)
        
        /**
         * Returns the name of the given CV, or NULL.
         */
        """
        pass

    def get_cv_out(self, HermiteCurve_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_cv_out(HermiteCurve self, int n)
        get_cv_out(HermiteCurve self, int n, LVecBase3f v)
        
        /**
         * Returns the out tangent of the given CV.
         */
        """
        pass

    def get_cv_point(self, HermiteCurve_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_cv_point(HermiteCurve self, int n)
        get_cv_point(HermiteCurve self, int n, LVecBase3f v)
        
        /**
         * Returns the position of the given CV.
         */
        """
        pass

    def get_cv_tstart(self, HermiteCurve_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_cv_tstart(HermiteCurve self, int n)
        
        /**
         * Returns the starting point in parametric space of the given CV.
         */
        """
        pass

    def get_cv_type(self, HermiteCurve_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_cv_type(HermiteCurve self, int n)
        
        /**
         * Returns the given CV's continuity type, HC_CUT, HC_FREE, HC_G1, or
         * HC_SMOOTH, or 0 if there is no such CV.
         */
        """
        pass

    def get_num_cvs(self, HermiteCurve_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_cvs(HermiteCurve self)
        
        /**
         * Returns the number of CV's in the curve.
         */
        """
        pass

    def insertCv(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        insert_cv(const HermiteCurve self, float t)
        
        /**
         * Inserts a new CV at the given parametric point along the curve.  If this
         * parametric point is already on the curve, the CV is assigned an index
         * between its two neighbors and the indices of all following CV's are
         * incremented by 1; its in and out tangents are chosen to keep the curve
         * consistent.  If the new parametric point is beyond the end of the existing
         * curve, the curve is extended to meet it and the new CV's position, in
         * tangent, and out tangent are set to zero.
         *
         * The index number of the new CV is returned.
         */
        """
        pass

    def insert_cv(self, const_HermiteCurve_self, float_t): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        insert_cv(const HermiteCurve self, float t)
        
        /**
         * Inserts a new CV at the given parametric point along the curve.  If this
         * parametric point is already on the curve, the CV is assigned an index
         * between its two neighbors and the indices of all following CV's are
         * incremented by 1; its in and out tangents are chosen to keep the curve
         * consistent.  If the new parametric point is beyond the end of the existing
         * curve, the curve is extended to meet it and the new CV's position, in
         * tangent, and out tangent are set to zero.
         *
         * The index number of the new CV is returned.
         */
        """
        pass

    def removeAllCvs(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_all_cvs(const HermiteCurve self)
        
        /**
         * Removes all CV's from the curve.
         */
        """
        pass

    def removeCv(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_cv(const HermiteCurve self, int n)
        
        /**
         * Removes the given CV from the curve.  Returns true if the CV existed, false
         * otherwise.
         */
        """
        pass

    def remove_all_cvs(self, const_HermiteCurve_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_all_cvs(const HermiteCurve self)
        
        /**
         * Removes all CV's from the curve.
         */
        """
        pass

    def remove_cv(self, const_HermiteCurve_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_cv(const HermiteCurve self, int n)
        
        /**
         * Removes the given CV from the curve.  Returns true if the CV existed, false
         * otherwise.
         */
        """
        pass

    def setCvIn(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_cv_in(const HermiteCurve self, int n, const LVecBase3f v)
        set_cv_in(const HermiteCurve self, int n, float x, float y, float z)
        
        /**
         * Changes the given CV's in tangent.  Depending on the continuity type, this
         * may also adjust the out tangent.
         */
        """
        pass

    def setCvName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_cv_name(const HermiteCurve self, int n, str name)
        
        /**
         * Changes the name associated with a particular CV.
         */
        """
        pass

    def setCvOut(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_cv_out(const HermiteCurve self, int n, const LVecBase3f v)
        set_cv_out(const HermiteCurve self, int n, float x, float y, float z)
        
        /**
         * Changes the given CV's out tangent.  Depending on the continuity type, this
         * may also adjust the in tangent.
         */
        """
        pass

    def setCvPoint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_cv_point(const HermiteCurve self, int n, const LVecBase3f v)
        set_cv_point(const HermiteCurve self, int n, float x, float y, float z)
        
        /**
         * Changes the given CV's position.
         */
        """
        pass

    def setCvTstart(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_cv_tstart(const HermiteCurve self, int n, float tstart)
        
        /**
         * Changes the given CV's parametric starting time.  This may affect the shape
         * of the curve.
         */
        """
        pass

    def setCvType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_cv_type(const HermiteCurve self, int n, int type)
        
        /**
         * Changes the given CV's continuity type.  Legal values are HC_CUT, HC_FREE,
         * HC_G1, or HC_SMOOTH.
         *
         * Other than HC_CUT, these have no effect on the actual curve; it remains up
         * to user software to impose the constraints these imply.
         *
         * HC_CUT implies a disconnection of the curve; HC_FREE imposes no constraints
         * on the tangents; HC_G1 forces the tangents to be collinear, and HC_SMOOTH
         * forces the tangents to be identical.  Setting type type to HC_G1 or
         * HC_SMOOTH may adjust the out tangent to match the in tangent.
         */
        """
        pass

    def set_cv_in(self, const_HermiteCurve_self, int_n, const_LVecBase3f_v): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_cv_in(const HermiteCurve self, int n, const LVecBase3f v)
        set_cv_in(const HermiteCurve self, int n, float x, float y, float z)
        
        /**
         * Changes the given CV's in tangent.  Depending on the continuity type, this
         * may also adjust the out tangent.
         */
        """
        pass

    def set_cv_name(self, const_HermiteCurve_self, int_n, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_cv_name(const HermiteCurve self, int n, str name)
        
        /**
         * Changes the name associated with a particular CV.
         */
        """
        pass

    def set_cv_out(self, const_HermiteCurve_self, int_n, const_LVecBase3f_v): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_cv_out(const HermiteCurve self, int n, const LVecBase3f v)
        set_cv_out(const HermiteCurve self, int n, float x, float y, float z)
        
        /**
         * Changes the given CV's out tangent.  Depending on the continuity type, this
         * may also adjust the in tangent.
         */
        """
        pass

    def set_cv_point(self, const_HermiteCurve_self, int_n, const_LVecBase3f_v): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_cv_point(const HermiteCurve self, int n, const LVecBase3f v)
        set_cv_point(const HermiteCurve self, int n, float x, float y, float z)
        
        /**
         * Changes the given CV's position.
         */
        """
        pass

    def set_cv_tstart(self, const_HermiteCurve_self, int_n, float_tstart): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_cv_tstart(const HermiteCurve self, int n, float tstart)
        
        /**
         * Changes the given CV's parametric starting time.  This may affect the shape
         * of the curve.
         */
        """
        pass

    def set_cv_type(self, const_HermiteCurve_self, int_n, int_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_cv_type(const HermiteCurve self, int n, int type)
        
        /**
         * Changes the given CV's continuity type.  Legal values are HC_CUT, HC_FREE,
         * HC_G1, or HC_SMOOTH.
         *
         * Other than HC_CUT, these have no effect on the actual curve; it remains up
         * to user software to impose the constraints these imply.
         *
         * HC_CUT implies a disconnection of the curve; HC_FREE imposes no constraints
         * on the tangents; HC_G1 forces the tangents to be collinear, and HC_SMOOTH
         * forces the tangents to be identical.  Setting type type to HC_G1 or
         * HC_SMOOTH may adjust the out tangent to match the in tangent.
         */
        """
        pass

    def writeCv(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        write_cv(HermiteCurve self, ostream out, int n)
        
        /**
         *
         */
        """
        pass

    def write_cv(self, HermiteCurve_self, ostream_out, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write_cv(HermiteCurve self, ostream out, int n)
        
        /**
         *
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': "/**\n * A parametric curve defined by a sequence of control vertices, each with an\n * in and out tangent.\n *\n * This class is actually implemented as a PiecewiseCurve made up of several\n * CubicCurvesegs, each of which is created using the hermite_basis() method.\n * The HermiteCurve class itself keeps its own list of the CV's that are used\n * to define the curve (since the CubicCurveseg class doesn't retain these).\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.HermiteCurve' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE34E7C0>'
        'appendCv': None, # (!) real value is "<method 'appendCv' of 'panda3d.core.HermiteCurve' objects>"
        'append_cv': None, # (!) real value is "<method 'append_cv' of 'panda3d.core.HermiteCurve' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE34E7C0>)>'
        'getCvIn': None, # (!) real value is "<method 'getCvIn' of 'panda3d.core.HermiteCurve' objects>"
        'getCvName': None, # (!) real value is "<method 'getCvName' of 'panda3d.core.HermiteCurve' objects>"
        'getCvOut': None, # (!) real value is "<method 'getCvOut' of 'panda3d.core.HermiteCurve' objects>"
        'getCvPoint': None, # (!) real value is "<method 'getCvPoint' of 'panda3d.core.HermiteCurve' objects>"
        'getCvTstart': None, # (!) real value is "<method 'getCvTstart' of 'panda3d.core.HermiteCurve' objects>"
        'getCvType': None, # (!) real value is "<method 'getCvType' of 'panda3d.core.HermiteCurve' objects>"
        'getNumCvs': None, # (!) real value is "<method 'getNumCvs' of 'panda3d.core.HermiteCurve' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE34E7C0>)>'
        'get_cv_in': None, # (!) real value is "<method 'get_cv_in' of 'panda3d.core.HermiteCurve' objects>"
        'get_cv_name': None, # (!) real value is "<method 'get_cv_name' of 'panda3d.core.HermiteCurve' objects>"
        'get_cv_out': None, # (!) real value is "<method 'get_cv_out' of 'panda3d.core.HermiteCurve' objects>"
        'get_cv_point': None, # (!) real value is "<method 'get_cv_point' of 'panda3d.core.HermiteCurve' objects>"
        'get_cv_tstart': None, # (!) real value is "<method 'get_cv_tstart' of 'panda3d.core.HermiteCurve' objects>"
        'get_cv_type': None, # (!) real value is "<method 'get_cv_type' of 'panda3d.core.HermiteCurve' objects>"
        'get_num_cvs': None, # (!) real value is "<method 'get_num_cvs' of 'panda3d.core.HermiteCurve' objects>"
        'insertCv': None, # (!) real value is "<method 'insertCv' of 'panda3d.core.HermiteCurve' objects>"
        'insert_cv': None, # (!) real value is "<method 'insert_cv' of 'panda3d.core.HermiteCurve' objects>"
        'removeAllCvs': None, # (!) real value is "<method 'removeAllCvs' of 'panda3d.core.HermiteCurve' objects>"
        'removeCv': None, # (!) real value is "<method 'removeCv' of 'panda3d.core.HermiteCurve' objects>"
        'remove_all_cvs': None, # (!) real value is "<method 'remove_all_cvs' of 'panda3d.core.HermiteCurve' objects>"
        'remove_cv': None, # (!) real value is "<method 'remove_cv' of 'panda3d.core.HermiteCurve' objects>"
        'setCvIn': None, # (!) real value is "<method 'setCvIn' of 'panda3d.core.HermiteCurve' objects>"
        'setCvName': None, # (!) real value is "<method 'setCvName' of 'panda3d.core.HermiteCurve' objects>"
        'setCvOut': None, # (!) real value is "<method 'setCvOut' of 'panda3d.core.HermiteCurve' objects>"
        'setCvPoint': None, # (!) real value is "<method 'setCvPoint' of 'panda3d.core.HermiteCurve' objects>"
        'setCvTstart': None, # (!) real value is "<method 'setCvTstart' of 'panda3d.core.HermiteCurve' objects>"
        'setCvType': None, # (!) real value is "<method 'setCvType' of 'panda3d.core.HermiteCurve' objects>"
        'set_cv_in': None, # (!) real value is "<method 'set_cv_in' of 'panda3d.core.HermiteCurve' objects>"
        'set_cv_name': None, # (!) real value is "<method 'set_cv_name' of 'panda3d.core.HermiteCurve' objects>"
        'set_cv_out': None, # (!) real value is "<method 'set_cv_out' of 'panda3d.core.HermiteCurve' objects>"
        'set_cv_point': None, # (!) real value is "<method 'set_cv_point' of 'panda3d.core.HermiteCurve' objects>"
        'set_cv_tstart': None, # (!) real value is "<method 'set_cv_tstart' of 'panda3d.core.HermiteCurve' objects>"
        'set_cv_type': None, # (!) real value is "<method 'set_cv_type' of 'panda3d.core.HermiteCurve' objects>"
        'writeCv': None, # (!) real value is "<method 'writeCv' of 'panda3d.core.HermiteCurve' objects>"
        'write_cv': None, # (!) real value is "<method 'write_cv' of 'panda3d.core.HermiteCurve' objects>"
    }


