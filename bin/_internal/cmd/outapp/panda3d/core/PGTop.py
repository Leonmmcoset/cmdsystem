# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .PandaNode import PandaNode

class PGTop(PandaNode):
    """
    /**
     * The "top" node of the new Panda GUI system.  This node must be parented to
     * the 2-d scene graph, and all PG objects should be parented to this node or
     * somewhere below it.  PG objects not parented within this hierarchy will not
     * be clickable.
     *
     * This node begins the special traversal of the PG objects that registers
     * each node within the MouseWatcher and forces everything to render in a
     * depth-first, left-to-right order, appropriate for 2-d objects.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getGroup(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_group(PGTop self)
        
        /**
         * Returns the MouseWatcherGroup pointer that the PGTop object registers its
         * PG items with, or NULL if the MouseWatcher has not yet been set.
         */
        """
        pass

    def getMouseWatcher(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_mouse_watcher(PGTop self)
        
        /**
         * Returns the MouseWatcher pointer that the PGTop object registers its PG
         * items with, or NULL if the MouseWatcher has not yet been set.
         */
        """
        pass

    def getStartSort(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_start_sort(PGTop self)
        
        /**
         * Returns the sort index that is assigned during the traversal to the first
         * PGItem that is discovered during traversal.  See set_start_sort().
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_group(self, PGTop_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_group(PGTop self)
        
        /**
         * Returns the MouseWatcherGroup pointer that the PGTop object registers its
         * PG items with, or NULL if the MouseWatcher has not yet been set.
         */
        """
        pass

    def get_mouse_watcher(self, PGTop_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_mouse_watcher(PGTop self)
        
        /**
         * Returns the MouseWatcher pointer that the PGTop object registers its PG
         * items with, or NULL if the MouseWatcher has not yet been set.
         */
        """
        pass

    def get_start_sort(self, PGTop_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_start_sort(PGTop self)
        
        /**
         * Returns the sort index that is assigned during the traversal to the first
         * PGItem that is discovered during traversal.  See set_start_sort().
         */
        """
        pass

    def setMouseWatcher(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_mouse_watcher(const PGTop self, MouseWatcher watcher)
        
        /**
         * Sets the MouseWatcher pointer that the PGTop object registers its PG items
         * with.  This must be set before the PG items are active.
         */
        """
        pass

    def setStartSort(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_start_sort(const PGTop self, int start_sort)
        
        /**
         * Specifies the sort index that is assigned during the traversal to the first
         * PGItem that is discovered during traversal.  Subsequent PGItems will be
         * assigned consecutively higher sort indexes.
         *
         * This number is used by the MouseWatcher system to rank the clickable mouse
         * regions in the same order in which the items are rendered, so that items on
         * top will receive mouse priority.
         *
         * Normally, it makes the most sense to leave this initial value at its
         * default value of 0, unless you need the PGItems to have a particular sort
         * value with respect to some other objects in the scene (particularly with a
         * second PGTop node).
         */
        """
        pass

    def set_mouse_watcher(self, const_PGTop_self, MouseWatcher_watcher): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_mouse_watcher(const PGTop self, MouseWatcher watcher)
        
        /**
         * Sets the MouseWatcher pointer that the PGTop object registers its PG items
         * with.  This must be set before the PG items are active.
         */
        """
        pass

    def set_start_sort(self, const_PGTop_self, int_start_sort): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_start_sort(const PGTop self, int start_sort)
        
        /**
         * Specifies the sort index that is assigned during the traversal to the first
         * PGItem that is discovered during traversal.  Subsequent PGItems will be
         * assigned consecutively higher sort indexes.
         *
         * This number is used by the MouseWatcher system to rank the clickable mouse
         * regions in the same order in which the items are rendered, so that items on
         * top will receive mouse priority.
         *
         * Normally, it makes the most sense to leave this initial value at its
         * default value of 0, unless you need the PGItems to have a particular sort
         * value with respect to some other objects in the scene (particularly with a
         * second PGTop node).
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
        '__doc__': '/**\n * The "top" node of the new Panda GUI system.  This node must be parented to\n * the 2-d scene graph, and all PG objects should be parented to this node or\n * somewhere below it.  PG objects not parented within this hierarchy will not\n * be clickable.\n *\n * This node begins the special traversal of the PG objects that registers\n * each node within the MouseWatcher and forces everything to render in a\n * depth-first, left-to-right order, appropriate for 2-d objects.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.PGTop' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE384370>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE384370>)>'
        'getGroup': None, # (!) real value is "<method 'getGroup' of 'panda3d.core.PGTop' objects>"
        'getMouseWatcher': None, # (!) real value is "<method 'getMouseWatcher' of 'panda3d.core.PGTop' objects>"
        'getStartSort': None, # (!) real value is "<method 'getStartSort' of 'panda3d.core.PGTop' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE384370>)>'
        'get_group': None, # (!) real value is "<method 'get_group' of 'panda3d.core.PGTop' objects>"
        'get_mouse_watcher': None, # (!) real value is "<method 'get_mouse_watcher' of 'panda3d.core.PGTop' objects>"
        'get_start_sort': None, # (!) real value is "<method 'get_start_sort' of 'panda3d.core.PGTop' objects>"
        'setMouseWatcher': None, # (!) real value is "<method 'setMouseWatcher' of 'panda3d.core.PGTop' objects>"
        'setStartSort': None, # (!) real value is "<method 'setStartSort' of 'panda3d.core.PGTop' objects>"
        'set_mouse_watcher': None, # (!) real value is "<method 'set_mouse_watcher' of 'panda3d.core.PGTop' objects>"
        'set_start_sort': None, # (!) real value is "<method 'set_start_sort' of 'panda3d.core.PGTop' objects>"
    }


