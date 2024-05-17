# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class WorkingNodePath(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This is a class designed to support low-overhead traversals of the complete
     * scene graph, with a memory of the complete path through the graph at any
     * given point.
     *
     * You could just use a regular NodePath to do this, but since the NodePath
     * requires storing NodePathComponents on each node as it is constructed, and
     * then removing them when it destructs, there is considerable overhead in
     * that approach.
     *
     * The WorkingNodePath eliminates this overhead (but does not guarantee
     * consistency if the scene graph changes while the path is held).
     *
     * At any given point, you may ask the WorkingNodePath for its actual
     * NodePath, and it will construct and return a new NodePath representing the
     * complete generated chain.
     */
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    node_path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    valid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * This is a class designed to support low-overhead traversals of the complete\n * scene graph, with a memory of the complete path through the graph at any\n * given point.\n *\n * You could just use a regular NodePath to do this, but since the NodePath\n * requires storing NodePathComponents on each node as it is constructed, and\n * then removing them when it destructs, there is considerable overhead in\n * that approach.\n *\n * The WorkingNodePath eliminates this overhead (but does not guarantee\n * consistency if the scene graph changes while the path is held).\n *\n * At any given point, you may ask the WorkingNodePath for its actual\n * NodePath, and it will construct and return a new NodePath representing the\n * complete generated chain.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.WorkingNodePath' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE296420>'
        'node_path': None, # (!) real value is "<attribute 'node_path' of 'panda3d.core.WorkingNodePath' objects>"
        'valid': None, # (!) real value is "<attribute 'valid' of 'panda3d.core.WorkingNodePath' objects>"
    }


