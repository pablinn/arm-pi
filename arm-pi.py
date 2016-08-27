#!/usr/bin/python
import os
import sys
from subprocess import Popen, PIPE


arch=sys.argv[1]+'/'+sys.argv[2]

cc_as="arm-linux-gnueabihf-as"
cc_gcc="arm-linux-gnueabihf-gcc"


proc = Popen([cc_as ,'-mthumb', '-o', arch+'.o' , arch + '.s'] , stdin = PIPE , stdout = PIPE)
proc.stdout.readline()
proc.stdout.flush()


proc1=Popen([cc_gcc,'-o',arch,arch+'.o'], stdin = PIPE, stdout = PIPE)
proc1.stdout.readline()
proc1.stdout.flush()

proc4=Popen(['rm','-vf',sys.argv[1]+'/*.o'])
#proc4.stdout.readline()
#proc4.stdout.flush()


host='pi@192.168.43.222'
destino=':/home/pi/pru-arm'

print 'scp', sys.argv[2] ,  host +  destino
print 'rm','-vf',sys.argv[1]+'/*.o'

proc3 = Popen(['scp', sys.argv[2] ,  host +  destino] , stdout = PIPE, stdin = PIPE)
proc3.stdout.readline()
proc3.stdout.flush()



""" arm-linux-gnueabihf-as -mthumb -o %e.o %f
arm-linux-gnueabihf-gcc -o %e %e.o 
arm-linux-gnueabihf-gcc -o %e %e.c 
rm -vf *.o
envia a la pi
entrara y lo ejecutara
"""
