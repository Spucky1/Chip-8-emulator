import os


class chip8:
    def __init__(self):
        self.registers = [16]
        self.memory = [4096]
        self.index
        self.pc
        self.stack = [16]
        self.sp 
        self.delaytimer
        self.soundtimer
        self.keypad = [16]
        self.video[64*32]
        self.opcode
    
START_ADDRES = int(0x200)
def loadrom_chip8():
    findrom_chip8("Airplane.ch8")
    

   
   
   
   
   
def findrom_chip8(rom_name, emulator):
        for root, dirs, files, in os.walk(emulator):
            if rom_name in files:
                return os.path.join(root, rom_name)
                with open(rom_name, "f")as f:
                     contents = function(f)
                     
                     

                     
                     
                     
                          
                
    
    
        
    


    


    
    
