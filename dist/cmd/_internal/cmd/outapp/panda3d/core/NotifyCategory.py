# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .ConfigFlags import ConfigFlags

class NotifyCategory(ConfigFlags):
    """
    /**
     * A particular category of error messages.  Typically there will be one of
     * these per package, so that we can turn on or off error messages at least at
     * a package level; further nested categories can be created within a package
     * if a finer grain of control is required.
     */
    """
    def debug(self, NotifyCategory_self, bool_prefix): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        debug(NotifyCategory self, bool prefix)
        
        /**
         * A shorthand way to write out(NS_debug).
         */
        """
        pass

    def error(self, NotifyCategory_self, bool_prefix): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        error(NotifyCategory self, bool prefix)
        
        /**
         * A shorthand way to write out(NS_error).
         */
        """
        pass

    def fatal(self, NotifyCategory_self, bool_prefix): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        fatal(NotifyCategory self, bool prefix)
        
        /**
         * A shorthand way to write out(NS_fatal).
         */
        """
        pass

    def getBasename(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_basename(NotifyCategory self)
        
        /**
         *
         */
        """
        pass

    def getChild(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_child(NotifyCategory self, int i)
        
        /**
         * Returns the nth child Category of this particular Category.
         */
        """
        pass

    def getChildren(self, *args, **kwargs): # real signature unknown
        pass

    def getFullname(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_fullname(NotifyCategory self)
        
        /**
         *
         */
        """
        pass

    def getNumChildren(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_children(NotifyCategory self)
        
        /**
         * Returns the number of child Categories of this particular Category.
         */
        """
        pass

    def getSeverity(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_severity(NotifyCategory self)
        
        /**
         *
         */
        """
        pass

    def get_basename(self, NotifyCategory_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_basename(NotifyCategory self)
        
        /**
         *
         */
        """
        pass

    def get_child(self, NotifyCategory_self, int_i): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_child(NotifyCategory self, int i)
        
        /**
         * Returns the nth child Category of this particular Category.
         */
        """
        pass

    def get_children(self, *args, **kwargs): # real signature unknown
        pass

    def get_fullname(self, NotifyCategory_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_fullname(NotifyCategory self)
        
        /**
         *
         */
        """
        pass

    def get_num_children(self, NotifyCategory_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_children(NotifyCategory self)
        
        /**
         * Returns the number of child Categories of this particular Category.
         */
        """
        pass

    def get_severity(self, NotifyCategory_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_severity(NotifyCategory self)
        
        /**
         *
         */
        """
        pass

    def info(self, NotifyCategory_self, bool_prefix): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        info(NotifyCategory self, bool prefix)
        
        /**
         * A shorthand way to write out(NS_info).
         */
        """
        pass

    def isDebug(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_debug(NotifyCategory self)
        
        /**
         * A shorthand way to write is_on(NS_debug).
         */
        """
        pass

    def isError(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_error(NotifyCategory self)
        
        /**
         * A shorthand way to write is_on(NS_error).
         */
        """
        pass

    def isFatal(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_fatal(NotifyCategory self)
        
        /**
         * A shorthand way to write is_on(NS_fatal).
         */
        """
        pass

    def isInfo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_info(NotifyCategory self)
        
        /**
         * A shorthand way to write is_on(NS_info).
         */
        """
        pass

    def isOn(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_on(NotifyCategory self, int severity)
        
        /**
         * Returns true if messages of the indicated severity level ought to be
         * reported for this Category.
         */
        """
        pass

    def isSpam(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_spam(NotifyCategory self)
        
        // When NOTIFY_DEBUG is not defined, the categories will never be set to
        // "spam" or "debug" severities, and these methods are redefined to be
        // static to make it more obvious to the compiler.  However, we still want
        // to present a consistent interface to our scripting language, so during
        // the interrogate pass (that is, when CPPPARSER is defined), we still
        // pretend they're nonstatic.
        
        /**
         * A shorthand way to write is_on(NS_spam).
         */
        """
        pass

    def isWarning(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_warning(NotifyCategory self)
        
        /**
         * A shorthand way to write is_on(NS_warning).
         */
        """
        pass

    def is_debug(self, NotifyCategory_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_debug(NotifyCategory self)
        
        /**
         * A shorthand way to write is_on(NS_debug).
         */
        """
        pass

    def is_error(self, NotifyCategory_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_error(NotifyCategory self)
        
        /**
         * A shorthand way to write is_on(NS_error).
         */
        """
        pass

    def is_fatal(self, NotifyCategory_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_fatal(NotifyCategory self)
        
        /**
         * A shorthand way to write is_on(NS_fatal).
         */
        """
        pass

    def is_info(self, NotifyCategory_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_info(NotifyCategory self)
        
        /**
         * A shorthand way to write is_on(NS_info).
         */
        """
        pass

    def is_on(self, NotifyCategory_self, int_severity): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_on(NotifyCategory self, int severity)
        
        /**
         * Returns true if messages of the indicated severity level ought to be
         * reported for this Category.
         */
        """
        pass

    def is_spam(self, NotifyCategory_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_spam(NotifyCategory self)
        
        // When NOTIFY_DEBUG is not defined, the categories will never be set to
        // "spam" or "debug" severities, and these methods are redefined to be
        // static to make it more obvious to the compiler.  However, we still want
        // to present a consistent interface to our scripting language, so during
        // the interrogate pass (that is, when CPPPARSER is defined), we still
        // pretend they're nonstatic.
        
        /**
         * A shorthand way to write is_on(NS_spam).
         */
        """
        pass

    def is_warning(self, NotifyCategory_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_warning(NotifyCategory self)
        
        /**
         * A shorthand way to write is_on(NS_warning).
         */
        """
        pass

    def out(self, NotifyCategory_self, int_severity, bool_prefix): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        out(NotifyCategory self, int severity, bool prefix)
        
        /**
         * Begins a new message to this Category at the indicated severity level.  If
         * the indicated severity level is enabled, this writes a prefixing string to
         * the Notify::out() stream and returns that.  If the severity level is
         * disabled, this returns Notify::null().
         */
        """
        pass

    def setServerDelta(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_server_delta(int delta)
        
        /**
         * Sets a global delta (in seconds) between the local time and the server's
         * time, for the purpose of synchronizing the time stamps in the log messages
         * of the client with that of a known server.
         */
        """
        pass

    def setSeverity(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_severity(const NotifyCategory self, int severity)
        
        /**
         * Sets the severity level of messages that will be reported from this
         * Category.  This allows any message of this severity level or higher.
         */
        """
        pass

    def set_server_delta(self, int_delta): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_server_delta(int delta)
        
        /**
         * Sets a global delta (in seconds) between the local time and the server's
         * time, for the purpose of synchronizing the time stamps in the log messages
         * of the client with that of a known server.
         */
        """
        pass

    def set_severity(self, const_NotifyCategory_self, int_severity): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_severity(const NotifyCategory self, int severity)
        
        /**
         * Sets the severity level of messages that will be reported from this
         * Category.  This allows any message of this severity level or higher.
         */
        """
        pass

    def spam(self, NotifyCategory_self, bool_prefix): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        spam(NotifyCategory self, bool prefix)
        
        /**
         * A shorthand way to write out(NS_spam).
         */
        """
        pass

    def upcastToConfigFlags(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_ConfigFlags(const NotifyCategory self)
        
        upcast from NotifyCategory to ConfigFlags
        """
        pass

    def upcast_to_ConfigFlags(self, const_NotifyCategory_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_ConfigFlags(const NotifyCategory self)
        
        upcast from NotifyCategory to ConfigFlags
        """
        pass

    def warning(self, NotifyCategory_self, bool_prefix): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        warning(NotifyCategory self, bool prefix)
        
        /**
         * A shorthand way to write out(NS_warning).
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

    basename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    children = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fullname = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    severity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.NotifyCategory' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.NotifyCategory' objects>"
        '__doc__': '/**\n * A particular category of error messages.  Typically there will be one of\n * these per package, so that we can turn on or off error messages at least at\n * a package level; further nested categories can be created within a package\n * if a finer grain of control is required.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.NotifyCategory' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE263F80>'
        'basename': None, # (!) real value is "<attribute 'basename' of 'panda3d.core.NotifyCategory' objects>"
        'children': None, # (!) real value is "<attribute 'children' of 'panda3d.core.NotifyCategory' objects>"
        'debug': None, # (!) real value is "<method 'debug' of 'panda3d.core.NotifyCategory' objects>"
        'error': None, # (!) real value is "<method 'error' of 'panda3d.core.NotifyCategory' objects>"
        'fatal': None, # (!) real value is "<method 'fatal' of 'panda3d.core.NotifyCategory' objects>"
        'fullname': None, # (!) real value is "<attribute 'fullname' of 'panda3d.core.NotifyCategory' objects>"
        'getBasename': None, # (!) real value is "<method 'getBasename' of 'panda3d.core.NotifyCategory' objects>"
        'getChild': None, # (!) real value is "<method 'getChild' of 'panda3d.core.NotifyCategory' objects>"
        'getChildren': None, # (!) real value is "<method 'getChildren' of 'panda3d.core.NotifyCategory' objects>"
        'getFullname': None, # (!) real value is "<method 'getFullname' of 'panda3d.core.NotifyCategory' objects>"
        'getNumChildren': None, # (!) real value is "<method 'getNumChildren' of 'panda3d.core.NotifyCategory' objects>"
        'getSeverity': None, # (!) real value is "<method 'getSeverity' of 'panda3d.core.NotifyCategory' objects>"
        'get_basename': None, # (!) real value is "<method 'get_basename' of 'panda3d.core.NotifyCategory' objects>"
        'get_child': None, # (!) real value is "<method 'get_child' of 'panda3d.core.NotifyCategory' objects>"
        'get_children': None, # (!) real value is "<method 'get_children' of 'panda3d.core.NotifyCategory' objects>"
        'get_fullname': None, # (!) real value is "<method 'get_fullname' of 'panda3d.core.NotifyCategory' objects>"
        'get_num_children': None, # (!) real value is "<method 'get_num_children' of 'panda3d.core.NotifyCategory' objects>"
        'get_severity': None, # (!) real value is "<method 'get_severity' of 'panda3d.core.NotifyCategory' objects>"
        'info': None, # (!) real value is "<method 'info' of 'panda3d.core.NotifyCategory' objects>"
        'isDebug': None, # (!) real value is "<method 'isDebug' of 'panda3d.core.NotifyCategory' objects>"
        'isError': None, # (!) real value is "<method 'isError' of 'panda3d.core.NotifyCategory' objects>"
        'isFatal': None, # (!) real value is "<method 'isFatal' of 'panda3d.core.NotifyCategory' objects>"
        'isInfo': None, # (!) real value is "<method 'isInfo' of 'panda3d.core.NotifyCategory' objects>"
        'isOn': None, # (!) real value is "<method 'isOn' of 'panda3d.core.NotifyCategory' objects>"
        'isSpam': None, # (!) real value is "<method 'isSpam' of 'panda3d.core.NotifyCategory' objects>"
        'isWarning': None, # (!) real value is "<method 'isWarning' of 'panda3d.core.NotifyCategory' objects>"
        'is_debug': None, # (!) real value is "<method 'is_debug' of 'panda3d.core.NotifyCategory' objects>"
        'is_error': None, # (!) real value is "<method 'is_error' of 'panda3d.core.NotifyCategory' objects>"
        'is_fatal': None, # (!) real value is "<method 'is_fatal' of 'panda3d.core.NotifyCategory' objects>"
        'is_info': None, # (!) real value is "<method 'is_info' of 'panda3d.core.NotifyCategory' objects>"
        'is_on': None, # (!) real value is "<method 'is_on' of 'panda3d.core.NotifyCategory' objects>"
        'is_spam': None, # (!) real value is "<method 'is_spam' of 'panda3d.core.NotifyCategory' objects>"
        'is_warning': None, # (!) real value is "<method 'is_warning' of 'panda3d.core.NotifyCategory' objects>"
        'out': None, # (!) real value is "<method 'out' of 'panda3d.core.NotifyCategory' objects>"
        'setServerDelta': None, # (!) real value is '<staticmethod(<built-in method setServerDelta of type object at 0x00007FFCFE263F80>)>'
        'setSeverity': None, # (!) real value is "<method 'setSeverity' of 'panda3d.core.NotifyCategory' objects>"
        'set_server_delta': None, # (!) real value is '<staticmethod(<built-in method set_server_delta of type object at 0x00007FFCFE263F80>)>'
        'set_severity': None, # (!) real value is "<method 'set_severity' of 'panda3d.core.NotifyCategory' objects>"
        'severity': None, # (!) real value is "<attribute 'severity' of 'panda3d.core.NotifyCategory' objects>"
        'spam': None, # (!) real value is "<method 'spam' of 'panda3d.core.NotifyCategory' objects>"
        'upcastToConfigFlags': None, # (!) real value is "<method 'upcastToConfigFlags' of 'panda3d.core.NotifyCategory' objects>"
        'upcast_to_ConfigFlags': None, # (!) real value is "<method 'upcast_to_ConfigFlags' of 'panda3d.core.NotifyCategory' objects>"
        'warning': None, # (!) real value is "<method 'warning' of 'panda3d.core.NotifyCategory' objects>"
    }


