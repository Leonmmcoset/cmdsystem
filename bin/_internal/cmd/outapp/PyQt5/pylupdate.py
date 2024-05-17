# encoding: utf-8
# module PyQt5.pylupdate
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\pylupdate.pyd
# by generator 1.147
# no doc

# imports
import sip as __sip


# functions

def fetchtr_py(fileName, bytes=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ fetchtr_py(fileName: Optional[bytes], tor: Optional[MetaTranslator], defaultContext: Optional[str], mustExist: bool, codecForSource: Optional[str], tr_func: Optional[str], translate_func: Optional[str]) """
    pass

def fetchtr_ui(fileName, bytes=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ fetchtr_ui(fileName: Optional[bytes], tor: Optional[MetaTranslator], defaultContext: Optional[str], mustExist: bool) """
    pass

def merge(tor, MetaTranslator=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ merge(tor: Optional[MetaTranslator], virginTor: Optional[MetaTranslator], out: Optional[MetaTranslator], noObsolete: bool, verbose: bool, filename: Optional[str]) """
    pass

def proFileTagMap(text, p_str=None): # real signature unknown; restored from __doc__
    """ proFileTagMap(text: Optional[str]) -> Dict[str, str] """
    return {}

# classes

class MetaTranslator(__sip.simplewrapper):
    """
    MetaTranslator()
    MetaTranslator(tor: MetaTranslator)
    """
    def load(self, filename, p_str=None): # real signature unknown; restored from __doc__
        """ load(self, filename: Optional[str]) -> bool """
        return False

    def save(self, filename, p_str=None): # real signature unknown; restored from __doc__
        """ save(self, filename: Optional[str]) -> bool """
        return False

    def setCodec(self, name, p_str=None): # real signature unknown; restored from __doc__
        """ setCodec(self, name: Optional[str]) """
        pass

    def stripEmptyContexts(self): # real signature unknown; restored from __doc__
        """ stripEmptyContexts(self) """
        pass

    def stripObsoleteMessages(self): # real signature unknown; restored from __doc__
        """ stripObsoleteMessages(self) """
        pass

    def __init__(self, tor=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values



