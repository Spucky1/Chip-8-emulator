import os
import textwrap
import binascii


START_ADDRESS = 0x200
FONTSET_START_ADRESS = 0x50
FONTSET_SIZE = 80
fontset = [ 0xF0, 0x90, 0x90, 0x90, 0xF0, 
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
	0xF0, 0x80, 0xF0, 0x80, 0x80 ]
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
        self.video = [64*32]
        self.opcode = None


    

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
                 print(self.memory)

            

          

            
                    
emulator = chip8()                    
emulator.loadrom_chip8("Airplane.ch8")
emulator.loadfont_chip8()
     
    

     




    

    
    

   
   
   
   
   


                     
                     

                     
                     
                     
                          
                
    
    
        
    


    


    
    
