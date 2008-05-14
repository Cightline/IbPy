#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" ib.ext.cfg.EReader -> config module for EReader.java.

"""
modulePreamble = [
    'from ib.lib import Boolean, Double, DataInputStream, Integer, Long, StringBuffer, Thread',
    'from ib.lib.overloading import overloaded',
    '',
    'from ib.ext.Contract import Contract',
    'from ib.ext.ContractDetails import ContractDetails',
    'from ib.ext.Execution import Execution',
    'from ib.ext.Order import Order',
    'from ib.ext.OrderState import OrderState',
    'from ib.ext.TickType import TickType',
    'from ib.lib.logger import logger',
    '',
    '# micro optimizations',
    'from __builtin__ import float, str, None, True, False',
    ]


outputSubs = [
    (r'    m_parent = object\(\)', '    m_parent = None'),
    (r'    m_dis = DataInputStream\(\)', '    m_dis = None'),
    (r'self\.m_parent = self\.parent',
     r'self.m_parent = parent'),

    (r'super\(EReader, self\)\.__init__\("EReader", self\.parent, dis\)',
     r'self.__init__("EReader", parent, dis)'),

    (r'return None if len\(\(strval\) == 0\) else strval',
     r'return None if strval == 0 else strval'),

    (r'(\s+)(self\.setName\(name\))',
     r'\1Thread.__init__(self, name, parent, dis)\1\2'),

    (r'Math\.abs', r'abs'),

    (r'len\(\(strval\) == 0\)', r'(len(strval) == 0)'),

    (r'(\s+)(self.parent\(\)\.wrapper\(\)\.error\(ex\))',
     r'\1errmsg = ("Exception while processing message.")\1logger().exception(errmsg)\1\2'),

    ]


typeTypeMap = {
    'EClientSocket':'object'
    }
