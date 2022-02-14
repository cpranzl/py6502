#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest

from py6502.cpu import CPU
from py6502.ram import RAM

def test_jmp_abs():

    memory = RAM()
    cpu = CPU()

    cpu.reset()

    # start - inline 6502 assembly
    memory.write(0xFFFC, cpu.INS_JSR)
    memory.write(0xFFFD, 0x21)
    memory.write(0xFFFE, 0x42)
    # end - inline 6502 assembly

    cpu.execute(6, memory)

    assert cpu.PC == 0x4221
    assert cpu.SP == 0x00FE
    assert cpu.A == 0
    assert cpu.X == 0
    assert cpu.Y == 0
    assert cpu.C == False
    assert cpu.Z == False
    assert cpu.I == False
    assert cpu.D == False
    assert cpu.B == False
    assert cpu.V == False
    assert cpu.N == False

    assert cpu.Cycle == 6