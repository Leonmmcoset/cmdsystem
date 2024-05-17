# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .VirtualFileMount import VirtualFileMount

class VirtualFileMountHTTP(VirtualFileMount):
    """
    /**
     * Maps a web page (URL root) into the VirtualFileSystem.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getHttpClient(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_http_client(VirtualFileMountHTTP self)
        
        /**
         * Returns the HTTPClient object that services this mount point.
         */
        """
        pass

    def getRoot(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_root(VirtualFileMountHTTP self)
        
        /**
         * Returns the URL that represents the root of this mount point.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_http_client(self, VirtualFileMountHTTP_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_http_client(VirtualFileMountHTTP self)
        
        /**
         * Returns the HTTPClient object that services this mount point.
         */
        """
        pass

    def get_root(self, VirtualFileMountHTTP_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_root(VirtualFileMountHTTP self)
        
        /**
         * Returns the URL that represents the root of this mount point.
         */
        """
        pass

    def reloadVfsMountUrl(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        reload_vfs_mount_url()
        
        /**
         * Reads all of the vfs-mount-url lines in the Config.prc file and replaces
         * the mount settings to match them.
         *
         * This will mount any url's mentioned in the config file, and unmount and
         * unmount any url's no longer mentioned in the config file.  Normally, it is
         * called automatically at startup, and need not be called again, unless you
         * have fiddled with some config settings.
         */
        """
        pass

    def reload_vfs_mount_url(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        reload_vfs_mount_url()
        
        /**
         * Reads all of the vfs-mount-url lines in the Config.prc file and replaces
         * the mount settings to match them.
         *
         * This will mount any url's mentioned in the config file, and unmount and
         * unmount any url's no longer mentioned in the config file.  Normally, it is
         * called automatically at startup, and need not be called again, unless you
         * have fiddled with some config settings.
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
        '__doc__': '/**\n * Maps a web page (URL root) into the VirtualFileSystem.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.VirtualFileMountHTTP' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE26D960>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE26D960>)>'
        'getHttpClient': None, # (!) real value is "<method 'getHttpClient' of 'panda3d.core.VirtualFileMountHTTP' objects>"
        'getRoot': None, # (!) real value is "<method 'getRoot' of 'panda3d.core.VirtualFileMountHTTP' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE26D960>)>'
        'get_http_client': None, # (!) real value is "<method 'get_http_client' of 'panda3d.core.VirtualFileMountHTTP' objects>"
        'get_root': None, # (!) real value is "<method 'get_root' of 'panda3d.core.VirtualFileMountHTTP' objects>"
        'reloadVfsMountUrl': None, # (!) real value is '<staticmethod(<built-in method reloadVfsMountUrl of type object at 0x00007FFCFE26D960>)>'
        'reload_vfs_mount_url': None, # (!) real value is '<staticmethod(<built-in method reload_vfs_mount_url of type object at 0x00007FFCFE26D960>)>'
    }


