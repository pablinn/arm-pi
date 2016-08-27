/*
r0  0
r1  /bin/sh
r2  /bin/sh

r7 11

*/


.section .text

.global main
main:

.code 32
    add r6,pc,#1
    bx  r6
    
.code 16     
    
	mov  r0,pc    /*guardomos el program counter en r0*/
	add  r0,#10 
	    
    str  r3,[sp,#4]
    add  r1,sp,#4
    sub  r2,r2,r2
    mov  r7,#11
    svc  1
      
    
     
.ascii "//bin/sh\n"
