# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class ShaderInput(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This is a small container class that can hold any one of the value types
     * that can be passed as input to a shader.
     */
    """
    def addHash(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_hash(ShaderInput self, int hash)
        
        /**
         *
         */
        """
        pass

    def add_hash(self, ShaderInput_self, int_hash): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_hash(ShaderInput self, int hash)
        
        /**
         *
         */
        """
        pass

    def getBlank(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_blank()
        
        /**
         * Returns a static ShaderInput object with name NULL, priority zero, type
         * INVALID, and all value-fields cleared.
         */
        """
        pass

    def getName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_name(ShaderInput self)
        
        /**
         *
         */
        """
        pass

    def getNodepath(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_nodepath(ShaderInput self)
        
        /**
         * Warning: no error checking is done.  This *will* crash if get_value_type()
         * is not M_nodepath.
         */
        """
        pass

    def getPriority(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_priority(ShaderInput self)
        
        /**
         *
         */
        """
        pass

    def getSampler(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_sampler(ShaderInput self)
        
        /**
         * Warning: no error checking is done.
         */
        """
        pass

    def getTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_texture(ShaderInput self)
        
        /**
         *
         */
        """
        pass

    def getValueType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_value_type(ShaderInput self)
        
        /**
         *
         */
        """
        pass

    def getVector(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_vector(ShaderInput self)
        
        /**
         *
         */
        """
        pass

    def get_blank(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_blank()
        
        /**
         * Returns a static ShaderInput object with name NULL, priority zero, type
         * INVALID, and all value-fields cleared.
         */
        """
        pass

    def get_name(self, ShaderInput_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_name(ShaderInput self)
        
        /**
         *
         */
        """
        pass

    def get_nodepath(self, ShaderInput_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_nodepath(ShaderInput self)
        
        /**
         * Warning: no error checking is done.  This *will* crash if get_value_type()
         * is not M_nodepath.
         */
        """
        pass

    def get_priority(self, ShaderInput_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_priority(ShaderInput self)
        
        /**
         *
         */
        """
        pass

    def get_sampler(self, ShaderInput_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_sampler(ShaderInput self)
        
        /**
         * Warning: no error checking is done.
         */
        """
        pass

    def get_texture(self, ShaderInput_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_texture(ShaderInput self)
        
        /**
         *
         */
        """
        pass

    def get_value_type(self, ShaderInput_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_value_type(ShaderInput self)
        
        /**
         *
         */
        """
        pass

    def get_vector(self, ShaderInput_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_vector(ShaderInput self)
        
        /**
         *
         */
        """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ True if self else False """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
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

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    ALayered = 4
    ARead = 1
    AWrite = 2
    A_layered = 4
    A_read = 1
    A_write = 2
    DtoolClassDict = {
        'ALayered': 4,
        'ARead': 1,
        'AWrite': 2,
        'A_layered': 4,
        'A_read': 1,
        'A_write': 2,
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'MBuffer': 8,
        'MInvalid': 0,
        'MNodepath': 2,
        'MNumeric': 4,
        'MParam': 6,
        'MTexture': 1,
        'MTextureImage': 7,
        'MTextureSampler': 5,
        'MVector': 3,
        'M_buffer': 8,
        'M_invalid': 0,
        'M_nodepath': 2,
        'M_numeric': 4,
        'M_param': 6,
        'M_texture': 1,
        'M_texture_image': 7,
        'M_texture_sampler': 5,
        'M_vector': 3,
        '__bool__': None, # (!) real value is "<slot wrapper '__bool__' of 'panda3d.core.ShaderInput' objects>"
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.ShaderInput' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.ShaderInput' objects>"
        '__doc__': '/**\n * This is a small container class that can hold any one of the value types\n * that can be passed as input to a shader.\n */',
        '__eq__': None, # (!) real value is "<slot wrapper '__eq__' of 'panda3d.core.ShaderInput' objects>"
        '__ge__': None, # (!) real value is "<slot wrapper '__ge__' of 'panda3d.core.ShaderInput' objects>"
        '__gt__': None, # (!) real value is "<slot wrapper '__gt__' of 'panda3d.core.ShaderInput' objects>"
        '__hash__': None, # (!) real value is "<slot wrapper '__hash__' of 'panda3d.core.ShaderInput' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.ShaderInput' objects>"
        '__le__': None, # (!) real value is "<slot wrapper '__le__' of 'panda3d.core.ShaderInput' objects>"
        '__lt__': None, # (!) real value is "<slot wrapper '__lt__' of 'panda3d.core.ShaderInput' objects>"
        '__ne__': None, # (!) real value is "<slot wrapper '__ne__' of 'panda3d.core.ShaderInput' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE293330>'
        'addHash': None, # (!) real value is "<method 'addHash' of 'panda3d.core.ShaderInput' objects>"
        'add_hash': None, # (!) real value is "<method 'add_hash' of 'panda3d.core.ShaderInput' objects>"
        'getBlank': None, # (!) real value is '<staticmethod(<built-in method getBlank of type object at 0x00007FFCFE293330>)>'
        'getName': None, # (!) real value is "<method 'getName' of 'panda3d.core.ShaderInput' objects>"
        'getNodepath': None, # (!) real value is "<method 'getNodepath' of 'panda3d.core.ShaderInput' objects>"
        'getPriority': None, # (!) real value is "<method 'getPriority' of 'panda3d.core.ShaderInput' objects>"
        'getSampler': None, # (!) real value is "<method 'getSampler' of 'panda3d.core.ShaderInput' objects>"
        'getTexture': None, # (!) real value is "<method 'getTexture' of 'panda3d.core.ShaderInput' objects>"
        'getValueType': None, # (!) real value is "<method 'getValueType' of 'panda3d.core.ShaderInput' objects>"
        'getVector': None, # (!) real value is "<method 'getVector' of 'panda3d.core.ShaderInput' objects>"
        'get_blank': None, # (!) real value is '<staticmethod(<built-in method get_blank of type object at 0x00007FFCFE293330>)>'
        'get_name': None, # (!) real value is "<method 'get_name' of 'panda3d.core.ShaderInput' objects>"
        'get_nodepath': None, # (!) real value is "<method 'get_nodepath' of 'panda3d.core.ShaderInput' objects>"
        'get_priority': None, # (!) real value is "<method 'get_priority' of 'panda3d.core.ShaderInput' objects>"
        'get_sampler': None, # (!) real value is "<method 'get_sampler' of 'panda3d.core.ShaderInput' objects>"
        'get_texture': None, # (!) real value is "<method 'get_texture' of 'panda3d.core.ShaderInput' objects>"
        'get_value_type': None, # (!) real value is "<method 'get_value_type' of 'panda3d.core.ShaderInput' objects>"
        'get_vector': None, # (!) real value is "<method 'get_vector' of 'panda3d.core.ShaderInput' objects>"
    }
    MBuffer = 8
    MInvalid = 0
    MNodepath = 2
    MNumeric = 4
    MParam = 6
    MTexture = 1
    MTextureImage = 7
    MTextureSampler = 5
    MVector = 3
    M_buffer = 8
    M_invalid = 0
    M_nodepath = 2
    M_numeric = 4
    M_param = 6
    M_texture = 1
    M_texture_image = 7
    M_texture_sampler = 5
    M_vector = 3


