# -*- coding: utf-8 -*-
"""
Created on Tue Dec 23 10:12:36 2025

@author: suresh.burra
"""

class Computer:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None
        self.gpu = None
        self.os = None
        
    def __str__(self):
        return f"Computer: CPU={self.cpu}," \
            f" RAM={self.ram}GB, Storage={self.storage}," \
                f" GPU={self.gpu}, OS={self.os}"
                
class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()
        
    def set_cpu(self, cpu):
        self.computer.cpu = cpu
        return self
    
    def set_ram(self, ram):
        self.computer.ram = ram
        return self
    
    def set_storage(self, storage):
        self.computer.storage = storage
        return self
    
    def set_gpu(self, gpu):
        self.computer.gpu = gpu
        return self
    
    def set_os(self, os):
        self.computer.os = os
        return self
    
    def build(self):
        return self.computer
    
    
# Usage
computer = (ComputerBuilder()
            .set_cpu("Intel i9")
            .set_ram(32)
            .set_storage("1TB SSD")
            .set_gpu("NVIDIA RTX 4090")
            .set_os("Windows 11")
            .build())
print(computer)