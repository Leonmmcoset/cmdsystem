# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class LParabolaf(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * An abstract mathematical description of a parabola, particularly useful for
     * describing arcs of projectiles.
     *
     * The parabolic equation, given parametrically here, is P = At^2 + Bt + C.
     */
    """
    def assign(self, const_LParabolaf_self, const_LParabolaf_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const LParabolaf self, const LParabolaf copy)
        """
        pass

    def calcPoint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        calc_point(LParabolaf self, float t)
        
        /**
         * Computes the point on the parabola at time t.
         */
        """
        pass

    def calc_point(self, LParabolaf_self, float_t): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        calc_point(LParabolaf self, float t)
        
        /**
         * Computes the point on the parabola at time t.
         */
        """
        pass

    def getA(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_a(LParabolaf self)
        
        /**
         * Returns the first point of the parabola's parametric equation: the
         * acceleration.
         */
        """
        pass

    def getB(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_b(LParabolaf self)
        
        /**
         * Returns the second point of the parabola's parametric equation: the initial
         * velocity.
         */
        """
        pass

    def getC(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_c(LParabolaf self)
        
        /**
         * Returns the third point of the parabola's parametric equation: the start
         * point.
         */
        """
        pass

    def get_a(self, LParabolaf_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_a(LParabolaf self)
        
        /**
         * Returns the first point of the parabola's parametric equation: the
         * acceleration.
         */
        """
        pass

    def get_b(self, LParabolaf_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_b(LParabolaf self)
        
        /**
         * Returns the second point of the parabola's parametric equation: the initial
         * velocity.
         */
        """
        pass

    def get_c(self, LParabolaf_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_c(LParabolaf self)
        
        /**
         * Returns the third point of the parabola's parametric equation: the start
         * point.
         */
        """
        pass

    def output(self, LParabolaf_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(LParabolaf self, ostream out)
        
        /**
         *
         */
        """
        pass

    def readDatagram(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        read_datagram(const LParabolaf self, DatagramIterator source)
        
        /**
         * Reads the parabola from the Datagram using get_stdfloat().
         */
        """
        pass

    def readDatagramFixed(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        read_datagram_fixed(const LParabolaf self, DatagramIterator source)
        
        /**
         * Reads the parabola from the Datagram using get_float32() or get_float64().
         * See write_datagram_fixed().
         */
        """
        pass

    def read_datagram(self, const_LParabolaf_self, DatagramIterator_source): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        read_datagram(const LParabolaf self, DatagramIterator source)
        
        /**
         * Reads the parabola from the Datagram using get_stdfloat().
         */
        """
        pass

    def read_datagram_fixed(self, const_LParabolaf_self, DatagramIterator_source): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        read_datagram_fixed(const LParabolaf self, DatagramIterator source)
        
        /**
         * Reads the parabola from the Datagram using get_float32() or get_float64().
         * See write_datagram_fixed().
         */
        """
        pass

    def write(self, LParabolaf_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(LParabolaf self, ostream out, int indent_level)
        
        /**
         *
         */
        """
        pass

    def writeDatagram(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        write_datagram(LParabolaf self, Datagram destination)
        
        /**
         * Writes the parabola to the Datagram using add_stdfloat().  This is
         * appropriate when you want to write the vector using the standard width
         * setting, especially when you are writing a bam file.
         */
        """
        pass

    def writeDatagramFixed(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        write_datagram_fixed(LParabolaf self, Datagram destination)
        
        /**
         * Writes the parabola to the Datagram using add_float32() or add_float64(),
         * depending on the type of floats in the parabola, regardless of the setting
         * of Datagram::set_stdfloat_double().  This is appropriate when you want to
         * write a fixed-width value to the datagram, especially when you are not
         * writing a bam file.
         */
        """
        pass

    def write_datagram(self, LParabolaf_self, Datagram_destination): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write_datagram(LParabolaf self, Datagram destination)
        
        /**
         * Writes the parabola to the Datagram using add_stdfloat().  This is
         * appropriate when you want to write the vector using the standard width
         * setting, especially when you are writing a bam file.
         */
        """
        pass

    def write_datagram_fixed(self, LParabolaf_self, Datagram_destination): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write_datagram_fixed(LParabolaf self, Datagram destination)
        
        /**
         * Writes the parabola to the Datagram using add_float32() or add_float64(),
         * depending on the type of floats in the parabola, regardless of the setting
         * of Datagram::set_stdfloat_double().  This is appropriate when you want to
         * write a fixed-width value to the datagram, especially when you are not
         * writing a bam file.
         */
        """
        pass

    def xform(self, const_LParabolaf_self, const_LMatrix4f_mat): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        xform(const LParabolaf self, const LMatrix4f mat)
        
        /**
         * Transforms the parabola by the indicated matrix.
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
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.LParabolaf' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.LParabolaf' objects>"
        '__doc__': '/**\n * An abstract mathematical description of a parabola, particularly useful for\n * describing arcs of projectiles.\n *\n * The parabolic equation, given parametrically here, is P = At^2 + Bt + C.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.LParabolaf' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE340FA0>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.LParabolaf' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.LParabolaf' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.LParabolaf' objects>"
        'calcPoint': None, # (!) real value is "<method 'calcPoint' of 'panda3d.core.LParabolaf' objects>"
        'calc_point': None, # (!) real value is "<method 'calc_point' of 'panda3d.core.LParabolaf' objects>"
        'getA': None, # (!) real value is "<method 'getA' of 'panda3d.core.LParabolaf' objects>"
        'getB': None, # (!) real value is "<method 'getB' of 'panda3d.core.LParabolaf' objects>"
        'getC': None, # (!) real value is "<method 'getC' of 'panda3d.core.LParabolaf' objects>"
        'get_a': None, # (!) real value is "<method 'get_a' of 'panda3d.core.LParabolaf' objects>"
        'get_b': None, # (!) real value is "<method 'get_b' of 'panda3d.core.LParabolaf' objects>"
        'get_c': None, # (!) real value is "<method 'get_c' of 'panda3d.core.LParabolaf' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.LParabolaf' objects>"
        'readDatagram': None, # (!) real value is "<method 'readDatagram' of 'panda3d.core.LParabolaf' objects>"
        'readDatagramFixed': None, # (!) real value is "<method 'readDatagramFixed' of 'panda3d.core.LParabolaf' objects>"
        'read_datagram': None, # (!) real value is "<method 'read_datagram' of 'panda3d.core.LParabolaf' objects>"
        'read_datagram_fixed': None, # (!) real value is "<method 'read_datagram_fixed' of 'panda3d.core.LParabolaf' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.LParabolaf' objects>"
        'writeDatagram': None, # (!) real value is "<method 'writeDatagram' of 'panda3d.core.LParabolaf' objects>"
        'writeDatagramFixed': None, # (!) real value is "<method 'writeDatagramFixed' of 'panda3d.core.LParabolaf' objects>"
        'write_datagram': None, # (!) real value is "<method 'write_datagram' of 'panda3d.core.LParabolaf' objects>"
        'write_datagram_fixed': None, # (!) real value is "<method 'write_datagram_fixed' of 'panda3d.core.LParabolaf' objects>"
        'xform': None, # (!) real value is "<method 'xform' of 'panda3d.core.LParabolaf' objects>"
    }


