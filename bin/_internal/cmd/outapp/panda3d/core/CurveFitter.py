# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class CurveFitter(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     *
     */
    """
    def addHpr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_hpr(const CurveFitter self, float t, const LVecBase3f hpr)
        
        /**
         * Adds a single sample hpr.
         */
        """
        pass

    def addXyz(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_xyz(const CurveFitter self, float t, const LVecBase3f xyz)
        
        /**
         * Adds a single sample xyz.
         */
        """
        pass

    def addXyzHpr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_xyz_hpr(const CurveFitter self, float t, const LVecBase3f xyz, const LVecBase3f hpr)
        
        /**
         * Adds a single sample xyz & hpr simultaneously.
         */
        """
        pass

    def add_hpr(self, const_CurveFitter_self, float_t, const_LVecBase3f_hpr): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_hpr(const CurveFitter self, float t, const LVecBase3f hpr)
        
        /**
         * Adds a single sample hpr.
         */
        """
        pass

    def add_xyz(self, const_CurveFitter_self, float_t, const_LVecBase3f_xyz): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_xyz(const CurveFitter self, float t, const LVecBase3f xyz)
        
        /**
         * Adds a single sample xyz.
         */
        """
        pass

    def add_xyz_hpr(self, const_CurveFitter_self, float_t, const_LVecBase3f_xyz, const_LVecBase3f_hpr): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_xyz_hpr(const CurveFitter self, float t, const LVecBase3f xyz, const LVecBase3f hpr)
        
        /**
         * Adds a single sample xyz & hpr simultaneously.
         */
        """
        pass

    def computeTangents(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        compute_tangents(const CurveFitter self, float scale)
        
        /**
         * Once a set of points has been built, and prior to calling MakeHermite() or
         * MakeNurbs(), ComputeTangents() must be called to set up the tangents
         * correctly (unless the tangents were defined as the points were added).
         */
        """
        pass

    def compute_tangents(self, const_CurveFitter_self, float_scale): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        compute_tangents(const CurveFitter self, float scale)
        
        /**
         * Once a set of points has been built, and prior to calling MakeHermite() or
         * MakeNurbs(), ComputeTangents() must be called to set up the tangents
         * correctly (unless the tangents were defined as the points were added).
         */
        """
        pass

    def desample(self, const_CurveFitter_self, float_factor): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        desample(const CurveFitter self, float factor)
        
        /**
         * Removes sample points in order to reduce the complexity of a sampled curve.
         * Keeps one out of every factor samples.  Also keeps the first and the last
         * samples.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getNumSamples(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_samples(CurveFitter self)
        
        /**
         * Returns the number of sample points that have been added.
         */
        """
        pass

    def getSampleHpr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_sample_hpr(CurveFitter self, int n)
        
        /**
         * Returns the orientation of the nth sample added.
         */
        """
        pass

    def getSampleT(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_sample_t(CurveFitter self, int n)
        
        /**
         * Returns the parametric value of the nth sample added.
         */
        """
        pass

    def getSampleTangent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_sample_tangent(CurveFitter self, int n)
        
        /**
         * Returns the tangent associated with the nth sample added.  This is only
         * meaningful if compute_tangents() has already been called.
         */
        """
        pass

    def getSampleXyz(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_sample_xyz(CurveFitter self, int n)
        
        /**
         * Returns the point in space of the nth sample added.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_num_samples(self, CurveFitter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_samples(CurveFitter self)
        
        /**
         * Returns the number of sample points that have been added.
         */
        """
        pass

    def get_sample_hpr(self, CurveFitter_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_sample_hpr(CurveFitter self, int n)
        
        /**
         * Returns the orientation of the nth sample added.
         */
        """
        pass

    def get_sample_t(self, CurveFitter_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_sample_t(CurveFitter self, int n)
        
        /**
         * Returns the parametric value of the nth sample added.
         */
        """
        pass

    def get_sample_tangent(self, CurveFitter_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_sample_tangent(CurveFitter self, int n)
        
        /**
         * Returns the tangent associated with the nth sample added.  This is only
         * meaningful if compute_tangents() has already been called.
         */
        """
        pass

    def get_sample_xyz(self, CurveFitter_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_sample_xyz(CurveFitter self, int n)
        
        /**
         * Returns the point in space of the nth sample added.
         */
        """
        pass

    def makeHermite(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_hermite(CurveFitter self)
        
        /**
         * Converts the current set of data points into a Hermite curve.
         */
        """
        pass

    def makeNurbs(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_nurbs(CurveFitter self)
        
        /**
         * Converts the current set of data points into a NURBS curve.  This gives a
         * smoother curve than produced by MakeHermite().
         */
        """
        pass

    def make_hermite(self, CurveFitter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_hermite(CurveFitter self)
        
        /**
         * Converts the current set of data points into a Hermite curve.
         */
        """
        pass

    def make_nurbs(self, CurveFitter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_nurbs(CurveFitter self)
        
        /**
         * Converts the current set of data points into a NURBS curve.  This gives a
         * smoother curve than produced by MakeHermite().
         */
        """
        pass

    def output(self, CurveFitter_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(CurveFitter self, ostream out)
        
        /**
         *
         */
        """
        pass

    def removeSamples(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_samples(const CurveFitter self, int begin, int end)
        
        /**
         * Eliminates all samples from index begin, up to but not including index end,
         * from the database.
         */
        """
        pass

    def remove_samples(self, const_CurveFitter_self, int_begin, int_end): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_samples(const CurveFitter self, int begin, int end)
        
        /**
         * Eliminates all samples from index begin, up to but not including index end,
         * from the database.
         */
        """
        pass

    def reset(self, const_CurveFitter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        reset(const CurveFitter self)
        
        /**
         * Removes all the data points previously added to the CurveFitter, and
         * initializes it for a new curve.
         */
        """
        pass

    def sample(self, const_CurveFitter_self, ParametricCurveCollection_curves, int_count): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        sample(const CurveFitter self, ParametricCurveCollection curves, int count)
        
        /**
         * Generates a series of data points by sampling the given curve (or xyz/hpr
         * curves) the indicated number of times.  The sampling is made evenly in
         * parametric time, and then the timewarps, if any, are applied.
         */
        """
        pass

    def sortPoints(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        sort_points(const CurveFitter self)
        
        /**
         * Sorts all the data points in order by parametric time, in case they were
         * added in an incorrect order.
         */
        """
        pass

    def sort_points(self, const_CurveFitter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        sort_points(const CurveFitter self)
        
        /**
         * Sorts all the data points in order by parametric time, in case they were
         * added in an incorrect order.
         */
        """
        pass

    def wrapHpr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        wrap_hpr(const CurveFitter self)
        
        /**
         * Resets each HPR data point so that the maximum delta between any two
         * consecutive points is 180 degrees, which should prevent incorrect HPR
         * wrapping.
         */
        """
        pass

    def wrap_hpr(self, const_CurveFitter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        wrap_hpr(const CurveFitter self)
        
        /**
         * Resets each HPR data point so that the maximum delta between any two
         * consecutive points is 180 degrees, which should prevent incorrect HPR
         * wrapping.
         */
        """
        pass

    def write(self, CurveFitter_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(CurveFitter self, ostream out)
        
        /**
         *
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

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.CurveFitter' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.CurveFitter' objects>"
        '__doc__': '/**\n *\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.CurveFitter' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE34E420>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.CurveFitter' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.CurveFitter' objects>"
        'addHpr': None, # (!) real value is "<method 'addHpr' of 'panda3d.core.CurveFitter' objects>"
        'addXyz': None, # (!) real value is "<method 'addXyz' of 'panda3d.core.CurveFitter' objects>"
        'addXyzHpr': None, # (!) real value is "<method 'addXyzHpr' of 'panda3d.core.CurveFitter' objects>"
        'add_hpr': None, # (!) real value is "<method 'add_hpr' of 'panda3d.core.CurveFitter' objects>"
        'add_xyz': None, # (!) real value is "<method 'add_xyz' of 'panda3d.core.CurveFitter' objects>"
        'add_xyz_hpr': None, # (!) real value is "<method 'add_xyz_hpr' of 'panda3d.core.CurveFitter' objects>"
        'computeTangents': None, # (!) real value is "<method 'computeTangents' of 'panda3d.core.CurveFitter' objects>"
        'compute_tangents': None, # (!) real value is "<method 'compute_tangents' of 'panda3d.core.CurveFitter' objects>"
        'desample': None, # (!) real value is "<method 'desample' of 'panda3d.core.CurveFitter' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE34E420>)>'
        'getNumSamples': None, # (!) real value is "<method 'getNumSamples' of 'panda3d.core.CurveFitter' objects>"
        'getSampleHpr': None, # (!) real value is "<method 'getSampleHpr' of 'panda3d.core.CurveFitter' objects>"
        'getSampleT': None, # (!) real value is "<method 'getSampleT' of 'panda3d.core.CurveFitter' objects>"
        'getSampleTangent': None, # (!) real value is "<method 'getSampleTangent' of 'panda3d.core.CurveFitter' objects>"
        'getSampleXyz': None, # (!) real value is "<method 'getSampleXyz' of 'panda3d.core.CurveFitter' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE34E420>)>'
        'get_num_samples': None, # (!) real value is "<method 'get_num_samples' of 'panda3d.core.CurveFitter' objects>"
        'get_sample_hpr': None, # (!) real value is "<method 'get_sample_hpr' of 'panda3d.core.CurveFitter' objects>"
        'get_sample_t': None, # (!) real value is "<method 'get_sample_t' of 'panda3d.core.CurveFitter' objects>"
        'get_sample_tangent': None, # (!) real value is "<method 'get_sample_tangent' of 'panda3d.core.CurveFitter' objects>"
        'get_sample_xyz': None, # (!) real value is "<method 'get_sample_xyz' of 'panda3d.core.CurveFitter' objects>"
        'makeHermite': None, # (!) real value is "<method 'makeHermite' of 'panda3d.core.CurveFitter' objects>"
        'makeNurbs': None, # (!) real value is "<method 'makeNurbs' of 'panda3d.core.CurveFitter' objects>"
        'make_hermite': None, # (!) real value is "<method 'make_hermite' of 'panda3d.core.CurveFitter' objects>"
        'make_nurbs': None, # (!) real value is "<method 'make_nurbs' of 'panda3d.core.CurveFitter' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.CurveFitter' objects>"
        'removeSamples': None, # (!) real value is "<method 'removeSamples' of 'panda3d.core.CurveFitter' objects>"
        'remove_samples': None, # (!) real value is "<method 'remove_samples' of 'panda3d.core.CurveFitter' objects>"
        'reset': None, # (!) real value is "<method 'reset' of 'panda3d.core.CurveFitter' objects>"
        'sample': None, # (!) real value is "<method 'sample' of 'panda3d.core.CurveFitter' objects>"
        'sortPoints': None, # (!) real value is "<method 'sortPoints' of 'panda3d.core.CurveFitter' objects>"
        'sort_points': None, # (!) real value is "<method 'sort_points' of 'panda3d.core.CurveFitter' objects>"
        'wrapHpr': None, # (!) real value is "<method 'wrapHpr' of 'panda3d.core.CurveFitter' objects>"
        'wrap_hpr': None, # (!) real value is "<method 'wrap_hpr' of 'panda3d.core.CurveFitter' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.CurveFitter' objects>"
    }


