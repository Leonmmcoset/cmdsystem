# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .ConnectionReader import ConnectionReader

class ConnectionListener(ConnectionReader):
    """
    /**
     * This is a special kind of ConnectionReader that waits for activity on a
     * rendezvous port and accepts a TCP connection (instead of attempting to read
     * a datagram from the rendezvous port).
     *
     * It is itself an abstract class, as it doesn't define what to do with the
     * established connection.  See QueuedConnectionListener.
     */
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': "/**\n * This is a special kind of ConnectionReader that waits for activity on a\n * rendezvous port and accepts a TCP connection (instead of attempting to read\n * a datagram from the rendezvous port).\n *\n * It is itself an abstract class, as it doesn't define what to do with the\n * established connection.  See QueuedConnectionListener.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.ConnectionListener' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE389C90>'
    }


