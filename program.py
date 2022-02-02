#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from py6502.cpu import CPU
from py6502.ram import RAM

memory = RAM()
cpu = CPU()
cpu.reset()

cpu.X = 0x5

# start - inline 6502 assembly
memory.write(0x0047, 0xA4)
memory.write(0xFFFC, cpu.INS_LDA_ZPX)
memory.write(0xFFFD, 0x42)
# end - inline 6502 assembly

cpu.execute(4, memory)