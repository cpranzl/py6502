#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest

from py6502.cpu import CPU
from py6502.ram import RAM

def test_reset():

    cpu = CPU()

    cpu.reset()

    assert cpu.PC == 0xFFFC
    assert cpu.SP == 0x0100