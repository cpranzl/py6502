#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class RAM:

    MAX_RAM = 1024 * 64
    Data = []

    def __init__(self):
        for address in range(self.MAX_RAM):
            self.Data.append(0x00)


    def reset(self):
        for address in range(self.MAX_RAM):
            self.Data[address] = 0x00


    def read(self, address):
        """
        Read a value from the given adress
        """
        value = self.Data[address]
        return value


    def write(self, address, value):
        """
        Write a value to the given adress
        """
        self.Data[address] = value


    def print(self, address):
        """
        Print 32 bytes containing the given address
        """
        startAddress = (address // 16) * 16
        for address in range(startAddress, (startAddress + 32), 16):
            if (address < self.MAX_RAM):
                print(f'{address:04X} -', end = ' ')
                for i in range(0, 16):
                    print(f'{self.Data[address + i]:02X}', end = ' ')
                print()