# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .CallbackData import CallbackData

class DisplayRegionDrawCallbackData(CallbackData):
    """
    /**
     * This specialization on CallbackData is passed when the callback is
     * initiated from the draw traversal, for a DisplayRegion.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getCullResult(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_cull_result(DisplayRegionDrawCallbackData self)
        
        /**
         * Returns a pointer to the CullResult, the list of CullableObjects that
         * should be drawn in this DisplayRegion.
         */
        """
        pass

    def getSceneSetup(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_scene_setup(DisplayRegionDrawCallbackData self)
        
        /**
         * Returns a pointer to the SceneSetup object, which contains information
         * about the camera and such.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_cull_result(self, DisplayRegionDrawCallbackData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_cull_result(DisplayRegionDrawCallbackData self)
        
        /**
         * Returns a pointer to the CullResult, the list of CullableObjects that
         * should be drawn in this DisplayRegion.
         */
        """
        pass

    def get_scene_setup(self, DisplayRegionDrawCallbackData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_scene_setup(DisplayRegionDrawCallbackData self)
        
        /**
         * Returns a pointer to the SceneSetup object, which contains information
         * about the camera and such.
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
        '__doc__': '/**\n * This specialization on CallbackData is passed when the callback is\n * initiated from the draw traversal, for a DisplayRegion.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.DisplayRegionDrawCallbackData' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2DF5D0>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2DF5D0>)>'
        'getCullResult': None, # (!) real value is "<method 'getCullResult' of 'panda3d.core.DisplayRegionDrawCallbackData' objects>"
        'getSceneSetup': None, # (!) real value is "<method 'getSceneSetup' of 'panda3d.core.DisplayRegionDrawCallbackData' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2DF5D0>)>'
        'get_cull_result': None, # (!) real value is "<method 'get_cull_result' of 'panda3d.core.DisplayRegionDrawCallbackData' objects>"
        'get_scene_setup': None, # (!) real value is "<method 'get_scene_setup' of 'panda3d.core.DisplayRegionDrawCallbackData' objects>"
    }


