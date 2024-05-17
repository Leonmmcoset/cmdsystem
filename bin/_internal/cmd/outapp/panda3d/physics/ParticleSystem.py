# encoding: utf-8
# module panda3d.physics
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\physics.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


from .Physical import Physical

class ParticleSystem(Physical):
    """
    /**
     * Contains and manages a particle system.
     */
    """
    def addSpawnTemplate(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_spawn_template(const ParticleSystem self, ParticleSystem ps)
        
        /**
        
         */
        """
        pass

    def add_spawn_template(self, const_ParticleSystem_self, ParticleSystem_ps): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_spawn_template(const ParticleSystem self, ParticleSystem ps)
        
        /**
        
         */
        """
        pass

    def clearFloorZ(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_floor_z(const ParticleSystem self)
        
        /**
        
         */
        """
        pass

    def clearSpawnTemplates(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_spawn_templates(const ParticleSystem self)
        
        /**
        
         */
        """
        pass

    def clearToInitial(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_to_initial(const ParticleSystem self)
        
        /**
         * Resets the system to its start state by resizing to 0, then resizing back
         * to current size.
         */
        """
        pass

    def clear_floor_z(self, const_ParticleSystem_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_floor_z(const ParticleSystem self)
        
        /**
        
         */
        """
        pass

    def clear_spawn_templates(self, const_ParticleSystem_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_spawn_templates(const ParticleSystem self)
        
        /**
        
         */
        """
        pass

    def clear_to_initial(self, const_ParticleSystem_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_to_initial(const ParticleSystem self)
        
        /**
         * Resets the system to its start state by resizing to 0, then resizing back
         * to current size.
         */
        """
        pass

    def getActiveSystemFlag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_active_system_flag(ParticleSystem self)
        
        /**
        
         */
        """
        pass

    def getBirthRate(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_birth_rate(ParticleSystem self)
        
        /**
        
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getEmitter(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_emitter(ParticleSystem self)
        
        /**
        
         */
        """
        pass

    def getFactory(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_factory(ParticleSystem self)
        
        /**
        
         */
        """
        pass

    def getFloorZ(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_floor_z(ParticleSystem self)
        
        /**
        
         */
        """
        pass

    def getIWasSpawnedFlag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_i_was_spawned_flag(ParticleSystem self)
        
        /**
        
         */
        """
        pass

    def getLitterSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_litter_size(ParticleSystem self)
        
        /**
        
         */
        """
        pass

    def getLitterSpread(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_litter_spread(ParticleSystem self)
        
        /**
        
         */
        """
        pass

    def getLivingParticles(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_living_particles(ParticleSystem self)
        
        /**
        
         */
        """
        pass

    def getLocalVelocityFlag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_local_velocity_flag(ParticleSystem self)
        
        /**
        
         */
        """
        pass

    def getPoolSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_pool_size(ParticleSystem self)
        
        /**
        
         */
        """
        pass

    def getRenderer(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_renderer(ParticleSystem self)
        
        /**
        
         */
        """
        pass

    def getRenderParent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_render_parent(ParticleSystem self)
        
        /**
        
         */
        """
        pass

    def getSoftBirthRate(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_soft_birth_rate(ParticleSystem self)
        
        /**
        
         */
        """
        pass

    def getSpawnOnDeathFlag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_spawn_on_death_flag(ParticleSystem self)
        
        /**
        
         */
        """
        pass

    def getSpawnRenderNode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_spawn_render_node(ParticleSystem self)
        
        /**
        
         */
        """
        pass

    def getSpawnRenderNodePath(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_spawn_render_node_path(ParticleSystem self)
        
        /**
        
         */
        """
        pass

    def getSystemAge(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_system_age(ParticleSystem self)
        
        /**
        
         */
        """
        pass

    def getSystemGrowsOlderFlag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_system_grows_older_flag(ParticleSystem self)
        
        /**
        
         */
        """
        pass

    def getSystemLifespan(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_system_lifespan(ParticleSystem self)
        
        /**
        
         */
        """
        pass

    def getTicsSinceBirth(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_tics_since_birth(ParticleSystem self)
        
        /**
        
        */
        """
        pass

    def get_active_system_flag(self, ParticleSystem_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_active_system_flag(ParticleSystem self)
        
        /**
        
         */
        """
        pass

    def get_birth_rate(self, ParticleSystem_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_birth_rate(ParticleSystem self)
        
        /**
        
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_emitter(self, ParticleSystem_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_emitter(ParticleSystem self)
        
        /**
        
         */
        """
        pass

    def get_factory(self, ParticleSystem_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_factory(ParticleSystem self)
        
        /**
        
         */
        """
        pass

    def get_floor_z(self, ParticleSystem_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_floor_z(ParticleSystem self)
        
        /**
        
         */
        """
        pass

    def get_i_was_spawned_flag(self, ParticleSystem_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_i_was_spawned_flag(ParticleSystem self)
        
        /**
        
         */
        """
        pass

    def get_litter_size(self, ParticleSystem_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_litter_size(ParticleSystem self)
        
        /**
        
         */
        """
        pass

    def get_litter_spread(self, ParticleSystem_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_litter_spread(ParticleSystem self)
        
        /**
        
         */
        """
        pass

    def get_living_particles(self, ParticleSystem_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_living_particles(ParticleSystem self)
        
        /**
        
         */
        """
        pass

    def get_local_velocity_flag(self, ParticleSystem_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_local_velocity_flag(ParticleSystem self)
        
        /**
        
         */
        """
        pass

    def get_pool_size(self, ParticleSystem_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_pool_size(ParticleSystem self)
        
        /**
        
         */
        """
        pass

    def get_renderer(self, ParticleSystem_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_renderer(ParticleSystem self)
        
        /**
        
         */
        """
        pass

    def get_render_parent(self, ParticleSystem_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_render_parent(ParticleSystem self)
        
        /**
        
         */
        """
        pass

    def get_soft_birth_rate(self, ParticleSystem_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_soft_birth_rate(ParticleSystem self)
        
        /**
        
         */
        """
        pass

    def get_spawn_on_death_flag(self, ParticleSystem_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_spawn_on_death_flag(ParticleSystem self)
        
        /**
        
         */
        """
        pass

    def get_spawn_render_node(self, ParticleSystem_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_spawn_render_node(ParticleSystem self)
        
        /**
        
         */
        """
        pass

    def get_spawn_render_node_path(self, ParticleSystem_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_spawn_render_node_path(ParticleSystem self)
        
        /**
        
         */
        """
        pass

    def get_system_age(self, ParticleSystem_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_system_age(ParticleSystem self)
        
        /**
        
         */
        """
        pass

    def get_system_grows_older_flag(self, ParticleSystem_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_system_grows_older_flag(ParticleSystem self)
        
        /**
        
         */
        """
        pass

    def get_system_lifespan(self, ParticleSystem_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_system_lifespan(ParticleSystem self)
        
        /**
        
         */
        """
        pass

    def get_tics_since_birth(self, ParticleSystem_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_tics_since_birth(ParticleSystem self)
        
        /**
        
        */
        """
        pass

    def induceLabor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        induce_labor(const ParticleSystem self)
        
        /**
         * Forces the birth of a particle litter this frame by resetting
         * _tics_since_birth
         */
        """
        pass

    def induce_labor(self, const_ParticleSystem_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        induce_labor(const ParticleSystem self)
        
        /**
         * Forces the birth of a particle litter this frame by resetting
         * _tics_since_birth
         */
        """
        pass

    def render(self, const_ParticleSystem_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        render(const ParticleSystem self)
        
        /**
         * Populates an attached GeomNode structure with the particle geometry for
         * rendering.  This is a wrapper for accessability.
         */
        """
        pass

    def setActiveSystemFlag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_active_system_flag(const ParticleSystem self, bool a)
        
        /**
        
         */
        """
        pass

    def setBirthRate(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_birth_rate(const ParticleSystem self, float new_br)
        
        /**
        
         */
        """
        pass

    def setEmitter(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_emitter(const ParticleSystem self, BaseParticleEmitter e)
        
        /**
        
         */
        """
        pass

    def setFactory(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_factory(const ParticleSystem self, BaseParticleFactory f)
        
        /**
        
         */
        """
        pass

    def setFloorZ(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_floor_z(const ParticleSystem self, float z)
        
        /**
        
         */
        """
        pass

    def setLitterSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_litter_size(const ParticleSystem self, int new_ls)
        
        /**
        
         */
        """
        pass

    def setLitterSpread(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_litter_spread(const ParticleSystem self, int new_ls)
        
        /**
        
         */
        """
        pass

    def setLocalVelocityFlag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_local_velocity_flag(const ParticleSystem self, bool lv)
        
        /**
        
         */
        """
        pass

    def setPoolSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_pool_size(const ParticleSystem self, int size)
        
        // accessqueries
        
        /**
        
         */
        """
        pass

    def setRenderer(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_renderer(const ParticleSystem self, BaseParticleRenderer r)
        
        /**
        
         */
        """
        pass

    def setRenderParent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_render_parent(const ParticleSystem self, PandaNode node)
        set_render_parent(const ParticleSystem self, const NodePath node)
        
        /**
        
         */
        
        /**
        
         */
        """
        pass

    def setSoftBirthRate(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_soft_birth_rate(const ParticleSystem self, float new_br)
        
        /**
        
         */
        """
        pass

    def setSpawnOnDeathFlag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_spawn_on_death_flag(const ParticleSystem self, bool sod)
        
        /**
        
         */
        """
        pass

    def setSpawnRenderNode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_spawn_render_node(const ParticleSystem self, PandaNode node)
        
        /**
        
         */
        """
        pass

    def setSpawnRenderNodePath(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_spawn_render_node_path(const ParticleSystem self, const NodePath node)
        
        /**
        
         */
        """
        pass

    def setSystemAge(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_system_age(const ParticleSystem self, float age)
        
        /**
        
         */
        """
        pass

    def setSystemGrowsOlderFlag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_system_grows_older_flag(const ParticleSystem self, bool sgo)
        
        /**
        
         */
        """
        pass

    def setSystemLifespan(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_system_lifespan(const ParticleSystem self, float sl)
        
        /**
        
         */
        """
        pass

    def setTemplateSystemFlag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_template_system_flag(const ParticleSystem self, bool tsf)
        
        /**
        
         */
        """
        pass

    def set_active_system_flag(self, const_ParticleSystem_self, bool_a): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_active_system_flag(const ParticleSystem self, bool a)
        
        /**
        
         */
        """
        pass

    def set_birth_rate(self, const_ParticleSystem_self, float_new_br): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_birth_rate(const ParticleSystem self, float new_br)
        
        /**
        
         */
        """
        pass

    def set_emitter(self, const_ParticleSystem_self, BaseParticleEmitter_e): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_emitter(const ParticleSystem self, BaseParticleEmitter e)
        
        /**
        
         */
        """
        pass

    def set_factory(self, const_ParticleSystem_self, BaseParticleFactory_f): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_factory(const ParticleSystem self, BaseParticleFactory f)
        
        /**
        
         */
        """
        pass

    def set_floor_z(self, const_ParticleSystem_self, float_z): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_floor_z(const ParticleSystem self, float z)
        
        /**
        
         */
        """
        pass

    def set_litter_size(self, const_ParticleSystem_self, int_new_ls): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_litter_size(const ParticleSystem self, int new_ls)
        
        /**
        
         */
        """
        pass

    def set_litter_spread(self, const_ParticleSystem_self, int_new_ls): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_litter_spread(const ParticleSystem self, int new_ls)
        
        /**
        
         */
        """
        pass

    def set_local_velocity_flag(self, const_ParticleSystem_self, bool_lv): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_local_velocity_flag(const ParticleSystem self, bool lv)
        
        /**
        
         */
        """
        pass

    def set_pool_size(self, const_ParticleSystem_self, int_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_pool_size(const ParticleSystem self, int size)
        
        // accessqueries
        
        /**
        
         */
        """
        pass

    def set_renderer(self, const_ParticleSystem_self, BaseParticleRenderer_r): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_renderer(const ParticleSystem self, BaseParticleRenderer r)
        
        /**
        
         */
        """
        pass

    def set_render_parent(self, const_ParticleSystem_self, PandaNode_node): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_render_parent(const ParticleSystem self, PandaNode node)
        set_render_parent(const ParticleSystem self, const NodePath node)
        
        /**
        
         */
        
        /**
        
         */
        """
        pass

    def set_soft_birth_rate(self, const_ParticleSystem_self, float_new_br): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_soft_birth_rate(const ParticleSystem self, float new_br)
        
        /**
        
         */
        """
        pass

    def set_spawn_on_death_flag(self, const_ParticleSystem_self, bool_sod): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_spawn_on_death_flag(const ParticleSystem self, bool sod)
        
        /**
        
         */
        """
        pass

    def set_spawn_render_node(self, const_ParticleSystem_self, PandaNode_node): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_spawn_render_node(const ParticleSystem self, PandaNode node)
        
        /**
        
         */
        """
        pass

    def set_spawn_render_node_path(self, const_ParticleSystem_self, const_NodePath_node): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_spawn_render_node_path(const ParticleSystem self, const NodePath node)
        
        /**
        
         */
        """
        pass

    def set_system_age(self, const_ParticleSystem_self, float_age): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_system_age(const ParticleSystem self, float age)
        
        /**
        
         */
        """
        pass

    def set_system_grows_older_flag(self, const_ParticleSystem_self, bool_sgo): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_system_grows_older_flag(const ParticleSystem self, bool sgo)
        
        /**
        
         */
        """
        pass

    def set_system_lifespan(self, const_ParticleSystem_self, float_sl): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_system_lifespan(const ParticleSystem self, float sl)
        
        /**
        
         */
        """
        pass

    def set_template_system_flag(self, const_ParticleSystem_self, bool_tsf): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_template_system_flag(const ParticleSystem self, bool tsf)
        
        /**
        
         */
        """
        pass

    def softStart(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        soft_start(const ParticleSystem self)
        soft_start(const ParticleSystem self, float br)
        soft_start(const ParticleSystem self, float br, float first_birth_delay)
        
        /**
         * Causes system to use birth rate set by set_birth_rate()
         */
        
        /**
         * Causes system to use birth rate set by set_birth_rate(), with the system's
         * first birth being delayed by the value of first_birth_delay. Note that a
         * negative delay is perfectly valid, causing the first birth to happen
         * sooner rather than later.
         */
        """
        pass

    def softStop(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        soft_stop(const ParticleSystem self, float br)
        
        /**
         * Causes system to use birth rate set by set_soft_birth_rate()
         */
        """
        pass

    def soft_start(self, const_ParticleSystem_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        soft_start(const ParticleSystem self)
        soft_start(const ParticleSystem self, float br)
        soft_start(const ParticleSystem self, float br, float first_birth_delay)
        
        /**
         * Causes system to use birth rate set by set_birth_rate()
         */
        
        /**
         * Causes system to use birth rate set by set_birth_rate(), with the system's
         * first birth being delayed by the value of first_birth_delay. Note that a
         * negative delay is perfectly valid, causing the first birth to happen
         * sooner rather than later.
         */
        """
        pass

    def soft_stop(self, const_ParticleSystem_self, float_br): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        soft_stop(const ParticleSystem self, float br)
        
        /**
         * Causes system to use birth rate set by set_soft_birth_rate()
         */
        """
        pass

    def update(self, const_ParticleSystem_self, float_dt): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        update(const ParticleSystem self, float dt)
        """
        pass

    def writeFreeParticleFifo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        write_free_particle_fifo(ParticleSystem self, ostream out, int indent)
        
        /**
         * Write a string representation of this instance to <out>.
         */
        """
        pass

    def writeSpawnTemplates(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        write_spawn_templates(ParticleSystem self, ostream out, int indent)
        
        /**
         * Write a string representation of this instance to <out>.
         */
        """
        pass

    def write_free_particle_fifo(self, ParticleSystem_self, ostream_out, int_indent): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write_free_particle_fifo(ParticleSystem self, ostream out, int indent)
        
        /**
         * Write a string representation of this instance to <out>.
         */
        """
        pass

    def write_spawn_templates(self, ParticleSystem_self, ostream_out, int_indent): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write_spawn_templates(ParticleSystem self, ostream out, int indent)
        
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

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.physics.ParticleSystem' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.physics.ParticleSystem' objects>"
        '__doc__': '/**\n * Contains and manages a particle system.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.physics.ParticleSystem' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC9DF4BE0>'
        'addSpawnTemplate': None, # (!) real value is "<method 'addSpawnTemplate' of 'panda3d.physics.ParticleSystem' objects>"
        'add_spawn_template': None, # (!) real value is "<method 'add_spawn_template' of 'panda3d.physics.ParticleSystem' objects>"
        'clearFloorZ': None, # (!) real value is "<method 'clearFloorZ' of 'panda3d.physics.ParticleSystem' objects>"
        'clearSpawnTemplates': None, # (!) real value is "<method 'clearSpawnTemplates' of 'panda3d.physics.ParticleSystem' objects>"
        'clearToInitial': None, # (!) real value is "<method 'clearToInitial' of 'panda3d.physics.ParticleSystem' objects>"
        'clear_floor_z': None, # (!) real value is "<method 'clear_floor_z' of 'panda3d.physics.ParticleSystem' objects>"
        'clear_spawn_templates': None, # (!) real value is "<method 'clear_spawn_templates' of 'panda3d.physics.ParticleSystem' objects>"
        'clear_to_initial': None, # (!) real value is "<method 'clear_to_initial' of 'panda3d.physics.ParticleSystem' objects>"
        'getActiveSystemFlag': None, # (!) real value is "<method 'getActiveSystemFlag' of 'panda3d.physics.ParticleSystem' objects>"
        'getBirthRate': None, # (!) real value is "<method 'getBirthRate' of 'panda3d.physics.ParticleSystem' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFDC9DF4BE0>)>'
        'getEmitter': None, # (!) real value is "<method 'getEmitter' of 'panda3d.physics.ParticleSystem' objects>"
        'getFactory': None, # (!) real value is "<method 'getFactory' of 'panda3d.physics.ParticleSystem' objects>"
        'getFloorZ': None, # (!) real value is "<method 'getFloorZ' of 'panda3d.physics.ParticleSystem' objects>"
        'getIWasSpawnedFlag': None, # (!) real value is "<method 'getIWasSpawnedFlag' of 'panda3d.physics.ParticleSystem' objects>"
        'getLitterSize': None, # (!) real value is "<method 'getLitterSize' of 'panda3d.physics.ParticleSystem' objects>"
        'getLitterSpread': None, # (!) real value is "<method 'getLitterSpread' of 'panda3d.physics.ParticleSystem' objects>"
        'getLivingParticles': None, # (!) real value is "<method 'getLivingParticles' of 'panda3d.physics.ParticleSystem' objects>"
        'getLocalVelocityFlag': None, # (!) real value is "<method 'getLocalVelocityFlag' of 'panda3d.physics.ParticleSystem' objects>"
        'getPoolSize': None, # (!) real value is "<method 'getPoolSize' of 'panda3d.physics.ParticleSystem' objects>"
        'getRenderParent': None, # (!) real value is "<method 'getRenderParent' of 'panda3d.physics.ParticleSystem' objects>"
        'getRenderer': None, # (!) real value is "<method 'getRenderer' of 'panda3d.physics.ParticleSystem' objects>"
        'getSoftBirthRate': None, # (!) real value is "<method 'getSoftBirthRate' of 'panda3d.physics.ParticleSystem' objects>"
        'getSpawnOnDeathFlag': None, # (!) real value is "<method 'getSpawnOnDeathFlag' of 'panda3d.physics.ParticleSystem' objects>"
        'getSpawnRenderNode': None, # (!) real value is "<method 'getSpawnRenderNode' of 'panda3d.physics.ParticleSystem' objects>"
        'getSpawnRenderNodePath': None, # (!) real value is "<method 'getSpawnRenderNodePath' of 'panda3d.physics.ParticleSystem' objects>"
        'getSystemAge': None, # (!) real value is "<method 'getSystemAge' of 'panda3d.physics.ParticleSystem' objects>"
        'getSystemGrowsOlderFlag': None, # (!) real value is "<method 'getSystemGrowsOlderFlag' of 'panda3d.physics.ParticleSystem' objects>"
        'getSystemLifespan': None, # (!) real value is "<method 'getSystemLifespan' of 'panda3d.physics.ParticleSystem' objects>"
        'getTicsSinceBirth': None, # (!) real value is "<method 'getTicsSinceBirth' of 'panda3d.physics.ParticleSystem' objects>"
        'get_active_system_flag': None, # (!) real value is "<method 'get_active_system_flag' of 'panda3d.physics.ParticleSystem' objects>"
        'get_birth_rate': None, # (!) real value is "<method 'get_birth_rate' of 'panda3d.physics.ParticleSystem' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFDC9DF4BE0>)>'
        'get_emitter': None, # (!) real value is "<method 'get_emitter' of 'panda3d.physics.ParticleSystem' objects>"
        'get_factory': None, # (!) real value is "<method 'get_factory' of 'panda3d.physics.ParticleSystem' objects>"
        'get_floor_z': None, # (!) real value is "<method 'get_floor_z' of 'panda3d.physics.ParticleSystem' objects>"
        'get_i_was_spawned_flag': None, # (!) real value is "<method 'get_i_was_spawned_flag' of 'panda3d.physics.ParticleSystem' objects>"
        'get_litter_size': None, # (!) real value is "<method 'get_litter_size' of 'panda3d.physics.ParticleSystem' objects>"
        'get_litter_spread': None, # (!) real value is "<method 'get_litter_spread' of 'panda3d.physics.ParticleSystem' objects>"
        'get_living_particles': None, # (!) real value is "<method 'get_living_particles' of 'panda3d.physics.ParticleSystem' objects>"
        'get_local_velocity_flag': None, # (!) real value is "<method 'get_local_velocity_flag' of 'panda3d.physics.ParticleSystem' objects>"
        'get_pool_size': None, # (!) real value is "<method 'get_pool_size' of 'panda3d.physics.ParticleSystem' objects>"
        'get_render_parent': None, # (!) real value is "<method 'get_render_parent' of 'panda3d.physics.ParticleSystem' objects>"
        'get_renderer': None, # (!) real value is "<method 'get_renderer' of 'panda3d.physics.ParticleSystem' objects>"
        'get_soft_birth_rate': None, # (!) real value is "<method 'get_soft_birth_rate' of 'panda3d.physics.ParticleSystem' objects>"
        'get_spawn_on_death_flag': None, # (!) real value is "<method 'get_spawn_on_death_flag' of 'panda3d.physics.ParticleSystem' objects>"
        'get_spawn_render_node': None, # (!) real value is "<method 'get_spawn_render_node' of 'panda3d.physics.ParticleSystem' objects>"
        'get_spawn_render_node_path': None, # (!) real value is "<method 'get_spawn_render_node_path' of 'panda3d.physics.ParticleSystem' objects>"
        'get_system_age': None, # (!) real value is "<method 'get_system_age' of 'panda3d.physics.ParticleSystem' objects>"
        'get_system_grows_older_flag': None, # (!) real value is "<method 'get_system_grows_older_flag' of 'panda3d.physics.ParticleSystem' objects>"
        'get_system_lifespan': None, # (!) real value is "<method 'get_system_lifespan' of 'panda3d.physics.ParticleSystem' objects>"
        'get_tics_since_birth': None, # (!) real value is "<method 'get_tics_since_birth' of 'panda3d.physics.ParticleSystem' objects>"
        'induceLabor': None, # (!) real value is "<method 'induceLabor' of 'panda3d.physics.ParticleSystem' objects>"
        'induce_labor': None, # (!) real value is "<method 'induce_labor' of 'panda3d.physics.ParticleSystem' objects>"
        'render': None, # (!) real value is "<method 'render' of 'panda3d.physics.ParticleSystem' objects>"
        'setActiveSystemFlag': None, # (!) real value is "<method 'setActiveSystemFlag' of 'panda3d.physics.ParticleSystem' objects>"
        'setBirthRate': None, # (!) real value is "<method 'setBirthRate' of 'panda3d.physics.ParticleSystem' objects>"
        'setEmitter': None, # (!) real value is "<method 'setEmitter' of 'panda3d.physics.ParticleSystem' objects>"
        'setFactory': None, # (!) real value is "<method 'setFactory' of 'panda3d.physics.ParticleSystem' objects>"
        'setFloorZ': None, # (!) real value is "<method 'setFloorZ' of 'panda3d.physics.ParticleSystem' objects>"
        'setLitterSize': None, # (!) real value is "<method 'setLitterSize' of 'panda3d.physics.ParticleSystem' objects>"
        'setLitterSpread': None, # (!) real value is "<method 'setLitterSpread' of 'panda3d.physics.ParticleSystem' objects>"
        'setLocalVelocityFlag': None, # (!) real value is "<method 'setLocalVelocityFlag' of 'panda3d.physics.ParticleSystem' objects>"
        'setPoolSize': None, # (!) real value is "<method 'setPoolSize' of 'panda3d.physics.ParticleSystem' objects>"
        'setRenderParent': None, # (!) real value is "<method 'setRenderParent' of 'panda3d.physics.ParticleSystem' objects>"
        'setRenderer': None, # (!) real value is "<method 'setRenderer' of 'panda3d.physics.ParticleSystem' objects>"
        'setSoftBirthRate': None, # (!) real value is "<method 'setSoftBirthRate' of 'panda3d.physics.ParticleSystem' objects>"
        'setSpawnOnDeathFlag': None, # (!) real value is "<method 'setSpawnOnDeathFlag' of 'panda3d.physics.ParticleSystem' objects>"
        'setSpawnRenderNode': None, # (!) real value is "<method 'setSpawnRenderNode' of 'panda3d.physics.ParticleSystem' objects>"
        'setSpawnRenderNodePath': None, # (!) real value is "<method 'setSpawnRenderNodePath' of 'panda3d.physics.ParticleSystem' objects>"
        'setSystemAge': None, # (!) real value is "<method 'setSystemAge' of 'panda3d.physics.ParticleSystem' objects>"
        'setSystemGrowsOlderFlag': None, # (!) real value is "<method 'setSystemGrowsOlderFlag' of 'panda3d.physics.ParticleSystem' objects>"
        'setSystemLifespan': None, # (!) real value is "<method 'setSystemLifespan' of 'panda3d.physics.ParticleSystem' objects>"
        'setTemplateSystemFlag': None, # (!) real value is "<method 'setTemplateSystemFlag' of 'panda3d.physics.ParticleSystem' objects>"
        'set_active_system_flag': None, # (!) real value is "<method 'set_active_system_flag' of 'panda3d.physics.ParticleSystem' objects>"
        'set_birth_rate': None, # (!) real value is "<method 'set_birth_rate' of 'panda3d.physics.ParticleSystem' objects>"
        'set_emitter': None, # (!) real value is "<method 'set_emitter' of 'panda3d.physics.ParticleSystem' objects>"
        'set_factory': None, # (!) real value is "<method 'set_factory' of 'panda3d.physics.ParticleSystem' objects>"
        'set_floor_z': None, # (!) real value is "<method 'set_floor_z' of 'panda3d.physics.ParticleSystem' objects>"
        'set_litter_size': None, # (!) real value is "<method 'set_litter_size' of 'panda3d.physics.ParticleSystem' objects>"
        'set_litter_spread': None, # (!) real value is "<method 'set_litter_spread' of 'panda3d.physics.ParticleSystem' objects>"
        'set_local_velocity_flag': None, # (!) real value is "<method 'set_local_velocity_flag' of 'panda3d.physics.ParticleSystem' objects>"
        'set_pool_size': None, # (!) real value is "<method 'set_pool_size' of 'panda3d.physics.ParticleSystem' objects>"
        'set_render_parent': None, # (!) real value is "<method 'set_render_parent' of 'panda3d.physics.ParticleSystem' objects>"
        'set_renderer': None, # (!) real value is "<method 'set_renderer' of 'panda3d.physics.ParticleSystem' objects>"
        'set_soft_birth_rate': None, # (!) real value is "<method 'set_soft_birth_rate' of 'panda3d.physics.ParticleSystem' objects>"
        'set_spawn_on_death_flag': None, # (!) real value is "<method 'set_spawn_on_death_flag' of 'panda3d.physics.ParticleSystem' objects>"
        'set_spawn_render_node': None, # (!) real value is "<method 'set_spawn_render_node' of 'panda3d.physics.ParticleSystem' objects>"
        'set_spawn_render_node_path': None, # (!) real value is "<method 'set_spawn_render_node_path' of 'panda3d.physics.ParticleSystem' objects>"
        'set_system_age': None, # (!) real value is "<method 'set_system_age' of 'panda3d.physics.ParticleSystem' objects>"
        'set_system_grows_older_flag': None, # (!) real value is "<method 'set_system_grows_older_flag' of 'panda3d.physics.ParticleSystem' objects>"
        'set_system_lifespan': None, # (!) real value is "<method 'set_system_lifespan' of 'panda3d.physics.ParticleSystem' objects>"
        'set_template_system_flag': None, # (!) real value is "<method 'set_template_system_flag' of 'panda3d.physics.ParticleSystem' objects>"
        'softStart': None, # (!) real value is "<method 'softStart' of 'panda3d.physics.ParticleSystem' objects>"
        'softStop': None, # (!) real value is "<method 'softStop' of 'panda3d.physics.ParticleSystem' objects>"
        'soft_start': None, # (!) real value is "<method 'soft_start' of 'panda3d.physics.ParticleSystem' objects>"
        'soft_stop': None, # (!) real value is "<method 'soft_stop' of 'panda3d.physics.ParticleSystem' objects>"
        'update': None, # (!) real value is "<method 'update' of 'panda3d.physics.ParticleSystem' objects>"
        'writeFreeParticleFifo': None, # (!) real value is "<method 'writeFreeParticleFifo' of 'panda3d.physics.ParticleSystem' objects>"
        'writeSpawnTemplates': None, # (!) real value is "<method 'writeSpawnTemplates' of 'panda3d.physics.ParticleSystem' objects>"
        'write_free_particle_fifo': None, # (!) real value is "<method 'write_free_particle_fifo' of 'panda3d.physics.ParticleSystem' objects>"
        'write_spawn_templates': None, # (!) real value is "<method 'write_spawn_templates' of 'panda3d.physics.ParticleSystem' objects>"
    }


