#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest

from py6502.cpu import CPU
from py6502.ram import RAM

def test_lda_im_positive():

    memory = RAM()
    cpu = CPU()

    cpu.reset()

    # start - inline 6502 assembly
    memory.write(0xFFFC, cpu.INS_LDA_IM)
    memory.write(0xFFFD, 0x7F)
    # end - inline 6502 assembly

    cpu.execute(2, memory)

    assert cpu.PC == 0xFFFE
    assert cpu.SP == 0x0100
    assert cpu.A == 0x7F
    assert cpu.X == 0
    assert cpu.Y == 0
    assert cpu.C == False
    assert cpu.Z == False
    assert cpu.I == False
    assert cpu.D == False
    assert cpu.B == False
    assert cpu.V == False
    assert cpu.N == False

    assert cpu.Cycle == 2


def test_lda_im_negative():

    memory = RAM()
    cpu = CPU()

    cpu.reset()

    # start - inline 6502 assembly
    memory.write(0xFFFC, cpu.INS_LDA_IM)
    memory.write(0xFFFD, 0x84)
    # end - inline 6502 assembly

    cpu.execute(2, memory)

    assert cpu.PC == 0xFFFE
    assert cpu.SP == 0x0100
    assert cpu.A == 0x84
    assert cpu.X == 0
    assert cpu.Y == 0
    assert cpu.C == False
    assert cpu.Z == False
    assert cpu.I == False
    assert cpu.D == False
    assert cpu.B == False
    assert cpu.V == False
    assert cpu.N == True

    assert cpu.Cycle == 2


def test_lda_im_zero():

    memory = RAM()
    cpu = CPU()

    cpu.reset()

    # start - inline 6502 assembly
    memory.write(0xFFFC, cpu.INS_LDA_IM)
    memory.write(0xFFFD, 0x00)
    # end - inline 6502 assembly

    cpu.execute(2, memory)

    assert cpu.PC == 0xFFFE
    assert cpu.SP == 0x0100
    assert cpu.A == 0x00
    assert cpu.X == 0
    assert cpu.Y == 0
    assert cpu.C == False
    assert cpu.Z == True
    assert cpu.I == False
    assert cpu.D == False
    assert cpu.B == False
    assert cpu.V == False
    assert cpu.N == False

    assert cpu.Cycle == 2


def test_lda_zp_positive():

    memory = RAM()
    cpu = CPU()

    cpu.reset()

    # start - inline 6502 assembly
    memory.write(0x0042, 0x37)
    memory.write(0xFFFC, cpu.INS_LDA_ZP)
    memory.write(0xFFFD, 0x42)
    # end - inline 6502 assembly

    cpu.execute(3, memory)

    assert cpu.PC == 0xFFFE
    assert cpu.SP == 0x0100
    assert cpu.A == 0x37
    assert cpu.X == 0
    assert cpu.Y == 0
    assert cpu.C == False
    assert cpu.Z == False
    assert cpu.I == False
    assert cpu.D == False
    assert cpu.B == False
    assert cpu.V == False
    assert cpu.N == False

    assert cpu.Cycle == 3


def test_lda_zpx_negative():

    memory = RAM()
    cpu = CPU()

    cpu.reset()

    cpu.X = 0x5

    # start - inline 6502 assembly
    memory.write(0x0047, 0x85)
    memory.write(0xFFFC, cpu.INS_LDA_ZPX)
    memory.write(0xFFFD, 0x42)
    # end - inline 6502 assembly

    cpu.execute(4, memory)

    assert cpu.PC == 0xFFFE
    assert cpu.SP == 0x0100
    assert cpu.A == 0x85
    assert cpu.X == 0x5
    assert cpu.Y == 0
    assert cpu.C == False
    assert cpu.Z == False
    assert cpu.I == False
    assert cpu.D == False
    assert cpu.B == False
    assert cpu.V == False
    assert cpu.N == True

    assert cpu.Cycle == 4


def test_lda_abs_negative():

    memory = RAM()
    cpu = CPU()

    cpu.reset()

    # start - inline 6502 assembly
    memory.write(0x4221, 0x86)
    memory.write(0xFFFC, cpu.INS_LDA_ABS)
    memory.write(0xFFFD, 0x21)
    memory.write(0xFFFE, 0x42)
    # end - inline 6502 assembly

    cpu.execute(3, memory)

    assert cpu.PC == 0xFFFE
    assert cpu.SP == 0x0100
    assert cpu.A == 0x86
    assert cpu.X == 0x5
    assert cpu.Y == 0
    assert cpu.C == False
    assert cpu.Z == False
    assert cpu.I == False
    assert cpu.D == False
    assert cpu.B == False
    assert cpu.V == False
    assert cpu.N == True

    assert cpu.Cycle == 3


def test_lda_absx_negative():

    memory = RAM()
    cpu = CPU()

    cpu.reset()

    cpu.X = 0x6

    # start - inline 6502 assembly
    memory.write(0x4227, 0x87)
    memory.write(0xFFFC, cpu.INS_LDA_ABS)
    memory.write(0xFFFD, 0x21)
    memory.write(0xFFFE, 0x42)
    # end - inline 6502 assembly

    cpu.execute(3, memory)

    assert cpu.PC == 0xFFFE
    assert cpu.SP == 0x0100
    assert cpu.A == 0x87
    assert cpu.X == 0x5
    assert cpu.Y == 0
    assert cpu.C == False
    assert cpu.Z == False
    assert cpu.I == False
    assert cpu.D == False
    assert cpu.B == False
    assert cpu.V == False
    assert cpu.N == True

    assert cpu.Cycle == 3


def test_lda_absy_negative():

    memory = RAM()
    cpu = CPU()

    cpu.reset()

    cpu.Y = 0x8

    # start - inline 6502 assembly
    memory.write(0x4229, 0x87)
    memory.write(0xFFFC, cpu.INS_LDA_ABS)
    memory.write(0xFFFD, 0x21)
    memory.write(0xFFFE, 0x42)
    # end - inline 6502 assembly

    cpu.execute(3, memory)

    assert cpu.PC == 0xFFFE
    assert cpu.SP == 0x0100
    assert cpu.A == 0x87
    assert cpu.X == 0x5
    assert cpu.Y == 0
    assert cpu.C == False
    assert cpu.Z == False
    assert cpu.I == False
    assert cpu.D == False
    assert cpu.B == False
    assert cpu.V == False
    assert cpu.N == True

    assert cpu.Cycle == 3


def test_lda_indx():

    memory = RAM()
    cpu = CPU()

    cpu.reset()


def test_lda_indy():

    memory = RAM()
    cpu = CPU()

    cpu.reset()

