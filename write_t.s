.section .text

.global main
main:

.code 32
    add r6,pc,#1
    bx  r6
    
.code 16     
    /*write()*/
	mov  r2,#6
    mov  r1,pc
    add  r1,#12
    mov  r0,$0x1 
    mov  r7,$0x4
    svc  0
    
     /*exit()*/
     sub r0,r0,r0      /*0=1-1*/ 
     mov r7,$0x1
     svc 0
     
     
     
.ascii "lsusb\n"
