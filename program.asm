.def	inputA	0x20	0x5	;
.def	inputB	0x21	0x7	;
.def	counter	0x22	0x0	;
.def	result	0x23	0x0	;

SETR	REGM	0x20	;	
LOAD	REGA			;	
SETR	REGM	0x22	;	
LOAD	REGB			;	
CMP						;	
JMPALUEQ	0x26		;	Counter equals multiplier
SETR	REGA	0x1		;	+1 to counter
ADD REGC				;	
SAVECI				;	Save counter to ram 0x22
SETR	REGM	0x21	;	
LOAD	REGA			;	From ram 0x20 to rega
SETR	REGM	0x23	;	
LOAD	REGB			;	
ADD	REGC				;	result=result+inputb
SETR	REGM	0x23	;	
SAVECI					;	ram 0x23 = 
JMP	0x00				;
