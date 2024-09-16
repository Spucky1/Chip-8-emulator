import os
import textwrap
import binascii


START_ADDRESS = 0x200
class chip8:
    def __init__(self):
        self.registers = [16]
        self.memory = [4096]
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
            
                    
emulator = chip8()                    
emulator.loadrom_chip8("Airplane.ch8")
     
    

     




    

    
    

   
   
   
   
   


                     
                     

                     
                     
                     
                          
                
    
    
        
    


    


    
    
