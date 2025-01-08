.MODEL SMALL
.STACK 100H
.DATA
.CODE
MAIN PROC
;In this program, we will see how values are stored in the Registers
MOV AL,25
MOV AH,255
MOV Bx,0FF4H
MOV Cx,12370
MOV DL,01001001B
MOV DH,0AH
MOV AH,4CH
INT 21h
MAIN ENDP
END MAIN