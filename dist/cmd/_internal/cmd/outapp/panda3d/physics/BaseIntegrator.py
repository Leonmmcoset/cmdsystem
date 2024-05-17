# encoding: utf-8
# module panda3d.physics
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\physics.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


class BaseIntegrator(__panda3d_core.ReferenceCount):
    """
    /**
     * pure virtual integrator class that holds cached matrix information that
     * really should be common to any possible child implementation.
     */
    """
    def output(self, BaseIntegrator_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(BaseIntegrator self, ostream out)
        
        /**
         * Write a string representation of this instance to <out>.
         */
        """
        pass

    def write(self, BaseIntegrator_self, ostream_out, int_indent): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(BaseIntegrator self, ostream out, int indent)
        
        /**
         * Write a string representation of this instance to <out>.
         */
        """
        pass

    def writePrecomputedAngularMatrices(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        write_precomputed_angular_matrices(BaseIntegrator self, ostream out, int indent)
        
        /**
         * Write a string representation of this instance to <out>.
         */
        """
        pass

    def writePrecomputedLinearMatrices(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        write_precomputed_linear_matrices(BaseIntegrator self, ostream out, int indent)
        
        /**
         * Write a string representation of this instance to <out>.
         */
        """
        pass

    def write_precomputed_angular_matrices(self, BaseIntegrator_self, ostream_out, int_indent): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write_precomputed_angular_matrices(BaseIntegrator self, ostream out, int indent)
        
        /**
         * Write a string representation of this instance to <out>.
         */
        """
        pass

    def write_precomputed_linear_matrices(self, BaseIntegrator_self, ostream_out, int_indent): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write_precomputed_linear_matrices(BaseIntegrator self, ostream out, int indent)
        
        /**
         * Write a string representation of this instance to <out>.
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
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.physics.BaseIntegrator' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.physics.BaseIntegrator' objects>"
        '__doc__': '/**\n * pure virtual integrator class that holds cached matrix information that\n * really should be common to any possible child implementation.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.physics.BaseIntegrator' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC9DEC260>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.physics.BaseIntegrator' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.physics.BaseIntegrator' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.physics.BaseIntegrator' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.physics.BaseIntegrator' objects>"
        'writePrecomputedAngularMatrices': None, # (!) real value is "<method 'writePrecomputedAngularMatrices' of 'panda3d.physics.BaseIntegrator' objects>"
        'writePrecomputedLinearMatrices': None, # (!) real value is "<method 'writePrecomputedLinearMatrices' of 'panda3d.physics.BaseIntegrator' objects>"
        'write_precomputed_angular_matrices': None, # (!) real value is "<method 'write_precomputed_angular_matrices' of 'panda3d.physics.BaseIntegrator' objects>"
        'write_precomputed_linear_matrices': None, # (!) real value is "<method 'write_precomputed_linear_matrices' of 'panda3d.physics.BaseIntegrator' objects>"
    }


