#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class CPU:

    def __init__(self, ram=None):
        self.reset()


    def reset(self):
        self.Cycle = 0
        self.PC = 0xFFFC
        self.SP = 0x0100
        self.A = 0
        self.X = 0
        self.Y = 0
        self.C = False
        self.Z = False
        self.I = False
        self.D = False
        self.B = False
        self.V = False
        self.N = False


    def __repr__(self):
        return "Cycle: %08 PC: %04X SP: %04X A: %02X X: %02X Y: %02X" % (
            self.Cycle, self.PC, self.SP, self.A, self.X, self.Y
        )


    # OPCodes
    # Load and Store
    INS_LDA_IM   = 0xA9
    INS_LDA_ZP   = 0xA5
    INS_LDA_ZPX  = 0xB5
    INS_LDA_ABS  = 0xAD
    INS_LDA_ABSX = 0xBD
    INS_LDA_ABSY = 0xB9
    INS_LDA_INDX = 0xA1
    INS_LDA_INDY = 0xB1
    # Jumps and Calls
    INS_JMP_ABS  = 0x4C
    INS_JSR      = 0x20
    INS_RTS      = 0x60  


    def fetchByte(self, memory):
        data = memory.read(self.PC)
        self.PC += 1

        self.Cycle += 1
        return data


    def fetchWord(self, memory):
        loByte = self.fetchByte(memory)
        hiByte = self.fetchByte(memory)
        data = (hiByte << 8) + loByte

        return data


    def readByte(self, memory, address):
        data = memory.read(address)

        self.Cycle += 1
        return data


    def readWord(self, memory, address):
        loByte = self.readByte(memory, address)
        address =+ 1
        hiByte = self.readByte(memory, address)
        data = (hiByte << 8) + loByte

        return data


    def writeByte(self, memory, address, value):
        memory.write(address, value)

        self.Cycle += 1

    
    def writeWord(self, memory, address, value):
        loByte = value & 0xFF
        self.writeByte(memory, address, loByte)
        address =+ 1
        hiByte = value >> 8
        self.writeByte(memory, address, hiByte)
    

    def pushByteOntoStack(self, memory, value):
        self.writeByte(memory, self.SP, value)
        self.SP =- 1


    def pushWordOntoStack(self, memory, value):
        loByte = value & 0xFF
        self.writeByte(memory, self.SP, loByte)
        self.SP -= 1
        hiByte = value >> 8
        self.writeByte(memory, self.SP, hiByte)
        self.SP -= 1


    def popByteFromStack(self, memory):
        self.SP =+ 1
        data = self.readByte(memory, self.SP)

        return data

    
    def popWordFromStack(self, memory):
        loByte = self.popByteFromStack(memory)
        hiByte = self.popByteFromStack(memory)
        data = (hiByte << 8) + loByte

        return data

    
    def setFlagsLDA(self):
        if (self.A == 0):
            self.Z = True
        if ((self.A & 0x80) > 0):
            self.N = True


    def execute(self, cycles, memory):
        while(cycles > self.Cycle):
            instruction = self.fetchByte(memory)

            if (instruction == self.INS_LDA_IM):
                value = \
                    self.fetchByte(memory)
                self.A = value
                self.setFlagsLDA()

            if (instruction == self.INS_LDA_ZP):
                zeroPageAddress = \
                    self.fetchByte(memory)
                value = \
                    self.readByte(memory, zeroPageAddress)
                self.A = value
                self.setFlagsLDA()

            if (instruction == self.INS_LDA_ZPX):
                zeroPageAddress = \
                    self.fetchByte(memory)
                zeroPageAddress += self.X
                self.Cycle += 1
                value = \
                    self.readByte(memory, zeroPageAddress)
                self.A = value
                self.setFlagsLDA()

            if (instruction == self.INS_LDA_ABS):
                address = \
                    self.fetchWord(memory)
                value = \
                    self.readByte(memory, address)
                self.A = value
                self.setFlagsLDA()

            if (instruction == self.INS_LDA_ABSX):
                address = \
                    self.fetchWord(memory)
                address += self.X
                if (address > 0xFF):
                    self.Cycle += 1
                else:
                    # Crossing the page
                    self.Cycle += 2
                value = \
                    self.readByte(memory, address)
                self.A = value
                self.setFlagsLDA()

            if (instruction == self.INS_LDA_ABSY):
                address = \
                    self.fetchByte(memory)
                address += self.Y
                if (address > 0xFF):
                    self.Cycle += 1
                else:
                    # Crossing the page
                    self.Cycle += 2
                value = \
                    self.readByte(memory, address)
                self.A = value
                self.setFlagsLDA()

            if (instruction == self.INS_JMP_ABS):
                subRoutineAddress = \
                    self.fetchWord(memory)
                self.PC = subRoutineAddress
                self.Cycle += 1

            if (instruction == self.INS_JSR):
                subRoutineAddress = \
                    self.fetchWord(memory)
                self.PC -= 1
                self.pushWordOntoStack(memory, self.PC)
                self.PC = subRoutineAddress
                self.Cycle += 1
            
