#!/usr/bin/python
import os
import sys
from subprocess import Popen, PIPE


arch=sys.argv[1]+'/'+sys.argv[2]

cc_as="arm-linux-gnueabihf-as"
cc_gcc="arm-linux-gnueabihf-gcc"

try:
	if (sys.argv[3]=='s'):
		#compila un archivo assembler arm a un obj-elf-arm
		proc = Popen([cc_as ,'-mthumb', '-o', arch+'.o' , arch + '.s'] , stdin = PIPE , stdout = PIPE)
		proc.stdout.readline()
		proc.stdout.flush()

		#linkea el obj-elf-arm a un bin-elf-arm
		proc1=Popen([cc_gcc,'-o',arch,arch+'.o'], stdin = PIPE, stdout = PIPE)
		proc1.stdout.readline()
		proc1.stdout.flush()
		print "Compilado para ARM cross-compiler -->"+cc_gcc+"\n"
        	print "Fuente"+arch+".s"

	if (sys.argv[3]=='c'):
		#linkea el obj-elf-arm a un bin-elf-arm
        	proc1=Popen([cc_gcc,'-o',arch,arch+'.c'], stdin = PIPE, stdout = PIPE)
       		proc1.stdout.readline()
        	proc1.stdout.flush()
		print "Compilado para ARM cross-compiler -->"+cc_gcc+"\n"
       		print "Fuente -->"+arch+".c"


	if (sys.argv[4]=='rpi'):
		#envia el archivo bin-elf-arm a la rpi por shell remoto SCP
		host='pi@192.168.43.222'
		destino=':/home/pi/pru-arm'
		proc3 = Popen(['scp', sys.argv[2] ,  host +  destino] , stdout = PIPE, stdin = PIPE)
		proc3.stdout.readline()
		proc3.stdout.flush()
		print "Archivo enviado -->"+host+destino

except IndexError as e:
	print e

"""no funcion
proc4=Popen(['rm','-vf',sys.argv[1]+'/*.o'])
proc4.stdout.readline()
proc4.stdout.flush()
"""

