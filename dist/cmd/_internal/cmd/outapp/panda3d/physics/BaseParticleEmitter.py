# encoding: utf-8
# module panda3d.physics
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\physics.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


class BaseParticleEmitter(__panda3d_core.ReferenceCount):
    # no doc
    def generate(self, const_BaseParticleEmitter_self, LPoint3f_pos, LVector3f_vel): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        generate(const BaseParticleEmitter self, LPoint3f pos, LVector3f vel)
        
        /**
         * parent generation function
         */
        """
        pass

    def getAmplitude(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_amplitude(BaseParticleEmitter self)
        
        /**
         * amplitude query
         */
        """
        pass

    def getAmplitudeSpread(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_amplitude_spread(BaseParticleEmitter self)
        
        /**
         * amplitude spread query
         */
        """
        pass

    def getEmissionType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_emission_type(BaseParticleEmitter self)
        
        /**
         * emission type query
         */
        """
        pass

    def getExplicitLaunchVector(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_explicit_launch_vector(BaseParticleEmitter self)
        
        /**
         * query for explicit emission launch vector
         */
        """
        pass

    def getOffsetForce(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_offset_force(BaseParticleEmitter self)
        
        /**
         * user-defined force
         */
        """
        pass

    def getRadiateOrigin(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_radiate_origin(BaseParticleEmitter self)
        
        /**
         * query for explicit emission launch vector
         */
        """
        pass

    def get_amplitude(self, BaseParticleEmitter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_amplitude(BaseParticleEmitter self)
        
        /**
         * amplitude query
         */
        """
        pass

    def get_amplitude_spread(self, BaseParticleEmitter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_amplitude_spread(BaseParticleEmitter self)
        
        /**
         * amplitude spread query
         */
        """
        pass

    def get_emission_type(self, BaseParticleEmitter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_emission_type(BaseParticleEmitter self)
        
        /**
         * emission type query
         */
        """
        pass

    def get_explicit_launch_vector(self, BaseParticleEmitter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_explicit_launch_vector(BaseParticleEmitter self)
        
        /**
         * query for explicit emission launch vector
         */
        """
        pass

    def get_offset_force(self, BaseParticleEmitter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_offset_force(BaseParticleEmitter self)
        
        /**
         * user-defined force
         */
        """
        pass

    def get_radiate_origin(self, BaseParticleEmitter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_radiate_origin(BaseParticleEmitter self)
        
        /**
         * query for explicit emission launch vector
         */
        """
        pass

    def makeCopy(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_copy(const BaseParticleEmitter self)
        """
        pass

    def make_copy(self, const_BaseParticleEmitter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_copy(const BaseParticleEmitter self)
        """
        pass

    def output(self, BaseParticleEmitter_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(BaseParticleEmitter self, ostream out)
        
        /**
         * Write a string representation of this instance to <out>.
         */
        """
        pass

    def setAmplitude(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_amplitude(const BaseParticleEmitter self, float a)
        
        /**
         * amplitude assignment
         */
        """
        pass

    def setAmplitudeSpread(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_amplitude_spread(const BaseParticleEmitter self, float as)
        
        /**
         * amplitude spread assignment
         */
        """
        pass

    def setEmissionType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_emission_type(const BaseParticleEmitter self, int et)
        
        /**
         * emission type assignment
         */
        """
        pass

    def setExplicitLaunchVector(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_explicit_launch_vector(const BaseParticleEmitter self, const LVector3f elv)
        
        // this is a constant force applied to all particles
        
        /**
         * assignment of explicit emission launch vector
         */
        """
        pass

    def setOffsetForce(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_offset_force(const BaseParticleEmitter self, const LVector3f of)
        
        // this is a constant force applied to all particles
        
        /**
         * user-defined force
         */
        """
        pass

    def setRadiateOrigin(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_radiate_origin(const BaseParticleEmitter self, const LPoint3f ro)
        
        /**
         * assignment of radiate emission origin point
         */
        """
        pass

    def set_amplitude(self, const_BaseParticleEmitter_self, float_a): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_amplitude(const BaseParticleEmitter self, float a)
        
        /**
         * amplitude assignment
         */
        """
        pass

    def set_amplitude_spread(self, const_BaseParticleEmitter_self, float_as): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_amplitude_spread(const BaseParticleEmitter self, float as)
        
        /**
         * amplitude spread assignment
         */
        """
        pass

    def set_emission_type(self, const_BaseParticleEmitter_self, int_et): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_emission_type(const BaseParticleEmitter self, int et)
        
        /**
         * emission type assignment
         */
        """
        pass

    def set_explicit_launch_vector(self, const_BaseParticleEmitter_self, const_LVector3f_elv): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_explicit_launch_vector(const BaseParticleEmitter self, const LVector3f elv)
        
        // this is a constant force applied to all particles
        
        /**
         * assignment of explicit emission launch vector
         */
        """
        pass

    def set_offset_force(self, const_BaseParticleEmitter_self, const_LVector3f_of): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_offset_force(const BaseParticleEmitter self, const LVector3f of)
        
        // this is a constant force applied to all particles
        
        /**
         * user-defined force
         */
        """
        pass

    def set_radiate_origin(self, const_BaseParticleEmitter_self, const_LPoint3f_ro): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_radiate_origin(const BaseParticleEmitter self, const LPoint3f ro)
        
        /**
         * assignment of radiate emission origin point
         */
        """
        pass

    def write(self, BaseParticleEmitter_self, ostream_out, int_indent): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(BaseParticleEmitter self, ostream out, int indent)
        
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
        'ETCUSTOM': 2,
        'ETEXPLICIT': 0,
        'ETRADIATE': 1,
        'ET_CUSTOM': 2,
        'ET_EXPLICIT': 0,
        'ET_RADIATE': 1,
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.physics.BaseParticleEmitter' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.physics.BaseParticleEmitter' objects>"
        '__doc__': None,
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.physics.BaseParticleEmitter' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC9DF2ED0>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.physics.BaseParticleEmitter' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.physics.BaseParticleEmitter' objects>"
        'generate': None, # (!) real value is "<method 'generate' of 'panda3d.physics.BaseParticleEmitter' objects>"
        'getAmplitude': None, # (!) real value is "<method 'getAmplitude' of 'panda3d.physics.BaseParticleEmitter' objects>"
        'getAmplitudeSpread': None, # (!) real value is "<method 'getAmplitudeSpread' of 'panda3d.physics.BaseParticleEmitter' objects>"
        'getEmissionType': None, # (!) real value is "<method 'getEmissionType' of 'panda3d.physics.BaseParticleEmitter' objects>"
        'getExplicitLaunchVector': None, # (!) real value is "<method 'getExplicitLaunchVector' of 'panda3d.physics.BaseParticleEmitter' objects>"
        'getOffsetForce': None, # (!) real value is "<method 'getOffsetForce' of 'panda3d.physics.BaseParticleEmitter' objects>"
        'getRadiateOrigin': None, # (!) real value is "<method 'getRadiateOrigin' of 'panda3d.physics.BaseParticleEmitter' objects>"
        'get_amplitude': None, # (!) real value is "<method 'get_amplitude' of 'panda3d.physics.BaseParticleEmitter' objects>"
        'get_amplitude_spread': None, # (!) real value is "<method 'get_amplitude_spread' of 'panda3d.physics.BaseParticleEmitter' objects>"
        'get_emission_type': None, # (!) real value is "<method 'get_emission_type' of 'panda3d.physics.BaseParticleEmitter' objects>"
        'get_explicit_launch_vector': None, # (!) real value is "<method 'get_explicit_launch_vector' of 'panda3d.physics.BaseParticleEmitter' objects>"
        'get_offset_force': None, # (!) real value is "<method 'get_offset_force' of 'panda3d.physics.BaseParticleEmitter' objects>"
        'get_radiate_origin': None, # (!) real value is "<method 'get_radiate_origin' of 'panda3d.physics.BaseParticleEmitter' objects>"
        'makeCopy': None, # (!) real value is "<method 'makeCopy' of 'panda3d.physics.BaseParticleEmitter' objects>"
        'make_copy': None, # (!) real value is "<method 'make_copy' of 'panda3d.physics.BaseParticleEmitter' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.physics.BaseParticleEmitter' objects>"
        'setAmplitude': None, # (!) real value is "<method 'setAmplitude' of 'panda3d.physics.BaseParticleEmitter' objects>"
        'setAmplitudeSpread': None, # (!) real value is "<method 'setAmplitudeSpread' of 'panda3d.physics.BaseParticleEmitter' objects>"
        'setEmissionType': None, # (!) real value is "<method 'setEmissionType' of 'panda3d.physics.BaseParticleEmitter' objects>"
        'setExplicitLaunchVector': None, # (!) real value is "<method 'setExplicitLaunchVector' of 'panda3d.physics.BaseParticleEmitter' objects>"
        'setOffsetForce': None, # (!) real value is "<method 'setOffsetForce' of 'panda3d.physics.BaseParticleEmitter' objects>"
        'setRadiateOrigin': None, # (!) real value is "<method 'setRadiateOrigin' of 'panda3d.physics.BaseParticleEmitter' objects>"
        'set_amplitude': None, # (!) real value is "<method 'set_amplitude' of 'panda3d.physics.BaseParticleEmitter' objects>"
        'set_amplitude_spread': None, # (!) real value is "<method 'set_amplitude_spread' of 'panda3d.physics.BaseParticleEmitter' objects>"
        'set_emission_type': None, # (!) real value is "<method 'set_emission_type' of 'panda3d.physics.BaseParticleEmitter' objects>"
        'set_explicit_launch_vector': None, # (!) real value is "<method 'set_explicit_launch_vector' of 'panda3d.physics.BaseParticleEmitter' objects>"
        'set_offset_force': None, # (!) real value is "<method 'set_offset_force' of 'panda3d.physics.BaseParticleEmitter' objects>"
        'set_radiate_origin': None, # (!) real value is "<method 'set_radiate_origin' of 'panda3d.physics.BaseParticleEmitter' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.physics.BaseParticleEmitter' objects>"
    }
    ETCUSTOM = 2
    ETEXPLICIT = 0
    ETRADIATE = 1
    ET_CUSTOM = 2
    ET_EXPLICIT = 0
    ET_RADIATE = 1


