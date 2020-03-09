# -*- coding: utf-8 -*-
"""
saltfactories.exceptions
~~~~~~~~~~~~~~~~~~~~~~~~

PyTest Salt Factories related exceptions
"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import traceback


class SaltFactoriesException(Exception):
    """
    Base exception for all pytest salt factories
    """


class ProcessNotStarted(SaltFactoriesException):
    """
    Exception raised when a process failed to start
    """

    def __init__(self, message, stdout=None, stderr=None, exc=None):
        super(ProcessNotStarted, self).__init__()
        self.message = message
        self.stdout = stdout
        self.stderr = stderr
        self.exc = exc

    def __str__(self):
        message = self.message
        if self.stdout or self.stderr:
            message += "\n Process Output:"
        if self.stdout:
            message += "\n>>>>> STDOUT >>>>>\n{}\n<<<<< STDOUT <<<<<".format(self.stdout)
        if self.stderr:
            message += "\n>>>>> STDERR >>>>>\n{}\n<<<<< STDERR <<<<<".format(self.stdout)
        if self.exc:
            message += "\n{}".format("".join(traceback.format_exception(*self.exc)))
        if self.stdout or self.stderr or self.exc:
            message += "\n"
        return message


class ProcessTimeout(ProcessNotStarted):
    """
    Exception raised when a process timmed out
    """