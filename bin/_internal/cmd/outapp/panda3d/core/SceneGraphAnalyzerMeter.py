# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TextNode import TextNode

class SceneGraphAnalyzerMeter(TextNode):
    """
    /**
     * This is a special TextNode that automatically updates itself with output
     * from a SceneGraphAnalyzer instance.  It can be placed anywhere in the world
     * where you'd like to see the output from SceneGraphAnalyzer.
     *
     * It also has a special mode in which it may be attached directly to a
     * channel or window.  If this is done, it creates a DisplayRegion for itself
     * and renders itself in the upper-right-hand corner.
     */
    """
    def clearWindow(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_window(const SceneGraphAnalyzerMeter self)
        
        /**
         * Undoes the effect of a previous call to setup_window().
         */
        """
        pass

    def clear_window(self, const_SceneGraphAnalyzerMeter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_window(const SceneGraphAnalyzerMeter self)
        
        /**
         * Undoes the effect of a previous call to setup_window().
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getDisplayRegion(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_display_region(SceneGraphAnalyzerMeter self)
        
        /**
         * Returns the DisplayRegion that the meter has created to render itself into
         * the window to setup_window(), or NULL if setup_window() has not been
         * called.
         */
        """
        pass

    def getNode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_node(SceneGraphAnalyzerMeter self)
        
        /**
         * Returns the node to be analyzed.
         */
        """
        pass

    def getUpdateInterval(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_update_interval(SceneGraphAnalyzerMeter self)
        
        /**
         * Returns the number of seconds that will elapse between updates to the frame
         * rate indication.
         */
        """
        pass

    def getWindow(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_window(SceneGraphAnalyzerMeter self)
        
        /**
         * Returns the GraphicsOutput that was passed to setup_window(), or NULL if
         * setup_window() has not been called.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_display_region(self, SceneGraphAnalyzerMeter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_display_region(SceneGraphAnalyzerMeter self)
        
        /**
         * Returns the DisplayRegion that the meter has created to render itself into
         * the window to setup_window(), or NULL if setup_window() has not been
         * called.
         */
        """
        pass

    def get_node(self, SceneGraphAnalyzerMeter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_node(SceneGraphAnalyzerMeter self)
        
        /**
         * Returns the node to be analyzed.
         */
        """
        pass

    def get_update_interval(self, SceneGraphAnalyzerMeter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_update_interval(SceneGraphAnalyzerMeter self)
        
        /**
         * Returns the number of seconds that will elapse between updates to the frame
         * rate indication.
         */
        """
        pass

    def get_window(self, SceneGraphAnalyzerMeter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_window(SceneGraphAnalyzerMeter self)
        
        /**
         * Returns the GraphicsOutput that was passed to setup_window(), or NULL if
         * setup_window() has not been called.
         */
        """
        pass

    def setNode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_node(const SceneGraphAnalyzerMeter self, PandaNode node)
        
        /**
         * Sets the node to be analyzed.
         */
        """
        pass

    def setUpdateInterval(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_update_interval(const SceneGraphAnalyzerMeter self, double update_interval)
        
        /**
         * Specifies the number of seconds that should elapse between updates to the
         * meter.  This should be reasonably slow (e.g.  0.5 to 2.0) so that the
         * calculation of the scene graph analysis does not itself dominate the frame
         * rate.
         */
        """
        pass

    def setupWindow(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        setup_window(const SceneGraphAnalyzerMeter self, GraphicsOutput window)
        
        /**
         * Sets up the frame rate meter to create a DisplayRegion to render itself
         * into the indicated window.
         */
        """
        pass

    def setup_window(self, const_SceneGraphAnalyzerMeter_self, GraphicsOutput_window): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        setup_window(const SceneGraphAnalyzerMeter self, GraphicsOutput window)
        
        /**
         * Sets up the frame rate meter to create a DisplayRegion to render itself
         * into the indicated window.
         */
        """
        pass

    def set_node(self, const_SceneGraphAnalyzerMeter_self, PandaNode_node): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_node(const SceneGraphAnalyzerMeter self, PandaNode node)
        
        /**
         * Sets the node to be analyzed.
         */
        """
        pass

    def set_update_interval(self, const_SceneGraphAnalyzerMeter_self, double_update_interval): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_update_interval(const SceneGraphAnalyzerMeter self, double update_interval)
        
        /**
         * Specifies the number of seconds that should elapse between updates to the
         * meter.  This should be reasonably slow (e.g.  0.5 to 2.0) so that the
         * calculation of the scene graph analysis does not itself dominate the frame
         * rate.
         */
        """
        pass

    def update(self, const_SceneGraphAnalyzerMeter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        update(const SceneGraphAnalyzerMeter self)
        
        /**
         * You can call this to explicitly force the SceneGraphAnalyzerMeter to update
         * itself with the latest scene graph analysis information.  Normally, it is
         * not necessary to call this explicitly.
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
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.SceneGraphAnalyzerMeter' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.SceneGraphAnalyzerMeter' objects>"
        '__doc__': "/**\n * This is a special TextNode that automatically updates itself with output\n * from a SceneGraphAnalyzer instance.  It can be placed anywhere in the world\n * where you'd like to see the output from SceneGraphAnalyzer.\n *\n * It also has a special mode in which it may be attached directly to a\n * channel or window.  If this is done, it creates a DisplayRegion for itself\n * and renders itself in the upper-right-hand corner.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.SceneGraphAnalyzerMeter' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2BD5B0>'
        'clearWindow': None, # (!) real value is "<method 'clearWindow' of 'panda3d.core.SceneGraphAnalyzerMeter' objects>"
        'clear_window': None, # (!) real value is "<method 'clear_window' of 'panda3d.core.SceneGraphAnalyzerMeter' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2BD5B0>)>'
        'getDisplayRegion': None, # (!) real value is "<method 'getDisplayRegion' of 'panda3d.core.SceneGraphAnalyzerMeter' objects>"
        'getNode': None, # (!) real value is "<method 'getNode' of 'panda3d.core.SceneGraphAnalyzerMeter' objects>"
        'getUpdateInterval': None, # (!) real value is "<method 'getUpdateInterval' of 'panda3d.core.SceneGraphAnalyzerMeter' objects>"
        'getWindow': None, # (!) real value is "<method 'getWindow' of 'panda3d.core.SceneGraphAnalyzerMeter' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2BD5B0>)>'
        'get_display_region': None, # (!) real value is "<method 'get_display_region' of 'panda3d.core.SceneGraphAnalyzerMeter' objects>"
        'get_node': None, # (!) real value is "<method 'get_node' of 'panda3d.core.SceneGraphAnalyzerMeter' objects>"
        'get_update_interval': None, # (!) real value is "<method 'get_update_interval' of 'panda3d.core.SceneGraphAnalyzerMeter' objects>"
        'get_window': None, # (!) real value is "<method 'get_window' of 'panda3d.core.SceneGraphAnalyzerMeter' objects>"
        'setNode': None, # (!) real value is "<method 'setNode' of 'panda3d.core.SceneGraphAnalyzerMeter' objects>"
        'setUpdateInterval': None, # (!) real value is "<method 'setUpdateInterval' of 'panda3d.core.SceneGraphAnalyzerMeter' objects>"
        'set_node': None, # (!) real value is "<method 'set_node' of 'panda3d.core.SceneGraphAnalyzerMeter' objects>"
        'set_update_interval': None, # (!) real value is "<method 'set_update_interval' of 'panda3d.core.SceneGraphAnalyzerMeter' objects>"
        'setupWindow': None, # (!) real value is "<method 'setupWindow' of 'panda3d.core.SceneGraphAnalyzerMeter' objects>"
        'setup_window': None, # (!) real value is "<method 'setup_window' of 'panda3d.core.SceneGraphAnalyzerMeter' objects>"
        'update': None, # (!) real value is "<method 'update' of 'panda3d.core.SceneGraphAnalyzerMeter' objects>"
    }


