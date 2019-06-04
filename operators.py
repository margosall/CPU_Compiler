OPCODES1 = {
    "NOP":0x00,

    "SETRI":0x08,
    "MOVI":0x08,
    "LOAD":0x08,

    "SETRD":0x10,
    "SETR":0x10,
    "MOVD":0x10,

    "AND":0x80,
    "OR":0x88,
    "NOR":0x90,
    "XOR":0x98,

    "ADD":0xA0,
    "SUB":0xA8,

    "INCA":0xF8,
    "DECB":0xF0
}
DESTINATIONS = {
    "NULL":0,
    "REGA":1,
    "REGB":2,
    "REGC":3,
    "MAR":4,
    "MDR":5,
    "PC":6,
    "REGM":7
}
#MOVR
SOURCES_MOVR = {
    "REGA":0x30,
    "REGB":0x38,
    "REGC":0x40,
    "REGM":0x48
}


OPCODES2 = {
    "MOVR":0,
    "ROR":0xC0,
    "ROL":0xD0,
    "INV":0xE0,
}

OPCODES_DIRECT = {
    "SAVECD":0x28,
    "JMPALU0":0x58,
    "JMPALUOFL":0x60,
    "JMPALUEQ":0x68,
    "JMP":0x70,

}
SPECIAL_OPCODES = {
    "SAVECI":0x20,
    "CMP":0xB0,
}
