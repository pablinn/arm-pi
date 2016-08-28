# arm-pi


Script en Python para Geany permite usar el cross-compiler en una x486 y subir el arm-elf a un dispositivo con ARM como raspberry pi o probarlo en algun emulador como qemu.

Geany es un excelente editor de texto con sintaxis de color.
Se agrega como un comando y permite compilar codigo en ensamblador o C/C++ para ARM

Comando a agregar a geany

path/arm-pi/arm-pi.py %d %e s rpi  -->para compilar un assembler y subirlo a una rpi

path/arm-pi/arm-pi.py %d %e c rpi  -->para compilar un C y subirlo a una rpi


path/arm-pi/arm-pi.py %d %e s -->para compilar un assembler y emu

path/arm-pi/arm-pi.py %d %e c -->para compilar un C y emu


Se puede usar desde la tty de linux

./arm-pi.py %1 %2 %3 %4

./arm-pi /home/usr prueba s rpi

./arm-pi /home/usr prueba c rpi

%1-path
%2-nombre_archivo
%3-s o c (codigo en assembler ARM o codigo en c ARM)
%4-rpi  (usa la sheel remota de raspbian para subirlo).
 
      
Usa el cross-compiler instalado sino instalar alguno

sudo apt-get install arm-linux-gnueabihf  -> para procesadores ARM

sudo apt-get install arm-linux-gnueabi

una vez compilado lo sube a la rpi pide la contraseña de la sesion ssh

usa scp archivo ---> shell remota

Hay que editar en el script (no configurable es mas facil desde el script)

host="usr@ip  o  usr@dominio"

destino=carpeta de destino  /home/pi generalmente




