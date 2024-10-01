import os
import textwrap
import binascii
import random


START_ADDRESS = 0x200
FONTSET_START_ADRESS = 0x50
FONTSET_SIZE = 80
fontset = [ 
     0xF0, 0x90, 0x90, 0x90, 0xF0, 
	0x20, 0x60, 0x20, 0x20, 0x70, 
	0xF0, 0x10, 0xF0, 0x80, 0xF0, 
     0xF0, 0x10, 0xF0, 0x10, 0xF0, 
	0x90, 0x90, 0xF0, 0x10, 0x10, 
	0xF0, 0x80, 0xF0, 0x10, 0xF0, 
	0xF0, 0x80, 0xF0, 0x90, 0xF0, 
	0xF0, 0x10, 0x20, 0x40, 0x40, 
	0xF0, 0x90, 0xF0, 0x90, 0xF0, 
     0xF0, 0x90, 0xF0, 0x10, 0xF0, 
	0xF0, 0x90, 0xF0, 0x90, 0x90, 
     0xE0, 0x90, 0xE0, 0x90, 0xE0,
	0xF0, 0x80, 0x80, 0x80, 0xF0, 
	0xE0, 0x90, 0x90, 0x90, 0xE0, 
	0xF0, 0x80, 0xF0, 0x80, 0xF0, 
	0xF0, 0x80, 0xF0, 0x80, 0x80 
     ]
class chip8:
        
        
    def __init__(self):
        self.registers = [16]
        self.memory = [None] * 4096
        self.index = 0
        self.pc = 0
        self.stack = [16]
        self.sp = 0
        self.timer = 0
        self.delaytimer = 0
        self.soundtimer = 0
        self.keypad = [16]
        self.video = [[0 for X in range(64)]for Y in range(32)]
        self.opcode = None
    
    def Chip8_chip8(self):
         self.pc = int(START_ADDRESS)
     
    def clear_screen_chip8(self):
         for X in self.video:
              for Y in self.video:
                   self.video[X][Y] = 0
               
               

    def OP_00E_chip8(self):
        self.sp -=self.sp
        self.pc= self.stack[self.sp]
        print(self.pc)
    
    def OP_1nnn_chip8(self):
         address = self.opcode & 0x0FFF
         self.pc = address

    def OP_2nnn_chip8(self):
         address = self.opcode & 0x0FFF
         self.stack[self.sp] =  self.pc
         self.sp += self.sp
         self.pc= address

    def OP_3xkk_chip8(self):
         Vx = (self.opcode & 0x0F00) >> 8
         Byte = self.opcode & 0x00FF
         if self.registers[Vx] == Byte:
              self.pc = self.pc + 2

    def OP_4xkk_chip8(self):
        Vx = (self.opcode & 0x0F00) >> 8
        Byte = self.opcode & 0x00FF
        if self.registers[Vx] != Byte:
              self.pc = self.pc + 2 
    
    def OP_5xy0_chip8(self):
         Vx = (self.opcode & 0x0F00) >> 8
         Vy = (self.opcode & 0x00F0 ) >> 4
         if self.register[Vx] == self.registers[Vy]:
              self.pc = self.pc + 2 
         
    def OP_6xkk_chip8(self):
         Vx = (self.opcode & 0x0F00) >> 8
         Byte =self.opcode & 0x00FF
         self.registers[Vx] = Byte

    def OP_7xkk_chip8(self):
         Vx = (self.opcode & 0x0F00) >> 8 
         Byte = self.opcode & 0x00FF
         self.registers[Vx] += Byte

    def OP_8xy0_chip8(self):
         Vx = (self.opcode & 0x0F00) >> 8
         Vy = (self.opcode & 0x00F0) >> 4
         self.registers[Vx] = self.registers[Vy]

    def OP_8xy1_chip8(self):
         Vx = (self.opcode & 0x0F00) >> 8
         Vy = (self.opcode & 0x00F0) >> 4
         self.register[Vx] |=  self.registers[Vy]
         
    def OP_8xy2_chip8(self):
         Vx = (self.opcode & 0x0F00) >> 8
         Vy = (self.opcode & 0x00F0) >>4
         self.register[Vx] &= self.registers[Vy]
     
    def OP_8xy3_chip8(self):
         Vx= (self.opcode & 0x0F00) >>8
         Vy = (self.opcode & 0x00F0) >> 4
         self.register[Vx] ^= self.registers[Vy]

    def OP_8xy4_chip8(self):
         Vx = (self.opcode & 0x0F00) >> 8
         Vy = (self.opcode & 0x00F0) >> 4
         sum = self.register[Vx] + self.registers[Vy]
         if sum  > 255:
              self.registers[0xF] = 1
         else:
              self.registers[0xF] =0
         
         self.registers[Vx] = sum & 0X0FF
         
    def OP_8xy5_chip8(self):
         Vx = (self.opcode & 0x0F00) >> 8
         Vy = (self.opcode & 0x00F0) >> 4
         if self.register[Vx]> self.registers[Vy]:
              self.register[0xF] = 1
         else:
              self.register[0xF] =0
         self.registers[Vx] -= self.register[Vy]
    
    def OP_8xy6_chip8(self):
         Vx = (self.opcode & 0x0F00) >>8
         self.registers[0xF] = (self.registers[Vx] & 0x1)
         self.registers[Vx] >>= 1
   
    def OP_8xy7_chip8(self):
         Vx = (self.opcode & 0x0F00) >>8
         Vy = (self.opcode & 0x00F0) >>4

         if self.registers[Vx] >> self.registers[Vy]:
              self.registers[0xF] = 1
         else:
              self.registers[0xF] =0
          
         self.registers[Vx] = self.registers[Vy] - self.registers[Vx]
     
    def OP_8xyE_chip8(self):
         Vx = (self.opcode & 0x0F00) >>8

         self.registers[0xF] = (self.registers[Vx] & 0x80) >> 7
         self.registers[Vx] >>= 1
     
    def OP_9xy0_(self):
         Vx = (self.opcode & 0x0F00) >>8
         Vy = (self.opcode & 0x00F0) >>4
         if self.registers[Vx] != self.registersr[Vy]:\
               pc += 2
    
    def OP_Annn_chip8(self):
         address = self.opcode & 0x0FFF
         self.index = address
  
    def OP_Bnnn_chip8(self):
         address = self.opcode & 0x0FFF

         self.pc = self.registers[0] +address

    def OP_Cxkk_chip8(self):
         Vx = (self.opcode & 0x0F00) >> 8
         Byte = self.opcode & 0x00FF
         self.registers[Vx] = random.randbytes(1) & Byte

    def OP_Dxyn_chip8(self):
         Vx = (self.opcode & 0x0F00) >> 8
         Vy = (self.opcode & 0x00F0) >> 4

         self.register[0xF] = 0

         spriteByte = self.memory[self.index]

         

         

         

         

     
         
    def loadrom_chip8(self, rom_path):
        with open(rom_path, "rb")as r:
            hexdata = textwrap.wrap(str(binascii.hexlify(r.read())),2)
            hexdata.pop()
            hexdata.pop(0)
            print(START_ADDRESS)
            for i in range(len(hexdata)):
                self.memory[START_ADDRESS + i] = hexdata[i]
    
    def loadfont_chip8(self):
            for i in range(FONTSET_SIZE):
                 self.memory[FONTSET_START_ADRESS + i] = fontset[i]
    
emulator = chip8()                    
emulator.loadrom_chip8("Airplane.ch8")
emulator.loadfont_chip8()
emulator.OP_00E_chip8()


     
    

     




    

    
    

   
   
   
   
   


                     
                     

                     
                     
                     
                          
                
    
    
        
    


    


    
    
