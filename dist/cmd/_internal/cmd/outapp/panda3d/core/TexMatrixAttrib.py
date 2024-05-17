# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .RenderAttrib import RenderAttrib

class TexMatrixAttrib(RenderAttrib):
    """
    /**
     * Applies a transform matrix to UV's before they are rendered.
     */
    """
    def addStage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_stage(TexMatrixAttrib self, TextureStage stage, const TransformState transform, int override)
        
        /**
         * Returns a new TexMatrixAttrib just like this one, with the indicated
         * transform for the given stage.  If this stage already exists, its transform
         * is replaced.
         */
        """
        pass

    def add_stage(self, TexMatrixAttrib_self, TextureStage_stage, const_TransformState_transform, int_override): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_stage(TexMatrixAttrib self, TextureStage stage, const TransformState transform, int override)
        
        /**
         * Returns a new TexMatrixAttrib just like this one, with the indicated
         * transform for the given stage.  If this stage already exists, its transform
         * is replaced.
         */
        """
        pass

    def getClassSlot(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_slot()
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getGeomRendering(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_geom_rendering(TexMatrixAttrib self, int geom_rendering)
        
        /**
         * Returns the union of the Geom::GeomRendering bits that will be required
         * once this TexMatrixAttrib is applied to a geom which includes the indicated
         * geom_rendering bits.
         */
        """
        pass

    def getMat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_mat(TexMatrixAttrib self)
        get_mat(TexMatrixAttrib self, TextureStage stage)
        
        /**
         * Returns the transformation matrix associated with the default texture
         * stage.
         */
        
        /**
         * Returns the transformation matrix associated with the indicated texture
         * stage, or identity matrix if nothing is associated with the indicated
         * stage.
         */
        """
        pass

    def getNumStages(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_stages(TexMatrixAttrib self)
        
        /**
         * Returns the number of stages that are represented by this attrib.
         */
        """
        pass

    def getOverride(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_override(TexMatrixAttrib self, TextureStage stage)
        
        /**
         * Returns the override value associated with the indicated stage.
         */
        """
        pass

    def getStage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_stage(TexMatrixAttrib self, int n)
        
        /**
         * Returns the nth stage that is represented by this attrib.  The
         * TextureStages are in no particular order.
         */
        """
        pass

    def getStages(self, *args, **kwargs): # real signature unknown
        pass

    def getTransform(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_transform(TexMatrixAttrib self, TextureStage stage)
        
        /**
         * Returns the transformation associated with the indicated texture stage, or
         * identity matrix if nothing is associated with the indicated stage.
         */
        """
        pass

    def get_class_slot(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_slot()
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_geom_rendering(self, TexMatrixAttrib_self, int_geom_rendering): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_geom_rendering(TexMatrixAttrib self, int geom_rendering)
        
        /**
         * Returns the union of the Geom::GeomRendering bits that will be required
         * once this TexMatrixAttrib is applied to a geom which includes the indicated
         * geom_rendering bits.
         */
        """
        pass

    def get_mat(self, TexMatrixAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_mat(TexMatrixAttrib self)
        get_mat(TexMatrixAttrib self, TextureStage stage)
        
        /**
         * Returns the transformation matrix associated with the default texture
         * stage.
         */
        
        /**
         * Returns the transformation matrix associated with the indicated texture
         * stage, or identity matrix if nothing is associated with the indicated
         * stage.
         */
        """
        pass

    def get_num_stages(self, TexMatrixAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_stages(TexMatrixAttrib self)
        
        /**
         * Returns the number of stages that are represented by this attrib.
         */
        """
        pass

    def get_override(self, TexMatrixAttrib_self, TextureStage_stage): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_override(TexMatrixAttrib self, TextureStage stage)
        
        /**
         * Returns the override value associated with the indicated stage.
         */
        """
        pass

    def get_stage(self, TexMatrixAttrib_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_stage(TexMatrixAttrib self, int n)
        
        /**
         * Returns the nth stage that is represented by this attrib.  The
         * TextureStages are in no particular order.
         */
        """
        pass

    def get_stages(self, *args, **kwargs): # real signature unknown
        pass

    def get_transform(self, TexMatrixAttrib_self, TextureStage_stage): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_transform(TexMatrixAttrib self, TextureStage stage)
        
        /**
         * Returns the transformation associated with the indicated texture stage, or
         * identity matrix if nothing is associated with the indicated stage.
         */
        """
        pass

    def hasStage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_stage(TexMatrixAttrib self, TextureStage stage)
        
        /**
         * Returns true if there is a transform associated with the indicated stage,
         * or false otherwise (in which case get_transform(stage) will return the
         * identity transform).
         */
        """
        pass

    def has_stage(self, TexMatrixAttrib_self, TextureStage_stage): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_stage(TexMatrixAttrib self, TextureStage stage)
        
        /**
         * Returns true if there is a transform associated with the indicated stage,
         * or false otherwise (in which case get_transform(stage) will return the
         * identity transform).
         */
        """
        pass

    def isEmpty(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_empty(TexMatrixAttrib self)
        
        /**
         * Returns true if no stages are defined in the TexMatrixAttrib, false if at
         * least one is.
         */
        """
        pass

    def is_empty(self, TexMatrixAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_empty(TexMatrixAttrib self)
        
        /**
         * Returns true if no stages are defined in the TexMatrixAttrib, false if at
         * least one is.
         */
        """
        pass

    def make(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make()
        make(const LMatrix4f mat)
        make(TextureStage stage, const TransformState transform)
        
        /**
         * Constructs a TexMatrixAttrib that applies no stages at all.
         */
        
        /**
         * Constructs a TexMatrixAttrib that applies the indicated matrix to the
         * default texture stage.  This interface is deprecated.
         *
         * @deprecated Use the constructor that takes a TextureStage instead.
         */
        
        /**
         * Constructs a TexMatrixAttrib that applies the indicated transform to the
         * named texture stage.
         */
        """
        pass

    def makeDefault(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_default()
        
        /**
         * Returns a RenderAttrib that corresponds to whatever the standard default
         * properties for render attributes of this type ought to be.
         */
        """
        pass

    def make_default(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_default()
        
        /**
         * Returns a RenderAttrib that corresponds to whatever the standard default
         * properties for render attributes of this type ought to be.
         */
        """
        pass

    def removeStage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_stage(TexMatrixAttrib self, TextureStage stage)
        
        /**
         * Returns a new TexMatrixAttrib just like this one, with the indicated stage
         * removed.
         */
        """
        pass

    def remove_stage(self, TexMatrixAttrib_self, TextureStage_stage): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_stage(TexMatrixAttrib self, TextureStage stage)
        
        /**
         * Returns a new TexMatrixAttrib just like this one, with the indicated stage
         * removed.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    class_slot = 26
    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': "/**\n * Applies a transform matrix to UV's before they are rendered.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.TexMatrixAttrib' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE291D70>'
        'addStage': None, # (!) real value is "<method 'addStage' of 'panda3d.core.TexMatrixAttrib' objects>"
        'add_stage': None, # (!) real value is "<method 'add_stage' of 'panda3d.core.TexMatrixAttrib' objects>"
        'class_slot': None, # (!) real value is "<attribute 'class_slot' of 'panda3d.core.TexMatrixAttrib'>"
        'getClassSlot': None, # (!) real value is '<staticmethod(<built-in method getClassSlot of type object at 0x00007FFCFE291D70>)>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE291D70>)>'
        'getGeomRendering': None, # (!) real value is "<method 'getGeomRendering' of 'panda3d.core.TexMatrixAttrib' objects>"
        'getMat': None, # (!) real value is "<method 'getMat' of 'panda3d.core.TexMatrixAttrib' objects>"
        'getNumStages': None, # (!) real value is "<method 'getNumStages' of 'panda3d.core.TexMatrixAttrib' objects>"
        'getOverride': None, # (!) real value is "<method 'getOverride' of 'panda3d.core.TexMatrixAttrib' objects>"
        'getStage': None, # (!) real value is "<method 'getStage' of 'panda3d.core.TexMatrixAttrib' objects>"
        'getStages': None, # (!) real value is "<method 'getStages' of 'panda3d.core.TexMatrixAttrib' objects>"
        'getTransform': None, # (!) real value is "<method 'getTransform' of 'panda3d.core.TexMatrixAttrib' objects>"
        'get_class_slot': None, # (!) real value is '<staticmethod(<built-in method get_class_slot of type object at 0x00007FFCFE291D70>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE291D70>)>'
        'get_geom_rendering': None, # (!) real value is "<method 'get_geom_rendering' of 'panda3d.core.TexMatrixAttrib' objects>"
        'get_mat': None, # (!) real value is "<method 'get_mat' of 'panda3d.core.TexMatrixAttrib' objects>"
        'get_num_stages': None, # (!) real value is "<method 'get_num_stages' of 'panda3d.core.TexMatrixAttrib' objects>"
        'get_override': None, # (!) real value is "<method 'get_override' of 'panda3d.core.TexMatrixAttrib' objects>"
        'get_stage': None, # (!) real value is "<method 'get_stage' of 'panda3d.core.TexMatrixAttrib' objects>"
        'get_stages': None, # (!) real value is "<method 'get_stages' of 'panda3d.core.TexMatrixAttrib' objects>"
        'get_transform': None, # (!) real value is "<method 'get_transform' of 'panda3d.core.TexMatrixAttrib' objects>"
        'hasStage': None, # (!) real value is "<method 'hasStage' of 'panda3d.core.TexMatrixAttrib' objects>"
        'has_stage': None, # (!) real value is "<method 'has_stage' of 'panda3d.core.TexMatrixAttrib' objects>"
        'isEmpty': None, # (!) real value is "<method 'isEmpty' of 'panda3d.core.TexMatrixAttrib' objects>"
        'is_empty': None, # (!) real value is "<method 'is_empty' of 'panda3d.core.TexMatrixAttrib' objects>"
        'make': None, # (!) real value is '<staticmethod(<built-in method make of type object at 0x00007FFCFE291D70>)>'
        'makeDefault': None, # (!) real value is '<staticmethod(<built-in method makeDefault of type object at 0x00007FFCFE291D70>)>'
        'make_default': None, # (!) real value is '<staticmethod(<built-in method make_default of type object at 0x00007FFCFE291D70>)>'
        'removeStage': None, # (!) real value is "<method 'removeStage' of 'panda3d.core.TexMatrixAttrib' objects>"
        'remove_stage': None, # (!) real value is "<method 'remove_stage' of 'panda3d.core.TexMatrixAttrib' objects>"
    }


