# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class ProfileTimer(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /*
        ProfileTimer
    
        HowTo:
          Create a ProfileTimer and hold onto it.
          Call init() whenever you like (the timer doesn't
            start yet).
          Call on() to start the timer.
          While the timer is on, call mark() at each point of interest,
            in the code you are timing.
          You can turn the timer off() and on() to skip things you
            don't want to time.
          When your timing is finished, call printTo() to see the
            results (e.g. myTimer.printTo(cerr)).
    
        Notes:
          You should be able to time things down to the millisecond
          well enough, but if you call on() and off() within micro-
          seconds of each other, I don't think you'll get very good
          results.
    */
    """
    def consolidateAllTo(self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        consolidateAllTo(ostream out)
        """
        pass

    def consolidateTo(self, ProfileTimer_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        consolidateTo(ProfileTimer self, ostream out)
        """
        pass

    def getTotalTime(self, ProfileTimer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        getTotalTime(ProfileTimer self)
        
        // Don't call any of the following during timing: (Because they are slow,
        // not because anything will break).
        """
        pass

    def init(self, const_ProfileTimer_self, str_name, int_maxEntries): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        init(const ProfileTimer self, str name, int maxEntries)
        """
        pass

    def mark(self, const_ProfileTimer_self, str_tag): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        mark(const ProfileTimer self, str tag)
        """
        pass

    def off(self, const_ProfileTimer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        off(const ProfileTimer self)
        off(const ProfileTimer self, str tag)
        """
        pass

    def on(self, const_ProfileTimer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        on(const ProfileTimer self)
        """
        pass

    def printAllTo(self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        printAllTo(ostream out)
        """
        pass

    def printTo(self, ProfileTimer_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        printTo(ProfileTimer self, ostream out)
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
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.ProfileTimer' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.ProfileTimer' objects>"
        '__doc__': "/*\n    ProfileTimer\n\n    HowTo:\n      Create a ProfileTimer and hold onto it.\n      Call init() whenever you like (the timer doesn't\n        start yet).\n      Call on() to start the timer.\n      While the timer is on, call mark() at each point of interest,\n        in the code you are timing.\n      You can turn the timer off() and on() to skip things you\n        don't want to time.\n      When your timing is finished, call printTo() to see the\n        results (e.g. myTimer.printTo(cerr)).\n\n    Notes:\n      You should be able to time things down to the millisecond\n      well enough, but if you call on() and off() within micro-\n      seconds of each other, I don't think you'll get very good\n      results.\n*/",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.ProfileTimer' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE27B350>'
        'consolidateAllTo': None, # (!) real value is '<staticmethod(<built-in method consolidateAllTo of type object at 0x00007FFCFE27B350>)>'
        'consolidateTo': None, # (!) real value is "<method 'consolidateTo' of 'panda3d.core.ProfileTimer' objects>"
        'getTotalTime': None, # (!) real value is "<method 'getTotalTime' of 'panda3d.core.ProfileTimer' objects>"
        'init': None, # (!) real value is "<method 'init' of 'panda3d.core.ProfileTimer' objects>"
        'mark': None, # (!) real value is "<method 'mark' of 'panda3d.core.ProfileTimer' objects>"
        'off': None, # (!) real value is "<method 'off' of 'panda3d.core.ProfileTimer' objects>"
        'on': None, # (!) real value is "<method 'on' of 'panda3d.core.ProfileTimer' objects>"
        'printAllTo': None, # (!) real value is '<staticmethod(<built-in method printAllTo of type object at 0x00007FFCFE27B350>)>'
        'printTo': None, # (!) real value is "<method 'printTo' of 'panda3d.core.ProfileTimer' objects>"
    }


