import sys
file_path = sys.argv[1]
Labels = [0] * 32
with open(file_path, 'r') as file:
    file_contents = file.read()

def SplitToInstructions(string):
    return [string[i:i+5] for i in range(0, len(string), 5)]

Registers = [0,0,0,0]
InstructPointer = 0
Stack = []
EqualsZero = 0
Underflow = 0
OBiggerThan1 = 0


def BinaryToNumber(arrayofint):
    Index = len(arrayofint) - 1
    Value = 0
    CValue = 1
    while Index != -1:
        if arrayofint[Index] == 1:
            Value += CValue
        CValue *= 2
        Index -= 1
    return Value



def s2a(a):
    return [int(a[0]),int(a[1]),int(a[2])]

def AddsIfLabel(test, textplusone):
    global InstructPointer
    global Labels
    if test[0] == "1" and test[1] =="1" and test[2]  == "1":
        Labels[BinaryToNumber([int(x) for x in textplusone])] = InstructPointer

def SetFlags(Arg1,Arg2):
    global Underflow
    global OBiggerThan1
    global EqualsZero
    if Arg1 + Arg2 == 0:
        EqualsZero = 1
    else:
        EqualsZero = 0
    if Arg1 + Arg2 < 0:
        Underflow = 1
    else:
        Underflow = 0
    if Arg1 > Arg2:
        OBiggerThan1 = 1
    else:
        OBiggerThan1 = 0
    
def execute(text,NextText="00000"):
    global InstructPointer
    global Registers
    text = [int(x) for x in text]
    NextText = [int(x) for x in NextText]
    Arguments = BinaryToNumber([text[3],text[4]])
    instruction = [text[0],text[1],text[2]]
    if instruction == s2a("000"):
        # SET
        Registers[Arguments] = BinaryToNumber(NextText)
        InstructPointer += 1
        return "SET"
    if instruction == s2a("001"):
        # PUSH
        Stack.append(Registers[Arguments])
        return "PUSH"
    if instruction == s2a("010"):
        # POP
        Registers[Arguments] = Stack[len(Stack) - 1]
        del Stack[len(Stack) - 1]
        return "POP"
    if instruction == s2a("011"):
        # SYSCALL
        if Registers[0] == 1:
            print(Registers[Arguments])
        return "SYSCALL"
    if instruction == s2a("100"):
        # ADD
        SetFlags(Registers[text[3]],Registers[text[4]])
        Registers[text[4]] =  Registers[text[3]] + Registers[text[4]]
        return "ADD"
    if instruction == s2a("101"):
        # SUB
        SetFlags(-1 * Registers[text[3]], Registers[text[4]])
        Registers[text[4]] =    Registers[text[4]] - Registers[text[3]]
        return "ADD"
    if instruction == s2a("111"):
        return "LABEL"
    if instruction == s2a("110"):
        if (Arguments == 1 and EqualsZero == 1) or (Arguments == 2 and Underflow == 1) or (Arguments == 3 and OBiggerThan1 == 1):
            return "JZMP"
        else:
            InstructPointer = Labels[BinaryToNumber(NextText)]
        return "JUMP"
fs = ""
for char in file_contents:
    if char == "0" or char == "1":
        fs += char
fixed_string = SplitToInstructions(fs)
while InstructPointer <= len(fixed_string) - 1:
    if InstructPointer != len(fixed_string) - 1:
        AddsIfLabel(fixed_string[InstructPointer], fixed_string[InstructPointer + 1])
    InstructPointer += 1
InstructPointer = 0
while InstructPointer <= len(fixed_string) - 1:

    if InstructPointer ==len(fixed_string) - 1:
        execute(fixed_string[InstructPointer])
    else:
        execute(fixed_string[InstructPointer], fixed_string[InstructPointer + 1])
    InstructPointer += 1