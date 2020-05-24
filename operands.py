#!/usr/bin/env python3.8

from aenum import Enum

class OperandCodes(Enum, start=0):
    LIST
    GARBAGE
    LINEFEED
