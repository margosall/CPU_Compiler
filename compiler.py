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
def SetMachineCode(addr,value):
    if(len(machineCode)<(addr+1)):
        machineCode.extend([0]*(addr-len(machineCode)+1))
    machineCode[addr]=value

#READFILE
with open("program.asm", 'r') as programInput:
    code = programInput.readlines()

#COMPILE TO MACHINECODE
for line in code:
    lineIndex+=1
    # print(line.split())
    operation=""
    if(len(line.split())>0):
        operation = line.split()[0]

    if operation == ".def":
        varName, addr,value = line.split()[1:4]
        # print(line.split()[1:])
        addr = IntConvert(addr)
        value = IntConvert(value)
        variables[varName]=addr
        SetMachineCode(addr,value)
    elif ((operation in OPCODES1) or (operation in OPCODES2)):
        dest, value = line.split()[1:3]
        if(dest in DESTINATIONS):
            if(operation in OPCODES1):
                SetMachineCode(machineCodeIndex,OPCODES1[operation]|DESTINATIONS[dest])
                machineCodeIndex+=1
                if(value!=';'):
                    SetMachineCode(machineCodeIndex,IntConvert(value))
                    machineCodeIndex+=1
            elif(operation in OPCODES2):
                if(operation == "MOVR"):
                    SetMachineCode(machineCodeIndex,SOURCES_MOVR[value]|DESTINATIONS[dest])
                    machineCodeIndex+=1
                else:
                    if(value=="REGA"):
                        SetMachineCode(machineCodeIndex,OPCODES2[operation] | 0x00 | DESTINATIONS[dest])
                        machineCodeIndex+=1
                    elif(value=="REGB"):
                        SetMachineCode(machineCodeIndex,OPCODES2[operation] | 0x08 | DESTINATIONS[dest])
                        machineCodeIndex+=1
    elif(operation in SPECIAL_OPCODES):
        SetMachineCode(machineCodeIndex,SPECIAL_OPCODES[operation])
        machineCodeIndex+=1
    elif(operation in OPCODES_DIRECT):
        SetMachineCode(machineCodeIndex,OPCODES_DIRECT[operation])
        machineCodeIndex+=1
        SetMachineCode(machineCodeIndex,IntConvert(line.split()[1]))
        machineCodeIndex+=1
print(hex(machineCodeIndex))









#PRINT TO FILE
# print(len(machineCode))
with open("program.txt","w") as machineOutput:
    machineOutput.write(HEADER+"\n")
    machineCodeLine = ""
    for i in range(len(machineCode)):
        if((i%8==0 and i!=0) or (i==len(machineCode)-1)):
            machineOutput.write(machineCodeLine[:-1]+"\n")
            machineCodeLine=""
            machineCodeLine+=hex(machineCode[i])[2:]+" "
        else:
            machineCodeLine+=hex(machineCode[i])[2:]+" "


# printHex(machineCode)
