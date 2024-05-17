# encoding: utf-8
# module panda3d.direct
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\direct.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


from .DCField import DCField

class DCMolecularField(DCField):
    """
    /**
     * A single molecular field of a Distributed Class, as read from a .dc file.
     * This represents a combination of two or more related atomic fields, that
     * will often be treated as a unit.
     */
    """
    def getAtomic(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_atomic(DCMolecularField self, int n)
        
        /**
         * Returns the nth atomic field that makes up this molecular field.  This may
         * or may not be a field of this particular class; it might be defined in a
         * parent class.
         */
        """
        pass

    def getNumAtomics(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_atomics(DCMolecularField self)
        
        /**
         * Returns the number of atomic fields that make up this molecular field.
         */
        """
        pass

    def get_atomic(self, DCMolecularField_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_atomic(DCMolecularField self, int n)
        
        /**
         * Returns the nth atomic field that makes up this molecular field.  This may
         * or may not be a field of this particular class; it might be defined in a
         * parent class.
         */
        """
        pass

    def get_num_atomics(self, DCMolecularField_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_atomics(DCMolecularField self)
        
        /**
         * Returns the number of atomic fields that make up this molecular field.
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
        '__doc__': '/**\n * A single molecular field of a Distributed Class, as read from a .dc file.\n * This represents a combination of two or more related atomic fields, that\n * will often be treated as a unit.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.direct.DCMolecularField' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC68DEF10>'
        'getAtomic': None, # (!) real value is "<method 'getAtomic' of 'panda3d.direct.DCMolecularField' objects>"
        'getNumAtomics': None, # (!) real value is "<method 'getNumAtomics' of 'panda3d.direct.DCMolecularField' objects>"
        'get_atomic': None, # (!) real value is "<method 'get_atomic' of 'panda3d.direct.DCMolecularField' objects>"
        'get_num_atomics': None, # (!) real value is "<method 'get_num_atomics' of 'panda3d.direct.DCMolecularField' objects>"
    }


