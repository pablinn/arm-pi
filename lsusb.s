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
    add  r1,#14
    mov  r0,$0x1 
    mov  r7,$0x4
    svc  1
    
     /*exit()*/
     sub r4,r4,r4
     mov r0,r4      
     mov r7,$0x1
     svc 1
     
.ascii "lsusb\n"
