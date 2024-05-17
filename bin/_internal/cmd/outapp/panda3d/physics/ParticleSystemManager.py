# encoding: utf-8
# module panda3d.physics
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\physics.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


class ParticleSystemManager(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * Manages a set of individual ParticleSystem objects, so that each individual
     * one doesn't have to be updated and rendered every frame See Also :
     * particleSystemManager.cxx
     */
    """
    def attachParticlesystem(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        attach_particlesystem(const ParticleSystemManager self, ParticleSystem ps)
        """
        pass

    def attach_particlesystem(self, const_ParticleSystemManager_self, ParticleSystem_ps): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        attach_particlesystem(const ParticleSystemManager self, ParticleSystem ps)
        """
        pass

    def clear(self, const_ParticleSystemManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear(const ParticleSystemManager self)
        """
        pass

    def doParticles(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        do_particles(const ParticleSystemManager self, float dt)
        do_particles(const ParticleSystemManager self, float dt, ParticleSystem ps, bool do_render)
        
        /**
         * does an update and render for each ps in the list.  this is probably the
         * one you want to use.  Rendering is the expensive operation, and particles
         * REALLY should at least be updated every frame, so nth_frame stepping
         * applies only to rendering.
         */
        
        /**
         * does an update and an optional render for a specific ps.  Since rendering
         * is the expensive operation, multiple updates could be applied before
         * calling the final render.
         */
        """
        pass

    def do_particles(self, const_ParticleSystemManager_self, float_dt): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        do_particles(const ParticleSystemManager self, float dt)
        do_particles(const ParticleSystemManager self, float dt, ParticleSystem ps, bool do_render)
        
        /**
         * does an update and render for each ps in the list.  this is probably the
         * one you want to use.  Rendering is the expensive operation, and particles
         * REALLY should at least be updated every frame, so nth_frame stepping
         * applies only to rendering.
         */
        
        /**
         * does an update and an optional render for a specific ps.  Since rendering
         * is the expensive operation, multiple updates could be applied before
         * calling the final render.
         */
        """
        pass

    def getFrameStepping(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_frame_stepping(ParticleSystemManager self)
        """
        pass

    def get_frame_stepping(self, ParticleSystemManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_frame_stepping(ParticleSystemManager self)
        """
        pass

    def output(self, ParticleSystemManager_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(ParticleSystemManager self, ostream out)
        
        /**
         * Write a string representation of this instance to <out>.
         */
        """
        pass

    def removeParticlesystem(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_particlesystem(const ParticleSystemManager self, ParticleSystem ps)
        
        /**
         * removes a ps from the maintenance list
         */
        """
        pass

    def remove_particlesystem(self, const_ParticleSystemManager_self, ParticleSystem_ps): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_particlesystem(const ParticleSystemManager self, ParticleSystem ps)
        
        /**
         * removes a ps from the maintenance list
         */
        """
        pass

    def setFrameStepping(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_frame_stepping(const ParticleSystemManager self, int every_nth_frame)
        """
        pass

    def set_frame_stepping(self, const_ParticleSystemManager_self, int_every_nth_frame): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_frame_stepping(const ParticleSystemManager self, int every_nth_frame)
        """
        pass

    def write(self, ParticleSystemManager_self, ostream_out, int_indent): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(ParticleSystemManager self, ostream out, int indent)
        
        /**
         * Write a string representation of this instance to <out>.
         */
        """
        pass

    def writePsList(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        write_ps_list(ParticleSystemManager self, ostream out, int indent)
        
        /**
         * Write a string representation of this instance to <out>.
         */
        """
        pass

    def write_ps_list(self, ParticleSystemManager_self, ostream_out, int_indent): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write_ps_list(ParticleSystemManager self, ostream out, int indent)
        
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
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.physics.ParticleSystemManager' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.physics.ParticleSystemManager' objects>"
        '__doc__': "/**\n * Manages a set of individual ParticleSystem objects, so that each individual\n * one doesn't have to be updated and rendered every frame See Also :\n * particleSystemManager.cxx\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.physics.ParticleSystemManager' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC9DF61A0>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.physics.ParticleSystemManager' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.physics.ParticleSystemManager' objects>"
        'attachParticlesystem': None, # (!) real value is "<method 'attachParticlesystem' of 'panda3d.physics.ParticleSystemManager' objects>"
        'attach_particlesystem': None, # (!) real value is "<method 'attach_particlesystem' of 'panda3d.physics.ParticleSystemManager' objects>"
        'clear': None, # (!) real value is "<method 'clear' of 'panda3d.physics.ParticleSystemManager' objects>"
        'doParticles': None, # (!) real value is "<method 'doParticles' of 'panda3d.physics.ParticleSystemManager' objects>"
        'do_particles': None, # (!) real value is "<method 'do_particles' of 'panda3d.physics.ParticleSystemManager' objects>"
        'getFrameStepping': None, # (!) real value is "<method 'getFrameStepping' of 'panda3d.physics.ParticleSystemManager' objects>"
        'get_frame_stepping': None, # (!) real value is "<method 'get_frame_stepping' of 'panda3d.physics.ParticleSystemManager' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.physics.ParticleSystemManager' objects>"
        'removeParticlesystem': None, # (!) real value is "<method 'removeParticlesystem' of 'panda3d.physics.ParticleSystemManager' objects>"
        'remove_particlesystem': None, # (!) real value is "<method 'remove_particlesystem' of 'panda3d.physics.ParticleSystemManager' objects>"
        'setFrameStepping': None, # (!) real value is "<method 'setFrameStepping' of 'panda3d.physics.ParticleSystemManager' objects>"
        'set_frame_stepping': None, # (!) real value is "<method 'set_frame_stepping' of 'panda3d.physics.ParticleSystemManager' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.physics.ParticleSystemManager' objects>"
        'writePsList': None, # (!) real value is "<method 'writePsList' of 'panda3d.physics.ParticleSystemManager' objects>"
        'write_ps_list': None, # (!) real value is "<method 'write_ps_list' of 'panda3d.physics.ParticleSystemManager' objects>"
    }


