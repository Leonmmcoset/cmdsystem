# encoding: utf-8
# module PyQt5.QtNetwork
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtNetwork.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QOcspRevocationReason(__enum.IntEnum):
    # no doc
    def _generate_next_value_(name, start, count, last_values): # reliably restored by inspect
        """
        Generate the next value when not given.
        
                name: the name of the member
                start: the initial start value or None
                count: the number of existing members
                last_values: the list of values assigned
        """
        pass

    def _new_member_(self, *args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def _value_repr_(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwds): # reliably restored by inspect
        # no doc
        pass

    @staticmethod # known case of __new__
    def __new__(cls, value): # reliably restored by inspect
        # no doc
        pass

    AffiliationChanged = 3
    CACompromise = 2
    CertificateHold = 6
    CessationOfOperation = 5
    KeyCompromise = 1
    None_ = -1
    RemoveFromCRL = 7
    Superseded = 4
    Unspecified = 0
    _member_map_ = {
        'AffiliationChanged': 3,
        'CACompromise': 2,
        'CertificateHold': 6,
        'CessationOfOperation': 5,
        'KeyCompromise': 1,
        'None_': -1,
        'RemoveFromCRL': 7,
        'Superseded': 4,
        'Unspecified': 0,
    }
    _member_names_ = [
        'AffiliationChanged',
        'CACompromise',
        'CertificateHold',
        'CessationOfOperation',
        'KeyCompromise',
        'None_',
        'RemoveFromCRL',
        'Superseded',
        'Unspecified',
    ]
    _member_type_ = int
    _unhashable_values_ = []
    _use_args_ = True
    _value2member_map_ = {
        -1: -1,
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
    }


