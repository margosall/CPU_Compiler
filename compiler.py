HEADER = "v2.0 raw"
code = ""
machineCode = [0]
variables = {}
machineCodeIndex=0
lineIndex = 0
from operators import *
def padList(listIn, targetLen):
    return listIn + ([0]*(targetLen - len(listIn)))
def printHex(listIn):
    print('[{}]'.format(', '.join(hex(x)[2:] for x in listIn)))
def IntConvert(integerIn):
    if(integerIn[:2]=="0x"):
        return int(integerIn,16)
    elif(integerIn[:2]=="0b"):
        return int(integerIn,2)
    else:
        return int(integerIn)

#READFILE
with open("program.asm", 'r') as programInput:
    code = programInput.readlines()

#COMPILE TO MACHINECODE
for line in code:
    lineIndex+=1
    print(line.split())
    operation = line.split()[0]

    if operation == ".def":
        varName, addr,value = line.split()[1:4]
        print(line.split()[1:])
        addr = IntConvert(addr)
        value = IntConvert(value)
        variables[varName]=addr
        if(len(machineCode)<addr):
            print(len(machineCode),addr)
            machineCode.extend([0]*addr)
        machineCode[addr]=value
    elif (operation in OPCODES):
        dest, value = line.split()[1:3]
        if(dest in DESTINATIONS):
            machineCode[machineCodeIndex]= OPCODES[operation]|DESTINATIONS[dest]
            machineCodeIndex+=1
            if(value!=';'):
                machineCode[machineCodeIndex]=IntConvert(value)
                machineCodeIndex+=1

#PRINT TO FILE
print(len(machineCode))
with open("program.txt","w") as machineOutput:
    machineOutput.write(HEADER+"\n")
    machineCodeLine = ""
    for i in range(len(machineCode)):
        machineCodeLine+=hex(machineCode[i])[2:]+" "
        if((i%7==0 and i!=0) or (i==len(machineCode)-1)):
            machineOutput.write(machineCodeLine[:-1]+"\n")
            machineCodeLine=""
printHex(machineCode)
