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
rom = False

Start_Address = 0x200

def chip8__Loadrom(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)
            rom = True
if rom == True:
    os.open()






    
    




