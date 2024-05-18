# encoding: utf-8
# module kiwisolver._cext
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\kiwisolver\_cext.cp311-win_amd64.pyd
# by generator 1.147
""" kiwisolver extension module """
# no imports

# Variables with simple values

__kiwi_version__ = '1.4.2'

__version__ = '1.4.5'

# no functions
# classes

class BadRequiredStrength(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class Constraint(object):
    # no doc
    def expression(self, *args, **kwargs): # real signature unknown
        """ Get the expression object for the constraint. """
        pass

    def op(self, *args, **kwargs): # real signature unknown
        """ Get the relational operator for the constraint. """
        pass

    def strength(self, *args, **kwargs): # real signature unknown
        """ Get the strength for the constraint. """
        pass

    def violated(self, *args, **kwargs): # real signature unknown
        """ Return whether or not the constraint was violated during the last solver pass. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass


class DuplicateConstraint(Exception):
    # no doc
    def __init__(self, constraint): # reliably restored by inspect
        # no doc
        pass

    constraint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __slots__ = (
        'constraint',
    )


class DuplicateEditVariable(Exception):
    # no doc
    def __init__(self, edit_variable): # reliably restored by inspect
        # no doc
        pass

    edit_variable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __slots__ = (
        'edit_variable',
    )


class Expression(object):
    # no doc
    def constant(self, *args, **kwargs): # real signature unknown
        """ Get the constant for the expression. """
        pass

    def terms(self, *args, **kwargs): # real signature unknown
        """ Get the tuple of terms for the expression. """
        pass

    def value(self, *args, **kwargs): # real signature unknown
        """ Get the value for the expression. """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    __hash__ = None


class Solver(object):
    # no doc
    def addConstraint(self, *args, **kwargs): # real signature unknown
        """ Add a constraint to the solver. """
        pass

    def addEditVariable(self, *args, **kwargs): # real signature unknown
        """ Add an edit variable to the solver. """
        pass

    def dump(self, *args, **kwargs): # real signature unknown
        """ Dump a representation of the solver internals to stdout. """
        pass

    def dumps(self, *args, **kwargs): # real signature unknown
        """ Dump a representation of the solver internals to a string. """
        pass

    def hasConstraint(self, *args, **kwargs): # real signature unknown
        """ Check whether the solver contains a constraint. """
        pass

    def hasEditVariable(self, *args, **kwargs): # real signature unknown
        """ Check whether the solver contains an edit variable. """
        pass

    def removeConstraint(self, *args, **kwargs): # real signature unknown
        """ Remove a constraint from the solver. """
        pass

    def removeEditVariable(self, *args, **kwargs): # real signature unknown
        """ Remove an edit variable from the solver. """
        pass

    def reset(self, *args, **kwargs): # real signature unknown
        """ Reset the solver to the initial empty starting condition. """
        pass

    def suggestValue(self, *args, **kwargs): # real signature unknown
        """ Suggest a desired value for an edit variable. """
        pass

    def updateVariables(self, *args, **kwargs): # real signature unknown
        """ Update the values of the solver variables. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class Term(object):
    # no doc
    def coefficient(self, *args, **kwargs): # real signature unknown
        """ Get the coefficient for the term. """
        pass

    def value(self, *args, **kwargs): # real signature unknown
        """ Get the value for the term. """
        pass

    def variable(self, *args, **kwargs): # real signature unknown
        """ Get the variable for the term. """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    __hash__ = None


class UnknownConstraint(Exception):
    # no doc
    def __init__(self, constraint): # reliably restored by inspect
        # no doc
        pass

    constraint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __slots__ = (
        'constraint',
    )


class UnknownEditVariable(Exception):
    # no doc
    def __init__(self, edit_variable): # reliably restored by inspect
        # no doc
        pass

    edit_variable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __slots__ = (
        'edit_variable',
    )


class UnsatisfiableConstraint(Exception):
    # no doc
    def __init__(self, constraint): # reliably restored by inspect
        # no doc
        pass

    constraint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __slots__ = (
        'constraint',
    )


class Variable(object):
    # no doc
    def context(self, *args, **kwargs): # real signature unknown
        """ Get the context object associated with the variable. """
        pass

    def name(self, *args, **kwargs): # real signature unknown
        """ Get the name of the variable. """
        pass

    def setContext(self, *args, **kwargs): # real signature unknown
        """ Set the context object associated with the variable. """
        pass

    def setName(self, *args, **kwargs): # real signature unknown
        """ Set the name of the variable. """
        pass

    def value(self, *args, **kwargs): # real signature unknown
        """ Get the current value of the variable. """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    __hash__ = None


# variables with complex values

strength = None # (!) real value is '<kiwisolver.Strength object at 0x000001C863124930>'

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001C86551EA90>'

__spec__ = None # (!) real value is "ModuleSpec(name='kiwisolver._cext', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001C86551EA90>, origin='C:\\\\Users\\\\leonm\\\\PycharmProjects\\\\leonsystem\\\\venv\\\\Lib\\\\site-packages\\\\kiwisolver\\\\_cext.cp311-win_amd64.pyd')"

