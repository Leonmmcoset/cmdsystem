# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .SavedContext import SavedContext

class GeomContext(SavedContext):
    """
    /**
     * This is a special class object that holds all the information returned by a
     * particular GSG to indicate the geom's internal context identifier.
     *
     * Geoms typically have an immediate-mode and a retained-mode operation.  When
     * using geoms in retained-mode (in response to Geom::prepare()), the GSG will
     * create some internal handle for the geom and store it here.  The geom
     * stores all of these handles internally.
     *
     * In the case of OpenGL, for example, a GeomContext corresponds to a display
     * list identifier.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getGeom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_geom(GeomContext self)
        
        /**
         *
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_geom(self, GeomContext_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_geom(GeomContext self)
        
        /**
         *
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    geom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': "/**\n * This is a special class object that holds all the information returned by a\n * particular GSG to indicate the geom's internal context identifier.\n *\n * Geoms typically have an immediate-mode and a retained-mode operation.  When\n * using geoms in retained-mode (in response to Geom::prepare()), the GSG will\n * create some internal handle for the geom and store it here.  The geom\n * stores all of these handles internally.\n *\n * In the case of OpenGL, for example, a GeomContext corresponds to a display\n * list identifier.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.GeomContext' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2FD040>'
        'geom': None, # (!) real value is "<attribute 'geom' of 'panda3d.core.GeomContext' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2FD040>)>'
        'getGeom': None, # (!) real value is "<method 'getGeom' of 'panda3d.core.GeomContext' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2FD040>)>'
        'get_geom': None, # (!) real value is "<method 'get_geom' of 'panda3d.core.GeomContext' objects>"
    }


