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
    findrom()
   
   
   
   
   
def findrom(name, ):
        for root, dirs, files, in os.walk(path):
            if name in files:
                return os.path.join(root, name)
                
    
    
        
    


    


    
    




