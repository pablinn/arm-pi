# arm-pi


Scritp Python para Geany que permite usar el cross-compiler una x486 y subirlo a un ARM como raspberry pi o algun emulador 

Geany es un excelente editor de texto con sintaxis de color.
Se agrega como un comando y permite compilar codigo en ensamblador o C/C++ para ARM

Comando a agregar a geany
path/arm-pi/arm-pi.py %d %e s rpi

Se puede usar desde la tty de linux
./arm-pi.py %1 %2 %3 %4

%1 ->path
%2 ->nombre_archivo
%3 -> s codigo en assembler ARM 
      c codigo en c ARM
%4  -->rpi  (usa la sheel remota de raspbian para subirlo)
    
      
usa el cross-compiler instalado
sudo apt-get install arm-linux-gnueabihf  -> para procesadores ARM
sudo apt-get install arm-linux-gnueabi

una vez compilado lo sube a la rpi pide la contraseña de la sesion ssh

usa scp archivo ---> shhel remota
hay que editar en el script
host="host de su rpi o dispositivo con arm no probado en celulares por ahora"
destino=carpeta de destino  /home/pi generalmente





