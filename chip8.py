import os
from os import path
import binascii
print("script is running")


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
def findrom_chip8(rom_name, path):
        for root, dirs, files, in os.walk(path):
            if rom_name in files:
                os.path.join(root, rom_name)
                with open(rom_name, "rb")as r:
                    hexdata = binascii.hexlify(r.read())
                    print(hexdata)
                    
                    
def loadrom_chip8():
     print("room is loading")
def main():
     findrom_chip8("Airplane.ch8","./")
    
main()
     




    

    
    

   
   
   
   
   


                     
                     

                     
                     
                     
                          
                
    
    
        
    


    


    
    
